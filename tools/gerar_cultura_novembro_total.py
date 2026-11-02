#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a edição cultural total de Novembro de 2026 para Faixa Oculta / Radar Cultural.
Restaura a densidade, escala e padrão editorial de Outubro:
- Música: 35 álbuns nas seções + 4 guias temáticos (21 álbuns nos guias)
- Cinema: 32 filmes/séries nas seções + 3 guias (15 filmes nos guias) com IDs do IMDb
- Livros: 22 obras nas seções + 2 guias (10 obras nos guias)
- Download automático de todas as capas em capas/<hash>.jpg com fallback PIL de alta fidelidade
- Cada obra possui 4 parágrafos de resenha crítica cultural aprofundada
- Playlist sequencial completa do mês montada para reprodução contínua
"""

import os
import sys
import json
import hashlib
import subprocess
import urllib.parse
import re
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.abspath("."))
import tools.dados_musica_nov as dm
import tools.dados_cinema_nov as dc
import tools.dados_livros_nov as dl
import tools.dados_semana_nov as ds

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
os.makedirs("capas", exist_ok=True)

def fallback_capa_elegante(texto_principal, subtitulo, categoria, hash_str):
    fn = f"capas/{hash_str}.jpg"
    if os.path.exists(fn) and os.path.getsize(fn) > 1500:
        return fn
    w, h = 600, 600
    paletas = {
        "musica": ((26, 24, 22), (235, 225, 210), (195, 70, 40)),
        "cinema": ((15, 23, 42), (241, 245, 249), (56, 189, 248)),
        "livros": ((30, 22, 16), (250, 246, 238), (217, 119, 6))
    }
    bg, fg, ac = paletas.get(categoria, ((20, 20, 20), (240, 240, 240), (200, 100, 50)))
    img = Image.new("RGB", (w, h), color=bg)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(20, 20), (w-20, h-20)], outline=ac, width=2)
    draw.line([(40, 110), (w-40, 110)], fill=ac, width=1)
    draw.text((40, 45), f"FAIXA OCULTA · {categoria.upper()}", fill=ac)
    draw.text((40, 150), str(texto_principal)[:32], fill=fg)
    draw.text((40, 205), str(subtitulo)[:36], fill=ac)
    draw.line([(40, h-90), (w-40, h-90)], fill=ac, width=1)
    draw.text((40, h-70), "NOVEMBRO 2026 · EDIÇÃO Nº 2", fill=fg)
    img.save(fn, "JPEG", quality=85)
    return fn

def wiki_poster(termo):
    h = hashlib.md5(termo.encode()).hexdigest()
    fn = f"capas/{h}.jpg"
    if os.path.exists(fn) and os.path.getsize(fn) > 2500:
        return fn
    q = urllib.parse.quote(termo)
    for lang in ["pt", "en"]:
        api = f"https://{lang}.wikipedia.org/w/api.php?action=query&list=search&srsearch={q}&srlimit=2&format=json"
        r = subprocess.run(["curl", "-s", "--max-time", "8", "-A", UA, api], capture_output=True)
        try:
            res = json.loads(r.stdout)
            for hit in res.get("query", {}).get("search", []):
                t = urllib.parse.quote(hit["title"])
                wt_url = f"https://{lang}.wikipedia.org/w/api.php?action=parse&page={t}&prop=wikitext&section=0&format=json"
                r2 = subprocess.run(["curl", "-s", "--max-time", "8", "-A", UA, wt_url], capture_output=True)
                wt = json.loads(r2.stdout)
                txt = wt.get("parse", {}).get("wikitext", {}).get("*", "")
                m = re.search(r"\|\s*(?:image|imagem|cover)\s*=\s*\[?\[?(?:File:|Ficheiro:|Arquivo:)?([^\n|\]]+\.(?:jpe?g|png|webp))", txt, re.I)
                if m:
                    f = urllib.parse.quote("File:" + m.group(1).strip())
                    ii_url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={f}&prop=imageinfo&iiprop=url&iiurlwidth=500&format=json"
                    r3 = subprocess.run(["curl", "-s", "--max-time", "8", "-A", UA, ii_url], capture_output=True)
                    ii = json.loads(r3.stdout)
                    for p in ii.get("query", {}).get("pages", {}).values():
                        if "imageinfo" in p:
                            img_url = p["imageinfo"][0].get("thumburl") or p["imageinfo"][0]["url"]
                            subprocess.run(["curl", "-s", "-L", "--max-time", "12", "-A", UA, "-o", fn, img_url])
                            if os.path.exists(fn) and os.path.getsize(fn) > 2500:
                                return fn
        except Exception:
            pass
    return None

def baixar_capa_disco(artista, album):
    termo = f"{artista} {album}"
    h = hashlib.md5(termo.encode()).hexdigest()
    fn = f"capas/{h}.jpg"
    if os.path.exists(fn) and os.path.getsize(fn) > 2500:
        return fn
    q = urllib.parse.quote(termo)
    url = f"https://itunes.apple.com/search?term={q}&entity=album&limit=3&country=br"
    r = subprocess.run(["curl", "-s", "--max-time", "10", "-A", UA, url], capture_output=True)
    try:
        data = json.loads(r.stdout)
        for it in data.get("results", []):
            art = it.get("artworkUrl100")
            if art:
                img_url = art.replace("100x100bb", "600x600bb")
                subprocess.run(["curl", "-s", "-L", "--max-time", "12", "-A", UA, "-o", fn, img_url])
                if os.path.exists(fn) and os.path.getsize(fn) > 2500:
                    return fn
    except Exception:
        pass
    # Fallback elegante
    return fallback_capa_elegante(album, artista, "musica", h)

def baixar_capa_filme(titulo, autor=None):
    termo = f"{titulo} {autor or ''}".strip()
    h = hashlib.md5(termo.encode()).hexdigest()
    fn = f"capas/{h}.jpg"
    if os.path.exists(fn) and os.path.getsize(fn) > 2500:
        return fn
    q = urllib.parse.quote(termo)
    for ent in ["movie", "tvSeason"]:
        url = f"https://itunes.apple.com/search?term={q}&entity={ent}&limit=3&country=br"
        r = subprocess.run(["curl", "-s", "--max-time", "8", "-A", UA, url], capture_output=True)
        try:
            data = json.loads(r.stdout)
            for it in data.get("results", []):
                art = it.get("artworkUrl100")
                if art:
                    img_url = art.replace("100x100bb", "600x600bb")
                    subprocess.run(["curl", "-s", "-L", "--max-time", "12", "-A", UA, "-o", fn, img_url])
                    if os.path.exists(fn) and os.path.getsize(fn) > 2500:
                        return fn
        except Exception:
            pass
    # Tenta Wikipedia
    p = wiki_poster(f"{titulo} filme")
    if p: return p
    p = wiki_poster(f"{titulo} film")
    if p: return p
    # Fallback elegante
    return fallback_capa_elegante(titulo, autor or "Cinema", "cinema", h)

def baixar_capa_livro(titulo, autor=None):
    termo = f"{titulo} {autor or ''}".strip()
    h = hashlib.md5(termo.encode()).hexdigest()
    fn = f"capas/{h}.jpg"
    if os.path.exists(fn) and os.path.getsize(fn) > 2500:
        return fn
    q = urllib.parse.quote(termo)
    for ent in ["ebook", "audiobook"]:
        url = f"https://itunes.apple.com/search?term={q}&entity={ent}&limit=3&country=br"
        r = subprocess.run(["curl", "-s", "--max-time", "8", "-A", UA, url], capture_output=True)
        try:
            data = json.loads(r.stdout)
            for it in data.get("results", []):
                art = it.get("artworkUrl100")
                if art:
                    img_url = art.replace("100x100bb", "600x600bb")
                    subprocess.run(["curl", "-s", "-L", "--max-time", "12", "-A", UA, "-o", fn, img_url])
                    if os.path.exists(fn) and os.path.getsize(fn) > 2500:
                        return fn
        except Exception:
            pass
    p = wiki_poster(f"{titulo} livro")
    if p: return p
    p = wiki_poster(f"{titulo} novel")
    if p: return p
    # Fallback elegante
    return fallback_capa_elegante(titulo, autor or "Literatura", "livros", h)

def main():
    print("=== INICIANDO GERAÇÃO CULTURAL TOTAL DE NOVEMBRO 2026 ===")
    with open("data/revista.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    # 1. PROCESSAR MÚSICA
    print("\n--- Processando Música de Novembro 2026 ---")
    musica_ed = dm.MUSICA_EDICAO
    musica_itens = dm.MUSICA_ITENS
    musica_guias = dm.MUSICA_GUIAS

    # Baixar capas para itens musicais
    for k, item in musica_itens.items():
        capa_path = baixar_capa_disco(item["artista"], item["album"])
        item["capa"] = capa_path

    # Baixar capas para álbuns de guias
    for gid, guia in musica_guias.items():
        for alb in guia.get("albuns", []):
            alb["capa"] = baixar_capa_disco(alb["artista"], alb["album"])

    # Capa da edição musical (Manning Fireworks de MJ Lenderman)
    dest_musica = musica_itens.get("2026-11--mj-lenderman-manning-fireworks")
    if dest_musica:
        musica_ed["capa"] = dest_musica["capa"]

    # Montar Playlist do Mês completa
    playlist_faixas = []
    for k, item in musica_itens.items():
        playlist_faixas.append({
            "artista": item["artista"],
            "album": item["album"],
            "faixa": item.get("faixas", ["Faixa Principal"])[0],
            "spotify_id": item.get("spotify_id", ""),
            "spotify_url": item.get("spotify_url", "")
        })
    musica_ed["playlist"] = {
        "url": "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M",
        "faixas": playlist_faixas
    }

    db.setdefault("edicoes", {})["2026-11"] = musica_ed
    db.setdefault("itens", {}).update(musica_itens)
    db.setdefault("guias", {}).update(musica_guias)
    print(f"Música carregada: {len(musica_itens)} álbuns editoriais, {len(musica_guias)} guias com {sum(len(g['albuns']) for g in musica_guias.values())} álbuns.")

    # 2. PROCESSAR CINEMA
    print("\n--- Processando Cinema de Novembro 2026 ---")
    cine_ed = dc.CINE_EDICAO
    cine_itens = dc.CINE_ITENS
    cine_guias = dc.CINE_GUIAS

    for k, item in cine_itens.items():
        capa_path = baixar_capa_filme(item["titulo"], item.get("autor"))
        item["capa"] = capa_path

    for gid, guia in cine_guias.items():
        for f_it in guia.get("filmes", []):
            f_it["capa"] = baixar_capa_filme(f_it["titulo"], f_it.get("autor"))

    dest_cine = cine_itens.get("2026-11--o-agente-secreto")
    if dest_cine:
        cine_ed["capa"] = dest_cine["capa"]

    db.setdefault("cine_edicoes", {})["2026-11"] = cine_ed
    db.setdefault("cine_itens", {}).update(cine_itens)
    db.setdefault("cine_guias", {}).update(cine_guias)
    print(f"Cinema carregado: {len(cine_itens)} filmes/séries, {len(cine_guias)} guias com {sum(len(g['filmes']) for g in cine_guias.values())} filmes.")

    # 3. PROCESSAR LIVROS
    print("\n--- Processando Livros de Novembro 2026 ---")
    livro_ed = dl.LIVRO_EDICAO
    livro_itens = dl.LIVRO_ITENS
    livro_guias = dl.LIVRO_GUIAS

    for k, item in livro_itens.items():
        capa_path = baixar_capa_livro(item["titulo"], item.get("autor"))
        item["capa"] = capa_path

    for gid, guia in livro_guias.items():
        for b_it in guia.get("livros", []):
            b_it["capa"] = baixar_capa_livro(b_it["titulo"], b_it.get("autor"))

    dest_livro = livro_itens.get("2026-11--a-trama-da-vida")
    if dest_livro:
        livro_ed["capa"] = dest_livro["capa"]

    db.setdefault("livro_edicoes", {})["2026-11"] = livro_ed
    db.setdefault("livro_itens", {}).update(livro_itens)
    db.setdefault("livro_guias", {}).update(livro_guias)
    print(f"Livros carregados: {len(livro_itens)} títulos, {len(livro_guias)} guias com {sum(len(g['livros']) for g in livro_guias.values())} títulos.")

    # 4. PROCESSAR REVISTA SEMANAL
    print("\n--- Processando Revista Semanal (01 a 07 de Novembro 2026) ---")
    semana_nov = ds.get_semana_nov()
    db.setdefault("semanas", {})["2026-11-07"] = semana_nov

    # Atualizar leituras no leitor
    import tools.revista_semanal as rs
    rs.atualizar_leituras_semanais(db, semana_nov)
    print(f"Revista semanal carregada com {len(semana_nov['temas'])} temas e {len(semana_nov['fora_do_radar'])} fora do radar.")

    # 5. SALVAR NO DB
    print("\nGravando data/revista.json...")
    with open("data/revista.json", "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    # 6. RECOMPILAR INDEX.HTML
    print("Recompilando index.html...")
    with open("pagina.html", "r", encoding="utf-8") as f:
        src = f.read()

    skeleton_head = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Faixa Oculta / Radar Cultural</title>
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
    skeleton_tail = "\n</body>\n</html>\n"

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(skeleton_head + src + skeleton_tail)

    print("\n=== CONCLUÍDO COM SUCESSO! ===")

if __name__ == "__main__":
    main()
