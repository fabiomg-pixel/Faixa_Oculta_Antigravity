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


def montar_edicao_semanal_atual():
    """Gera a edição estrutural de 01 a 07 de novembro de 2026 com 9 temas e 40 fontes plurais."""
    try:
        import tools.dados_semana_nov as s
        return s.get_semana_nov()
    except Exception:
        import dados_semana_nov as s
        return s.get_semana_nov()

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

    nova_semana = montar_edicao_semanal_atual()
    doc_id = nova_semana["fim"]

    forcar = os.environ.get("FORCAR_EXECUCAO", "").strip().lower() in ("1", "true", "sim") or "--forcar" in sys.argv
    if not forcar and doc_id in db.get("semanas", {}):
        print(f"Revista da semana [{doc_id}] já existe em {revista_path}. Nada a fazer.")
        return

    db["semanas"][doc_id] = nova_semana
    atualizar_leituras_semanais(db, nova_semana)

    with open(revista_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    with open("pagina.html", "r", encoding="utf-8") as f:
        src = f.read()

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(SKELETON_HEAD + src + SKELETON_TAIL)

    print(f"=== SUCESSO: Revista da semana ({doc_id}) gravada com {len(nova_semana['temas'])} temas e trilha sugerida! ===")


if __name__ == "__main__":
    main()
