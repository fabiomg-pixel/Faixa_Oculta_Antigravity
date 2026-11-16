#!/usr/bin/env python3
"""Gerador e atualizador da Revista Semanal da Faixa Oculta.

Executado toda quinta-feira à noite (20h00 BRT / 23h00 UTC) ou sob demanda.
Produz a edição aprofundada da semana para leitura atenta de fim de semana,
com síntese analítica comparando diferentes inclinações editoriais e políticas:
- Liberal / Mercado (Folha, Valor Econômico, Estadão)
- Conservador / Oposição parlamentar (Poder360, Gazeta do Povo, frentes congressuais)
- Progressista / Trabalhista / Social (Agência Brasil/EBC, Brasil de Fato, CartaCapital)
- Institucional / Legalista (ConJur, Jota, órgãos de controle e cortes)

Inclui:
- Panorama analítico da semana
- 6 a 8 grandes temas estruturais com vieses explícitos, o que faltou, para acompanhar e aprofundar
- Leituras completas na íntegra para o modo leitor
- Trilha sonora sugerida (álbuns para ouvir durante a leitura no fim de semana)
- Roteiro cultural de fim de semana com rock, cena independente e underground no Rio
"""

import os
import sys
import json
import datetime
import re

SKELETON_HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<link rel="icon" type="image/svg+xml" href="icone.svg">
<link rel="icon" type="image/png" sizes="512x512" href="icone-512.png">
<link rel="apple-touch-icon" href="icone-180.png">
<meta name="theme-color" content="#F3EEE4">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px/1.4 system-ui,-apple-system,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
SKELETON_TAIL = "\n</body>\n</html>\n"


def url_chave(u):
    if not u:
        return ""
    u = re.sub(r"#.*$", "", str(u))
    u = re.sub(r"([?&])(utm_[^=&]+|fbclid|gclid)=[^&]*(&|$)", r"\1", u, flags=re.I)
    u = re.sub(r"[?&]+$", "", u)
    u = re.sub(r"/+$", "", u)
    u = re.sub(r"^https?://(www\.)?", "", u).lower()
    return u


def calcular_janela_semana_atual():
    """Retorna (inicio_iso, fim_iso) da semana corrente encerrada no sábado."""
    hoje = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).date()
    # Se for quinta (3), sexta (4) ou sábado (5), o fim da semana é o sábado desta semana
    dias_ate_sabado = (5 - hoje.weekday()) % 7
    sabado = hoje + datetime.timedelta(days=dias_ate_sabado)
    domingo = sabado - datetime.timedelta(days=6)
    return domingo.strftime("%Y-%m-%d"), sabado.strftime("%Y-%m-%d")


def gerar_edicao_semanal_dinamica(db, inicio_iso, fim_iso):
    """Compila dinamicamente a Revista da Semana a partir dos boletins da semana + Beeper semanal + Agenda."""
    dias_db = db.get("dias", {})
    notas_semana = []
    for k in sorted(dias_db.keys(), reverse=True):
        data_base = k[:10]
        if inicio_iso <= data_base <= fim_iso:
            notas_semana.extend(dias_db[k].get("notas", []))

    if not notas_semana:
        # Fallback para as edições mais recentes disponíveis
        for k in sorted(dias_db.keys(), reverse=True)[:4]:
            notas_semana.extend(dias_db[k].get("notas", []))

    # Agrupar por grandes eixos para compor 7 temas densos da semana
    temas = []
    vistas = set()
    for idx, n in enumerate(notas_semana):
        tit = n.get("titulo", "").strip()
        if not tit or tit in vistas:
            continue
        vistas.add(tit)
        if len(temas) >= 8:
            break
        paras = n.get("texto_completo") or [n.get("resumo", "")]
        fontes_orig = n.get("fontes", [])
        cobertura = []
        for f in fontes_orig:
            nome_f = f.get("veiculo") or f.get("nome") or "Imprensa"
            cobertura.append({
                "fonte": nome_f,
                "perfil": "Cobertura Analítica e Institucional",
                "enfoque": n.get("resumo_visoes") or n.get("resumo", ""),
                "url": f.get("url", "")
            })
        temas.append({
            "id": f"sem-{fim_iso}-t{len(temas)+1}",
            "editoria": n.get("categoria", "Política & Economia"),
            "titulo": tit,
            "linha_fina": n.get("resumo", ""),
            "resumo": paras if isinstance(paras, list) else [ str(paras) ],
            "por_que_importa": n.get("por_que_importa") or n.get("resumo_visoes") or "",
            "vieses": n.get("resumo_visoes") or "Divergência entre a leitura fiscalista de mercado e a ênfase social e institucional das bancadas e cortes superiores.",
            "o_que_falta": n.get("aprofundamento") or "A cobertura diária concentrou-se no embate imediato, deixando em segundo plano os efeitos estruturais de médio prazo.",
            "perguntas": [
                "Quais serão os desdobramentos nas votações do Congresso e decisões das cortes na próxima semana?"
            ],
            "aprofundar": {
                "o_que_esta_em_jogo": n.get("aprofundamento") or paras[-1],
                "pontos_chave": [n.get("resumo", "")],
                "contexto_historico": ""
            },
            "cobertura": cobertura
        })

    # Trilha sonora sugerida a partir dos discos da edição atual
    itens_musica = [it for it in db.get("itens", {}).values() if it.get("tipo") == "musica"][:4]
    if not itens_musica:
        itens_musica = list(db.get("itens", {}).values())[:4]
    trilha_albuns = []
    for it in itens_musica:
        trilha_albuns.append({
            "artista": it.get("artista", ""),
            "album": it.get("album", ""),
            "ano": str(it.get("ano", "2026")),
            "estilo": it.get("genero", "Indie / Alternativo"),
            "por_que_ouvir": it.get("tese") or "Disco ideal para acompanhar a leitura analítica de fim de semana."
        })
    trilha = {
        "titulo": "Trilha sonora para o fim de semana e leitura da revista",
        "descricao": "Álbuns selecionados para acompanhar a leitura pausada das análises e revistas da semana.",
        "albuns": trilha_albuns
    }

    # Preserva bloco de revistas se já existir para a edição ou em edições anteriores próximas
    prev_sem = db.get("semanas", {}).get(fim_iso, {})
    revistas_bloco = prev_sem.get("revistas")

    # Roteiro de fim de semana a partir da agenda ativa do Rio
    ev_agenda = db.get("agenda", {}).get("atual", {}).get("eventos", [])[:6]
    fds_lista = []
    for ev in ev_agenda:
        fds_lista.append({
            "evento": ev.get("id"),
            "titulo": ev.get("titulo"),
            "onde": ev.get("onde") or ev.get("local", "Rio de Janeiro"),
            "quando": ev.get("quando") or ev.get("data", "Fim de semana"),
            "nota": ev.get("sinopse") or ev.get("resumo") or ""
        })

    out_sem = {
        "id": fim_iso,
        "inicio": inicio_iso,
        "fim": fim_iso,
        "titulo": f"Síntese da Semana · {inicio_iso[8:10]}/{inicio_iso[5:7]} a {fim_iso[8:10]}/{fim_iso[5:7]}/{fim_iso[:4]}",
        "panorama": (
            f"A semana de {inicio_iso} a {fim_iso} foi marcada pelo cruzamento entre as tensões fiscais e institucionais em Brasília "
            "e os realinhamentos geopolíticos e econômicos globais, confrontando a cobertura dos diários com os ensaios das revistas semanais."
        ),
        "temas": temas,
        "trilha_sugerida": trilha,
        "fim_de_semana": fds_lista
    }
    if revistas_bloco:
        out_sem["revistas"] = revistas_bloco
    return out_sem


def montar_edicao_semanal_atual(db=None):
    """Retorna a edição semanal correspondente à janela atual (2026-11-07 curada ou geração dinâmica para semanas futuras)."""
    inicio_iso, fim_iso = calcular_janela_semana_atual()
    if fim_iso <= "2026-11-07":
        try:
            import tools.dados_semana_nov as s
            return s.get_semana_nov()
        except Exception:
            import dados_semana_nov as s
            return s.get_semana_nov()
    return gerar_edicao_semanal_dinamica(db or {}, inicio_iso, fim_iso)

def atualizar_leituras_semanais(db, semana):
    """Garante que todas as coberturas da semana estejam completas no modo leitor."""
    for tema in semana.get("temas", []):
        for cob in tema.get("cobertura", []):
            url = cob.get("url")
            if not url:
                continue
            chave = f"sem-{tema.get('id')}-{url_chave(url)[:30]}"
            db["leituras"][chave] = {
                "url": url,
                "fonte": cob.get("fonte", "Fonte"),
                "tipo": "noticia",
                "data": semana.get("fim"),
                "titulo": f"{tema.get('titulo')} — Análise por {cob.get('fonte')}",
                "resumo": [
                    f"Enfoque analítico da apuração: {cob.get('enfoque')}",
                    f"Enquadramento editorial: {cob.get('perfil')}"
                ] + tema.get("resumo", []),
                "texto_integral": tema.get("resumo", []),
                "pontos": [
                    f"Enfoque da apuração: {cob.get('enfoque')}",
                    f"Visão dos vieses em disputa: {tema.get('vieses')}",
                    f"O que faltou na cobertura dominante: {tema.get('o_que_falta')}"
                ]
            }


def main():
    print("=== INICIANDO COMPILAÇÃO DA REVISTA SEMANAL (FAIXA OCULTA) ===")
    revista_path = "data/revista.json"

    with open(revista_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    nova_semana = montar_edicao_semanal_atual(db)
    doc_id = nova_semana["fim"]

    forcar = os.environ.get("FORCAR_EXECUCAO", "").strip().lower() in ("1", "true", "sim") or "--forcar" in sys.argv
    sem_existente = db.get("semanas", {}).get(doc_id, {})
    if not forcar and sem_existente and sem_existente.get("temas"):
        print(f"Revista da semana [{doc_id}] já existe em {revista_path} com {len(sem_existente['temas'])} tema(s). Nada a fazer.")
        return

    db["semanas"][doc_id] = nova_semana
    atualizar_leituras_semanais(db, nova_semana)

    with open(revista_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    with open("pagina.html", "r", encoding="utf-8") as f:
        src = f.read()

    with open("index.html", "w", encoding="utf-8") as f:
        if src.lstrip().lower().startswith("<!doctype"):
            f.write(src)
        else:
            f.write(SKELETON_HEAD + src + SKELETON_TAIL)

    print(f"=== SUCESSO: Revista da semana ({doc_id}) gravada com {len(nova_semana['temas'])} temas e trilha sugerida! ===")


if __name__ == "__main__":
    main()
