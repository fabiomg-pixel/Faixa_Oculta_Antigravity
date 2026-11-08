#!/usr/bin/env python3
"""
tools/injetar_jornais_edicao_atual.py
-------------------------------------
Injeta a 'Banca de Jornais do Dia' e o acesso direto aos PDFs impressos
na edição atual (2026-11-08) em data/revista.json.
"""

import json
import os

REVISTA_JSON = "data/revista.json"

JORNAIS_DATA = {
    "data_edicao": "2026-11-08",
    "resumo": "Edições impressas integrais apuradas nas primeiras horas deste domingo, 8 de novembro de 2026. Os 8 principais diários nacionais e internacionais estão baixados no Mac e disponíveis na íntegra.",
    "contraste": "Enquanto Folha de S.Paulo e Estadão dedicam suas manchetes à corrida energética na Margem Equatorial e ao impasse político em Israel, The Washington Post e Financial Times analisam a recomposição geopolítica global e os desdobramentos sobre bancos centrais e política externa.",
    "manchetes": [
        {
            "jornal": "Folha de S.Paulo",
            "pais": "Brasil",
            "escopo": "nacional",
            "manchete": "Presidente de Israel escolhe oposição para tentar formar novo governo",
            "nota": "Isaac Herzog designa Gadi Eisenkot, principal rival de Netanyahu e ex-chefe militar. Cadernos de Poder, Mercado, Cotidiano e Ilustrada na íntegra.",
            "imagem": "capas/c9bacc2fca63fe56b371beec3bede644.jpg",
            "pagina": "jornais/2026-11-08-Folha-de-SPaulo.pdf",
            "pdf_url": "jornais/2026-11-08-Folha-de-SPaulo.pdf",
            "site": "https://www.folha.uol.com.br",
            "tamanho_mb": 50.0,
            "total_paginas": 52
        },
        {
            "jornal": "O Estado de S. Paulo",
            "pais": "Brasil",
            "escopo": "nacional",
            "manchete": "Corrida em torno do petróleo no extremo norte atrai investimento e expõe desafios",
            "nota": "Especial de abertura do caderno Economia & Negócios sobre a Margem Equatorial, pressões fiscais e transição energética. Caderno Opinião com editorial estrutural.",
            "imagem": "capas/2f684ae3bf05a8443187bd01fda31792.jpg",
            "pagina": "jornais/2026-11-08-O-Estado-de-S-Paulo.pdf",
            "pdf_url": "jornais/2026-11-08-O-Estado-de-S-Paulo.pdf",
            "site": "https://www.estadao.com.br",
            "tamanho_mb": 15.4,
            "total_paginas": 56
        },
        {
            "jornal": "O Globo",
            "pais": "Brasil",
            "escopo": "nacional",
            "manchete": "Ajuste fiscal, governabilidade e o cenário de reformas estruturais",
            "nota": "Artigos exclusivos de Demétrio Magnoli e Carlos Alberto Sardenberg na página 3 de Opinião. Cadernos de Economia, País e suplemento Ela.",
            "imagem": "capas/6fab3f67898cb8d4a34987de51cc8096.jpg",
            "pagina": "jornais/2026-11-08-O-Globo.pdf",
            "pdf_url": "jornais/2026-11-08-O-Globo.pdf",
            "site": "https://oglobo.globo.com",
            "tamanho_mb": 48.0,
            "total_paginas": 45
        },
        {
            "jornal": "Valor Econômico",
            "pais": "Brasil",
            "escopo": "nacional",
            "manchete": "Mercado calibra Selic e curva de juros pressiona Fazenda por corte estrutural",
            "nota": "Edição de fim de semana (número 6625). Análise das contas públicas, balança comercial e o caderno cultural EU& com ensaios.",
            "imagem": "capas/f7ca66c665dded5afed2d18e4326f3be.jpg",
            "pagina": "jornais/2026-11-08-Valor-Econômico.pdf",
            "pdf_url": "jornais/2026-11-08-Valor-Econômico.pdf",
            "site": "https://valor.globo.com",
            "tamanho_mb": 40.5,
            "total_paginas": 58
        },
        {
            "jornal": "The Washington Post",
            "pais": "Estados Unidos",
            "escopo": "internacional",
            "manchete": "Democracy Dies in Darkness · The National & Global Outlook",
            "nota": "Edição dominical completa (Sunday, Nov 8, 2026). Tabuleiro geopolítico do Congresso americano, diplomacia externa e cobertura aprofundada.",
            "imagem": "capas/b5d4af1c3eb955d1290f64e6e01a5050.jpg",
            "pagina": "jornais/2026-11-08-The-Washington-Post.pdf",
            "pdf_url": "jornais/2026-11-08-The-Washington-Post.pdf",
            "site": "https://www.washingtonpost.com",
            "tamanho_mb": 27.3,
            "total_paginas": 78
        },
        {
            "jornal": "The Guardian",
            "pais": "Reino Unido",
            "escopo": "internacional",
            "manchete": "European security pact, British politics and the public sector reform",
            "nota": "Edição completa de sábado/domingo (212 páginas). Cadernos de Opinião Internacional, Economia Europeia, Revista Feast e Cultura.",
            "imagem": "capas/2e1aa3fcbbfbf326be665fcd38725cf1.jpg",
            "pagina": "jornais/2026-11-08-The-Guardian.pdf",
            "pdf_url": "jornais/2026-11-08-The-Guardian.pdf",
            "site": "https://www.theguardian.com",
            "tamanho_mb": 83.5,
            "total_paginas": 212
        },
        {
            "jornal": "Financial Times",
            "pais": "Reino Unido / EUA",
            "escopo": "internacional",
            "manchete": "Where now for America? Simon Schama on the great course correction",
            "nota": "FT Weekend completo (edição de 7 e 8 de novembro de 2026). Macroeconomia global, política monetária, mercados e o suplemento cultural HTSI.",
            "imagem": "capas/eacada5fa80b94df678e21bc519a80a6.jpg",
            "pagina": "jornais/2026-11-08-Financial-Times.pdf",
            "pdf_url": "jornais/2026-11-08-Financial-Times.pdf",
            "site": "https://www.ft.com",
            "tamanho_mb": 95.3,
            "total_paginas": 56
        },
        {
            "jornal": "The Times UK",
            "pais": "Reino Unido",
            "escopo": "internacional",
            "manchete": "The Sunday Times: Westminster politics and the international chessboard",
            "nota": "Edição monumental de domingo (352 páginas). Panorama político britânico, análises de Katy Balls e caderno internacional.",
            "imagem": "capas/e6fb42aa821ecc16ae643f00033b8152.jpg",
            "pagina": "jornais/2026-11-08-The-Times-UK.pdf",
            "pdf_url": "jornais/2026-11-08-The-Times-UK.pdf",
            "site": "https://www.thetimes.co.uk",
            "tamanho_mb": 105.6,
            "total_paginas": 352
        }
    ],
    "leitura": [
        {
            "jornal": "O Estado de S. Paulo",
            "titulo": "Margem Equatorial: Os dilemas econômicos e ambientais da nova fronteira petrolífera",
            "pagina": "B1 a B3",
            "nota": "Caderno Economia & Negócios · Análise detalhada no PDF do Estadão."
        },
        {
            "jornal": "O Globo",
            "titulo": "Artigos de Demétrio Magnoli e Carlos Alberto Sardenberg sobre os rumos institucionais",
            "pagina": "Opinião, p. 3",
            "nota": "Disponível na íntegra no PDF arquivado de O Globo."
        },
        {
            "jornal": "Financial Times",
            "titulo": "Simon Schama: The mother of all course corrections in Western politics",
            "pagina": "p. 9 (FT Weekend)",
            "nota": "Ensaio imperdível de fim de semana sobre os rumos das democracias liberais."
        },
        {
            "jornal": "Folha de S.Paulo",
            "titulo": "Presidente de Israel e o dilema militar: a escolha de Gadi Eisenkot",
            "pagina": "Mundo, p. 1 e A12",
            "nota": "Reportagem aprofundada de bastidores diplomáticos e defesa."
        }
    ]
}


def main():
    if not os.path.exists(REVISTA_JSON):
        print(f"Erro: {REVISTA_JSON} não encontrado.")
        return

    with open(REVISTA_JSON, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Injetar em 2026-11-08
    dias = db.setdefault("dias", {})
    if "2026-11-08" in dias:
        edicao_hoje = dias["2026-11-08"]
        edicao_hoje["jornais"] = JORNAIS_DATA
        print("Bloco 'jornais' injetado com sucesso na edição 2026-11-08!")

        # Mapear PDFs nas notas correspondentes de hoje
        pdf_map = {
            "Folha": "jornais/2026-11-08-Folha-de-SPaulo.pdf",
            "Estadão": "jornais/2026-11-08-O-Estado-de-S-Paulo.pdf",
            "Estado de S. Paulo": "jornais/2026-11-08-O-Estado-de-S-Paulo.pdf",
            "Globo": "jornais/2026-11-08-O-Globo.pdf",
            "Valor": "jornais/2026-11-08-Valor-Econômico.pdf",
            "Washington Post": "jornais/2026-11-08-The-Washington-Post.pdf",
            "Guardian": "jornais/2026-11-08-The-Guardian.pdf",
            "Financial Times": "jornais/2026-11-08-Financial-Times.pdf",
            "Times": "jornais/2026-11-08-The-Times-UK.pdf"
        }

        atualizadas = 0
        for n in edicao_hoje.get("notas", []):
            tit_txt = f"{n.get('titulo', '')} {n.get('chapeu', '')} {n.get('texto', '')}"
            for k, pdf_path in pdf_map.items():
                if k.lower() in tit_txt.lower() or any(k.lower() in str(f.get("fonte", "")).lower() for f in n.get("fontes", [])):
                    n["url_pdf"] = pdf_path
                    n["jornal_pdf_nome"] = k
                    atualizadas += 1
                    break
        print(f"Total de notas vinculadas a links de PDF originais: {atualizadas}")

    with open(REVISTA_JSON, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print("Salvo data/revista.json!")


if __name__ == "__main__":
    main()
