import json, os, subprocess, urllib.parse, re, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def clean_text(s):
    if not s: return ""
    s = re.sub(r"\([^)]*\)", "", str(s)) # remove parens like (Edição Expandida), (2024), etc.
    s = s.split(" — ")[0].split(" - ")[0].split(":")[0] # take before colon or dash
    return s.strip()

def download_img(url, dest_path):
    if not url: return False
    # download with curl
    tmp = dest_path + ".tmp"
    cmd = ["curl", "-s", "-L", "--max-time", "15", "-A", UA, "-o", tmp, url]
    r = subprocess.run(cmd)
    if r.returncode == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 3000:
        # Check if valid image
        try:
            from PIL import Image
            im = Image.open(tmp)
            im.verify()
            os.replace(tmp, dest_path)
            return True
        except Exception as e:
            if os.path.exists(tmp): os.remove(tmp)
            return False
    if os.path.exists(tmp): os.remove(tmp)
    return False

def get_deezer(term):
    for q in [term, clean_text(term)]:
        if not q: continue
        url = f"https://api.deezer.com/search/album?q={urllib.parse.quote(q)}"
        res = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
        try:
            d = json.loads(res.stdout).get("data", [])
            if d:
                c = d[0].get("cover_xl") or d[0].get("cover_big") or d[0].get("cover_medium")
                if c: return c
        except Exception:
            pass
    return None

def get_itunes(term, media="all", entity=None):
    params_entity = f"&entity={entity}" if entity else ""
    for c in ["br", "us", "gb"]:
        url = f"https://itunes.apple.com/search?term={urllib.parse.quote(term)}&media={media}{params_entity}&limit=3&country={c}"
        res = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
        try:
            results = json.loads(res.stdout).get("results", [])
            if results:
                art = results[0].get("artworkUrl100")
                if art:
                    return art.replace("100x100bb", "600x600bb")
        except Exception:
            pass
    return None

def get_openlibrary(title, author=""):
    queries = [f"{clean_text(title)} {author}".strip(), clean_text(title), f"{title} {author}".strip()]
    for q in queries:
        url = f"https://openlibrary.org/search.json?q={urllib.parse.quote(q)}&limit=3"
        res = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
        try:
            docs = json.loads(res.stdout).get("docs", [])
            for d in docs:
                cov = d.get("cover_i")
                if cov:
                    return f"https://covers.openlibrary.org/b/id/{cov}-L.jpg"
        except Exception:
            pass
    return None

def get_wikipedia(term, cat_hint=""):
    queries = []
    c_term = clean_text(term)
    if "cine" in cat_hint:
        queries.extend([f"{term} (filme)", f"{c_term} (filme)", f"{c_term} (série)", f"{term} (film)", f"{c_term} (film)", term, c_term])
    elif "livro" in cat_hint:
        queries.extend([f"{term} (livro)", f"{c_term} (livro)", f"{term} (novel)", f"{c_term} (novel)", term, c_term])
    elif "musica" in cat_hint:
        queries.extend([f"{term} (álbum)", f"{c_term} (álbum)", f"{term} (album)", f"{c_term} (album)", term, c_term])
    else:
        queries.extend([term, c_term])

    for q in queries:
        for lang in ["pt", "en"]:
            # Try opensearch first
            os_url = f"https://{lang}.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(q)}&limit=3&format=json"
            res = subprocess.run(["curl", "-s", "-A", UA, os_url], capture_output=True, text=True)
            try:
                hits = json.loads(res.stdout)[1]
                for hit in hits:
                    sum_url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(hit)}"
                    res2 = subprocess.run(["curl", "-s", "-A", UA, sum_url], capture_output=True, text=True)
                    d = json.loads(res2.stdout)
                    img = d.get("originalimage", {}).get("source") or d.get("thumbnail", {}).get("source")
                    if img and not any(bad in img.lower() for bad in ["disambig", "question_mark", "folder", "icon"]):
                        return img
            except Exception:
                pass
    return None

def main():
    with open("tools/targets_fallback.json") as f:
        targets = json.load(f)

    print(f"Total targets to resolve: {len(targets)}")
    sucessos = 0
    falhas = []

    for idx, t in enumerate(targets, 1):
        dest = t["file"]
        title = t.get("title", "")
        author = t.get("author", "")
        cat = t.get("cat", "")
        print(f"[{idx}/{len(targets)}] {cat.upper()}: {title} (de {author}) -> {dest} ... ", end="", flush=True)

        img_url = None
        if "musica" in cat:
            # 1. Deezer
            img_url = get_deezer(f"{author} {title}")
            # 2. iTunes music
            if not img_url:
                img_url = get_itunes(f"{author} {clean_text(title)}", media="music", entity="album")
            # 3. Wikipedia
            if not img_url:
                img_url = get_wikipedia(f"{author} {title}", "musica")
        elif "livro" in cat:
            # 1. Open Library
            img_url = get_openlibrary(title, author)
            # 2. Wikipedia
            if not img_url:
                img_url = get_wikipedia(f"{title}", "livros")
            # 3. iTunes ebook
            if not img_url:
                img_url = get_itunes(f"{clean_text(title)} {author}", media="ebook")
        elif "cine" in cat:
            # 1. Wikipedia
            img_url = get_wikipedia(f"{title}", "cine")
            # 2. iTunes movie / tvSeason
            if not img_url:
                img_url = get_itunes(f"{clean_text(title)}", media="movie", entity="movie")
            if not img_url:
                img_url = get_itunes(f"{clean_text(title)}", media="tvShow", entity="tvSeason")

        if img_url and download_img(img_url, dest):
            print(f"SUCESSO! ({img_url[:40]}...)")
            sucessos += 1
        else:
            print("NÃO ENCONTRADO.")
            falhas.append(t)

        time.sleep(0.1)

    print(f"\nResultado final: {sucessos} recuperados com sucesso, {len(falhas)} pendentes.")
    with open("tools/pendentes.json", "w") as fp:
        json.dump(falhas, fp, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
