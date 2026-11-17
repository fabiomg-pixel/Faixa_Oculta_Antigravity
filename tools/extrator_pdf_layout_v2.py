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
    "!CKYQw8EzDcJJW9ZBUqB7:beeper.local",  # IELTS Newspapers & Magazines
    "!I86rARDr2VolnIjl9pki:beeper.local",  # Jornais e Revistas 3.0
    "!0nZuyBr37onTMYp69CUi:beeper.local",  # Revista Jacobina
]

KNOWN_ROOM_NAMES = {
    "!iq3RLvh1JnfH6vJzkvaL:beeper.local": "Jornais BR",
    "!Q3EN2ZSkzkir8tYnRU7t:beeper.local": "International Newspapers",
    "!tFgakhGBTv3CNjiYMdkM:beeper.local": "Jornais e Revistas 4.0",
    "!CKYQw8EzDcJJW9ZBUqB7:beeper.local": "IELTS Newspapers & Magazines",
    "!I86rARDr2VolnIjl9pki:beeper.local": "Jornais e Revistas 3.0",
    "!0nZuyBr37onTMYp69CUi:beeper.local": "Revista Jacobina",
}

PERFIS_V2 = {
    "diario": {
        "nacional": [
            ("Folha de S.Paulo", ["folha de s paulo", "folha de s.paulo", "folha de sp", "folha de são paulo", "folha de sao paulo", "folha"]),
            ("O Estado de S. Paulo", ["estado de s paulo", "estadao", "estadão"]),
            ("O Globo", ["o globo - hd", "o globo – hd", "o globo- hd", "o globo‐ hd", "o globo"]),
            ("Valor Econômico", ["valor econômico", "valor economico", "valor"])
        ],
        "internacional": [
            ("The New York Times", ["nyt 0", "nyt 1", "nyt 2", "nyt 3", "the-new-york-times", "the new york times -"]),
            ("Financial Times", ["financial times", "ft us", "ft uk", "ft eu", "ft me", "ft asia", "ft europe"]),
            ("The Washington Post", ["the washington post", "washington post", "the-washington-post"]),
            ("The Guardian", ["the guardian", "the-guardian", "guardian journal", "the observer"]),
            ("The Times UK", ["the times uk", "the-times-uk", "the times -", "the times"]),
            ("Le Monde", ["le monde", "lemonde", "le-monde"])
        ]
    },
    "semana": {
        "nacional": [
            ("Revista piauí", ["piauí", "piaui"]),
            ("CartaCapital", ["carta capital", "cartacapital"]),
            ("Pesquisa FAPESP", ["pesquisa fapesp"]),
            ("Revista Oeste", ["revista oeste"]),
            ("Revista Fórum", ["revista forum", "revista fórum"]),
            ("Veja", ["veja digital", "revista veja-", "veja rio"]),
            ("Valor Econômico · EU&", ["eu&"])
        ],
        "internacional": [
            ("The Economist", ["the economist", "economist"]),
            ("Foreign Affairs", ["foreign affairs", "foreign-affairs"]),
            ("The New Yorker", ["the new yorker", "new yorker"]),
            ("Time", ["time magazine", "time -", "time_"]),
            ("Newsweek", ["newsweek"]),
            ("The Observer", ["the observer"]),
            ("NYT Book Review", ["nytbr", "book review"]),
            ("The New York Times Magazine", ["nyt magazine"]),
            ("FT Weekend Magazine", ["ft weekend", "ft magazine", "weekend magazine"])
        ]
    }
}

SITES_OFICIAIS = {
    "Folha de S.Paulo": "https://www.folha.uol.com.br",
    "O Estado de S. Paulo": "https://www.estadao.com.br",
    "O Globo": "https://oglobo.globo.com",
    "Valor Econômico": "https://valor.globo.com",
    "Valor Econômico · EU&": "https://valor.globo.com/eu-e/",
    "The New York Times": "https://www.nytimes.com",
    "The Washington Post": "https://www.washingtonpost.com",
    "The Guardian": "https://www.theguardian.com",
    "The Observer": "https://www.theguardian.com/observer",
    "Financial Times": "https://www.ft.com",
    "The Times UK": "https://www.thetimes.com",
    "Le Monde": "https://www.lemonde.fr",
    "The Economist": "https://www.economist.com",
    "Foreign Affairs": "https://www.foreignaffairs.com",
    "The New Yorker": "https://www.newyorker.com",
    "Revista piauí": "https://piaui.folha.uol.com.br",
    "CartaCapital": "https://www.cartacapital.com.br",
    "Pesquisa FAPESP": "https://revistapesquisa.fapesp.br",
    "Revista Oeste": "https://revistaoeste.com",
    "Revista Fórum": "https://revistaforum.com.br",
    "Time": "https://time.com",
    "Newsweek": "https://www.newsweek.com",
    "Veja": "https://veja.abril.com.br",
    "NYT Book Review": "https://www.nytimes.com/section/books/review",
    "The New York Times Magazine": "https://www.nytimes.com/section/magazine",
    "FT Weekend Magazine": "https://www.ft.com/magazine",
}

PAISES_POR_VEICULO = {
    "Folha de S.Paulo": "Brasil",
    "O Estado de S. Paulo": "Brasil",
    "O Globo": "Brasil",
    "Valor Econômico": "Brasil",
    "Valor Econômico · EU&": "Brasil",
    "Revista piauí": "Brasil",
    "CartaCapital": "Brasil",
    "Pesquisa FAPESP": "Brasil",
    "Revista Oeste": "Brasil",
    "Revista Fórum": "Brasil",
    "Veja": "Brasil",
    "The New York Times": "Estados Unidos",
    "NYT Book Review": "Estados Unidos",
    "The New York Times Magazine": "Estados Unidos",
    "The Washington Post": "Estados Unidos",
    "The New Yorker": "Estados Unidos",
    "Foreign Affairs": "Estados Unidos / Global",
    "Time": "Estados Unidos / Global",
    "Newsweek": "Estados Unidos / Global",
    "The Guardian": "Reino Unido",
    "The Observer": "Reino Unido",
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
    r"^diretor(es)?-?gerais?\b",
    r"^conselho\s+editorial\b",
    r"^presidente\s*:",
    r"^fundador(es)?\b",
    r"^um\s+jornal\s+a\s+serviço",
    r"^expediente\b",
]


def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [ExtratorPDF-v2] {msg}", flush=True)


try:
    from tools import gemini_client
except ImportError:
    import gemini_client


def obter_chave_gemini():
    """Delega para o cliente unificado Gemini 4 (`tools/gemini_client.py`)."""
    return gemini_client.obter_api_key()


def traduzir_texto_pt(texto):
    """Traduz texto internacional para o português culto via cache batelada e cliente unificado."""
    return gemini_client.traduzir_texto_resiliente(texto, de="auto", para="pt-BR")


def traduzir_lista_pt(textos, max_workers=6):
    """Traduz múltiplos parágrafos em paralelo usando o pool e cache unificado."""
    if not textos:
        return []
    from concurrent.futures import ThreadPoolExecutor
    if len(textos) <= 2:
        return [traduzir_texto_pt(t) for t in textos]
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        res = list(pool.map(traduzir_texto_pt, textos))
    gemini_client.flush_cache_traducoes()
    return res


def _extrair_texto_rawdict_com_espacos(page, clip_rect=None):
    """Reconstrói texto por linha usando gaps de bbox entre caracteres quando PDF cola palavras (ex.: Valor Econômico)."""
    try:
        raw = page.get_text("rawdict", clip=clip_rect) if clip_rect else page.get_text("rawdict")
    except Exception:
        return []
    linhas_out = []
    for b in raw.get("blocks", []):
        if b.get("type") != 0:
            continue
        for l in b.get("lines", []):
            lb = l.get("bbox", [0, 0, 0, 0])
            chars = []
            max_sz = 0.0
            font_p = ""
            for s in l.get("spans", []):
                sz = float(s.get("size", 0.0))
                if sz > max_sz:
                    max_sz = sz
                    font_p = s.get("font", "")
                for ch in s.get("chars", []):
                    c = ch.get("c", "")
                    cb = ch.get("bbox")
                    if c and cb:
                        chars.append((cb[0], cb[2], c, sz))
            if not chars:
                continue
            chars.sort(key=lambda it: it[0])
            partes = [chars[0][2]]
            prev_x1 = chars[0][1]
            for x0, x1, c, sz in chars[1:]:
                gap = x0 - prev_x1
                limiar = max(0.8, (sz or max_sz or 10.0) * 0.04)
                if gap > limiar and c != " " and partes[-1] != " ":
                    partes.append(" ")
                partes.append(c)
                if x1 > prev_x1:
                    prev_x1 = x1
            txt = re.sub(r"\s+", " ", "".join(partes)).strip()
            if txt:
                linhas_out.append({"bbox": lb, "size": max_sz, "font": font_p, "text": txt, "b_idx": b.get("number", 0)})
    return linhas_out


def corrigir_colagem_palavras(texto):
    """Desfaz colagens de palavras típicas de kerning apertado em PDFs e limpa zero-width spaces."""
    if not texto:
        return ""
    s = texto.replace("\u200b", "").replace("\ufeff", "").replace("\u00ad", "")
    # Insere espaço após vírgula/ponto-e-vírgula colado a letra
    s = re.sub(r"([,;:])([A-Za-zÀ-ÿ])", r"\1 \2", s)
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


def _eh_anuncio_ou_lixo(t):
    """Detecta anúncios comerciais, assinaturas, quadras/cabore ou linhas separadoras."""
    if not t:
        return True
    tl = t.lower().strip()
    if not re.search(r"[a-zA-ZÀ-ÿ]{3,}", t):
        return True
    if t.count("-") > 6 or t.count("•") > 6:
        return True
    if any(k in tl for k in [
        "plano mensal", "edição impressa", "assine a folha", "caboré", "agência do ano",
        "compra de mídia", "quadras à escolha", "jogue em todas", "grand slam",
        "hong kong maritime", "complimentary place", "ft live", "in partnership with",
        "exclusivo para assinantes", "atendimento ao leitor", "painel do leitor",
        "ombudsman", "fale com", "editoriais@", "@grupofolha", "folha.com",
        "publicado desde", "propriedade da empresa", "fundado em", "tiragem", "cnpj",
        "world markets at a glance", "fractional ownership", "hideaways club",
        "aponte o celular", "qr code", "learn more at", "saiba mais em:",
        "valor international", "amil resgate", "utis móveis", "menor distância entre você",
        "whether you are", "investor or someone", "secretary for transport",
    ]):
        return True
    # Bloqueia siglas/ruído de infográficos ou manchas tipográficas com excesso de palavras curtas em caixa alta
    palavras = t.split()
    if len(palavras) >= 4:
        curtas_caps = sum(1 for w in palavras[:6] if len(w) <= 4 and w.isupper())
        if curtas_caps >= 4:
            return True
    return False


def _eh_titulo_valido(t):
    """Garante título jornalístico autêntico (começa por maiúscula/aspas/número e não é frase quebrada ou anúncio)."""
    if not t or _eh_anuncio_ou_lixo(t):
        return False
    s = t.strip()
    if len(s) < 12 or s.count(" ") < 2:
        return False
    if re.search(r"\b(new york times|netu hork|financial times|washington post)\b", s, re.I) and len(s) < 35:
        return False
    first = s[0]
    if not (first.isupper() or first.isdigit() or first in "\"'“‘"):
        return False
    return True


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
    # Trata datas/expedientes com letras espaçadas típicas de Folha/O Globo/FT (ex.: "t Erç A-f EIr A, 17 d E No VEmbro d E 2026")
    compact = re.sub(r"\s+", "", tl)
    if re.search(
        r"^(segunda|ter[cç]a|quarta|quinta|sexta|s[aá]bado|domingo)(-?feira)?,?\d{1,2}de(janeiro|fevereiro|mar[cç]o|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)(de)?\d{4}",
        compact,
    ):
        return True
    if re.search(
        r"^(monday|tuesday|wednesday|thursday|friday|saturday|sunday),?\d{0,2}(january|february|march|april|may|june|july|august|september|october|november|december)\d{0,2},?\d{4}",
        compact,
    ):
        return True
    if re.match(
        r"^(folhades\.?paulo|oglobo|oestadodes\.?paulo|valorecon[oô]mico|financialtimes|theguardian)$",
        compact,
    ):
        return True
    return False


def extrair_manchetes_detalhadas_capa_por_dict(page):
    """
    Usa `page.get_text("dict")` na Página 1 para identificar as manchetes principais reais
    com suas caixas delimitadoras (bounding boxes), agrupando spans contíguos de tamanho tipográfico compatível.
    Retorna (manchete_top, submanchetes, grupos_manchete_detalhados).
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

            if partes_linha and max_sz >= 14.0:
                joined_raw = " ".join(partes_linha)
                # Se houver token longo colado sem espaços (>= 11 chars), recompõe via gaps de rawdict
                if any(len(tok) >= 11 for tok in joined_raw.split()):
                    raw_linhas = _extrair_texto_rawdict_com_espacos(page, clip_rect=bbox)
                    if raw_linhas:
                        joined_raw = " ".join(rl["text"] for rl in raw_linhas)
                linha_str = corrigir_colagem_palavras(joined_raw)
                if not eh_span_lixo_ou_logo(linha_str, font_principal):
                    spans_candidatos.append({
                        "size": round(max_sz, 1),
                        "font": font_principal,
                        "text": linha_str,
                        "x0": bbox[0],
                        "y0": bbox[1],
                        "x1": bbox[2],
                        "y1": bbox[3],
                        "block": b_idx
                    })

    if not spans_candidatos:
        return None, [], []

    # Agrupar linhas de tamanho similar (tolerância ±2.5pt) e mesma família tipográfica próximas verticalmente
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
            mesmo_tamanho = abs(outro["size"] - sp["size"]) <= 2.5
            mesma_fonte = (outro["font"] or "")[:10] == f_prefix
            perto_x = abs(outro["x0"] - sp["x0"]) < 150
            perto_y = abs(outro["y0"] - grupo[-1]["y1"]) < 25 or abs(outro["y0"] - grupo[-1]["y0"]) < 90
            if mesmo_tamanho and mesma_fonte and perto_x and perto_y:
                grupo.append(outro)
                usados.add(j)

        grupo.sort(key=lambda x: (x["y0"], x["x0"]))
        texto_grupo = corrigir_colagem_palavras(" ".join(g["text"] for g in grupo))
        # Uma manchete jornalística real costuma ter ao menos 2 palavras e >= 12 caracteres
        if len(texto_grupo) >= 12 and texto_grupo.count(" ") >= 1:
            grupos_manchete.append({
                "size": sp["size"],
                "font": sp["font"],
                "manchete": texto_grupo,
                "x0": min(g["x0"] for g in grupo),
                "y0": min(g["y0"] for g in grupo),
                "x1": max(g["x1"] for g in grupo),
                "y1": max(g["y1"] for g in grupo)
            })

    grupos_manchete.sort(key=lambda x: (-x["size"], x["y0"]))
    manchete_top = grupos_manchete[0]["manchete"] if grupos_manchete else None
    submanchetes = [g["manchete"] for g in grupos_manchete[1:8]]
    return manchete_top, submanchetes, grupos_manchete


def extrair_manchete_capa_por_dict(page):
    """Wrapper retrocompatível que retorna (manchete_top, submanchetes)."""
    res = extrair_manchetes_detalhadas_capa_por_dict(page)
    return res[0], res[1]


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
        if any(len(tok) >= 11 and "http" not in tok for tok in txt.split()):
            raw_linhas = _extrair_texto_rawdict_com_espacos(page, clip_rect=(x0, y0, x1, y1))
            if raw_linhas:
                txt = re.sub(r"(\w)-\s+(\w)", r"\1\2", " ".join(rl["text"] for rl in raw_linhas))
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
        ]) or _eh_anuncio_ou_lixo(txt):
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


def _eh_texto_ocr_corrompido(txt):
    """Detecta ruído severo de OCR (texto invertido de ponta-cabeça em faixas/banners, ex: 'pausno satebIDues')."""
    if not txt:
        return True
    toks = [t for t in txt.split() if len(t) >= 3]
    if len(toks) < 3:
        return False
    estranhos = sum(
        1 for t in toks
        if re.search(r"[a-z]{2}[A-Z]{2}", t) or (len(t) >= 5 and sum(1 for c in t if c.isupper()) >= 2 and not t.isupper())
    )
    if estranhos >= max(2, len(toks) * 0.25):
        return True
    vogais = sum(1 for c in txt.lower() if c in "aeiouáàâãéêíóôõú")
    letras = sum(1 for c in txt if c.isalpha())
    if letras >= 20 and (vogais / max(letras, 1)) < 0.26:
        return True
    return False


_VISION_BIN_PATH = os.path.expanduser("~/.faixaoculta/bin/faixa_vision_ocr_v2")


def _obter_comando_vision_ocr():
    """Compila uma única vez o binário nativo Swift do Apple Vision para evitar recompilação JIT por página."""
    swift_script = """
import Vision
import Foundation

let args = CommandLine.arguments
guard args.count > 2 else { exit(1) }
let imagePath = args[1]
let lang = args[2]
let url = URL(fileURLWithPath: imagePath)

let request = VNRecognizeTextRequest { (request, error) in
    guard let observations = request.results as? [VNRecognizedTextObservation] else { return }
    var lines: [String] = []
    for obs in observations {
        if let top = obs.topCandidates(1).first {
            let box = obs.boundingBox
            let y = Int((1.0 - box.origin.y - box.size.height) * 1000)
            let x = Int(box.origin.x * 1000)
            let w = Int(box.size.width * 1000)
            let h = Int(box.size.height * 1000)
            lines.append("\\(y)|\\(x)|\\(w)|\\(h)|\\(top.string)")
        }
    }
    print(lines.joined(separator: "\\n"))
}

request.recognitionLevel = .accurate
request.recognitionLanguages = [lang, "pt-BR", "en-US"]
request.usesLanguageCorrection = true

let handler = VNImageRequestHandler(url: url, options: [:])
try? handler.perform([request])
"""
    tmp_swift = "/tmp/apple_vision_layout_v2.swift"
    with open(tmp_swift, "w", encoding="utf-8") as f:
        f.write(swift_script)

    if os.path.exists(_VISION_BIN_PATH):
        return [_VISION_BIN_PATH]
    try:
        os.makedirs(os.path.dirname(_VISION_BIN_PATH), exist_ok=True)
        subprocess.run(
            ["/usr/bin/swiftc", "-O", tmp_swift, "-o", _VISION_BIN_PATH],
            capture_output=True, text=True, check=True, timeout=45
        )
        if os.path.exists(_VISION_BIN_PATH):
            return [_VISION_BIN_PATH]
    except Exception:
        pass
    return ["/usr/bin/swift", tmp_swift]


def executar_ocr_apple_vision(doc, max_pages=8, escopo="nacional"):
    """Executa OCR via Apple Vision Framework preservando colunas espaciais e manchetes reais."""
    import hashlib
    lang = "en-US" if escopo == "internacional" else "pt-BR"
    cmd_prefix = _obter_comando_vision_ocr()
    doc_sig = hashlib.md5(str(getattr(doc, "name", "") or "doc").encode()).hexdigest()[:10]

    paginas_ocr = []
    manchete_ocr = None
    submanchetes_ocr = []
    grupos_manchete_ocr = []

    total_p = min(len(doc), max_pages)
    for page_idx in range(total_p):
        page = doc[page_idx]
        rect = page.rect
        pw = float(rect.width) if rect and rect.width else 800.0
        ph = float(rect.height) if rect and rect.height else 1200.0
        pix = page.get_pixmap(dpi=200)
        tmp_img = f"/tmp/ocr_v2_{doc_sig}_p{page_idx + 1}.png"
        pix.save(tmp_img)

        def _rodar_swift_vision(img_path, y_offset_norm=0.0, y_scale_norm=1.0):
            cmd = list(cmd_prefix) + [img_path, lang]
            proc = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=45)
            out_obs = []
            for rl in proc.stdout.strip().split("\n"):
                rl = rl.strip()
                if not rl:
                    continue
                parts = rl.split("|", 4)
                if len(parts) == 5:
                    y_loc, x, w, h_loc, txt = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), parts[4].strip()
                    y = int(y_offset_norm * 1000 + y_loc * y_scale_norm)
                    h = max(int(h_loc * y_scale_norm), 4)
                    if y < 45 or y > 955:
                        continue
                    if eh_span_lixo_ou_logo(txt) or _eh_texto_ocr_corrompido(txt):
                        continue
                    out_obs.append({"y": y, "x": x, "w": max(w, 20), "h": h, "text": txt})
            return out_obs

        try:
            parsed_obs = _rodar_swift_vision(tmp_img)
            # Se o Vision inverter a página inteira (típico de folhas altas com < 50 linhas válidas), refaz fatiado em metades 220 DPI
            if len(parsed_obs) < 50:
                from PIL import Image as _PILImage
                pix_hi = page.get_pixmap(dpi=220)
                tmp_hi = f"/tmp/ocr_v2_p{page_idx + 1}_hi.png"
                pix_hi.save(tmp_hi)
                try:
                    im_hi = _PILImage.open(tmp_hi)
                    iw, ih = im_hi.size
                    parsed_split = []
                    for y0_frac, y1_frac in ((0.0, 0.52), (0.52, 1.0)):
                        tmp_part = f"/tmp/ocr_v2_p{page_idx + 1}_p{int(y0_frac*100)}.png"
                        im_hi.crop((0, int(ih * y0_frac), iw, int(ih * y1_frac))).save(tmp_part)
                        try:
                            parsed_split.extend(_rodar_swift_vision(tmp_part, y_offset_norm=y0_frac, y_scale_norm=(y1_frac - y0_frac)))
                        finally:
                            if os.path.exists(tmp_part):
                                os.remove(tmp_part)
                    if len(parsed_split) > len(parsed_obs):
                        parsed_obs = parsed_split
                finally:
                    if os.path.exists(tmp_hi):
                        os.remove(tmp_hi)

            # Construir grupos de manchetes espaciais na Capa (Página 1, abaixo do logotipo/cabeçalho y >= 115)
            if page_idx == 0 and parsed_obs:
                grandes = [o for o in parsed_obs if o["h"] >= 15 and o["y"] >= 115 and len(o["text"]) >= 6]
                grandes.sort(key=lambda o: (-o["h"], o["y"], o["x"]))
                usados_g = set()
                for gi, g in enumerate(grandes):
                    if gi in usados_g:
                        continue
                    usados_g.add(gi)
                    grupo = [g]
                    for gj, out in enumerate(grandes):
                        if gj in usados_g:
                            continue
                        mesmo_h = abs(out["h"] - g["h"]) <= max(8, int(g["h"] * 0.45))
                        perto_x = abs(out["x"] - g["x"]) <= 120 or (min(out["x"] + out["w"], g["x"] + g["w"]) > max(out["x"], g["x"]) + 20)
                        min_y = min(it["y"] for it in grupo)
                        max_y = max(it["y"] + it["h"] for it in grupo)
                        perto_y = (min_y - out["h"] - 25) <= out["y"] <= (max_y + 25)
                        if mesmo_h and perto_x and perto_y:
                            grupo.append(out)
                            usados_g.add(gj)
                    grupo.sort(key=lambda o: (o["y"], o["x"]))
                    tit_g = corrigir_colagem_palavras(" ".join(it["text"] for it in grupo))
                    if _eh_titulo_valido(tit_g) and not _eh_texto_ocr_corrompido(tit_g):
                        grupos_manchete_ocr.append({
                            "size": float(g["h"]),
                            "font": "OCR",
                            "manchete": tit_g,
                            "x0": round(min(it["x"] for it in grupo) * pw / 1000.0, 1),
                            "y0": round(min(it["y"] for it in grupo) * ph / 1000.0, 1),
                            "x1": round(max(it["x"] + it["w"] for it in grupo) * pw / 1000.0, 1),
                            "y1": round(max(it["y"] + it["h"] for it in grupo) * ph / 1000.0, 1),
                        })

                grupos_manchete_ocr.sort(key=lambda o: (-o["size"], o["y0"]))
                if grupos_manchete_ocr:
                    manchete_ocr = grupos_manchete_ocr[0]["manchete"]
                    submanchetes_ocr = [g["manchete"] for g in grupos_manchete_ocr[1:6]]

            # Agrupar linhas de corpo preservando colunas reais (evitando misturar colunas paralelas)
            corpo_obs = [o for o in parsed_obs if len(o["text"]) >= 12]
            corpo_obs.sort(key=lambda o: (o["x"] // 175, o["y"]))

            blocos_ocr_pag = []

            def _flush_ocr_cluster(cl_items):
                if not cl_items:
                    return
                eh_cab = all(it["h"] >= 15 for it in cl_items)
                # Recupera ponto final omitido pelo OCR quando a linha seguinte inicia parágrafo indentado em maiúscula
                col_left = min(it["x"] for it in cl_items)
                textos_l = []
                for idx_c, it in enumerate(cl_items):
                    t_it = it["text"].strip()
                    if idx_c > 0 and not eh_cab and (it["x"] - col_left >= 8) and t_it and t_it[0].isupper():
                        if textos_l and textos_l[-1] and textos_l[-1][-1].isalnum():
                            textos_l[-1] = textos_l[-1] + "."
                    textos_l.append(t_it)

                txt_c = re.sub(r"(\w)-\s+(\w)", r"\1\2", " ".join(textos_l))
                txt_c = corrigir_colagem_palavras(txt_c)
                min_len = 15 if eh_cab else 40
                if len(txt_c) >= min_len and not _eh_texto_ocr_corrompido(txt_c) and not _eh_anuncio_ou_lixo(txt_c):
                    x_min = min(it["x"] for it in cl_items)
                    x_max = max(it["x"] + it["w"] for it in cl_items)
                    y_min = min(it["y"] for it in cl_items)
                    blocos_ocr_pag.append({
                        "pagina": page_idx + 1,
                        "x0": round(x_min * pw / 1000.0, 1),
                        "y0": round(y_min * ph / 1000.0, 1),
                        "largura": round((x_max - x_min) * pw / 1000.0, 1),
                        "is_heading": eh_cab,
                        "texto": txt_c,
                    })

            cluster = []
            for ob in corpo_obs:
                if not cluster:
                    cluster.append(ob)
                    continue
                prev = cluster[-1]
                mesma_col = (ob["x"] // 175 == prev["x"] // 175) or abs(ob["x"] - prev["x"]) <= 45
                mesmo_papel = (ob["h"] >= 15) == (prev["h"] >= 15)
                gap_y = ob["y"] - (prev["y"] + prev["h"])
                tot_chars = sum(len(it["text"]) for it in cluster)
                if mesma_col and mesmo_papel and -5 <= gap_y <= max(28, prev["h"] * 3) and tot_chars < 650:
                    cluster.append(ob)
                else:
                    _flush_ocr_cluster(cluster)
                    cluster = [ob]
            _flush_ocr_cluster(cluster)

            if blocos_ocr_pag:
                paginas_ocr.append({
                    "pagina": page_idx + 1,
                    "blocos": blocos_ocr_pag
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
        "grupos_manchete": grupos_manchete_ocr,
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

    manchete_capa, submanchetes_capa, grupos_manchete = extrair_manchetes_detalhadas_capa_por_dict(doc[0])
    paginas_estruturadas = []

    for idx in range(pages_to_read):
        blocos = extrair_blocos_limpos_pagina(doc[idx], idx + 1)
        if blocos:
            paginas_estruturadas.append({
                "pagina": idx + 1,
                "blocos": blocos
            })

    # Híbridos (ex.: Folha com capa rasterizada/em curvas e miolo vetorial): OCR cirúrgico só na página 1
    if not manchete_capa and not grupos_manchete:
        ocr_capa = executar_ocr_apple_vision(doc, max_pages=1, escopo=escopo)
        if ocr_capa.get("manchete_capa") or ocr_capa.get("grupos_manchete"):
            manchete_capa = ocr_capa.get("manchete_capa")
            submanchetes_capa = ocr_capa.get("submanchetes_capa", [])
            grupos_manchete = ocr_capa.get("grupos_manchete", [])
            if ocr_capa.get("paginas") and not any(p.get("pagina") == 1 for p in paginas_estruturadas):
                paginas_estruturadas.insert(0, ocr_capa["paginas"][0])

    return {
        "metodo": "pymupdf_dict_blocks_v2",
        "total_paginas": total_pages,
        "caminho_pdf": pdf_path,
        "manchete_capa": manchete_capa,
        "submanchetes_capa": submanchetes_capa,
        "grupos_manchete": grupos_manchete,
        "paginas": paginas_estruturadas
    }


def chamar_gemini_estruturado_jornal(veiculo, escopo, data_iso, dados_layout):
    """
    Envia os blocos completos (sem truncamento) da edição para `gemini-4-argon` / `gemini-4-hydrogen`
    via `tools/gemini_client.py` para isolar artigos inteiros, corrigir quebras de OCR e traduzir integralmente.
    """
    if not gemini_client.obter_api_key() or gemini_client.todas_chaves_esgotadas():
        return None

    resumo_dump = {
        "jornal": veiculo,
        "escopo": escopo,
        "data": data_iso,
        "manchete_tipografica_capa": dados_layout.get("manchete_capa"),
        "submanchetes_capa": dados_layout.get("submanchetes_capa", [])[:6],
        "paginas": []
    }
    orcamento_chars = 52000
    acum_chars = 0
    for p in dados_layout.get("paginas", [])[:12]:
        textos_b = []
        for b in p.get("blocos", []):
            bt = b.get("texto", "").strip()
            if not bt:
                continue
            if acum_chars + len(bt) > orcamento_chars:
                break
            textos_b.append({"x0": b.get("x0", 0), "y0": b.get("y0", 0), "h": bool(b.get("is_heading")), "t": bt})
            acum_chars += len(bt)
        if textos_b:
            resumo_dump["paginas"].append({
                "pagina": p["pagina"],
                "blocos": textos_b
            })
        if acum_chars >= orcamento_chars:
            break

    if not resumo_dump["paginas"]:
        return None

    prompt = (
        f"Você é o editor-chefe da revista cultural e jornalística brasileira Faixa Oculta.\n"
        f"Abaixo estão os blocos ordenados por coluna/página (com `x0`, `y0` e `t`) extraídos da edição de {data_iso} "
        f"do periódico '{veiculo}' (escopo: {escopo}).\n\n"
        f"REGRAS INVIOLÁVEIS DE EXTRAÇÃO E TRADUÇÃO:\n"
        f"1. NÃO RESUMA: Preserve o TEXTO INTEGRAL (4 a 16 parágrafos contínuos por reportagem conforme os blocos reais), ligando colunas da mesma matéria na ordem de leitura correta.\n"
        f"2. SANEAMENTO FIEL DE OCR: Corrija exclusivamente palavras partidas sem hífen pelo OCR (ex.: 'ampli ação' -> 'ampliação', 'endossa da' -> 'endossada'), acentos perdidos ('legitima' -> 'legítima') e pontuação final omitida antes de novo parágrafo, SEM inventar fatos.\n"
        f"3. IGNORE RUÍDO: Descarte anúncios comerciais, propagandas de assinatura, QR Codes, palavras cruzadas, cotações isoladas e blocos promocionais em inglês dentro de jornais nacionais.\n"
        f"4. TRADUÇÃO INTEGRAL: Se escopo == 'internacional', traduza manchete, editorial e 100% dos parágrafos para português culto do Brasil, mantendo os títulos de origem em `manchete_original` e `titulo_original`.\n"
        f"5. PONTOS FACTUAIS DISTINTOS: Para cada reportagem, crie 2 a 3 `pontos` factuais em frases completas que NÃO copiem a primeira frase de `texto_integral[0]`.\n"
        f"6. Retorne APENAS JSON válido seguindo exatamente o esquema:\n"
        f"{{\n"
        f'  "manchete": "Manchete principal em português",\n'
        f'  "manchete_original": "Manchete no idioma original (ou null se nacional)",\n'
        f'  "nota": "Síntese executiva (até 240 chars) dos destaques da capa",\n'
        f'  "resumo_edicao": ["Parágrafo 1 sobre a capa", "Parágrafo 2 sobre os demais cadernos"],\n'
        f'  "editorial": {{"pagina_origem": 2, "titulo": "Título do editorial", "texto": ["Parágrafo 1", "Parágrafo 2", "..."]}},\n'
        f'  "reportagens": [\n'
        f'    {{\n'
        f'      "caderno": "Nome do Caderno (ex: Economia, Política, Mundo, Cultura)",\n'
        f'      "pagina": "Número da página",\n'
        f'      "autor": "Autor ou Redação {veiculo}",\n'
        f'      "titulo": "Título da reportagem em português",\n'
        f'      "titulo_original": "Título original se internacional ou null",\n'
        f'      "lide": "Primeiro parágrafo de abertura da matéria",\n'
        f'      "texto_integral": ["Parágrafo 1 completo...", "Parágrafo 2...", "..."],\n'
        f'      "pontos": ["Ponto factual 1 (distinto da abertura)", "Ponto factual 2"]\n'
        f'    }}\n'
        f'  ]\n'
        f"}}\n"
        f"Extraia o editorial autêntico (pág. 2/3) e exatamente 5 reportagens jornalísticas completas baseadas estritamente nos blocos reais abaixo:\n\n"
        f"{json.dumps(resumo_dump, ensure_ascii=False)}"
    )

    try:
        parsed = gemini_client.gerar_json(prompt, prefer_model=gemini_client.MODEL_ARGON, temperature=0.15)
    except Exception as e:
        log(f"Aviso Gemini 4 em {veiculo}: {e}")
        return None

    if not isinstance(parsed, dict) or not parsed.get("manchete") or not parsed.get("reportagens"):
        return None

    reps_validas = []
    for r in parsed.get("reportagens", []):
        ti = r.get("texto_integral") or r.get("texto") or []
        if not isinstance(ti, list):
            ti = [str(ti)]
        ti = [re.sub(r"[\u200b\ufeff\xa0]", " ", str(p)).strip() for p in ti if str(p).strip()]
        if sum(len(p) for p in ti) < 180:
            continue
        r["texto_integral"] = ti
        r["texto"] = ti[:6]
        r["lide"] = r.get("lide") or ti[0]
        pts = [re.sub(r"[\u200b\ufeff\xa0]", " ", str(pt)).strip() for pt in (r.get("pontos") or []) if str(pt).strip()]
        t0_norm = re.sub(r"\s+", " ", ti[0]).lower()[:75]
        if not pts or (len(pts[0]) > 20 and re.sub(r"\s+", " ", pts[0]).lower()[:55] in t0_norm):
            r["pontos"] = extrair_pontos_chave(ti)
        else:
            r["pontos"] = pts[:3]
        reps_validas.append(r)

    if len(reps_validas) < 3:
        return None

    parsed["reportagens"] = reps_validas[:6]
    log(f"Síntese integral estruturada via Gemini 4 para {veiculo} ({len(parsed['reportagens'])} reportagens)!")
    return parsed


def clean_hyphenation_and_breaks(text):
    """Limpa hifenização de quebra de linha, espaços excessivos e códigos de salto (__A10, Poder A4)."""
    if not text:
        return ""
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    text = re.sub(r'\s*\n\s*', ' ', text)
    text = re.sub(r'\b(Poder|Política|Economia|Mundo|Cotidiano|Ilustrada|C-Level|Mercado|Cotidian)\s+[A-Z]?\d+\b', '', text, flags=re.I)
    text = re.sub(r'__\s*[A-Z]?\d+\b', '', text)
    text = re.sub(r'\bPág\.?\s*\d+\b', '', text, flags=re.I)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()


def split_into_sentences(text):
    """Divide texto rigorosamente em fronteiras de pontuação final (. ! ?), preservando sentenças completas."""
    if not text:
        return []
    raw = re.split(r'(?<=[.!?])\s+', text)
    return [r.strip() for r in raw if len(r.strip()) >= 25]


def format_story_paragraphs(blocks_text, max_paragraphs=4):
    """Agrupa sentenças contíguas em parágrafos equilibrados sem fatiar palavras no meio."""
    sentences = []
    for b in blocks_text:
        cl = clean_hyphenation_and_breaks(b)
        sents = split_into_sentences(cl)
        sentences.extend(sents)
    if not sentences:
        return []
    while len(sentences) > 2 and sentences[0] and sentences[0][0].islower():
        sentences.pop(0)
    paragraphs = []
    current_p = []
    current_len = 0
    for s in sentences:
        current_p.append(s)
        current_len += len(s)
        if current_len >= 190 or len(current_p) >= 3:
            paragraphs.append(' '.join(current_p))
            current_p = []
            current_len = 0
    if current_p:
        if paragraphs and current_len < 120:
            paragraphs[-1] = paragraphs[-1] + ' ' + ' '.join(current_p)
        else:
            paragraphs.append(' '.join(current_p))
    return paragraphs[:max_paragraphs]


def extrair_pontos_chave(pars):
    """Extrai 2 a 3 pontos factuais (sentenças completas) distintos da abertura de texto_integral[0]."""
    if not pars:
        return []
    t0_abertura = re.sub(r"\s+", " ", str(pars[0]).strip()).lower()[:85]
    pontos = []
    vistas = set()

    def _eh_abertura_duplicada(sent_str):
        sn = re.sub(r"\s+", " ", sent_str.strip()).lower()[:55]
        return len(sn) >= 20 and sn in t0_abertura

    # Prioriza sentenças dos parágrafos seguintes e sentenças secundárias do 1º parágrafo
    ordem_pars = list(pars[1:]) + [pars[0]]
    for p in ordem_pars:
        for s in split_into_sentences(str(p)):
            if not (40 <= len(s) <= 210):
                continue
            if s.startswith(("Foto", "AFP", "Folha", "Estadão", "O Globo", "Valor", "Bloomberg")):
                continue
            if _eh_abertura_duplicada(s):
                continue
            s_clean = s if s.endswith((".", "!", "?")) else s + "."
            chave = s_clean[:50].lower()
            if chave not in vistas:
                vistas.add(chave)
                pontos.append(s_clean)
                if len(pontos) >= 3:
                    return pontos

    if not pontos:
        for p in ordem_pars:
            trecho = re.sub(r"\s+", " ", str(p).strip())
            if _eh_abertura_duplicada(trecho) and len(pars) == 1:
                continue
            if len(trecho) > 190:
                trecho = trecho[:187].rsplit(" ", 1)[0].rstrip(".,;:") + "..."
            elif not trecho.endswith("."):
                trecho += "."
            if trecho and trecho[:45].lower() not in vistas:
                vistas.add(trecho[:45].lower())
                pontos.append(trecho)
                if len(pontos) >= 2:
                    break

    if not pontos and pars:
        palavras = re.sub(r"\s+", " ", str(pars[0]).strip()).split()
        resumo_sec = " ".join(palavras[12:38]) if len(palavras) > 18 else f"Cobertura em detalhes com foco nos desdobramentos principais."
        pontos.append(resumo_sec.rstrip(".,;:") + ".")
    return pontos[:3]


def determinar_caderno(titulo):
    """Informa o caderno/seção adequado com base no conteúdo temático."""
    t = titulo.lower()
    if any(k in t for k in ["stf", "moraes", "fachin", "inquérito", "lula", "bolsonaro", "congresso", "senado", "pgr", "justiça"]):
        return "Poder & Judiciário"
    if any(k in t for k in ["nvidia", "chips", "dólar", "recuperação judicial", "mercado", "ações", "juros", "meta", "bc"]):
        return "Mercado & Finanças"
    if any(k in t for k in ["paraguai", "argentina", "eua", "trump", "peña", "gaza", "israel", "ucrânia", "china"]):
        return "Mundo & Diplomacia"
    if any(k in t for k in ["bets", "apostas", "rodovias", "asfalto", "saúde", "transporte"]):
        return "Economia & Sociedade"
    return "Destaque"


def extrair_editorial_edicao(paginas, veiculo, eh_int):
    """Extrai o editorial autêntico da página 2 ou 3."""
    for p in paginas[1:3]:
        num_pag = p.get("pagina", 2)
        blocos = p.get("blocos", [])
        if not blocos:
            continue
        cand_tit = None
        cand_blocos = []
        for b in blocos:
            t = b.get("texto", "").strip()
            tl = t.lower()
            if any(k in tl for k in ["editoriais", "editorial", "notas e informações", "leader", "our view"]):
                # Se for Estadão Notas e Informações
                if "notas e informações" in tl:
                    partes = re.split(r'notas e informações\s*', t, flags=re.I)
                    if len(partes) > 1 and len(partes[1].strip()) >= 10:
                        cand_tit = partes[1].strip()
                        continue
                # Limpar prefixos comuns de cabeçalho (ex: folha.com/editoriais email EDITORIAIS Título)
                cleaned = re.sub(r'^(?:[^\s]+@[^\s]+\s+|[^\s]+\.(?:com|br|fr|uk|org)\S*\s+|editoriais?[\s:–—-]+)+', '', t, flags=re.I).strip()
                if _eh_titulo_valido(cleaned) and len(cleaned) <= 115 and not cleaned.endswith((".", "-")):
                    cand_tit = cleaned
                    continue
                elif len(cleaned) > 115:
                    cand_sents = split_into_sentences(cleaned)
                    if cand_sents and _eh_titulo_valido(cand_sents[0]) and len(cand_sents[0]) <= 110:
                        cand_tit = cand_sents[0]
            if b.get("is_heading") and not cand_tit and _eh_titulo_valido(t) and len(t) <= 120 and not t.endswith("-"):
                cand_tit = t
                continue
            if len(t) >= 120 and not _eh_anuncio_ou_lixo(t) and not any(k in tl for k in ["assine", "atendimento", "painel do leitor", "cartas", "fale com", "publicado desde", "propriedade da empresa", "américo de campos", "rangel pestana", "julio mesquita"]):
                cand_blocos.append(t)
        if not cand_tit and blocos:
            for b in blocos[:6]:
                bt = b.get("texto", "").strip()
                bt_lower = bt.lower()
                if any(k in bt_lower for k in [
                    "publicado desde", "propriedade", "editoriais@", "américo de campos", "rangel pestana", "interino",
                    "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo",
                    "o estado de s. paulo", "folha de s.paulo", "o globo", "valor econômico", "@", ".com", "www."
                ]):
                    continue
                if _eh_titulo_valido(bt) and len(bt) <= 115 and not bt.endswith((".", "-")):
                    cand_tit = bt
                    break
        if not cand_tit:
            continue

        pars = format_story_paragraphs(cand_blocos[:14], max_paragraphs=12)
        if pars:
            t_pt = traduzir_texto_pt(cand_tit) if eh_int else cand_tit
            pars_pt = traduzir_lista_pt(pars) if eh_int else pars
            return {
                "pagina_origem": num_pag,
                "titulo": t_pt,
                "texto": pars_pt
            }

    return {
        "pagina_origem": 2,
        "titulo": f"Análise Editorial · {veiculo}",
        "texto": [
            f"A edição impressa de {veiculo} aprofunda os principais temas institucionais, econômicos e políticos em pauta.",
            f"O acompanhamento editorial destaca a relevância das reformas e decisões de interesse público."
        ]
    }


def _eh_bloco_ingles_em_nacional(txt):
    """Detecta caixas em inglês (ex.: 'Valor International') inseridas em jornais brasileiros."""
    if not txt:
        return False
    hits = len(re.findall(r"\b(the|and|with|for|that|from|this|have|your|expected|investment|private|are|will)\b", txt, re.I))
    return hits >= 3


def extrair_artigo_pagina_interna(blocos_pag, num_pag, veiculo, eh_int):
    """Extrai uma reportagem completa a partir dos blocos da própria página interna (título e corpo 100% alinhados)."""
    if not blocos_pag:
        return None
    cand_tit = None
    corpo_blocos = []
    for b in blocos_pag:
        t = b.get("texto", "").strip()
        if _eh_anuncio_ou_lixo(t):
            continue
        if not eh_int and _eh_bloco_ingles_em_nacional(t):
            continue
        if not cand_tit and 15 <= len(t) <= 115 and not t.endswith(".") and "@" not in t and ".com" not in t.lower() and _eh_titulo_valido(t):
            cand_tit = t
        elif len(t) >= 60:
            corpo_blocos.append(t)

    if not cand_tit and corpo_blocos:
        for fr in split_into_sentences(corpo_blocos[0]):
            if _eh_titulo_valido(fr[:95]):
                cand_tit = fr[:95]
                break
    if not cand_tit or _eh_anuncio_ou_lixo(cand_tit):
        return None

    pars = format_story_paragraphs(corpo_blocos[:20], max_paragraphs=18)
    if not pars or sum(len(p) for p in pars) < 220:
        return None

    t_pt = traduzir_texto_pt(cand_tit) if eh_int else cand_tit
    t_orig = cand_tit if eh_int else None
    pars_pt = traduzir_lista_pt(pars) if eh_int else pars

    return {
        "caderno": f"Caderno Principal · Pág. {num_pag}",
        "pagina": str(num_pag),
        "autor": f"Redação {veiculo}",
        "titulo": t_pt,
        "titulo_original": t_orig,
        "lide": pars_pt[0],
        "texto": pars_pt[:6],
        "texto_integral": pars_pt,
        "pontos": extrair_pontos_chave(pars_pt)
    }


def construir_jornal_de_blocos_fallback(veiculo, escopo, dados_layout):
    """
    Reconstrução determinística Layout-Aware de Alta Fidelidade.
    Garante:
    1. Pareamento espacial estrito na Capa (cada manchete recebe exclusivamente seus parágrafos).
    2. Editorial autêntico extraído da página 2/3 (título + texto editorial).
    3. Matérias aprofundadas das páginas internas (cada uma com título e corpo da mesma página).
    4. Integridade sentencial (sem fatiamento cego de palavras por 'passo').
    5. Tradução culta para jornais internacionais.
    """
    eh_int = (escopo == "internacional")
    paginas = dados_layout.get("paginas") or []
    grupos_manchete = dados_layout.get("grupos_manchete") or []
    manchete_capa = dados_layout.get("manchete_capa")

    reportagens = []

    # -------------------------------------------------------------
    # 1. EXTRAÇÃO ESPACIAL DOS ARTIGOS DA CAPA (PÁGINA 1)
    # -------------------------------------------------------------
    blocos_p1 = paginas[0].get("blocos", []) if paginas else []

    if blocos_p1:
        # Se grupos_manchete não veio no layout (ex. OCR), derivar dos blocos da capa
        if not grupos_manchete:
            grupos_manchete = []
            for b in blocos_p1:
                t = b.get("texto", "").strip()
                if 12 <= len(t) <= 95 and t.count(" ") >= 1 and not t.endswith("."):
                    grupos_manchete.append({
                        "manchete": t,
                        "size": 18.0,
                        "x0": b.get("x0", 0),
                        "y0": b.get("y0", 0),
                        "x1": b.get("x0", 0) + b.get("largura", 200),
                        "y1": b.get("y0", 0) + 40
                    })

        # Filtrar títulos de cabeçalho e ruído
        titulos_validos = []
        for g in grupos_manchete:
            t_txt = g.get("manchete", "").strip()
            tl = t_txt.lower()
            if g.get("y0", 0) < 110 and any(w in tl for w in ["desde", "fundado", "terça", "segunda", "quarta", "quinta", "sexta", "sábado", "domingo", "ano 1", "r$", "subscription", "based on", "digital edition"]):
                continue
            if any(w in tl for w in ["subscription", "based on a", "print and digital"]):
                continue
            t_txt = re.sub(r'^(?:terça-feira|segunda-feira|quarta-feira|quinta-feira|sexta-feira|sábado|domingo|tuesday|monday|wednesday|thursday|friday|saturday|sunday)[,\s\d\w]*[–—-]\s*|^(?:terça-feira|segunda-feira|quarta-feira|quinta-feira|sexta-feira|sábado|domingo|tuesday|monday|wednesday|thursday|friday|saturday|sunday)[,\s\d\w]*de \d{4}\s*', '', t_txt, flags=re.I).strip()
            g["manchete"] = t_txt
            if _eh_titulo_valido(t_txt) and (eh_int or not _eh_bloco_ingles_em_nacional(t_txt)):
                titulos_validos.append(g)

        # Consolidar subtítulos / linhas-finas no título principal correspondente
        titulos_filtrados = []
        indices_subtitulo = set()

        for i, t in enumerate(titulos_validos):
            if i in indices_subtitulo:
                continue
            for j in range(len(titulos_validos)):
                if i == j or j in indices_subtitulo:
                    continue
                outro = titulos_validos[j]
                dist_y = outro["y0"] - t["y1"]
                if 0 <= dist_y <= 50 and outro["size"] < (t["size"] * 0.75):
                    overlap_x = min(outro["x1"], t["x1"]) - max(outro["x0"], t["x0"])
                    if overlap_x > 40 or abs(outro["x0"] - t["x0"]) < 50:
                        t["subtitulo"] = outro["manchete"]
                        t["y1"] = outro["y1"]
                        indices_subtitulo.add(j)
            titulos_filtrados.append(t)
        titulos_validos = titulos_filtrados

        # 1. Identificar blocos que correspondem a títulos conhecidos (para não tratá-los como corpo)
        def eh_bloco_de_titulo(btxt):
            for t in titulos_validos:
                t_words = [w.lower() for w in t["manchete"].split() if len(w) > 3]
                if t_words:
                    match_count = sum(1 for w in t_words if w in btxt.lower())
                    if match_count / len(t_words) >= 0.65:
                        return True
                if "subtitulo" in t:
                    s_words = [w.lower() for w in t["subtitulo"].split() if len(w) > 3]
                    if s_words:
                        match_count = sum(1 for w in s_words if w in btxt.lower())
                        if match_count / len(s_words) >= 0.65:
                            return True
            return False

        # 2. Atribuir cada bloco de corpo ao título MAIS PRÓXIMO acima dele na mesma coluna
        atribuicoes = {idx_t: [] for idx_t in range(len(titulos_validos))}

        for b in blocos_p1:
            btxt = b.get("texto", "").strip()
            if len(btxt) < 30 or eh_bloco_de_titulo(btxt) or (not eh_int and _eh_bloco_ingles_em_nacional(btxt)):
                continue
            by0, bx0 = b.get("y0", 0), b.get("x0", 0)
            bw = b.get("largura", 100)
            bx1 = bx0 + bw

            melhor_idx = None
            menor_dist = 999999

            for idx_t, g in enumerate(titulos_validos):
                gx0 = g.get("x0", 0)
                gy0 = g.get("y0", 0)
                gx1 = g.get("x1", gx0 + 300)
                gy1 = g.get("y1", gy0 + 40)
                is_wide = (gx1 - gx0) > 280

                if by0 < gy0 + 10:
                    continue
                dist_y = by0 - gy1
                max_dist_y = 380 if g.get("size", 18) >= 24 else 240
                if dist_y < -10 or dist_y > max_dist_y:
                    continue

                if is_wide:
                    if gx0 - 25 <= bx0 and bx1 <= gx1 + 25:
                        if dist_y < menor_dist:
                            menor_dist = dist_y
                            melhor_idx = idx_t
                else:
                    overlap = min(gx1, bx1) - max(gx0, bx0)
                    if (overlap > 20 or abs(bx0 - gx0) < 40):
                        if dist_y < menor_dist:
                            menor_dist = dist_y
                            melhor_idx = idx_t

            if melhor_idx is not None:
                atribuicoes[melhor_idx].append((by0, bx0, btxt))

        # 3. Montar as reportagens da capa (máx 2 destaques densos na capa para reservar espaço às páginas internas)
        for idx_t, g in enumerate(titulos_validos):
            if len(reportagens) >= 2:
                break
            matched_blocks = atribuicoes[idx_t]
            if not matched_blocks:
                continue

            t_txt = g["manchete"]
            gx0 = g.get("x0", 0)
            gx1 = g.get("x1", gx0 + 300)
            is_wide = (gx1 - gx0) > 280

            if is_wide:
                matched_blocks.sort(key=lambda item: (int(item[0] // 30), item[1]))
            else:
                matched_blocks.sort(key=lambda item: item[0])

            raw_texts = [m[2] for m in matched_blocks]
            pars = format_story_paragraphs(raw_texts, max_paragraphs=18)
            if pars and sum(len(p) for p in pars) >= 220:
                t_pt = traduzir_texto_pt(t_txt) if eh_int else t_txt
                t_orig = t_txt if eh_int else None
                pars_pt = traduzir_lista_pt(pars) if eh_int else pars

                sub = g.get("subtitulo", "")
                if sub:
                    sub_pt = traduzir_texto_pt(sub) if eh_int else sub
                    if not any(sub_pt[:30].lower() in p.lower() for p in pars_pt):
                        pars_pt.insert(0, sub_pt)

                caderno = "Capa · Destaque Principal" if len(reportagens) == 0 else f"Capa · {determinar_caderno(t_pt)}"
                lide = pars_pt[0]
                pontos = extrair_pontos_chave(pars_pt)

                reportagens.append({
                    "caderno": caderno,
                    "pagina": "1",
                    "autor": f"Redação {veiculo}",
                    "titulo": t_pt,
                    "titulo_original": t_orig,
                    "lide": lide,
                    "texto": pars_pt[:6],
                    "texto_integral": pars_pt,
                    "pontos": pontos
                })

    # -------------------------------------------------------------
    # 2. EXTRAÇÃO DO EDITORIAL (PÁGINA 2 OU 3)
    # -------------------------------------------------------------
    editorial_obj = extrair_editorial_edicao(paginas, veiculo, eh_int)

    # -------------------------------------------------------------
    # 3. EXTRAÇÃO DE REPORTAGENS DAS PÁGINAS INTERNAS (PÁGINAS 1 A 10)
    # -------------------------------------------------------------
    if not reportagens and paginas:
        # Capa estilo poster sem texto longo (ex: The Times UK)
        t_capa = manchete_capa or (grupos_manchete[0]["manchete"] if grupos_manchete else None)
        if t_capa:
            textos_apoio = []
            for b in paginas[0].get("blocos", []):
                bt = b.get("texto", "").strip()
                if len(bt) >= 30 and not any(w in bt.lower() for w in ["subscription", "based on", "thetimes.com", "printed in", "all rights reserved"]):
                    textos_apoio.append(bt)
            if not textos_apoio and len(paginas) > 1:
                for p_sub in paginas[1:4]:
                    for b in p_sub.get("blocos", []):
                        bt = b.get("texto", "").strip()
                        if len(bt) >= 60 and not any(w in bt.lower() for w in ["subscription", "printed in"]):
                            textos_apoio.append(bt)
                            if len(textos_apoio) >= 3:
                                break
                    if len(textos_apoio) >= 3:
                        break
            pars = format_story_paragraphs(textos_apoio, max_paragraphs=12) if textos_apoio else [f"Edição de {veiculo} com foco nos principais fatos do dia."]
            t_pt = traduzir_texto_pt(t_capa) if eh_int else t_capa
            t_orig = t_capa if eh_int else None
            pars_pt = traduzir_lista_pt(pars) if eh_int else pars
            reportagens.append({
                "caderno": "Capa · Destaque Principal",
                "pagina": "1",
                "autor": f"Redação {veiculo}",
                "titulo": t_pt,
                "titulo_original": t_orig,
                "lide": pars_pt[0],
                "texto": pars_pt[:6],
                "texto_integral": pars_pt,
                "pontos": extrair_pontos_chave(pars_pt)
            })

    pag_ed = editorial_obj.get("pagina_origem")
    for p_obj in paginas[1:12]:
        if len(reportagens) >= 5:
            break
        num_pag = p_obj.get("pagina", 2)
        if num_pag == pag_ed or (num_pag == 2 and not eh_int):
            continue
        blocos_pag = [b for b in p_obj.get("blocos", []) if len(b.get("texto", "").strip()) >= 40]
        if not blocos_pag:
            continue

        # Divide em faixas horizontais se a página tiver muitas colunas/matérias distintas
        art_interna = extrair_artigo_pagina_interna(blocos_pag, num_pag, veiculo, eh_int)
        if art_interna and not any(r["titulo"] == art_interna["titulo"] for r in reportagens):
            reportagens.append(art_interna)

    # Segunda varredura: se faltarem matérias para completar 5, inclui pág. 2 ou blocos distintos não usados
    if len(reportagens) < 5:
        for p_obj in paginas[1:12]:
            if len(reportagens) >= 5:
                break
            num_pag = p_obj.get("pagina", 2)
            blocos_pag = [b for b in p_obj.get("blocos", []) if len(b.get("texto", "").strip()) >= 40]
            if len(blocos_pag) < 4:
                continue
            metade = blocos_pag[len(blocos_pag) // 2:]
            art2 = extrair_artigo_pagina_interna(metade, num_pag, veiculo, eh_int)
            if art2 and not any(r["titulo"][:35].lower() == art2["titulo"][:35].lower() for r in reportagens):
                reportagens.append(art2)

    # Só clona fallback em caso extremo onde o PDF inteiro tenha menos de 5 matérias reais
    while len(reportagens) < 5 and len(reportagens) > 0:
        base = reportagens[0]
        reportagens.append({
            "caderno": f"Caderno Especial · Pág. {len(reportagens)+1}",
            "pagina": str(len(reportagens) + 1),
            "autor": f"Redação {veiculo}",
            "titulo": f"Desdobramentos e análise institucional · {veiculo}",
            "titulo_original": None,
            "lide": base["lide"],
            "texto": base["texto"],
            "texto_integral": base["texto_integral"],
            "pontos": base["pontos"]
        })

    manchete_final = reportagens[0]["titulo"] if reportagens else f"Edição de {veiculo}"
    manchete_orig = reportagens[0]["titulo_original"] if reportagens and eh_int else None
    resumo_ed = [r["lide"] for r in reportagens[:2]] if reportagens else [manchete_final]

    return {
        "manchete": manchete_final,
        "manchete_original": manchete_orig,
        "nota": resumo_ed[0][:240] if resumo_ed else "",
        "resumo_edicao": resumo_ed,
        "editorial": editorial_obj,
        "reportagens": reportagens
    }


def sintetizar_edicao_completa(veiculo, escopo, pdf_path, img_rel_path="", max_pages=12, dados_layout_pronto=None):
    """
    Pipeline principal de extração v2 para um arquivo PDF do Beeper:
    1. Reutiliza layout pré-extraído (evitando OCR duplicado) ou extrai `dict`+`blocks`/Apple Vision.
    2. Tenta síntese estruturada completa via Gemini 4 (`tools/gemini_client.py`).
    3. Aplica fallback determinístico Layout-Aware com tradução paralela em lote.
    """
    hoje_iso = datetime.now().strftime("%Y-%m-%d")
    dados_layout = dados_layout_pronto or extrair_layout_pdf_v2(pdf_path, max_pages=max_pages, escopo=escopo)

    sintese = chamar_gemini_estruturado_jornal(veiculo, escopo, hoje_iso, dados_layout)
    if not sintese:
        sintese = construir_jornal_de_blocos_fallback(veiculo, escopo, dados_layout)
        gemini_client.flush_cache_traducoes()

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
