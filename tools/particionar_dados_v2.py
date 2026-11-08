#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Particionador de Dados da Arquitetura v2 da Faixa Oculta (tools/particionar_dados_v2.py).

Lê `data/revista.json` (preservando-o intacto para retrocompatibilidade) e gera:
1. `data/boot.json` (< 150 KB):
   - `dias_index`: índice cronológico de todas as edições diárias disponíveis
   - `semanas_index`: índice de todas as edições da Revista da Semana
   - `edicoes_index`: índice das edições mensais de Música, Cinema e Livros
   - `hoje_inicial`: boletim diário mais recente pronto para renderização imediata
   - `agenda`: agenda cultural ativa do Rio, playlists e mapas de artistas
2. `data/dias/<id>.json`:
   - Cada edição diária isolada com 100% das notas, textos integrais das fontes (mesclados de `leituras`) e jornais completos.
3. `data/semanas/<id>.json`:
   - Cada edição semanal isolada com todas as coberturas enriquecidas a partir de `leituras`.
4. `data/cultura/musica_<YYYY-MM>.json`, `data/cultura/cinema_<YYYY-MM>.json`, `data/cultura/livros_<YYYY-MM>.json`:
   - Edição mensal completa (metadados da edição + `destaque_autor` + `itens` do mês + `guias` do mês),
     embutindo diretamente todas as críticas de `leituras` (`ref` / `url`) dentro de cada item para eliminar os 4,5 MB órfãos.
"""

import copy
import datetime
import json
import os
import re
import urllib.parse


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
        u = normalizar_url_chave(lv.get("url"))
        if u:
            por_url[u] = lv
    for ref_k in por_ref:
        por_ref[ref_k].sort(key=lambda x: x.get("ordem", 99))
    return por_ref, por_url


def compactar_hoje_para_boot(dia_id, dia_obj):
    """Prepara `hoje_inicial` para `data/boot.json`, mantendo 100% das notas e manchetes dentro do orçamento < 150 KB."""
    d = copy.deepcopy(dia_obj)
    d["id"] = dia_id

    # Nas notas do boot, `texto_completo` já está no nível da nota; detalhes repetidos de fontes ficam no shard completo
    for n in d.get("notas", []):
        for f in n.get("fontes", []):
            f.pop("texto_integral", None)
            f.pop("pontos", None)
            f.pop("citacao", None)

    # Em jornais do boot, preservamos todas as 8 capas, manchetes, editoriais, notas e títulos/lides das reportagens
    if isinstance(d.get("jornais"), dict):
        j = d["jornais"]
        j["shard_completo"] = f"data/dias/{dia_id}.json"
        for m in j.get("manchetes", []):
            for rep in m.get("reportagens", []):
                rep.pop("pontos", None)
                ti = rep.get("texto_integral") or []
                if len(ti) >= 1:
                    rep["texto_integral"] = [ti[0][:140]]
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

    # Coletar artistas ativos nos eventos e nas playlists atuais
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

    # Manter apenas as últimas 5 playlists em `anteriores` no boot
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
        db = json.load(f)

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

        # Embutir leituras completas dentro de cada fonte das notas
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
            for cob in tema.get("cobertura", []):
                u_key = normalizar_url_chave(cob.get("url"))
                leitura_match = por_url.get(u_key)
                if leitura_match:
                    if not cob.get("texto_integral"):
                        cob["texto_integral"] = leitura_match.get("texto_integral") or leitura_match.get("resumo") or []
                    if not cob.get("pontos") and leitura_match.get("pontos"):
                        cob["pontos"] = leitura_match["pontos"]
                    if not cob.get("citacao") and leitura_match.get("citacao"):
                        cob["citacao"] = leitura_match["citacao"]

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
    # 3. GERAR SHARDS DE CULTURA MENSAL (data/cultura/<eixo>_<YYYY-MM>.json)
    # ---------------------------------------------------------
    config_cultura = [
        ("musica", "edicoes", "itens", "guias"),
        ("cinema", "cine_edicoes", "cine_itens", "cine_guias"),
        ("livros", "livro_edicoes", "livro_itens", "livro_guias"),
    ]
    edicoes_index = {"musica": [], "cinema": [], "livros": []}
    contagem_criticas_embutidas = 0

    for prefixo, col_ed, col_it, col_guia in config_cultura:
        edicoes_map = db.get(col_ed, {})
        itens_map = db.get(col_it, {})
        guias_map = db.get(col_guia, {})

        for mes_id in sorted(list(edicoes_map.keys())):
            ed_obj = copy.deepcopy(edicoes_map[mes_id])
            itens_mes = {}
            guias_mes = {}

            for item_id, item_val in itens_map.items():
                if item_val.get("edicao") == mes_id:
                    it_copy = copy.deepcopy(item_val)
                    # Embutir críticas de `leituras` associadas por `ref == item_id` ou por URL
                    criticas_ref = copy.deepcopy(por_ref.get(item_id, []))
                    u_item = normalizar_url_chave(it_copy.get("fonte"))
                    if u_item and u_item in por_url:
                        cand_u = por_url[u_item]
                        if cand_u not in criticas_ref:
                            criticas_ref.append(copy.deepcopy(cand_u))

                    if criticas_ref:
                        it_copy["leituras_criticas"] = criticas_ref
                        contagem_criticas_embutidas += len(criticas_ref)
                        # Se o item (ex: safra 2026-10) não tinha `analises_criticas`, converte automaticamente
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
                    itens_mes[item_id] = it_copy

            for guia_id, guia_val in guias_map.items():
                if guia_val.get("edicao") == mes_id:
                    guias_mes[guia_id] = copy.deepcopy(guia_val)

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
                "numero": ed_obj.get("numero"),
                "mes": ed_obj.get("mes", mes_id),
                "data": ed_obj.get("data", ""),
                "manchete": ed_obj.get("manchete", ""),
                "capa": ed_obj.get("capa", ""),
                "total_itens": len(itens_mes),
                "total_guias": len(guias_mes),
                "tem_destaque_autor": bool(ed_obj.get("destaque_autor") or ed_obj.get("retrato_autor")),
                "shard": f"data/cultura/{prefixo}_{mes_id}.json",
            })

    # ---------------------------------------------------------
    # 4. GERAR data/boot.json (< 150 KB)
    # ---------------------------------------------------------
    id_recente = chaves_dias[-1] if chaves_dias else None
    hoje_inicial = compactar_hoje_para_boot(id_recente, dias[id_recente]) if id_recente else {}
    agenda_boot = compactar_agenda_para_boot(db.get("agenda", {}))

    agora_iso = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).isoformat()
    boot_obj = {
        "versao": "2.0",
        "gerado_em": agora_iso,
        "hoje_id": id_recente,
        "dias_index": list(reversed(dias_index)),
        "semanas_index": list(reversed(semanas_index)),
        "edicoes_index": edicoes_index,
        "hoje_inicial": hoje_inicial,
        "agenda": agenda_boot,
    }

    boot_path = os.path.join(base_dir, "boot.json")
    with open(boot_path, "w", encoding="utf-8") as f:
        json.dump(boot_obj, f, ensure_ascii=False, separators=(",", ":"))

    tamanho_boot = os.path.getsize(boot_path)
    # Caso o boletim inicial + jornais exceda 148 KB, enxuga os resumos secundários de reportagens no boot
    if tamanho_boot > 148 * 1024 and isinstance(boot_obj["hoje_inicial"].get("jornais"), dict):
        for m in boot_obj["hoje_inicial"]["jornais"].get("manchetes", []):
            for rep in m.get("reportagens", []):
                rep.pop("pontos", None)
                if rep.get("texto_integral"):
                    rep["texto_integral"] = [rep["texto_integral"][0][:220]]
        with open(boot_path, "w", encoding="utf-8") as f:
            json.dump(boot_obj, f, ensure_ascii=False, separators=(",", ":"))
        tamanho_boot = os.path.getsize(boot_path)

    return {
        "boot_path": boot_path,
        "boot_bytes": tamanho_boot,
        "dias_shards": len(dias_index),
        "semanas_shards": len(semanas_index),
        "cultura_shards": sum(len(v) for v in edicoes_index.values()),
        "criticas_embutidas": contagem_criticas_embutidas,
    }


def main():
    print("=== INICIANDO PARTICIONAMENTO DE DADOS V2 (FAIXA OCULTA) ===")
    res = particionar_dados()
    print(f"  [OK] data/boot.json gerado   : {res['boot_bytes']:,} bytes ({res['boot_bytes']/1024:.1f} KB — meta < 150 KB)")
    print(f"  [OK] Shards em data/dias/    : {res['dias_shards']} arquivos")
    print(f"  [OK] Shards em data/semanas/ : {res['semanas_shards']} arquivos")
    print(f"  [OK] Shards em data/cultura/ : {res['cultura_shards']} arquivos")
    print(f"  [OK] Críticas de 'leituras' embutidas nos itens culturais: {res['criticas_embutidas']}")
    print("=== PARTICIONAMENTO CONCLUÍDO COM SUCESSO! ===")


if __name__ == "__main__":
    main()
