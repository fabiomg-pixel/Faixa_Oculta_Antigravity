#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Particionador de Dados da Arquitetura v2 da Faixa Oculta (tools/particionar_dados_v2.py).

Lê `data/revista.json` (preservando-o intacto para retrocompatibilidade) e gera:
1. `data/boot.json` (< 150 KB):
   - `versao_dados`: hash curto determinístico do estado atual para cache HTTP eficiente dos shards
   - `dias_index`: índice cronológico de todas as edições diárias disponíveis
   - `semanas_index`: índice de todas as edições da Revista da Semana
   - `edicoes_index`: índice das edições mensais de Música, Cinema e Livros
   - `hoje_inicial`: boletim diário mais recente pronto para renderização imediata
   - `agenda`: agenda cultural ativa do Rio, playlists e mapas de artistas
2. `data/dias/<id>.json`:
   - Cada edição diária isolada com 100% das notas, textos integrais das fontes (mesclados de `leituras`) e jornais completos.
3. `data/semanas/<id>.json`:
   - Cada edição semanal isolada com todas as coberturas e temas `fora_do_radar` enriquecidos a partir de `leituras`.
4. `data/cultura/musica_<YYYY-MM>.json`, `data/cultura/cinema_<YYYY-MM>.json`, `data/cultura/livros_<YYYY-MM>.json`:
   - Edição mensal completa (metadados da edição + `destaque_autor` + `itens` do mês + `guias` do mês),
     embutindo diretamente todas as críticas de `leituras` (`ref` / `url`) dentro de cada item.
5. `data/arquivo_index.json`:
   - Índice compacto de busca e cross-links (`Na revista`) cobrindo 100% dos discos, filmes, séries e livros publicados,
     eliminando a necessidade de baixar os 20 MB de `data/revista.json` no cliente.
"""

import copy
import datetime
import hashlib
import json
import os
import re
import unicodedata
import urllib.parse


SECOES_TITULOS = {
    "musica": {
        "radar": "no seu radar",
        "descobertas": "descobertas",
        "brasil": "brasil 2026",
        "breve": "em breve",
    },
    "cinema": {
        "cartaz": "nos cinemas",
        "achados": "achados no streaming",
        "series": "séries que acabam",
        "pop": "cultura pop",
        "brasil": "cinema brasileiro",
        "breve": "em breve",
    },
    "livros": {
        "lancamentos": "lançamentos",
        "brasil": "literatura brasileira",
        "ideias": "ideias",
        "achados": "achados",
    },
}


def nrm_busca(texto):
    s = unicodedata.normalize("NFD", str(texto or ""))
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def normalizar_url_chave(url):
    if not url:
        return ""
    try:
        s = urllib.parse.urlsplit(str(url).strip())
        q = [
            (k, v)
            for k, v in urllib.parse.parse_qsl(s.query, keep_blank_values=True)
            if not k.lower().startswith(("utm_", "fbclid", "gclid"))
        ]
        limpa = urllib.parse.urlunsplit((s.scheme, s.netloc, s.path, urllib.parse.urlencode(q), "")).rstrip("/")
    except Exception:
        limpa = str(url).strip().rstrip("/")
    limpa = re.sub(r"#.*$", "", limpa)
    return re.sub(r"^https?://(www\.)?", "", limpa).lower()


def ordenar_chaves_dias(chaves):
    """Ordena chaves de dias cronologicamente (AAAA-MM-DD antes de AAAA-MM-DD-noite)."""
    def _key(k):
        base = k[:10]
        turno = 1 if k.endswith("-noite") else 0
        return (base, turno, k)
    return sorted(chaves, key=_key)


def indexar_leituras(leituras_dict):
    """Cria índices rápidos de `leituras` por `ref` (item cultural) e por `url` normalizada."""
    por_ref = {}
    por_url = {}
    for lk, lv in (leituras_dict or {}).items():
        if not isinstance(lv, dict):
            continue
        ref = lv.get("ref")
        if ref:
            por_ref.setdefault(ref, []).append(lv)
            slug_limpo = re.sub(r"^\d{4}-\d{2}--", "", str(ref))
            if slug_limpo and slug_limpo != ref:
                por_ref.setdefault(slug_limpo, []).append(lv)
        u = normalizar_url_chave(lv.get("url"))
        if u:
            por_url[u] = lv
    for ref_k in por_ref:
        por_ref[ref_k].sort(key=lambda x: x.get("ordem", 99))
    return por_ref, por_url


def _enriquecer_item_cultural(it_copy, item_id, por_ref, por_url):
    slug_limpo = re.sub(r"^\d{4}-\d{2}--", "", str(item_id))
    criticas_ref = []
    vistos_tit = set()
    for chave_r in (item_id, slug_limpo):
        for c in por_ref.get(chave_r, []):
            id_c = (c.get("fonte", ""), c.get("titulo", ""), c.get("url", ""))
            if id_c not in vistos_tit:
                vistos_tit.add(id_c)
                criticas_ref.append(copy.deepcopy(c))

    u_item = normalizar_url_chave(it_copy.get("fonte"))
    if u_item and u_item in por_url:
        cand_u = por_url[u_item]
        id_u = (cand_u.get("fonte", ""), cand_u.get("titulo", ""), cand_u.get("url", ""))
        if id_u not in vistos_tit:
            vistos_tit.add(id_u)
            criticas_ref.append(copy.deepcopy(cand_u))

    if criticas_ref:
        it_copy["leituras_criticas"] = criticas_ref
        if not it_copy.get("analises_criticas"):
            it_copy["analises_criticas"] = [
                {
                    "veiculo": c.get("fonte", "Crítica Especializada"),
                    "autor": c.get("autor", "Redação"),
                    "nota": c.get("nota", ""),
                    "url": c.get("url", ""),
                    "titulo": c.get("titulo", it_copy.get("titulo") or it_copy.get("album", "")),
                    "citacao": c.get("citacao", ""),
                    "paragrafos": c.get("texto_integral") or c.get("resumo") or [],
                    "pontos": c.get("pontos", []),
                }
                for c in criticas_ref
            ]
    return len(criticas_ref)


def compactar_hoje_para_boot(dia_id, dia_obj):
    """Prepara `hoje_inicial` para `data/boot.json`, mantendo 100% das notas e manchetes dentro do orçamento < 150 KB."""
    d = copy.deepcopy(dia_obj)
    d["id"] = dia_id

    for n in d.get("notas", []):
        for f in n.get("fontes", []):
            f.pop("texto_integral", None)
            f.pop("pontos", None)
            f.pop("citacao", None)

    if isinstance(d.get("jornais"), dict):
        j = d["jornais"]
        j["shard_completo"] = f"data/dias/{dia_id}.json"
        for m in j.get("manchetes", []):
            for rep in m.get("reportagens", []):
                rep.pop("pontos", None)
                rep.pop("lide", None)
                ti = rep.get("texto_integral") or []
                if len(ti) >= 1:
                    rep["texto_integral"] = [ti[0][:80]]
            if isinstance(m.get("editorial"), dict):
                ed_t = m["editorial"].get("texto") or []
                if len(ed_t) > 1:
                    m["editorial"]["texto"] = [ed_t[0]]
        for l_it in j.get("leitura", []):
            l_it.pop("pontos", None)
            ti = l_it.get("texto_integral") or []
            if len(ti) >= 1:
                l_it["texto_integral"] = [ti[0][:240]]

    return d


def compactar_agenda_para_boot(agenda_obj):
    """Mantém eventos ativos, playlists atuais (semana e trinta) e artistas mapeados para os eventos em cartaz."""
    ag = copy.deepcopy(agenda_obj or {})
    atual = ag.get("atual", {})
    eventos = atual.get("eventos", [])

    artistas_ativos = set()
    for ev in eventos:
        for a in ev.get("artistas") or []:
            artistas_ativos.add(a)
        for d in ev.get("destaques") or []:
            for a in d.get("artistas") or []:
                artistas_ativos.add(a)
            d.pop("analises_criticas", None)

    playlists = atual.get("playlists", {})
    for pk in ("semana", "trinta"):
        for a in playlists.get(pk, {}).get("artistas") or []:
            artistas_ativos.add(a)

    if isinstance(playlists.get("anteriores"), list):
        playlists["anteriores"] = playlists["anteriores"][-5:]

    mapa_sp = ag.get("artistas", {}).get("mapa", {})
    mapa_yt = ag.get("artistas", {}).get("youtube", {})

    if artistas_ativos:
        ag["artistas"] = {
            "mapa": {k: v for k, v in mapa_sp.items() if k in artistas_ativos},
            "youtube": {k: v for k, v in mapa_yt.items() if k in artistas_ativos},
        }

    return ag


def particionar_dados(caminho_revista="data/revista.json", base_dir="data"):
    if not os.path.exists(caminho_revista):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_revista}")

    with open(caminho_revista, "r", encoding="utf-8") as f:
        raw_revista = f.read()
    db = json.loads(raw_revista)
    versao_dados = hashlib.md5(raw_revista.encode("utf-8")).hexdigest()[:10]

    dias_dir = os.path.join(base_dir, "dias")
    semanas_dir = os.path.join(base_dir, "semanas")
    cultura_dir = os.path.join(base_dir, "cultura")
    for d in (dias_dir, semanas_dir, cultura_dir):
        os.makedirs(d, exist_ok=True)

    por_ref, por_url = indexar_leituras(db.get("leituras", {}))

    # ---------------------------------------------------------
    # 1. GERAR SHARDS DE DIAS (data/dias/<id>.json)
    # ---------------------------------------------------------
    dias = db.get("dias", {})
    chaves_dias = ordenar_chaves_dias(list(dias.keys()))
    dias_index = []

    for d_id in chaves_dias:
        d_obj = copy.deepcopy(dias[d_id])
        d_obj["id"] = d_id

        for n in d_obj.get("notas", []):
            for ft in n.get("fontes", []):
                u_key = normalizar_url_chave(ft.get("url"))
                leitura_match = por_url.get(u_key)
                if leitura_match:
                    if not ft.get("texto_integral") and leitura_match.get("texto_integral"):
                        ft["texto_integral"] = leitura_match["texto_integral"]
                    elif not ft.get("texto_integral") and leitura_match.get("resumo"):
                        ft["texto_integral"] = leitura_match["resumo"]
                    if not ft.get("pontos") and leitura_match.get("pontos"):
                        ft["pontos"] = leitura_match["pontos"]
                    if not ft.get("citacao") and leitura_match.get("citacao"):
                        ft["citacao"] = leitura_match["citacao"]

        shard_dia_path = os.path.join(dias_dir, f"{d_id}.json")
        with open(shard_dia_path, "w", encoding="utf-8") as f:
            json.dump(d_obj, f, ensure_ascii=False, separators=(",", ":"))

        dias_index.append({
            "id": d_id,
            "data": d_obj.get("data", d_id[:10]),
            "edicao": d_obj.get("edicao", "noite" if d_id.endswith("-noite") else "manha"),
            "titulo": d_obj.get("titulo", ""),
            "total_notas": len(d_obj.get("notas", [])),
            "tem_audio": bool(d_obj.get("audio")),
            "tem_jornais": bool(d_obj.get("jornais")),
            "shard": f"data/dias/{d_id}.json",
        })

    # ---------------------------------------------------------
    # 2. GERAR SHARDS DE SEMANAS (data/semanas/<id>.json)
    # ---------------------------------------------------------
    semanas = db.get("semanas", {})
    chaves_semanas = sorted(list(semanas.keys()))
    semanas_index = []

    for s_id in chaves_semanas:
        s_obj = copy.deepcopy(semanas[s_id])
        s_obj["id"] = s_id

        for tema in s_obj.get("temas", []):
            if not isinstance(tema, dict):
                continue
            for cob in tema.get("cobertura", []):
                if not isinstance(cob, dict):
                    continue
                u_key = normalizar_url_chave(cob.get("url"))
                leitura_match = por_url.get(u_key)
                if leitura_match:
                    if not cob.get("texto_integral"):
                        cob["texto_integral"] = leitura_match.get("texto_integral") or leitura_match.get("resumo") or []
                    if not cob.get("pontos") and leitura_match.get("pontos"):
                        cob["pontos"] = leitura_match["pontos"]
                    if not cob.get("citacao") and leitura_match.get("citacao"):
                        cob["citacao"] = leitura_match["citacao"]
                    if not cob.get("titulo") and leitura_match.get("titulo"):
                        cob["titulo"] = leitura_match["titulo"]
                    if not cob.get("autor") and leitura_match.get("autor"):
                        cob["autor"] = leitura_match["autor"]

        for r_item in s_obj.get("fora_do_radar", []):
            if not isinstance(r_item, dict):
                continue
            for ler_it in r_item.get("ler", []):
                if not isinstance(ler_it, dict):
                    continue
                u_key = normalizar_url_chave(ler_it.get("url"))
                leitura_match = por_url.get(u_key)
                if leitura_match:
                    if not ler_it.get("texto_integral"):
                        ler_it["texto_integral"] = leitura_match.get("texto_integral") or leitura_match.get("resumo") or []
                    if not ler_it.get("pontos") and leitura_match.get("pontos"):
                        ler_it["pontos"] = leitura_match["pontos"]
                    if not ler_it.get("citacao") and leitura_match.get("citacao"):
                        ler_it["citacao"] = leitura_match["citacao"]
                    if not ler_it.get("autor") and leitura_match.get("autor"):
                        ler_it["autor"] = leitura_match["autor"]
                    if not ler_it.get("data") and leitura_match.get("data"):
                        ler_it["data"] = leitura_match["data"]

        shard_sem_path = os.path.join(semanas_dir, f"{s_id}.json")
        with open(shard_sem_path, "w", encoding="utf-8") as f:
            json.dump(s_obj, f, ensure_ascii=False, separators=(",", ":"))

        semanas_index.append({
            "id": s_id,
            "inicio": s_obj.get("inicio", ""),
            "fim": s_obj.get("fim", s_id),
            "titulo": s_obj.get("titulo", ""),
            "total_temas": len(s_obj.get("temas", [])),
            "shard": f"data/semanas/{s_id}.json",
        })

    # ---------------------------------------------------------
    # 3. GERAR SHARDS DE CULTURA MENSAL & ÍNDICE DO ARQUIVO
    # ---------------------------------------------------------
    config_cultura = [
        ("musica", "edicoes", "itens", "guias", "albuns", "música", "Música"),
        ("cinema", "cine_edicoes", "cine_itens", "cine_guias", "filmes", "cinema", "Cinema"),
        ("livros", "livro_edicoes", "livro_itens", "livro_guias", "livros", "livros", "Livros"),
    ]
    edicoes_index = {"musica": [], "cinema": [], "livros": []}
    arquivo_entradas = []
    contagem_criticas_embutidas = 0

    for prefixo, col_ed, col_it, col_guia, chave_lista_guia, rot_rev, rot_ed in config_cultura:
        edicoes_map = db.get(col_ed, {})
        itens_map = db.get(col_it, {})
        guias_map = db.get(col_guia, {})

        # Ordenar edições da mais recente para a mais antiga para o índice do arquivo
        chaves_meses = sorted(list(edicoes_map.keys()))
        for mes_id in chaves_meses:
            ed_obj = copy.deepcopy(edicoes_map[mes_id])
            itens_mes = {}
            guias_mes = {}

            for item_id, item_val in itens_map.items():
                if item_val.get("edicao") == mes_id:
                    it_copy = copy.deepcopy(item_val)
                    contagem_criticas_embutidas += _enriquecer_item_cultural(it_copy, item_id, por_ref, por_url)
                    itens_mes[item_id] = it_copy

            for guia_id, guia_val in guias_map.items():
                if guia_val.get("edicao") == mes_id:
                    g_copy = copy.deepcopy(guia_val)
                    for idx_g, g_it in enumerate(g_copy.get(chave_lista_guia) or []):
                        if isinstance(g_it, dict):
                            contagem_criticas_embutidas += _enriquecer_item_cultural(g_it, f"{guia_id}~{idx_g}", por_ref, por_url)
                    guias_mes[guia_id] = g_copy

            shard_rel = f"data/cultura/{prefixo}_{mes_id}.json"
            pacote_cultura = {
                "eixo": prefixo,
                "mes_id": mes_id,
                "edicao": ed_obj,
                "itens": itens_mes,
                "guias": guias_mes,
            }
            shard_cult_path = os.path.join(cultura_dir, f"{prefixo}_{mes_id}.json")
            with open(shard_cult_path, "w", encoding="utf-8") as f:
                json.dump(pacote_cultura, f, ensure_ascii=False, separators=(",", ":"))

            edicoes_index[prefixo].append({
                "id": mes_id,
                "data": ed_obj.get("data", mes_id),
                "numero": ed_obj.get("numero"),
                "mes": ed_obj.get("mes", mes_id),
                "manchete": ed_obj.get("manchete", ""),
                "capa": ed_obj.get("capa", ""),
                "total_itens": len(itens_mes),
                "total_guias": len(guias_mes),
                "tem_destaque_autor": bool(ed_obj.get("destaque_autor") or ed_obj.get("retrato_autor")),
                "shard": shard_rel,
            })

        # Construir entradas de arquivo na ordem exata de leitura (edições mais recentes primeiro)
        for mes_id in sorted(chaves_meses, key=lambda m: str(edicoes_map[m].get("data") or m), reverse=True):
            ed_obj = edicoes_map[mes_id]
            ed_label = f"Nº {ed_obj.get('numero', '')} · {ed_obj.get('mes', mes_id)}"
            shard_rel = f"data/cultura/{prefixo}_{mes_id}.json"
            itens_lista = sorted(
                [(iid, iv) for iid, iv in itens_map.items() if iv.get("edicao") == mes_id],
                key=lambda par: par[1].get("ordem", 0) or 0,
            )
            dest = next(((iid, iv) for iid, iv in itens_lista if iv.get("destaque")), None)

            def _empacotar_entrada(key, obj_a, ctx):
                if prefixo == "musica":
                    t1 = str(obj_a.get("album") or "")
                    t2 = str(obj_a.get("exibir_artista") or obj_a.get("artista") or "")
                    artista_idx = str(obj_a.get("artista") or t2)
                    tipo_ic = ""
                else:
                    t1 = str(obj_a.get("titulo") or "")
                    autor_s = str(obj_a.get("autor") or "")
                    ano_s = str(obj_a.get("ano") or "")
                    t2 = ", ".join(x for x in (autor_s, ano_s) if x)
                    artista_idx = autor_s
                    tipo_ic = str(obj_a.get("tipo") or "")

                resenha_str = " ".join(str(p) for p in (obj_a.get("resenha") or []))
                generos_str = " ".join(str(g) for g in (obj_a.get("generos") or []))
                busca_txt = nrm_busca(" ".join([
                    t1, t2, str(obj_a.get("titulo_original") or ""),
                    str(obj_a.get("genero") or ""), generos_str,
                    str(obj_a.get("pais") or ""), str(obj_a.get("onde") or ""),
                    ctx, ed_label, rot_rev, resenha_str[:600], str(obj_a.get("linha_fina") or ""),
                ]))
                return {
                    "key": key,
                    "eixo": prefixo,
                    "mes_id": mes_id,
                    "shard": shard_rel,
                    "rev": rot_rev,
                    "ed": ed_label,
                    "ctx": ctx,
                    "t1": t1,
                    "t2": t2,
                    "artista": artista_idx,
                    "titulo_original": str(obj_a.get("titulo_original") or ""),
                    "capa": str(obj_a.get("capa") or obj_a.get("imagem") or ""),
                    "_tipo": tipo_ic,
                    "busca": busca_txt,
                }

            if dest:
                ctx_d = "Matéria de capa" if prefixo == "musica" else f"{rot_ed} · matéria de capa"
                arquivo_entradas.append(_empacotar_entrada(dest[0], dest[1], ctx_d))

            for bloco in ed_obj.get("layout") or []:
                b_tipo = bloco.get("tipo")
                if b_tipo == "secao":
                    sec_k = bloco.get("secao", "")
                    tit_sec = SECOES_TITULOS.get(prefixo, {}).get(sec_k, sec_k)
                    ctx_s = tit_sec if prefixo == "musica" else f"{rot_ed} · {tit_sec}"
                    for iid, iv in itens_lista:
                        if iv.get("secao") == sec_k and (not dest or iid != dest[0]):
                            arquivo_entradas.append(_empacotar_entrada(iid, iv, ctx_s))
                elif b_tipo == "guia":
                    g_id = bloco.get("id")
                    g_obj = guias_map.get(g_id)
                    if g_obj:
                        lista_g = g_obj.get(chave_lista_guia) or []
                        for idx_g, a_g in enumerate(lista_g):
                            ctx_g = f"Guia · {g_obj.get('titulo', '')} · {idx_g + 1} de {len(lista_g)}"
                            arquivo_entradas.append(_empacotar_entrada(f"{g_id}~{idx_g}", a_g, ctx_g))

    arquivo_index_path = os.path.join(base_dir, "arquivo_index.json")
    with open(arquivo_index_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "versao_dados": versao_dados,
                "total": len(arquivo_entradas),
                "cultura_curta": db.get("cultura", {}),
                "entradas": arquivo_entradas,
            },
            f,
            ensure_ascii=False,
            separators=(",", ":"),
        )

    # ---------------------------------------------------------
    # 4. GERAR data/boot.json (< 150 KB)
    # ---------------------------------------------------------
    id_recente = chaves_dias[-1] if chaves_dias else None
    hoje_inicial = compactar_hoje_para_boot(id_recente, dias[id_recente]) if id_recente else {}
    agenda_boot = compactar_agenda_para_boot(db.get("agenda", {}))

    agora_iso = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).isoformat()
    boot_obj = {
        "versao": "2.1",
        "versao_dados": versao_dados,
        "gerado_em": agora_iso,
        "hoje_id": id_recente,
        "dias_index": list(reversed(dias_index)),
        "semanas_index": list(reversed(semanas_index)),
        "edicoes_index": {k: list(reversed(v)) for k, v in edicoes_index.items()},
        "hoje_inicial": hoje_inicial,
        "agenda": agenda_boot,
    }

    boot_path = os.path.join(base_dir, "boot.json")
    with open(boot_path, "w", encoding="utf-8") as f:
        json.dump(boot_obj, f, ensure_ascii=False, separators=(",", ":"))

    tamanho_boot = os.path.getsize(boot_path)
    if tamanho_boot > 148 * 1024 and isinstance(boot_obj["hoje_inicial"].get("jornais"), dict):
        jornais_boot = boot_obj["hoje_inicial"]["jornais"]
        for m in jornais_boot.get("manchetes", []):
            m["resumo_edicao"] = []
            nota_m = str(m.get("nota") or "")
            if len(nota_m) > 160:
                m["nota"] = nota_m[:157] + "..."
            ed = m.get("editorial")
            if isinstance(ed, dict):
                ed.pop("texto", None)
                if ed.get("texto_integral"):
                    ed["texto_integral"] = [str(ed["texto_integral"][0])[:100]]
            for rep in m.get("reportagens", []):
                rep.pop("pontos", None)
                rep.pop("texto", None)
                rep.pop("citacao", None)
                rep.pop("lide", None)
                rep.pop("titulo_original", None)
                # Preserva stub de 1 elemento <=145 chars para manter hidratação automática em abrirJornalCompleto()
                if rep.get("texto_integral"):
                    rep["texto_integral"] = [""]
        jornais_boot["leitura"] = []
        with open(boot_path, "w", encoding="utf-8") as f:
            json.dump(boot_obj, f, ensure_ascii=False, separators=(",", ":"))
        tamanho_boot = os.path.getsize(boot_path)

    if tamanho_boot > 148 * 1024 and isinstance(boot_obj.get("dias_index"), list):
        for idx_d, d_meta in enumerate(boot_obj["dias_index"]):
            if idx_d >= 10:
                tit_d = str(d_meta.get("titulo") or "")
                if len(tit_d) > 96:
                    d_meta["titulo"] = tit_d[:93] + "..."
        with open(boot_path, "w", encoding="utf-8") as f:
            json.dump(boot_obj, f, ensure_ascii=False, separators=(",", ":"))
        tamanho_boot = os.path.getsize(boot_path)

    if tamanho_boot > 148 * 1024 and isinstance(boot_obj["hoje_inicial"].get("notas"), list):
        for n in boot_obj["hoje_inicial"]["notas"]:
            tc = n.get("texto_completo")
            if isinstance(tc, list) and len(tc) > 1:
                n["texto_completo"] = tc[:1]
        with open(boot_path, "w", encoding="utf-8") as f:
            json.dump(boot_obj, f, ensure_ascii=False, separators=(",", ":"))
        tamanho_boot = os.path.getsize(boot_path)

    return {
        "boot_path": boot_path,
        "boot_bytes": tamanho_boot,
        "arquivo_index_bytes": os.path.getsize(arquivo_index_path),
        "arquivo_total": len(arquivo_entradas),
        "dias_shards": len(dias_index),
        "semanas_shards": len(semanas_index),
        "cultura_shards": sum(len(v) for v in edicoes_index.values()),
        "criticas_embutidas": contagem_criticas_embutidas,
    }


def main():
    print("=== INICIANDO PARTICIONAMENTO DE DADOS V2.1 (FAIXA OCULTA) ===")
    res = particionar_dados()
    print(f"  [OK] data/boot.json gerado          : {res['boot_bytes']:,} bytes ({res['boot_bytes']/1024:.1f} KB — meta < 150 KB)")
    print(f"  [OK] data/arquivo_index.json gerado : {res['arquivo_index_bytes']:,} bytes ({res['arquivo_index_bytes']/1024:.1f} KB · {res['arquivo_total']} títulos)")
    print(f"  [OK] Shards em data/dias/           : {res['dias_shards']} arquivos")
    print(f"  [OK] Shards em data/semanas/        : {res['semanas_shards']} arquivos")
    print(f"  [OK] Shards em data/cultura/        : {res['cultura_shards']} arquivos")
    print(f"  [OK] Críticas embutidas nos itens   : {res['criticas_embutidas']}")
    print("=== PARTICIONAMENTO CONCLUÍDO COM SUCESSO! ===")


if __name__ == "__main__":
    main()
