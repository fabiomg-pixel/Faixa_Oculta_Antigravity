"""Posters (films/series via Wikipedia, then iTunes) and book covers (iTunes ebook) for magazine JSON batches.
Usage: python3 -I capas_obras.py <out_dir> <batch.json> [<batch.json> ...]
Each batch: {"itens": [...], "guias": [{"filmes"|"livros": [...]}]}. Writes <slug>.jpg and prints OK/MISS per work.
"""
import json, os, re, subprocess, sys, time, unicodedata, urllib.parse

UA = "FaixaOculta/1.0 (personal magazine)"
out = sys.argv[1]
os.makedirs(out, exist_ok=True)


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def slug(s):
    return norm(s).replace(" ", "-")[:70]


def get_json(url):
    for _ in range(3):
        r = subprocess.run(["curl", "-s", "--max-time", "20", "-A", UA, url], capture_output=True)
        try:
            return json.loads(r.stdout)
        except Exception:
            time.sleep(2)
    return {}


def baixar(url, fn):
    subprocess.run(["curl", "-s", "-L", "--max-time", "25", "-A", UA, "-o", os.path.join(out, fn), url])
    p = os.path.join(out, fn)
    ok = os.path.exists(p) and os.path.getsize(p) > 3000
    if not ok and os.path.exists(p):
        os.remove(p)
    return ok


def wiki_poster(a):
    titles = []
    for t in [a.get("titulo_original"), a.get("titulo")]:
        if t:
            for v in (t, re.split(r"\s[–—-]\s|:\s", t)[0]):
                if v not in titles:
                    titles.append(v)
    kind = {"serie": "miniseries", "documentario": "documentary film"}.get(a.get("tipo"), "film")
    for lang in ("en", "pt"):
        api = f"https://{lang}.wikipedia.org/w/api.php?"
        for t in titles:
            q = f'{t} {a.get("ano", "")} {kind if lang == "en" else ""} {a.get("autor", "")}'
            res = get_json(api + urllib.parse.urlencode({"action": "query", "list": "search", "srsearch": q, "srlimit": 3, "format": "json"}))
            for hit in res.get("query", {}).get("search", []):
                if norm(t).split(" ")[0] not in norm(hit["title"]):
                    continue
                wt = get_json(api + urllib.parse.urlencode({"action": "parse", "page": hit["title"], "prop": "wikitext", "section": 0, "format": "json"}))
                txt = wt.get("parse", {}).get("wikitext", {}).get("*", "")
                m = re.search(r"\|\s*(?:image|imagem)\s*=\s*\[?\[?(?:File:|Ficheiro:|Arquivo:)?([^\n|\]]+\.(?:jpe?g|png|webp))", txt, re.I)
                if not m:
                    continue
                f = m.group(1).strip()
                ii = get_json(api + urllib.parse.urlencode({"action": "query", "titles": "File:" + f, "prop": "imageinfo", "iiprop": "url", "iiurlwidth": 500, "format": "json"}))
                for p in ii.get("query", {}).get("pages", {}).values():
                    if "imageinfo" in p:
                        return p["imageinfo"][0].get("thumburl") or p["imageinfo"][0]["url"], f"{lang}:{hit['title']}"
            time.sleep(0.5)
    return None, None


def itunes(a, entities):
    titles = [t for t in [a.get("titulo"), a.get("titulo_original")] if t]
    last = norm(a.get("autor", "")).split(" ")[-1] if a.get("autor") else ""
    for entity in entities:
        for country in ("br", "us"):
            for t in titles:
                term = f"{t} {a.get('autor', '')}" if entity in ("ebook", "audiobook") else t
                res = get_json("https://itunes.apple.com/search?" + urllib.parse.urlencode({"term": term, "entity": entity, "limit": 15, "country": country}))
                for r in res.get("results", []):
                    name = norm(r.get("trackName") or r.get("collectionName") or "")
                    if not (norm(t) and (norm(t) in name or name in norm(t))):
                        continue
                    if entity in ("ebook", "audiobook") and last and last not in norm(r.get("artistName", "")):
                        continue
                    if entity == "movie" and a.get("ano") and str(a["ano"])[:4] not in str(r.get("releaseDate", ""))[:4]:
                        continue
                    art = r.get("artworkUrl100", "")
                    if art:
                        return art.replace("100x100bb", "600x600bb"), f"itunes:{r.get('trackName') or r.get('collectionName')}"
    return None, None


obras = []
for b in sys.argv[2:]:
    j = json.load(open(b))
    obras += j.get("itens", [])
    for g in j.get("guias", []):
        obras += g.get("filmes", []) + g.get("livros", [])

vistos = set()
for a in obras:
    fn = slug(f"{a.get('titulo')} {a.get('ano', '')}") + ".jpg"
    if fn in vistos:
        continue
    vistos.add(fn)
    if os.path.exists(os.path.join(out, fn)):
        print("HAVE", fn)
        continue
    livro = a.get("tipo") in ("ficcao", "contos", "nao_ficcao")
    url, fonte = (itunes(a, ["ebook", "audiobook"]) if livro else wiki_poster(a))
    if not url and not livro:
        url, fonte = itunes(a, ["movie", "tvSeason"])
    if url and baixar(url, fn):
        print("OK  ", fn, "<=", fonte)
    else:
        print("MISS", fn, "|", a.get("titulo"), "|", a.get("autor"))
