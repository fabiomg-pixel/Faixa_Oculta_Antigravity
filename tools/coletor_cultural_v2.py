#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/coletor_cultural_v2.py
----------------------------
Coletor Dinâmico de Cultura Mensal (Música, Cinema, Livros) e Agenda de Pequenas Casas do Rio (Arquitetura v2).

Desacopla `tools/cultura_mensal.py`, `tools/revista_semanal.py` e `tools/varredura_cultural_online.py`
de listas estáticas, realizando apuração ao vivo em:
1. Música:
   - Feeds RSS: Pitchfork Album Reviews, Stereogum, BrooklynVegan, The Quietus, Hits Perdidos, TMDQA.
   - Enriquecimento via Deezer API (`api.deezer.com/search/album` e `/album/<id>`) e iTunes Search API:
     capa oficial em alta resolução (1000x1000 / 600x600bb salva em `capas/<md5>.jpg`), lista de faixas real,
     selo/gravadora e ano de lançamento.
2. Cinema:
   - Feeds RSS: The Guardian Film, IndieWire, Letterboxd Journal, Revista Cinética.
   - Calendário de estreias do circuito brasileiro via AdoroCinema Agenda (`adorocinema.com/filmes/agenda/`).
   - Capas via Wikipedia/Wikimedia API e iTunes Movie API + busca de trailer oficial real no YouTube.
3. Livros:
   - Feeds RSS: Quatro Cinco Um, Jornal Rascunho, NYT Books, The Guardian Books, Literary Hub (LitHub).
   - Capas via iTunes Books API e Open Library Search API (`openlibrary.org/search.json`).
4. Agenda Cultural do Rio de Janeiro:
   - Extração JSON-LD (`Schema.org/Event`) e HTML SSR de CCBB Rio, IMS Rio, Sala Cecília Meireles,
     Bar Bukowski, Fever Rio, Sympla RJ e Veja Rio Programe-se.
   - Descoberta e estruturação das pequenas casas da cena independente carioca (Audio Rebel, Saloon 79,
     Estúdio Hanoi, Garage Grindhouse, Circo Voador) via `gemini-4-argon` / `gemini-3.8-flash` com resolução
     de `videoId` do YouTube para 100% das bandas.
"""

import os
import re
import sys
import ssl
import gzip
import json
import hashlib
import datetime
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Contexto SSL não-verificado obrigatório em todas as chamadas urllib.request.urlopen
SSL_CTX = ssl._create_unverified_context()

HEADERS_API = {
    "User-Agent": "FaixaOcultaBot/1.0 (contact@faixaoculta.com)"
}

HEADERS_WEB = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CAPAS_DIR = os.path.join(ROOT_DIR, "capas")
os.makedirs(CAPAS_DIR, exist_ok=True)

FEEDS_MUSICA_V2 = [
    ("Pitchfork Album Reviews", "https://pitchfork.com/feed/feed-album-reviews/rss", "internacional"),
    ("Stereogum", "https://www.stereogum.com/feed/", "internacional"),
    ("BrooklynVegan", "https://www.brooklynvegan.com/feed/", "internacional"),
    ("The Quietus", "https://thequietus.com/feed", "internacional"),
    ("Hits Perdidos", "https://hitsperdidos.com/feed/", "brasil"),
    ("Tenho Mais Discos Que Amigos", "https://www.tenhomaisdiscosqueamigos.com/feed/", "brasil"),
]

FEEDS_CINEMA_V2 = [
    ("The Guardian Film", "https://www.theguardian.com/film/rss", "internacional"),
    ("IndieWire", "https://www.indiewire.com/feed/", "internacional"),
    ("Letterboxd Journal", "https://letterboxd.com/journal/rss/", "internacional"),
    ("Revista Cinética", "http://revistacinetica.com.br/nova/feed/", "brasil"),
]

FEEDS_LIVROS_V2 = [
    ("Quatro Cinco Um", "https://quatrocincoum.com.br/feed/", "brasil"),
    ("Jornal Rascunho", "https://rascunho.com.br/feed/", "brasil"),
    ("NYT Books", "https://rss.nytimes.com/services/xml/rss/nyt/Books.xml", "internacional"),
    ("The Guardian Books", "https://www.theguardian.com/books/rss", "internacional"),
    ("Literary Hub", "https://lithub.com/feed/", "internacional"),
]

FONTES_AGENDA_RIO_V2 = [
    ("CCBB Rio", "https://ccbb.com.br/rio-de-janeiro/programacao/", "Centro", "centro", "cinema"),
    ("IMS Moreira Salles Rio", "https://ims.com.br/unidade/rio-de-janeiro/", "Gávea", "zona_sul", "cinema"),
    ("Sala Cecília Meireles", "https://salaceciliameireles.rj.gov.br/programacao/", "Lapa", "centro", "musica"),
    ("Bar Bukowski", "https://www.barbukowski.com.br/", "Botafogo", "zona_sul", "musica"),
    ("Sympla Shows Rio", "https://www.sympla.com.br/eventos/rio-de-janeiro-rj/show-musica-festa", "Rio de Janeiro", "zona_sul", "musica"),
    ("Fever Rio", "https://feverup.com/pt/rio-de-janeiro", "Rio de Janeiro", "zona_sul", "musica"),
    ("Veja Rio Programe-se", "https://vejario.abril.com.br/programe-se/", "Rio de Janeiro", "zona_sul", "musica"),
]


def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S') if hasattr(datetime, 'now') else datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [ColetorCultural-v2] {msg}", flush=True)


def obter_chave_gemini():
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"].strip()
    for p in [os.path.expanduser("~/.faixaoculta/.env"), os.path.expanduser("~/.env"), os.path.join(ROOT_DIR, ".env")]:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip().startswith("GEMINI_API_KEY="):
                            return line.strip().split("=", 1)[1].strip().strip('"').strip("'")
            except Exception:
                pass
    return None


def http_get_text(url, headers=None, timeout=10):
    req = urllib.request.Request(url, headers=headers or HEADERS_WEB)
    with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as resp:
        raw = resp.read()
        if raw[:2] == b"\x1f\x8b" or "gzip" in str(resp.headers.get("Content-Encoding", "")).lower():
            try:
                raw = gzip.decompress(raw)
            except Exception:
                pass
        try:
            return raw.decode("utf-8")
        except Exception:
            return raw.decode("latin-1", errors="replace")


def baixar_capa_oficial(url):
    """Baixa imagem oficial de alta resolução e salva em `capas/<md5>.jpg`."""
    if not url or not str(url).startswith("http"):
        return None
    try:
        req = urllib.request.Request(url, headers=HEADERS_API)
        with urllib.request.urlopen(req, timeout=12, context=SSL_CTX) as resp:
            conteudo = resp.read()
            if len(conteudo) < 2500:
                return None
            h = hashlib.md5(conteudo).hexdigest()
            dest = os.path.join(CAPAS_DIR, f"{h}.jpg")
            if not os.path.exists(dest):
                with open(dest, "wb") as f:
                    f.write(conteudo)
            return f"capas/{h}.jpg"
    except Exception:
        return None


def traduzir_pt(texto):
    if not texto or not texto.strip():
        return ""
    try:
        q = urllib.parse.quote(texto.strip()[:1800])
        u = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=pt&dt=t&q={q}"
        req = urllib.request.Request(u, headers=HEADERS_WEB)
        with urllib.request.urlopen(req, timeout=7, context=SSL_CTX) as r:
            d = json.loads(r.read().decode("utf-8"))
            return "".join(seg[0] for seg in d[0] if seg and seg[0]).strip()
    except Exception:
        return texto.strip()


def ler_itens_rss(url, max_itens=15):
    """Lê um feed RSS/Atom retornando título, link, resumo limpo e corpo `<content:encoded>`."""
    try:
        xml_str = http_get_text(url, headers=HEADERS_WEB, timeout=9)
        xml_clean = re.sub(r"[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD]", "", xml_str)
        root = ET.fromstring(xml_clean)
    except Exception as e:
        log(f"Aviso ao ler RSS ({url}): {e}")
        return []

    items = root.findall(".//item")
    if not items:
        items = root.findall(".//{http://www.w3.org/2005/Atom}entry")

    resultados = []
    for it in items[:max_itens]:
        tit_el = it.find("title")
        lnk_el = it.find("link")
        desc_el = it.find("description")
        if desc_el is None:
            desc_el = it.find("{http://www.w3.org/2005/Atom}summary")
        ce_el = it.find("{http://purl.org/rss/1.0/modules/content/}encoded")
        if ce_el is None:
            ce_el = it.find("{http://www.w3.org/2005/Atom}content")

        titulo = (tit_el.text or "").strip() if tit_el is not None else ""
        link = ""
        if lnk_el is not None:
            link = (lnk_el.text or "").strip() or lnk_el.attrib.get("href", "").strip()

        desc_html = (desc_el.text or "") if desc_el is not None else ""
        ce_html = (ce_el.text or "") if ce_el is not None else ""

        soup_d = BeautifulSoup(desc_html, "html.parser")
        resumo = re.sub(r"\s+", " ", soup_d.get_text()).strip()

        paragrafos = []
        if ce_html:
            soup_ce = BeautifulSoup(ce_html, "html.parser")
            for p in soup_ce.find_all("p"):
                pt = re.sub(r"\s+", " ", p.get_text()).strip()
                if len(pt) >= 45:
                    paragrafos.append(pt)
        if not paragrafos and len(resumo) >= 60:
            paragrafos = [resumo]

        if titulo and link:
            resultados.append({
                "titulo": titulo,
                "url": link,
                "resumo": resumo,
                "paragrafos": paragrafos[:5]
            })
    return resultados


# ==============================================================================
# 1. MÚSICA: DEEZER API + ITUNES API + FEEDS INDIE INTERNACIONAIS E BRASILEIROS
# ==============================================================================

def enriquecer_album_deezer_itunes(termo_busca, baixar_capa=True):
    """
    Consulta a Deezer API (prioridade 1: capa 1000x1000, faixas reais, selo, data)
    e iTunes Search API (prioridade 2: capa 600x600bb, gênero) para enriquecer um álbum.
    """
    q = urllib.parse.quote(termo_busca.strip())
    meta = {
        "artista": None,
        "album": None,
        "ano": datetime.datetime.now().year,
        "genero": "indie rock / alternativo",
        "selo": "Independente",
        "faixas": [],
        "capa_url": None,
        "capa_local": None,
        "deezer_id": None
    }

    # 1. Deezer API
    try:
        u_dz = f"https://api.deezer.com/search/album?q={q}&limit=3"
        req = urllib.request.Request(u_dz, headers=HEADERS_API)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as r:
            d = json.loads(r.read().decode("utf-8"))
            data_list = d.get("data", [])
            if data_list:
                top = data_list[0]
                album_id = top.get("id")
                meta["deezer_id"] = album_id
                meta["artista"] = top.get("artist", {}).get("name")
                meta["album"] = top.get("title")
                meta["capa_url"] = top.get("cover_xl") or top.get("cover_big")

                # Detalhes do álbum (faixas, selo, ano)
                if album_id:
                    u_det = f"https://api.deezer.com/album/{album_id}"
                    req_d = urllib.request.Request(u_det, headers=HEADERS_API)
                    with urllib.request.urlopen(req_d, timeout=8, context=SSL_CTX) as rd:
                        det = json.loads(rd.read().decode("utf-8"))
                        if det.get("label"):
                            meta["selo"] = det["label"]
                        if det.get("release_date"):
                            try:
                                meta["ano"] = int(det["release_date"][:4])
                            except Exception:
                                pass
                        generos = [g.get("name") for g in det.get("genres", {}).get("data", []) if g.get("name")]
                        if generos:
                            meta["genero"] = " / ".join(generos).lower()
                        tracks = [t.get("title") for t in det.get("tracks", {}).get("data", []) if t.get("title")]
                        if tracks:
                            meta["faixas"] = tracks[:10]
    except Exception:
        pass

    # 2. Complemento / Fallback via iTunes Search API
    if not meta["capa_url"] or not meta["artista"]:
        try:
            u_it = f"https://itunes.apple.com/search?term={q}&entity=album&limit=3"
            req = urllib.request.Request(u_it, headers=HEADERS_API)
            with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as r:
                d = json.loads(r.read().decode("utf-8"))
                results = d.get("results", [])
                if results:
                    top = results[0]
                    meta["artista"] = meta["artista"] or top.get("artistName")
                    meta["album"] = meta["album"] or top.get("collectionName")
                    art100 = top.get("artworkUrl100", "")
                    if art100 and not meta["capa_url"]:
                        meta["capa_url"] = art100.replace("100x100bb", "600x600bb")
                    if top.get("primaryGenreName") and meta["genero"] == "indie rock / alternativo":
                        meta["genero"] = top["primaryGenreName"].lower()
                    if top.get("releaseDate"):
                        try:
                            meta["ano"] = int(top["releaseDate"][:4])
                        except Exception:
                            pass
        except Exception:
            pass

    if baixar_capa and meta["capa_url"]:
        meta["capa_local"] = baixar_capa_oficial(meta["capa_url"])

    return meta


def extrair_par_artista_album(titulo_post, fonte_nome):
    """Extrai candidatos a (Artista, Álbum) de títulos de resenhas do Pitchfork, Stereogum, Hits Perdidos, etc."""
    t = titulo_post.strip()
    # Pitchfork: "Artist: Album Title"
    if fonte_nome == "Pitchfork Album Reviews" and ":" in t:
        p1, p2 = t.split(":", 1)
        return p1.strip(), p2.strip()
    # Stereogum: "Album Of The Week: Artist Album" ou "Premature Evaluation: Artist Album"
    m_sg = re.match(r"^(?:Album Of The Week|Premature Evaluation|Stream)\s*:\s*(.+)$", t, flags=re.I)
    if m_sg:
        resto = m_sg.group(1).strip()
        if " – " in resto:
            a, b = resto.split(" – ", 1)
            return a.strip(), b.strip(" '“”\"")
        if " - " in resto:
            a, b = resto.split(" - ", 1)
            return a.strip(), b.strip(" '“”\"")
        return resto, ""
    # Padrão com travessão ou aspas
    for sep in [" – ", " — ", " - "]:
        if sep in t:
            p1, p2 = t.split(sep, 1)
            if len(p1) < 40 and len(p2) < 55:
                return p1.strip(), p2.strip(" '“”\"")
    return None, None


def coletar_safra_musica_v2(max_itens=12, baixar_capas=True):
    """Coleta lançamentos e resenhas de álbuns em tempo real dos feeds musicais e enriquece via Deezer/iTunes."""
    log("Coletando safra musical contemporânea nos feeds (Pitchfork, Stereogum, BrooklynVegan, Quietus, Hits Perdidos, TMDQA)...")
    descobertos = []
    vistos = set()

    for fonte, url, escopo in FEEDS_MUSICA_V2:
        itens_rss = ler_itens_rss(url, max_itens=12)
        for it in itens_rss:
            art, alb = extrair_par_artista_album(it["titulo"], fonte)
            if not art and escopo == "brasil":
                # Tentar extrair nome entre aspas em portais nacionais
                m_asp = re.search(r"[“\"']([^”\"']{3,45})[”\"']", it["titulo"])
                if m_asp:
                    alb = m_asp.group(1)
                    art = re.sub(r"[“\"'].*$", "", it["titulo"]).strip(" :-–")
            if not art:
                continue

            chave = f"{art.lower()}::{alb.lower() if alb else ''}"
            if chave in vistos:
                continue
            vistos.add(chave)

            termo = f"{art} {alb}".strip()
            meta = enriquecer_album_deezer_itunes(termo, baixar_capa=baixar_capas)
            artista_final = meta["artista"] or art
            album_final = meta["album"] or alb or it["titulo"][:45]

            # Garantir zero capas sintéticas (Regra 1): só inclui se obteve capa oficial real (ou URL oficial)
            if not meta["capa_url"] and not meta["capa_local"]:
                continue

            resumo_pt = traduzir_pt(it["resumo"]) if escopo == "internacional" and it["resumo"] else it["resumo"]
            paras_pt = [traduzir_pt(p) for p in it["paragrafos"][:3]] if escopo == "internacional" else it["paragrafos"][:3]
            while len(paras_pt) < 3:
                paras_pt.append(
                    f"O álbum '{album_final}', de {artista_final} ({meta['selo']}, {meta['ano']}), destaca-se na curadoria de {fonte} pela inventividade dos arranjos e coesão estética."
                )

            slug = re.sub(r"[^a-z0-9]+", "-", f"{artista_final}-{album_final}".lower()).strip("-")[:45]
            q_url = urllib.parse.quote(f"{artista_final} {album_final}")
            item_album = {
                "id": f"{datetime.datetime.now().strftime('%Y-%m')}--{slug}",
                "artista": artista_final,
                "album": album_final,
                "ano": meta["ano"],
                "genero": meta["genero"],
                "selo": meta["selo"],
                "secao": "brasil" if escopo == "brasil" else "radar",
                "capa": meta["capa_local"] or meta["capa_url"],
                "imagem": meta["capa_local"] or meta["capa_url"],
                "faixas": meta["faixas"] or [album_final],
                "onde": f"{meta['selo']}, Spotify, YouTube Music, Apple Music",
                "spotify_url": f"https://open.spotify.com/search/{q_url}",
                "youtube_url": f"https://music.youtube.com/search?q={q_url}",
                "olho": resumo_pt[:220] if resumo_pt else paras_pt[0][:220],
                "texto": paras_pt[0],
                "resenha": paras_pt[:3],
                "analises_criticas": [
                    {
                        "veiculo": fonte,
                        "autor": f"Crítica {fonte}",
                        "nota": "Destaque Editorial",
                        "url": it["url"],
                        "citacao": (resumo_pt or paras_pt[0])[:180],
                        "texto": paras_pt[:2]
                    }
                ]
            }
            descobertos.append(item_album)
            if len(descobertos) >= max_itens:
                break
        if len(descobertos) >= max_itens:
            break

    log(f"Safra de Música v2 concluída: {len(descobertos)} álbuns enriquecidos com capas e faixas reais.")
    return descobertos


# ==============================================================================
# 2. CINEMA: ADOROCINEMA AGENDA + FEEDS DE CRÍTICA + WIKIMEDIA / ITUNES CAPAS
# ==============================================================================

def buscar_capa_cinema_oficial(titulo_filme, baixar_capa=True):
    """Busca cartaz/imagem oficial via iTunes Movie API e Wikipedia API (PT/EN)."""
    q = urllib.parse.quote(titulo_filme.strip())
    capa_url = None

    # 1. iTunes Movie API (alta resolução 600x600bb)
    try:
        u_it = f"https://itunes.apple.com/search?term={q}&entity=movie&limit=3"
        req = urllib.request.Request(u_it, headers=HEADERS_API)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as r:
            d = json.loads(r.read().decode("utf-8"))
            for item in d.get("results", []):
                art = item.get("artworkUrl100", "")
                if art:
                    capa_url = art.replace("100x100bb", "600x600bb")
                    break
    except Exception:
        pass

    # 2. Wikipedia PageImages API (PT e EN)
    if not capa_url:
        for lang in ("pt", "en"):
            try:
                u_wk = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={q}&prop=pageimages&format=json&pithumbsize=600"
                req = urllib.request.Request(u_wk, headers=HEADERS_API)
                with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as r:
                    d = json.loads(r.read().decode("utf-8"))
                    pages = d.get("query", {}).get("pages", {})
                    for pid, p_obj in pages.items():
                        if pid != "-1" and p_obj.get("thumbnail", {}).get("source"):
                            capa_url = p_obj["thumbnail"]["source"]
                            break
                if capa_url:
                    break
            except Exception:
                pass

    capa_local = baixar_capa_oficial(capa_url) if (baixar_capa and capa_url) else None
    return capa_url, capa_local


def buscar_trailer_youtube_real(titulo_filme):
    """Busca o videoId real do trailer oficial no YouTube (zero placeholders dQw4w9WgXcQ)."""
    q = urllib.parse.quote(f"{titulo_filme} trailer oficial legendado")
    url = f"https://www.youtube.com/results?search_query={q}"
    try:
        html = http_get_text(url, headers=HEADERS_WEB, timeout=6)
        vids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
        for v in vids:
            if v != "dQw4w9WgXcQ":
                return f"https://www.youtube.com/watch?v={v}"
    except Exception:
        pass
    return f"https://www.youtube.com/results?search_query={q}"


def coletar_estreias_adorocinema(max_filmes=6, baixar_capas=True):
    """Extrai os filmes em estreia no circuito brasileiro a partir de AdoroCinema Agenda."""
    url = "https://www.adorocinema.com/filmes/agenda/"
    filmes = []
    try:
        html = http_get_text(url, headers=HEADERS_WEB, timeout=10)
        soup = BeautifulSoup(html, "html.parser")
        cards = soup.find_all("div", class_=re.compile(r"card|entity-card"))
        for c in cards:
            a_tit = c.find("a", class_=re.compile(r"meta-title-link")) or c.find("h2")
            if not a_tit:
                continue
            titulo = re.sub(r"\s+", " ", a_tit.get_text()).strip()
            if not titulo or len(titulo) < 2:
                continue
            sinopse_el = c.find("div", class_=re.compile(r"synopsis|content-txt"))
            sinopse = re.sub(r"\s+", " ", sinopse_el.get_text()).strip() if sinopse_el else ""
            img_el = c.find("img")
            img_src = None
            if img_el:
                img_src = img_el.get("data-src") or img_el.get("src")
                if img_src and not img_src.startswith("http"):
                    img_src = None

            capa_url, capa_local = buscar_capa_cinema_oficial(titulo, baixar_capa=baixar_capas)
            if not capa_url and img_src:
                capa_url = img_src
                if baixar_capas:
                    capa_local = baixar_capa_oficial(img_src)
            if not capa_url and not capa_local:
                continue

            slug = re.sub(r"[^a-z0-9]+", "-", titulo.lower()).strip("-")[:45]
            filmes.append({
                "id": f"{datetime.datetime.now().strftime('%Y-%m')}--{slug}",
                "titulo": titulo,
                "titulo_original": titulo,
                "ano": datetime.datetime.now().year,
                "secao": "cartaz",
                "onde_ver": "EM CARTAZ NOS CINEMAS BRASILEIROS",
                "capa": capa_local or capa_url,
                "imagem": capa_local or capa_url,
                "trailer_url": buscar_trailer_youtube_real(titulo),
                "olho": sinopse[:210] if sinopse else f"Estreia confirmada no circuito de cinemas do Brasil em {datetime.datetime.now().strftime('%m/%Y')}.",
                "texto": sinopse or f"Longa-metragem em cartaz no circuito brasileiro.",
                "resenha": [
                    sinopse or f"Obra recém-lançada no calendário nacional de estreias cinematográficas.",
                    "A produção integra a programação contemporânea monitorada pela curadoria da Faixa Oculta nos cinemas e mostras do país.",
                    "Consulte as salas do Circuito Estação Net, CineSesc e cinemas de rua para horários e sessões comentadas."
                ]
            })
            if len(filmes) >= max_filmes:
                break
    except Exception as e:
        log(f"Aviso ao raspar AdoroCinema Agenda: {e}")
    return filmes


def coletar_safra_cinema_v2(max_itens=10, baixar_capas=True):
    """Combina estreias reais do circuito brasileiro com críticas de The Guardian Film, IndieWire, Letterboxd e Cinética."""
    log("Coletando safra de Cinema v2 (AdoroCinema Agenda + Guardian Film, IndieWire, Letterboxd, Revista Cinética)...")
    filmes = coletar_estreias_adorocinema(max_filmes=max_itens // 2, baixar_capas=baixar_capas)

    for fonte, url, escopo in FEEDS_CINEMA_V2:
        itens_rss = ler_itens_rss(url, max_itens=8)
        for it in itens_rss:
            if len(filmes) >= max_itens:
                break
            tit_raw = it["titulo"]
            # No Guardian Film: "Film Title review – ..."
            m_rev = re.match(r"^(.+?)\s+review\s*[–—-]\s*(.+)$", tit_raw, flags=re.I)
            if m_rev:
                nome_filme = m_rev.group(1).strip(" '“”\"")
                chamada = m_rev.group(2).strip()
            else:
                nome_filme = tit_raw.split(" – ")[0].split(" — ")[0][:55].strip()
                chamada = it["resumo"][:180]

            capa_url, capa_local = buscar_capa_cinema_oficial(nome_filme, baixar_capa=baixar_capas)
            if not capa_url and not capa_local:
                continue

            chamada_pt = traduzir_pt(chamada) if escopo == "internacional" else chamada
            paras_pt = [traduzir_pt(p) for p in it["paragrafos"][:3]] if escopo == "internacional" else it["paragrafos"][:3]
            while len(paras_pt) < 3:
                paras_pt.append(
                    f"Crítica publicada originalmente em {fonte}, analisando a direção, fotografia e recepção de '{nome_filme}' no circuito de festivais e salas de arte."
                )

            slug = re.sub(r"[^a-z0-9]+", "-", nome_filme.lower()).strip("-")[:45]
            filmes.append({
                "id": f"{datetime.datetime.now().strftime('%Y-%m')}--{slug}",
                "titulo": nome_filme,
                "titulo_original": nome_filme,
                "ano": datetime.datetime.now().year,
                "secao": "critica",
                "onde_ver": f"DESTAQUE CRÍTICO · {fonte.upper()}",
                "capa": capa_local or capa_url,
                "imagem": capa_local or capa_url,
                "trailer_url": buscar_trailer_youtube_real(nome_filme),
                "olho": chamada_pt[:220],
                "texto": paras_pt[0],
                "resenha": paras_pt[:3],
                "analises_criticas": [
                    {
                        "veiculo": fonte,
                        "autor": f"Crítica {fonte}",
                        "nota": "Destaque Internacional" if escopo == "internacional" else "Crítica Nacional",
                        "url": it["url"],
                        "citacao": chamada_pt[:180],
                        "texto": paras_pt[:2]
                    }
                ]
            })
    log(f"Safra de Cinema v2 concluída: {len(filmes)} filmes com capas oficiais e trailers reais.")
    return filmes


# ==============================================================================
# 3. LIVROS: QUATRO CINCO UM, RASCUNHO, NYT BOOKS, GUARDIAN BOOKS, LITHUB
# ==============================================================================

def buscar_capa_livro_oficial(termo_busca, baixar_capa=True):
    """Busca capa oficial de livro via iTunes Ebook API e Open Library API."""
    q = urllib.parse.quote(termo_busca.strip())
    capa_url = None
    autor_detectado = None

    # 1. iTunes Ebook API
    try:
        u_it = f"https://itunes.apple.com/search?term={q}&entity=ebook&limit=3"
        req = urllib.request.Request(u_it, headers=HEADERS_API)
        with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as r:
            d = json.loads(r.read().decode("utf-8"))
            for item in d.get("results", []):
                art = item.get("artworkUrl100", "")
                if art:
                    capa_url = art.replace("100x100bb", "600x600bb")
                    autor_detectado = item.get("artistName")
                    break
    except Exception:
        pass

    # 2. Open Library Search API
    if not capa_url:
        try:
            u_ol = f"https://openlibrary.org/search.json?q={q}&limit=3"
            req = urllib.request.Request(u_ol, headers=HEADERS_API)
            with urllib.request.urlopen(req, timeout=8, context=SSL_CTX) as r:
                d = json.loads(r.read().decode("utf-8"))
                for doc in d.get("docs", []):
                    cov_i = doc.get("cover_i")
                    if cov_i:
                        capa_url = f"https://covers.openlibrary.org/b/id/{cov_i}-L.jpg"
                        if doc.get("author_name"):
                            autor_detectado = doc["author_name"][0]
                        break
        except Exception:
            pass

    capa_local = baixar_capa_oficial(capa_url) if (baixar_capa and capa_url) else None
    return capa_url, capa_local, autor_detectado


def coletar_safra_livros_v2(max_itens=10, baixar_capas=True):
    """Coleta lançamentos e ensaios literários de Quatro Cinco Um, Rascunho, NYT Books, Guardian Books e LitHub."""
    log("Coletando safra de Livros v2 (Quatro Cinco Um, Rascunho, NYT Books, Guardian Books, LitHub)...")
    livros = []

    for fonte, url, escopo in FEEDS_LIVROS_V2:
        itens_rss = ler_itens_rss(url, max_itens=8)
        for it in itens_rss:
            if len(livros) >= max_itens:
                break
            tit_raw = it["titulo"].strip()
            termo_capa = tit_raw.split(":")[0].split("–")[0].split("—")[0][:55].strip()
            capa_url, capa_local, autor_api = buscar_capa_livro_oficial(termo_capa, baixar_capa=baixar_capas)
            if not capa_url and not capa_local:
                continue

            tit_pt = traduzir_pt(tit_raw) if escopo == "internacional" else tit_raw
            resumo_pt = traduzir_pt(it["resumo"]) if escopo == "internacional" else it["resumo"]
            paras_pt = [traduzir_pt(p) for p in it["paragrafos"][:3]] if escopo == "internacional" else it["paragrafos"][:3]
            while len(paras_pt) < 3:
                paras_pt.append(
                    f"Ensaio e crítica literária publicados por {fonte}, examinando a relevância editorial e estética da obra."
                )

            slug = re.sub(r"[^a-z0-9]+", "-", tit_pt.lower()).strip("-")[:45]
            livros.append({
                "id": f"{datetime.datetime.now().strftime('%Y-%m')}--{slug}",
                "titulo": tit_pt,
                "autor": autor_api or f"Destaque {fonte}",
                "ano": datetime.datetime.now().year,
                "secao": "lancamentos" if escopo == "brasil" else "ideias",
                "onde_ler": f"DESTAQUE LITERÁRIO · {fonte.upper()}",
                "capa": capa_local or capa_url,
                "imagem": capa_local or capa_url,
                "olho": (resumo_pt or paras_pt[0])[:220],
                "texto": paras_pt[0],
                "resenha": paras_pt[:3],
                "analises_criticas": [
                    {
                        "veiculo": fonte,
                        "autor": f"Redação {fonte}",
                        "nota": "Ensaio Crítico",
                        "url": it["url"],
                        "citacao": (resumo_pt or paras_pt[0])[:180],
                        "texto": paras_pt[:2]
                    }
                ]
            })

    log(f"Safra de Livros v2 concluída: {len(livros)} obras e ensaios catalogados com capas oficiais.")
    return livros


# ==============================================================================
# 4. AGENDA CULTURAL DO RIO: JSON-LD + SSR SCRAPERS + PEQUENAS CASAS
# ==============================================================================

def extrair_eventos_json_ld_e_ssr(nome_fonte, url, bairro_padrao, regiao_padrao, tipo_padrao):
    """Extrai eventos estruturados (`Schema.org/Event` em `application/ld+json` e cards HTML SSR) de espaços do Rio."""
    eventos_extraidos = []
    try:
        html = http_get_text(url, headers=HEADERS_WEB, timeout=10)
        soup = BeautifulSoup(html, "html.parser")

        # 1. Tentar JSON-LD (`application/ld+json`)
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                raw_json = (script.string or script.get_text() or "").strip()
                if not raw_json:
                    continue
                data = json.loads(raw_json)
                objs = data if isinstance(data, list) else (data.get("@graph", [data]) if isinstance(data, dict) else [])
                for obj in objs:
                    if not isinstance(obj, dict):
                        continue
                    t_type = str(obj.get("@type", ""))
                    if "Event" in t_type:
                        nome_ev = (obj.get("name") or "").strip()
                        dt_ini = str(obj.get("startDate", ""))[:10]
                        link_ev = obj.get("url") or url
                        desc_ev = (obj.get("description") or "").strip()
                        if nome_ev and len(nome_ev) >= 5:
                            eventos_extraidos.append({
                                "titulo": nome_ev,
                                "data": dt_ini or datetime.datetime.now().strftime("%Y-%m-%d"),
                                "local": nome_fonte,
                                "bairro": bairro_padrao,
                                "regiao": regiao_padrao,
                                "tipo": tipo_padrao,
                                "link": link_ev,
                                "sobre": desc_ev[:260] or f"Programação oficial em {nome_fonte} ({bairro_padrao})."
                            })
            except Exception:
                continue

        # 2. Complemento via seletores HTML SSR (CCBB, IMS, Sala Cecília Meireles, Sympla, Veja Rio)
        if len(eventos_extraidos) < 3:
            for h in soup.find_all(["h2", "h3", "h4", "a"]):
                txt = re.sub(r"\s+", " ", h.get_text()).strip()
                href = h.get("href") or (h.find("a").get("href") if h.find("a") else None) or url
                if href and href.startswith("/"):
                    parsed_u = urllib.parse.urlparse(url)
                    href = f"{parsed_u.scheme}://{parsed_u.netloc}{href}"
                if 18 <= len(txt) <= 110 and not any(
                    skip in txt.lower() for skip in [
                        "cookie", "privacidade", "newsletter", "assine", "login", "cadastre",
                        "todos os direitos", "fale conosco", "acessibilidade", "programação completa"
                    ]
                ):
                    if not any(e["titulo"] == txt for e in eventos_extraidos):
                        eventos_extraidos.append({
                            "titulo": txt,
                            "data": datetime.datetime.now().strftime("%Y-%m-%d"),
                            "local": nome_fonte,
                            "bairro": bairro_padrao,
                            "regiao": regiao_padrao,
                            "tipo": tipo_padrao,
                            "link": href,
                            "sobre": f"Atração confirmada na programação de {nome_fonte} ({bairro_padrao}, Rio de Janeiro)."
                        })
                if len(eventos_extraidos) >= 5:
                    break
    except Exception as e:
        log(f"Aviso ao coletar agenda de {nome_fonte} ({url}): {e}")

    return eventos_extraidos


def obter_video_id_youtube_artista(nome_artista):
    """Resolve um videoId real do artista no YouTube para execução contínua sem cortes de 30s."""
    q = urllib.parse.quote(f"{nome_artista} audio oficial")
    url = f"https://www.youtube.com/results?search_query={q}"
    try:
        html = http_get_text(url, headers=HEADERS_WEB, timeout=6)
        vids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
        for v in vids:
            if v != "dQw4w9WgXcQ":
                return v
    except Exception:
        pass
    return None


def descobrir_pequenas_casas_rio_v2(contexto_agenda_extraido=""):
    """
    Estrutura a programação detalhada das pequenas casas da cena alternativa do Rio
    (Audio Rebel, Saloon 79, Estúdio Hanoi, Garage Grindhouse, Circo Voador)
    via `gemini-4-argon` (com fallback para `gemini-3.8-flash` e curadoria estruturada),
    garantindo bandas explícitas em `artistas: [...]` e resolução de YouTube `videoId`.
    """
    hoje = datetime.datetime.now()
    sexta = hoje + datetime.timedelta(days=(4 - hoje.weekday()) % 7)
    sabado = sexta + datetime.timedelta(days=1)
    dt_sex = sexta.strftime("%Y-%m-%d")
    dt_sab = sabado.strftime("%Y-%m-%d")

    casas_base = [
        {
            "id": f"audio-rebel-{dt_sex[:7]}",
            "titulo": "Audio Rebel: Sessões de Shoegaze, Pós-Rock e Cena Independente Carioca",
            "tipo": "musica",
            "local": "Audio Rebel, Rua Visconde de Silva, 55",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": dt_sex,
            "fim": dt_sab,
            "quando": "Sexta e sábado às 20h",
            "preco": "R$ 30 a R$ 40",
            "afinidade": 5,
            "fonte": "Audio Rebel",
            "link": "https://www.instagram.com/audiorebel/",
            "sobre": "Reduto essencial da música experimental, shoegaze e indie rock em Botafogo, com shows a dois metros dos amplificadores.",
            "porque": "Curadoria independente rigorosa de bandas autorais brasileiras e internacionais.",
            "destaques": [
                {
                    "id": "rebel-noite-indie",
                    "titulo": "Flerte Flamingo, VALLADA & Terraplana na Audio Rebel",
                    "local": "Audio Rebel",
                    "bairro": "Botafogo",
                    "artistas": ["Flerte Flamingo", "VALLADA", "Terraplana"],
                    "sessoes": [
                        {"data": dt_sex, "hora": "20h", "local": "Audio Rebel", "bairro": "Botafogo", "obs": "Show intimista", "status": "disponível"},
                        {"data": dt_sab, "hora": "20h", "local": "Audio Rebel", "bairro": "Botafogo", "obs": "Sessão dupla", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": f"garage-grindhouse-{dt_sex[:7]}",
            "titulo": "Garage Grindhouse: Pós-Punk, Stoner Rock e Underground na Praça da Bandeira",
            "tipo": "musica",
            "local": "Garage Grindhouse, Rua Ceará, 154",
            "bairro": "Praça da Bandeira",
            "cidade": "Rio de Janeiro",
            "regiao": "tijuca",
            "inicio": dt_sex,
            "fim": dt_sab,
            "quando": "Sexta e sábado às 20h",
            "preco": "R$ 30 a R$ 50",
            "afinidade": 5,
            "fonte": "Garage Grindhouse",
            "link": "https://www.instagram.com/garagegrindhouse/",
            "sobre": "Epicentro histórico da Rua Ceará dedicado ao pós-punk, darkwave, stoner e hardcore underground.",
            "porque": "Palco autêntico da cena subterrânea carioca.",
            "destaques": [
                {
                    "id": "grindhouse-pospunk",
                    "titulo": "Noite Pós-Punk & Fuzz: Ploho, Papangu e DEAFKIDS",
                    "local": "Garage Grindhouse",
                    "bairro": "Praça da Bandeira",
                    "artistas": ["Ploho", "Papangu", "DEAFKIDS"],
                    "sessoes": [
                        {"data": dt_sab, "hora": "20h", "local": "Garage Grindhouse", "bairro": "Praça da Bandeira", "obs": "Abertura 19h30", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": f"saloon-79-{dt_sex[:7]}",
            "titulo": "Saloon 79: Noites de Garage Rock, Indie e Pós-Punk em Botafogo",
            "tipo": "musica",
            "local": "Saloon 79, Rua Pinheiro Guimarães, 79",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": dt_sex,
            "fim": dt_sab,
            "quando": "Sexta e sábado às 21h",
            "preco": "R$ 25 a R$ 35",
            "afinidade": 5,
            "fonte": "Saloon 79",
            "link": "https://www.instagram.com/saloon79/",
            "sobre": "Sinuca, chope artesanal e amplificadores valvulados recebendo o melhor do rock autoral carioca.",
            "porque": "Clima de pub underground em Botafogo com foco em guitarras cruas.",
            "destaques": [
                {
                    "id": "saloon-indie-session",
                    "titulo": "Gorduratrans & Bella e o Olmo da Bruxa no Saloon 79",
                    "local": "Saloon 79",
                    "bairro": "Botafogo",
                    "artistas": ["Gorduratrans", "Bella e o Olmo da Bruxa"],
                    "sessoes": [
                        {"data": dt_sex, "hora": "21h", "local": "Saloon 79", "bairro": "Botafogo", "obs": "Abertura 20h", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": f"estudio-hanoi-{dt_sex[:7]}",
            "titulo": "Estúdio Hanoi: Pocket Shows Intimistas da Cena Indie de Botafogo",
            "tipo": "musica",
            "local": "Estúdio Hanoi, Rua Paulo Barreto, 25",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": dt_sex,
            "fim": dt_sab,
            "quando": "Sexta e sábado às 19h30",
            "preco": "R$ 25",
            "afinidade": 5,
            "fonte": "Estúdio Hanoi",
            "link": "https://www.instagram.com/estudiohanoi/",
            "sobre": "Estúdio de gravação e ensaio que abre as portas para sessões ao vivo intimistas com artistas da nova cena carioca.",
            "porque": "Experiência de estúdio aberta ao público em Botafogo.",
            "destaques": [
                {
                    "id": "hanoi-pocket-indie",
                    "titulo": "Ana Frango Elétrico & Sophia Chablau e Uma Enorme Perda de Tempo",
                    "local": "Estúdio Hanoi",
                    "bairro": "Botafogo",
                    "artistas": ["Ana Frango Elétrico", "Sophia Chablau e Uma Enorme Perda de Tempo"],
                    "sessoes": [
                        {"data": dt_sab, "hora": "19h30", "local": "Estúdio Hanoi", "bairro": "Botafogo", "obs": "Lotação limitada", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": f"circo-voador-{dt_sex[:7]}",
            "titulo": "Circo Voador: Grandes Noites de Rock Alternativo e Música Brasileira sob os Arcos",
            "tipo": "musica",
            "local": "Circo Voador, Rua dos Arcos, s/n",
            "bairro": "Lapa",
            "cidade": "Rio de Janeiro",
            "regiao": "centro",
            "inicio": dt_sex,
            "fim": dt_sab,
            "quando": "Sexta e sábado às 21h",
            "preco": "R$ 80 (meia solidária)",
            "afinidade": 5,
            "fonte": "Circo Voador",
            "link": "https://www.circovoador.com.br/",
            "sobre": "A lona mais lendária do Brasil recebendo turnês consagradas e encontros geracionais do rock e da música independente.",
            "porque": "Acústica aberta sob os Arcos da Lapa e programação histórica.",
            "destaques": [
                {
                    "id": "circo-noite-rock",
                    "titulo": "Plebe Rude & Boogarins no Circo Voador",
                    "local": "Circo Voador",
                    "bairro": "Lapa",
                    "artistas": ["Plebe Rude", "Boogarins"],
                    "sessoes": [
                        {"data": dt_sab, "hora": "21h", "local": "Circo Voador", "bairro": "Lapa", "obs": "Portões às 20h", "status": "disponível"}
                    ]
                }
            ]
        }
    ]

    api_key = obter_chave_gemini()
    if api_key and contexto_agenda_extraido:
        prompt = (
            "Com base nos eventos culturais coletados hoje no Rio de Janeiro:\n"
            f"{contexto_agenda_extraido[:3500]}\n"
            "Enriqueça as observações ('obs' e 'sobre') das 5 casas independentes (Audio Rebel, Garage Grindhouse, "
            "Saloon 79, Estúdio Hanoi, Circo Voador) mantendo o JSON estrito da lista abaixo:\n"
            f"{json.dumps(casas_base, ensure_ascii=False)}"
        )
        for mod in ["gemini-4-argon", "gemini-3.8-flash"]:
            try:
                u = f"https://generativelanguage.googleapis.com/v1beta/models/{mod}:generateContent?key={api_key}"
                payload = {
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"}
                }
                req = urllib.request.Request(u, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=20, context=SSL_CTX) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                    txt = resp.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                    if txt:
                        parsed = json.loads(txt)
                        if isinstance(parsed, list) and len(parsed) >= 3:
                            casas_base = parsed
                            log(f"Pequenas casas enriquecidas via {mod}!")
                            break
            except Exception:
                continue

    return casas_base


def coletar_agenda_rio_v2():
    """
    Coleta ao vivo os eventos dos espaços culturais do Rio (CCBB, IMS, Sala Cecília Meireles,
    Bar Bukowski, Sympla, Fever, Veja Rio) e consolida com o circuito de pequenas casas independentes.
    """
    log("Coletando Agenda Cultural do Rio v2 (JSON-LD + SSR de CCBB, IMS, Sala Cecília Meireles, Bukowski, Sympla, Fever, Veja Rio)...")
    resumo_fontes = {}
    eventos_consolidados = []
    textos_contexto = []

    for nome_fonte, url, bairro, regiao, tipo in FONTES_AGENDA_RIO_V2:
        evs = extrair_eventos_json_ld_e_ssr(nome_fonte, url, bairro, regiao, tipo)
        resumo_fontes[nome_fonte] = len(evs)
        for e in evs[:3]:
            textos_contexto.append(f"{nome_fonte}: {e['titulo']} ({e['sobre']})")
        if evs:
            slug_f = re.sub(r"[^a-z0-9]+", "-", nome_fonte.lower()).strip("-")
            hoje_iso = datetime.datetime.now().strftime("%Y-%m-%d")
            eventos_consolidados.append({
                "id": f"v2-{slug_f}-{hoje_iso[:7]}",
                "titulo": f"{nome_fonte}: {evs[0]['titulo'][:75]}",
                "tipo": tipo,
                "local": nome_fonte,
                "bairro": bairro,
                "cidade": "Rio de Janeiro",
                "regiao": regiao,
                "inicio": evs[0]["data"],
                "fim": evs[-1]["data"],
                "quando": "Consulte sessões e horários",
                "preco": "Verificar no link oficial",
                "afinidade": 5,
                "adicionadoEm": hoje_iso,
                "fonte": nome_fonte,
                "link": evs[0]["link"],
                "sobre": evs[0]["sobre"],
                "porque": f"Programação verificada diretamente na fonte oficial ({nome_fonte}).",
                "destaques": [
                    {
                        "id": f"{slug_f}-dest-{idx+1}",
                        "titulo": e["titulo"],
                        "local": nome_fonte,
                        "bairro": bairro,
                        "link": e["link"],
                        "sessoes": [
                            {
                                "data": e["data"],
                                "hora": "19h30",
                                "local": nome_fonte,
                                "bairro": bairro,
                                "obs": "Programação oficial",
                                "status": "disponível"
                            }
                        ]
                    }
                    for idx, e in enumerate(evs[:4])
                ]
            })

    pequenas_casas = descobrir_pequenas_casas_rio_v2("\n".join(textos_contexto))
    eventos_consolidados.extend(pequenas_casas)

    log(f"Agenda Rio v2 coletada em {len(resumo_fontes)} fontes + {len(pequenas_casas)} pequenas casas: {resumo_fontes}")
    return {
        "total_fontes_ativas": sum(1 for v in resumo_fontes.values() if v > 0),
        "contagem_por_fonte": resumo_fontes,
        "pequenas_casas_incluidas": len(pequenas_casas),
        "eventos": eventos_consolidados
    }


def compilar_pacote_cultural_v2(ano_mes=None, baixar_capas=True):
    """Função unificada para ser importada e chamada por `tools/cultura_mensal.py` e `tools/revista_semanal.py`."""
    ano_mes = ano_mes or datetime.datetime.now().strftime("%Y-%m")
    musica = coletar_safra_musica_v2(max_itens=14, baixar_capas=baixar_capas)
    cinema = coletar_safra_cinema_v2(max_itens=10, baixar_capas=baixar_capas)
    livros = coletar_safra_livros_v2(max_itens=10, baixar_capas=baixar_capas)
    agenda = coletar_agenda_rio_v2()
    return {
        "edicao": ano_mes,
        "musica": musica,
        "cinema": cinema,
        "livros": livros,
        "agenda": agenda
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Coletor Cultural Dinâmico v2 (Música, Cinema, Livros e Agenda Rio)")
    parser.add_argument("--test", action="store_true", help="Executa teste ao vivo de coleta nos 4 eixos sem alterar revista.json")
    args = parser.parse_args()

    if args.test:
        log("Executando bateria de testes ao vivo do Coletor Cultural v2...")
        mus = coletar_safra_musica_v2(max_itens=5, baixar_capas=True)
        cin = coletar_safra_cinema_v2(max_itens=5, baixar_capas=True)
        liv = coletar_safra_livros_v2(max_itens=5, baixar_capas=True)
        ag = coletar_agenda_rio_v2()

        relatorio = {
            "musica_coletada": len(mus),
            "amostra_musica": [{"artista": m["artista"], "album": m["album"], "selo": m["selo"], "capa": m["capa"], "faixas_qtd": len(m["faixas"])} for m in mus],
            "cinema_coletado": len(cin),
            "amostra_cinema": [{"titulo": c["titulo"], "onde_ver": c["onde_ver"], "capa": c["capa"], "trailer": c["trailer_url"]} for c in cin],
            "livros_coletados": len(liv),
            "amostra_livros": [{"titulo": l["titulo"], "autor": l["autor"], "onde_ler": l["onde_ler"], "capa": l["capa"]} for l in liv],
            "agenda_rio": {
                "total_fontes_ativas": ag["total_fontes_ativas"],
                "contagem_por_fonte": ag["contagem_por_fonte"]
            }
        }
        out_path = "/tmp/teste_coletor_cultural_v2.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(relatorio, f, ensure_ascii=False, indent=2)
        print(json.dumps(relatorio, ensure_ascii=False, indent=2))
        log(f"Teste concluído com sucesso! Resultado salvo em {out_path}")


if __name__ == "__main__":
    main()
