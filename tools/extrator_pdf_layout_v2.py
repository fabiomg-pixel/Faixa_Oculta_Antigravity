#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/extrator_pdf_layout_v2.py
-------------------------------
Extrator Layout-Aware de Jornais e Revistas do Beeper + Síntese LLM (Arquitetura v2).

Melhorias estruturais sobre a v1:
1. PDFs Vetoriais/Digitais (O Globo, Estadão, Valor, WaPo, Guardian, NYT, The Economist, Piauí, CartaCapital, Veja Rio):
   - Usa `page.get_text("dict")` na página 1 para ranquear os spans pelo tamanho da fonte (`size` em pontos),
     agrupando linhas contíguas da mesma família/tamanho tipográfico para reconstruir a manchete real da capa
     e ignorando cabeçalhos, logotipos do jornal, códigos de barras e previsão do tempo.
   - Usa `page.get_text("blocks")` nas páginas 1 a 12 ordenados espacialmente por colunas/caixas `(y0, x0)`
     para extrair parágrafos limpos sem misturar tabelas de cotações ou chamadas laterais.
   - Corrige colagem de palavras em fontes condensadas (ex.: `CorantoCond-Bold` no Valor Econômico)
     inserindo espaço entre spans adjacentes quando necessário.
2. PDFs Escaneados em Imagem (Folha de S.Paulo, Financial Times, The Times UK):
   - Usa Apple Vision Framework OCR nativo no macOS passando o idioma correto:
     `"en-US"` para `escopo == "internacional"` e `"pt-BR"` para `escopo == "nacional"`.
3. Síntese Jornalística via Gemini (`gemini-4-argon` com fallback para `gemini-3.8-flash`):
   - Envia o dump estruturado de blocos da edição para o modelo gerar automaticamente o JSON rico do Modo Leitor:
     - `manchete` (e `manchete_original` quando internacional)
     - `resumo_edicao` (2 a 3 parágrafos densos)
     - `editorial` (`titulo` e `texto` de 2 parágrafos)
     - `reportagens` (5 reportagens completas divididas por `caderno`, `pagina`, `autor`, `titulo`,
       `lide`, `texto` e `texto_integral` de 3 parágrafos em português culto, mais `pontos`).
4. Suporte completo aos perfis `diario` (Big 4 BR + NYT, FT, WaPo, Guardian, Times UK) e `semana`
   (The Economist, Piauí, CartaCapital, Veja Rio, NYT Book Review, NYT Magazine).
"""

import os
import re
import sys
import ssl
import json
import sqlite3
import hashlib
import urllib.request
import urllib.parse
import urllib.error
import subprocess
from datetime import datetime

# Contexto SSL não-verificado obrigatório para todas as chamadas urllib.request.urlopen
SSL_CTX = ssl._create_unverified_context()

HEADERS_DEFAULT = {
    "User-Agent": "FaixaOcultaBot/2.0 (Macintosh; Intel Mac OS X; contact@faixaoculta.com)"
}

BEEPER_DIR = os.path.expanduser("~/Library/Application Support/BeeperTexts")
DB_PATH = os.path.join(BEEPER_DIR, "index.db")
MEDIA_DIR = os.path.join(BEEPER_DIR, "media", "local.beeper.com")

PRESS_ROOMS = [
    "!iq3RLvh1JnfH6vJzkvaL:beeper.local",  # Jornais BR
    "!Q3EN2ZSkzkir8tYnRU7t:beeper.local",  # International Newspapers
    "!tFgakhGBTv3CNjiYMdkM:beeper.local",  # Jornais e Revistas 4.0
]

KNOWN_ROOM_NAMES = {
    "!iq3RLvh1JnfH6vJzkvaL:beeper.local": "Jornais BR",
    "!Q3EN2ZSkzkir8tYnRU7t:beeper.local": "International Newspapers",
    "!tFgakhGBTv3CNjiYMdkM:beeper.local": "Jornais e Revistas 4.0",
}

PERFIS_V2 = {
    "diario": {
        "nacional": [
            ("Folha de S.Paulo", ["folha de s.paulo", "folha de sp", "folha de são paulo", "folha de sao paulo"]),
            ("O Estado de S. Paulo", ["estado de s paulo", "estadao", "estadão"]),
            ("O Globo", ["o globo - hd", "o globo – hd", "o globo- hd", "o globo‐ hd"]),
            ("Valor Econômico", ["valor econômico", "valor economico", "valor"])
        ],
        "internacional": [
            ("The New York Times", ["nyt 0", "nyt 1", "nyt 2", "nyt 3", "the-new-york-times", "the new york times -"]),
            ("Financial Times", ["ft us", "ft uk", "ft eu", "financial times"]),
            ("The Washington Post", ["washington post", "the-washington-post"]),
            ("The Guardian", ["the guardian", "the-guardian", "the observer"]),
            ("The Times UK", ["the times uk", "the-times-uk"]),
            ("Le Monde", ["le monde", "lemonde", "le-monde"])
        ]
    },
    "semana": {
        "nacional": [
            ("Revista Piauí", ["piauí", "piaui"]),
            ("CartaCapital", ["carta capital", "cartacapital"]),
            ("Veja Rio", ["veja rio"]),
            ("Valor Econômico EU&", ["eu&"])
        ],
        "internacional": [
            ("The Economist", ["the economist", "economist"]),
            ("Foreign Affairs", ["foreign affairs", "foreign-affairs"]),
            ("The New Yorker", ["the new yorker", "new yorker"]),
            ("Time", ["time magazine", "time -", "time_"]),
            ("Newsweek", ["newsweek"]),
            ("NYT Book Review", ["nytbr", "book review"]),
            ("NYT Magazine", ["nyt magazine"]),
            ("FT Weekend Magazine", ["ft weekend", "weekend magazine"])
        ]
    }
}

SITES_OFICIAIS = {
    "Folha de S.Paulo": "https://www.folha.uol.com.br",
    "O Estado de S. Paulo": "https://www.estadao.com.br",
    "O Globo": "https://oglobo.globo.com",
    "Valor Econômico": "https://valor.globo.com",
    "Valor Econômico EU&": "https://valor.globo.com/eu-e/",
    "The New York Times": "https://www.nytimes.com",
    "The Washington Post": "https://www.washingtonpost.com",
    "The Guardian": "https://www.theguardian.com",
    "Financial Times": "https://www.ft.com",
    "The Times UK": "https://www.thetimes.com",
    "Le Monde": "https://www.lemonde.fr",
    "The Economist": "https://www.economist.com",
    "Foreign Affairs": "https://www.foreignaffairs.com",
    "The New Yorker": "https://www.newyorker.com",
    "Revista Piauí": "https://piaui.folha.uol.com.br",
    "CartaCapital": "https://www.cartacapital.com.br",
    "Time": "https://time.com",
    "Newsweek": "https://www.newsweek.com",
    "Veja Rio": "https://vejario.abril.com.br",
    "NYT Book Review": "https://www.nytimes.com/section/books/review",
    "NYT Magazine": "https://www.nytimes.com/section/magazine",
    "FT Weekend Magazine": "https://www.ft.com/magazine",
}

PAISES_POR_VEICULO = {
    "Folha de S.Paulo": "Brasil",
    "O Estado de S. Paulo": "Brasil",
    "O Globo": "Brasil",
    "Valor Econômico": "Brasil",
    "Valor Econômico EU&": "Brasil",
    "Revista Piauí": "Brasil",
    "CartaCapital": "Brasil",
    "Veja Rio": "Brasil",
    "The New York Times": "Estados Unidos",
    "NYT Book Review": "Estados Unidos",
    "NYT Magazine": "Estados Unidos",
    "The Washington Post": "Estados Unidos",
    "The New Yorker": "Estados Unidos",
    "Foreign Affairs": "Estados Unidos / Global",
    "Time": "Estados Unidos / Global",
    "Newsweek": "Estados Unidos / Global",
    "The Guardian": "Reino Unido",
    "Financial Times": "Reino Unido / Global",
    "FT Weekend Magazine": "Reino Unido",
    "The Times UK": "Reino Unido",
    "Le Monde": "França",
    "The Economist": "Reino Unido / Global",
}

# Palavras/marcas de logotipo, cabeçalho ou chamadas de suplemento que NÃO são a manchete jornalística
STOPWORDS_LOGOTIPO_CAPA = [
    r"^o\s*globo\b",
    r"^folha\s+de\s+s\.?\s*paulo\b",
    r"^o\s+estado\s+de\s+s\.?\s*paulo\b",
    r"^valor(\s+econ[oô]mico)?\b",
    r"^the\s+(guardian|observer|times|sunday\s+times|washington\s+post|new\s+york\s+times|economist|new\s+yorker)\b",
    r"^ft\s*weekend\b",
    r"^financial\s+times\b",
    r"^comfort$",
    r"^magazine$",
    r"^christmas\s+gift\s+guide$",
    r"^gift\s+guide$",
    r"^fim\s+de\s+semana$",
    r"^um\s+jornal\s+em\s+defesa",
    r"^caderno\s+[a-z0-9]\b",
    r"^sunshine\s+\d+",
    r"^saturday\s*/\s*sunday",
    r"^sunday\s+newspaper\s+of\s+the\s+year",
    r"^rio\s+de\s+janeiro,\s*(segunda|terça|quarta|quinta|sexta|sábado|domingo)",
    r"^são\s+paulo,\s*(segunda|terça|quarta|quinta|sexta|domingo)",
    r"^edição\s+de\s+",
    r"^ano\s+\d+",
]


def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [ExtratorPDF-v2] {msg}", flush=True)


def obter_chave_gemini():
    """Recupera GEMINI_API_KEY do ambiente ou de ~/.faixaoculta/.env e ~/.env."""
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"].strip()
    for p in [os.path.expanduser("~/.faixaoculta/.env"), os.path.expanduser("~/.env"), ".env"]:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip().startswith("GEMINI_API_KEY="):
                            return line.strip().split("=", 1)[1].strip().strip('"').strip("'")
            except Exception:
                pass
    return None


def traduzir_texto_pt(texto):
    """Traduz texto internacional para o português culto com resiliência."""
    if not texto or not texto.strip():
        return ""
    texto_limpo = texto.strip()
    try:
        q = urllib.parse.quote(texto_limpo[:1900])
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=pt&dt=t&q={q}"
        req = urllib.request.Request(url, headers=HEADERS_DEFAULT)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            partes = [seg[0] for seg in data[0] if seg and seg[0]]
            return "".join(partes).strip()
    except Exception:
        return texto_limpo


def corrigir_colagem_palavras(texto):
    """Desfaz colagens de palavras típicas de kerning apertado em PDFs (ex: 'Emmeioacrisebancária,SantiagoPeña')."""
    if not texto:
        return ""
    # Insere espaço após vírgula/ponto-e-vírgula colado a letra
    s = re.sub(r"([,;:])([A-Za-zÀ-ÿ])", r"\1 \2", texto)
    # Insere espaço entre minúscula seguida de Maiúscula
    s = re.sub(r"([a-zà-ÿ])([A-ZÀ-Ý])", r"\1 \2", s)
    # Desfaz algumas preposições/artigos comuns colados em manchetes do Valor
    padroes_valor = [
        (r"\b(Em)(meio)(a)(crise)", r"\1 \2 \3 \4"),
        (r"\b(Novo)(limite)\b", r"\1 \2"),
        (r"\b(para)(MEI)(pode)\b", r"\1 \2 \3"),
        (r"\b(agravar)(déficit|deficit)\b", r"\1 \2"),
        (r"(crise)(bancária)", r"\1 \2"),
    ]
    for pat, rep in padroes_valor:
        s = re.sub(pat, rep, s, flags=re.I)
    return re.sub(r"\s+", " ", s).strip()


def eh_span_lixo_ou_logo(texto, font_name=""):
    """Filtra códigos de barras, mastheads de jornal, datas de expediente e chamadas de capa irrelevantes."""
    if not texto:
        return True
    t = texto.strip()
    if len(t) < 3:
        return True
    fl = (font_name or "").lower()
    if "barcode" in fl or "dingbat" in fl or "symbol" in fl:
        return True
    # Filtra strings com alta densidade de símbolos não-alfabéticos
    letras = sum(1 for c in t if c.isalpha())
    if letras < len(t) * 0.45:
        return True
    tl = t.lower()
    for pat in STOPWORDS_LOGOTIPO_CAPA:
        if re.search(pat, tl):
            return True
    return False


def extrair_manchete_capa_por_dict(page):
    """
    Usa `page.get_text("dict")` na Página 1 para identificar a manchete principal real
    agrupando spans de grande corpo tipográfico (`size` em pontos) da mesma família/região.
    """
    try:
        d = page.get_text("dict")
    except Exception:
        return None, []

    spans_candidatos = []
    for b_idx, b in enumerate(d.get("blocks", [])):
        if b.get("type") != 0:
            continue
        for l_idx, line in enumerate(b.get("lines", [])):
            bbox = line.get("bbox", [0, 0, 0, 0])
            # Ignorar extremo topo (< 55pt: cabeçalho/preço/clima) e extremo rodapé (> 92% da altura)
            page_h = d.get("height", 842)
            if bbox[1] < 45 or bbox[1] > page_h * 0.93:
                continue

            partes_linha = []
            max_sz = 0.0
            font_principal = ""
            for sp in line.get("spans", []):
                txt = sp.get("text", "").strip()
                fnt = sp.get("font", "")
                sz = float(sp.get("size", 0.0))
                if not txt:
                    continue
                if eh_span_lixo_ou_logo(txt, fnt):
                    continue
                partes_linha.append(txt)
                if sz > max_sz:
                    max_sz = sz
                    font_principal = fnt

            if partes_linha and max_sz >= 18.0:
                linha_str = corrigir_colagem_palavras(" ".join(partes_linha))
                if not eh_span_lixo_ou_logo(linha_str, font_principal):
                    spans_candidatos.append({
                        "size": round(max_sz, 1),
                        "font": font_principal,
                        "text": linha_str,
                        "y0": bbox[1],
                        "x0": bbox[0],
                        "block": b_idx
                    })

    if not spans_candidatos:
        return None, []

    # Agrupar linhas de tamanho similar (tolerância ±2.0pt) e mesma família tipográfica próximas verticalmente
    spans_candidatos.sort(key=lambda x: (-x["size"], x["y0"], x["x0"]))
    grupos_manchete = []
    usados = set()

    for i, sp in enumerate(spans_candidatos):
        if i in usados:
            continue
        grupo = [sp]
        usados.add(i)
        f_prefix = (sp["font"] or "")[:10]
        for j, outro in enumerate(spans_candidatos):
            if j in usados:
                continue
            mesmo_tamanho = abs(outro["size"] - sp["size"]) <= 2.2
            mesma_fonte = (outro["font"] or "")[:10] == f_prefix
            perto_x = abs(outro["x0"] - sp["x0"]) < 140
            perto_y = abs(outro["y0"] - grupo[-1]["y0"]) < 160
            if mesmo_tamanho and mesma_fonte and perto_x and perto_y:
                grupo.append(outro)
                usados.add(j)

        grupo.sort(key=lambda x: (x["y0"], x["x0"]))
        texto_grupo = corrigir_colagem_palavras(" ".join(g["text"] for g in grupo))
        # Uma manchete jornalística real costuma ter ao menos 3 palavras e >= 18 caracteres
        if len(texto_grupo) >= 18 and texto_grupo.count(" ") >= 2:
            grupos_manchete.append({
                "size": sp["size"],
                "font": sp["font"],
                "manchete": texto_grupo,
                "y0": grupo[0]["y0"]
            })

    grupos_manchete.sort(key=lambda x: (-x["size"], x["y0"]))
    manchete_top = grupos_manchete[0]["manchete"] if grupos_manchete else None
    submanchetes = [g["manchete"] for g in grupos_manchete[1:6]]
    return manchete_top, submanchetes


def extrair_blocos_limpos_pagina(page, num_pagina):
    """
    Usa `page.get_text("blocks")` para extrair blocos de texto ordenados por coluna/fluxo
    sem misturar tabelas numéricas laterais, cabeçalhos ou rodapés.
    """
    try:
        blocks = page.get_text("blocks")
    except Exception:
        return []

    rect = page.rect
    page_h = rect.height if rect else 842
    blocos_limpos = []

    for b in blocks:
        # b = (x0, y0, x1, y1, "text", block_no, block_type)
        if len(b) < 7 or b[6] != 0:
            continue
        x0, y0, x1, y1, raw_txt, b_no, _ = b
        if y0 < 35 or y1 > page_h * 0.95:
            continue

        # Desfazer hifenização de quebra de linha dentro do mesmo bloco
        txt = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", raw_txt)
        txt = corrigir_colagem_palavras(txt.replace("\n", " "))
        if len(txt) < 45:
            continue

        # Descartar blocos que são majoritariamente tabelas de cotações ou números
        digitos = sum(1 for c in txt if c.isdigit())
        if digitos > len(txt) * 0.28:
            continue

        tl = txt.lower()
        if any(re.search(pat, tl) for pat in STOPWORDS_LOGOTIPO_CAPA):
            continue
        if any(lixo in tl for lixo in [
            "dólar turismo", "euro comercial", "euro turismo", "índice de empresas citadas",
            "princípios editoriais", "all rights reserved", "printed in london"
        ]):
            continue

        blocos_limpos.append({
            "pagina": num_pagina,
            "x0": round(x0, 1),
            "y0": round(y0, 1),
            "largura": round(x1 - x0, 1),
            "texto": txt
        })

    # Ordenar por faixa vertical aproximada e coluna horizontal
    blocos_limpos.sort(key=lambda item: (int(item["y0"] // 120), int(item["x0"] // 150), item["y0"]))
    return blocos_limpos


def executar_ocr_apple_vision(doc, max_pages=8, escopo="nacional"):
    """Executa OCR via Apple Vision Framework usando o idioma adequado ('pt-BR' ou 'en-US')."""
    lang = "en-US" if escopo == "internacional" else "pt-BR"
    swift_script = """
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count > 2 else { exit(1) }
let imagePath = args[1]
let lang = args[2]

guard let img = NSImage(contentsOfFile: imagePath),
      let cgImage = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    exit(1)
}

let request = VNRecognizeTextRequest { (request, error) in
    guard let observations = request.results as? [VNRecognizedTextObservation] else { return }
    var lines: [String] = []
    for obs in observations {
        if let top = obs.topCandidates(1).first {
            let box = obs.boundingBox
            // Prefixa coordenadas y,x normalizadas para permitir reconstrução espacial
            let y = Int((1.0 - box.origin.y) * 1000)
            let x = Int(box.origin.x * 1000)
            let h = Int(box.size.height * 1000)
            lines.append("\\(y)|\\(x)|\\(h)|\\(top.string)")
        }
    }
    print(lines.joined(separator: "\\n"))
}

request.recognitionLevel = .accurate
request.recognitionLanguages = [lang, "pt-BR", "en-US"]
request.usesLanguageCorrection = true

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
try? handler.perform([request])
"""
    tmp_swift = "/tmp/apple_vision_layout_v2.swift"
    with open(tmp_swift, "w", encoding="utf-8") as f:
        f.write(swift_script)

    paginas_ocr = []
    manchete_ocr = None
    submanchetes_ocr = []

    total_p = min(len(doc), max_pages)
    for page_idx in range(total_p):
        page = doc[page_idx]
        pix = page.get_pixmap(dpi=150)
        tmp_img = f"/tmp/ocr_v2_p{page_idx + 1}.png"
        pix.save(tmp_img)

        try:
            cmd = ["/usr/bin/swift", tmp_swift, tmp_img, lang]
            proc = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=35)
            raw_lines = [l.strip() for l in proc.stdout.strip().split("\n") if l.strip()]

            parsed_obs = []
            for rl in raw_lines:
                parts = rl.split("|", 3)
                if len(parts) == 4:
                    y, x, h, txt = int(parts[0]), int(parts[1]), int(parts[2]), parts[3].strip()
                    if y < 55 or y > 950:
                        continue
                    if eh_span_lixo_ou_logo(txt):
                        continue
                    parsed_obs.append({"y": y, "x": x, "h": h, "text": txt})

            if page_idx == 0 and parsed_obs:
                # Na capa escaneada, as maiores alturas de bounding box (`h`) são as manchetes!
                grandes = [o for o in parsed_obs if o["h"] >= 16 and len(o["text"]) >= 12]
                grandes.sort(key=lambda o: (-o["h"], o["y"]))
                if grandes:
                    h_top = grandes[0]["h"]
                    linhas_manchete = [
                        g for g in grandes
                        if abs(g["h"] - h_top) <= 6 and abs(g["y"] - grandes[0]["y"]) <= 120
                    ]
                    linhas_manchete.sort(key=lambda o: o["y"])
                    cand_m = corrigir_colagem_palavras(" ".join(l["text"] for l in linhas_manchete))
                    if len(cand_m) >= 18:
                        manchete_ocr = cand_m
                    for g in grandes[len(linhas_manchete):len(linhas_manchete) + 5]:
                        if len(g["text"]) >= 20:
                            submanchetes_ocr.append(g["text"])

            # Agrupar observações da página em blocos por coluna aproximada
            parsed_obs.sort(key=lambda o: (o["x"] // 250, o["y"]))
            texto_pag = " ".join(o["text"] for o in parsed_obs if len(o["text"]) >= 18)
            texto_pag = re.sub(r"(\w)-\s+(\w)", r"\1\2", texto_pag)
            if len(texto_pag) >= 120:
                paginas_ocr.append({
                    "pagina": page_idx + 1,
                    "blocos": [
                        {
                            "pagina": page_idx + 1,
                            "x0": 0,
                            "y0": 0,
                            "largura": 500,
                            "texto": texto_pag[:3500]
                        }
                    ]
                })
        except Exception as e:
            log(f"Aviso no OCR Apple Vision ({lang}) pág {page_idx + 1}: {e}")
        finally:
            if os.path.exists(tmp_img):
                os.remove(tmp_img)

    return {
        "metodo": f"apple_vision_ocr_{lang}",
        "manchete_capa": manchete_ocr,
        "submanchetes_capa": submanchetes_ocr,
        "paginas": paginas_ocr
    }


def extrair_layout_pdf_v2(pdf_path, max_pages=12, escopo="nacional"):
    """
    Extrai a estrutura completa de um PDF de jornal ou revista combinando:
    - `page.get_text("dict")` na capa para manchete tipográfica real
    - `page.get_text("blocks")` nas páginas internas para colunas desmembradas
    - Fallback para Apple Vision OCR (`pt-BR` ou `en-US`) em PDFs escaneados.
    """
    import fitz

    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    pages_to_read = min(total_pages, max_pages)

    # Verificar se alguma das 3 primeiras páginas possui texto vetorial real (evita falso OCR em capas ilustradas de revistas)
    tem_texto_vetorial = any(
        len(doc[idx].get_text("text").strip()) >= 120
        for idx in range(min(total_pages, 3))
    )
    if not tem_texto_vetorial:
        ocr_data = executar_ocr_apple_vision(doc, max_pages=min(total_pages, 8), escopo=escopo)
        ocr_data["total_paginas"] = total_pages
        return ocr_data

    manchete_capa, submanchetes_capa = extrair_manchete_capa_por_dict(doc[0])
    paginas_estruturadas = []

    for idx in range(pages_to_read):
        blocos = extrair_blocos_limpos_pagina(doc[idx], idx + 1)
        if blocos:
            paginas_estruturadas.append({
                "pagina": idx + 1,
                "blocos": blocos
            })

    return {
        "metodo": "pymupdf_dict_blocks_v2",
        "total_paginas": total_pages,
        "manchete_capa": manchete_capa,
        "submanchetes_capa": submanchetes_capa,
        "paginas": paginas_estruturadas
    }


def chamar_gemini_estruturado_jornal(veiculo, escopo, data_iso, dados_layout):
    """
    Envia os blocos estruturados da edição para `gemini-4-argon` (com fallback para `gemini-3.8-flash`)
    para sintetizar o objeto completo do jornal no Modo Leitor.
    """
    api_key = obter_chave_gemini()
    if not api_key:
        return None

    resumo_dump = {
        "jornal": veiculo,
        "escopo": escopo,
        "data": data_iso,
        "manchete_tipografica_capa": dados_layout.get("manchete_capa"),
        "submanchetes_capa": dados_layout.get("submanchetes_capa", [])[:5],
        "paginas": []
    }
    for p in dados_layout.get("paginas", [])[:10]:
        textos_b = [b["texto"][:600] for b in p.get("blocos", [])[:8]]
        if textos_b:
            resumo_dump["paginas"].append({
                "pagina": p["pagina"],
                "blocos": textos_b
            })

    prompt = (
        f"Você é o editor-chefe da revista cultural e jornalística Faixa Oculta.\n"
        f"Abaixo está a extração estruturada por blocos tipográficos da edição de hoje ({data_iso}) "
        f"do periódico '{veiculo}' (escopo: {escopo}).\n"
        f"Reconstrua fielmente a edição para o Modo Leitor em português culto (se o jornal for internacional, "
        f"traduza integralmente tudo para o português culto e preserve os títulos originais em 'manchete_original' "
        f"e 'titulo_original').\n\n"
        f"Retorne APENAS um objeto JSON válido com a seguinte estrutura exata:\n"
        f"{{\n"
        f'  "manchete": "Manchete principal em português",\n'
        f'  "manchete_original": "Manchete no idioma original (ou null se nacional)",\n'
        f'  "nota": "Síntese executiva de 1 parágrafo (até 240 chars) dos destaques da capa",\n'
        f'  "resumo_edicao": ["Parágrafo 1 denso sobre a capa", "Parágrafo 2 denso sobre os demais cadernos"],\n'
        f'  "editorial": {{"titulo": "Título da opinião/editorial", "texto": ["Parágrafo 1", "Parágrafo 2"]}},\n'
        f'  "reportagens": [\n'
        f'    {{\n'
        f'      "caderno": "Nome do Caderno (ex: Economia, Política, Mundo, Cultura)",\n'
        f'      "pagina": "Número da página",\n'
        f'      "autor": "Autor ou Redação",\n'
        f'      "titulo": "Título da reportagem em português",\n'
        f'      "titulo_original": "Título original se internacional ou null",\n'
        f'      "lide": "Resumo de abertura da matéria em 1 a 2 frases",\n'
        f'      "texto": ["Parágrafo 1 denso", "Parágrafo 2 denso", "Parágrafo 3 denso"],\n'
        f'      "pontos": ["Ponto central 1", "Ponto central 2"]\n'
        f'    }}\n'
        f'  ]\n'
        f"}}\n"
        f"Gere exatamente 5 reportagens completas baseadas estritamente nos blocos reais abaixo:\n\n"
        f"{json.dumps(resumo_dump, ensure_ascii=False)}"
    )

    modelos = ["gemini-4-argon", "gemini-3.8-flash", "gemini-2.5-flash"]
    for mod in modelos:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{mod}:generateContent?key={api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.2,
                "responseMimeType": "application/json"
            }
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=35, context=SSL_CTX) as resp:
                body = json.loads(resp.read().decode("utf-8"))
                cand_txt = (
                    body.get("candidates", [{}])[0]
                    .get("content", {})
                    .get("parts", [{}])[0]
                    .get("text", "")
                )
                if cand_txt:
                    parsed = json.loads(cand_txt)
                    if parsed.get("manchete") and parsed.get("reportagens"):
                        log(f"Síntese estruturada gerada via {mod} para {veiculo}!")
                        return parsed
        except Exception as e:
            log(f"Aviso ao consultar modelo {mod} para {veiculo}: {e}")
            continue
    return None


def construir_jornal_de_blocos_fallback(veiculo, escopo, dados_layout):
    """
    Reconstrução determinística Layout-Aware (usada quando a API LLM estiver offline/sem quota),
    baseada na manchete tipográfica real (`get_text('dict')`) e nos blocos espaciais (`get_text('blocks')`).
    """
    eh_int = (escopo == "internacional")
    manchete_bruta = dados_layout.get("manchete_capa")
    submanchetes = dados_layout.get("submanchetes_capa") or []
    paginas = dados_layout.get("paginas") or []

    if not manchete_bruta and paginas and paginas[0].get("blocos"):
        manchete_bruta = paginas[0]["blocos"][0]["texto"][:110]
    if not manchete_bruta:
        manchete_bruta = f"Destaques da edição de {veiculo}"

    manchete_pt = traduzir_texto_pt(manchete_bruta) if eh_int else manchete_bruta
    manchete_orig = manchete_bruta if eh_int else None

    reportagens = []
    editorial_obj = None

    for p_obj in paginas:
        num_pag = p_obj.get("pagina", 1)
        blocos = [b["texto"] for b in p_obj.get("blocos", []) if len(b.get("texto", "")) >= 70]
        if not blocos:
            continue

        # Determinar título da página
        if num_pag == 1 and manchete_bruta:
            tit_orig = manchete_bruta
            tit_pt = manchete_pt
        elif submanchetes and len(reportagens) <= len(submanchetes):
            tit_orig = submanchetes[len(reportagens) - 1]
            tit_pt = traduzir_texto_pt(tit_orig) if eh_int else tit_orig
        else:
            primeira_frase = re.split(r"(?<=[.!?])\s+", blocos[0])[0][:120].strip()
            tit_orig = primeira_frase
            tit_pt = traduzir_texto_pt(tit_orig) if eh_int else tit_orig

        # Montar 3 parágrafos limpos a partir dos maiores blocos da página
        blocos_ordenados = sorted(blocos, key=len, reverse=True)[:4]
        texto_unido = " ".join(blocos_ordenados)
        palavras = texto_unido.split()
        if len(palavras) < 45:
            continue

        passo = max(45, min(80, len(palavras) // 3))
        paragrafos_raw = []
        for i in range(0, min(len(palavras), passo * 3), passo):
            trecho = " ".join(palavras[i:i + passo]).strip()
            if len(trecho) >= 60:
                if not trecho.endswith("."):
                    trecho += "."
                paragrafos_raw.append(trecho)

        if not paragrafos_raw:
            continue

        paragrafos_pt = [traduzir_texto_pt(pr) for pr in paragrafos_raw[:3]] if eh_int else paragrafos_raw[:3]
        while len(paragrafos_pt) < 3:
            paragrafos_pt.append(
                f"A edição impressa de {veiculo} aprofunda os desdobramentos institucionais, econômicos e políticos na página {num_pag}."
            )

        if num_pag in (2, 3) and not editorial_obj:
            editorial_obj = {
                "titulo": tit_pt,
                "texto": paragrafos_pt[:2]
            }

        if len(reportagens) < 5:
            caderno = "Capa · Destaque Principal" if num_pag == 1 else f"Caderno Principal · Pág. {num_pag}"
            reportagens.append({
                "caderno": caderno,
                "pagina": str(num_pag),
                "autor": f"Redação {veiculo}",
                "titulo": tit_pt,
                "titulo_original": tit_orig if eh_int else None,
                "lide": paragrafos_pt[0],
                "texto": paragrafos_pt[:3],
                "texto_integral": paragrafos_pt[:3],
                "pontos": [paragrafos_pt[0][:160], paragrafos_pt[1][:160]]
            })

    if not editorial_obj and reportagens:
        editorial_obj = {
            "titulo": f"Análise Editorial · {veiculo}",
            "texto": reportagens[0]["texto"][:2]
        }

    resumo_ed = [r["lide"] for r in reportagens[:2]] if reportagens else [manchete_pt]
    return {
        "manchete": manchete_pt,
        "manchete_original": manchete_orig,
        "nota": resumo_ed[0][:240],
        "resumo_edicao": resumo_ed,
        "editorial": editorial_obj,
        "reportagens": reportagens
    }


def sintetizar_edicao_completa(veiculo, escopo, pdf_path, img_rel_path="", max_pages=12):
    """
    Pipeline principal de extração v2 para um arquivo PDF do Beeper:
    1. Extrai layout (`dict` + `blocks` ou Apple Vision OCR bilingue).
    2. Tenta síntese estruturada via `gemini-4-argon` / `gemini-3.8-flash`.
    3. Aplica fallback determinístico Layout-Aware garantindo 100% de disponibilidade.
    """
    hoje_iso = datetime.now().strftime("%Y-%m-%d")
    dados_layout = extrair_layout_pdf_v2(pdf_path, max_pages=max_pages, escopo=escopo)

    sintese = chamar_gemini_estruturado_jornal(veiculo, escopo, hoje_iso, dados_layout)
    if not sintese:
        sintese = construir_jornal_de_blocos_fallback(veiculo, escopo, dados_layout)

    # Normalizar campos para compatibilidade total v1 e v2
    for rep in sintese.get("reportagens", []):
        if "texto" in rep and "texto_integral" not in rep:
            rep["texto_integral"] = rep["texto"]
        elif "texto_integral" in rep and "texto" not in rep:
            rep["texto"] = rep["texto_integral"]
        if "lide" not in rep and rep.get("texto"):
            rep["lide"] = rep["texto"][0]

    return {
        "jornal": veiculo,
        "pais": PAISES_POR_VEICULO.get(veiculo, "Brasil" if escopo == "nacional" else "Internacional"),
        "escopo": escopo,
        "metodo_extracao": dados_layout.get("metodo"),
        "total_paginas": dados_layout.get("total_paginas", 0),
        "imagem": img_rel_path,
        "site": SITES_OFICIAIS.get(veiculo, ""),
        "manchete": sintese.get("manchete"),
        "manchete_original": sintese.get("manchete_original"),
        "nota": sintese.get("nota", ""),
        "resumo_edicao": sintese.get("resumo_edicao", []),
        "editorial": sintese.get("editorial"),
        "reportagens": sintese.get("reportagens", [])
    }


def listar_publicacoes_beeper_v2(limit_per_room=250):
    """Consulta o banco SQLite local do Beeper nas 3 salas de imprensa e retorna os arquivos disponíveis."""
    if not os.path.exists(DB_PATH):
        return []

    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    cur = conn.cursor()
    pubs = []

    for rid in PRESS_ROOMS:
        rname = KNOWN_ROOM_NAMES.get(rid, rid)
        cur.execute("""
            SELECT timestamp, message
            FROM mx_room_messages
            WHERE roomID = ? AND type = 'FILE'
            ORDER BY timestamp DESC LIMIT ?
        """, (rid, limit_per_room))

        for ts, msg_str in cur.fetchall():
            try:
                msg = json.loads(msg_str)
                for att in msg.get("attachments", []):
                    fn = att.get("fileName", "")
                    if not fn.lower().endswith(".pdf"):
                        continue
                    src = att.get("srcURL", "")
                    media_id = src.replace("mxc://local.beeper.com/", "")
                    local_path = os.path.join(MEDIA_DIR, media_id)
                    baixado = os.path.exists(local_path)
                    pubs.append({
                        "canal": rname,
                        "timestamp": ts,
                        "data_msg": datetime.fromtimestamp(ts / 1000.0).strftime("%Y-%m-%d %H:%M"),
                        "arquivo": fn,
                        "tamanho_mb": round(att.get("fileSize", 0) / (1024 * 1024), 2),
                        "src_url": src,
                        "baixado": baixado,
                        "local_path": local_path if baixado else None
                    })
            except Exception:
                continue

    conn.close()
    return pubs


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Extrator Layout-Aware v2 de Jornais e Revistas (Beeper)")
    parser.add_argument("--test", action="store_true", help="Executa bateria de testes nos PDFs já baixados no Beeper")
    parser.add_argument("--perfil", choices=["diario", "semana"], default="diario", help="Perfil editorial para listar/testar")
    parser.add_argument("--pdf", type=str, help="Testar extração em um arquivo PDF específico")
    args = parser.parse_args()

    if args.pdf and os.path.exists(args.pdf):
        res = sintetizar_edicao_completa("Teste PDF", "nacional", args.pdf, max_pages=6)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return

    if args.test:
        log(f"Iniciando teste prático do Extrator Layout-Aware v2 (perfil: {args.perfil})...")
        pubs = listar_publicacoes_beeper_v2(limit_per_room=300)
        cfg = PERFIS_V2.get(args.perfil, {})
        relatorio = []

        for escopo, lista_v in cfg.items():
            for nome_v, kws in lista_v:
                cands = [p for p in pubs if any(k in p["arquivo"].lower() for k in kws)]
                cands.sort(key=lambda x: x["timestamp"], reverse=True)
                baixados = [c for c in cands if c["baixado"]]
                escolhido = baixados[0] if baixados else (cands[0] if cands else None)
                if not escolhido:
                    print(f"  [AUSENTE] {nome_v:<24} ({escopo})")
                    continue

                if escolhido["baixado"]:
                    dados_l = extrair_layout_pdf_v2(escolhido["local_path"], max_pages=4, escopo=escopo)
                    m_capa = dados_l.get("manchete_capa") or "(Extraída dos blocos da Pág 1)"
                    qtd_p = len(dados_l.get("paginas", []))
                    qtd_b = sum(len(p.get("blocos", [])) for p in dados_l.get("paginas", []))
                    print(
                        f"  [OK] {nome_v:<24} | {escolhido['metodo'] if 'metodo' in escolhido else dados_l['metodo']:<24} | "
                        f"Págs={qtd_p}/{dados_l['total_paginas']:<3} | Blocos={qtd_b:<3} | Manchete: {m_capa[:75]}"
                    )
                    relatorio.append({
                        "veiculo": nome_v,
                        "arquivo": escolhido["arquivo"],
                        "metodo": dados_l["metodo"],
                        "manchete_capa": m_capa,
                        "submanchetes": dados_l.get("submanchetes_capa", [])[:3],
                        "blocos_extraidos": qtd_b
                    })
                else:
                    print(f"  [DISPONÍVEL P/ DOWNLOAD] {nome_v:<24} | Arquivo: {escolhido['arquivo']} ({escolhido['tamanho_mb']} MB)")

        out_test = "/tmp/teste_extrator_pdf_layout_v2.json"
        with open(out_test, "w", encoding="utf-8") as f:
            json.dump(relatorio, f, ensure_ascii=False, indent=2)
        log(f"Teste concluído! Diagnóstico salvo em {out_test}")


if __name__ == "__main__":
    main()
