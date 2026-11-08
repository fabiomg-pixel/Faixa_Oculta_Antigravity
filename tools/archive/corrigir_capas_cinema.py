import json, subprocess, hashlib, os
from PIL import Image

posters_para_baixar = {
    "2026-11--sugar": "https://image.tmdb.org/t/p/w780/tLmwLYiI7EpPbhgmdeivNGY0xw7.jpg",
    "2026-11--delegado": "https://image.tmdb.org/t/p/w780/cIOmMW9cNqVvA6d2LY3c7FZjVCe.jpg",
    "2026-11--malu": "https://image.tmdb.org/t/p/w780/2XSeWLTAWhR7e6pfnYcoBSF1UR4.jpg",
    "2026-11--feito-pipa": "https://image.tmdb.org/t/p/w780/3BFxMOi3HFsOGHEojiRI4hk1500.jpg",
    "2026-11--duna-parte-3": "https://image.tmdb.org/t/p/w780/glt0v4I89rMWstDNCaFXc5SNyO1.jpg",
    "2026-11--a-queda-do-ceu": "https://image.tmdb.org/t/p/w780/eEQ9oJWHGOFwANau1tEyCfJ01sl.jpg",
    "2026-11--mother-mary": "https://image.tmdb.org/t/p/w780/uVcsN3yoHh7ZcJ6ecj1FJfv7dLa.jpg",
    "2026-11--jogos-vorazes-amanhecer-na-colheita": "https://image.tmdb.org/t/p/w780/jNcZH8yplxttRlf0wwqfGGMKHxX.jpg",
    "2026-11--godzilla-minus-zero": "https://image.tmdb.org/t/p/w780/hSmIJluOJmTWvJs4d7kHRxjc8s8.jpg",
    "2026-11--cloud-nuvem": "https://image.tmdb.org/t/p/w780/8DQWjKkvg4o0vXsHoFKxwpvT4yp.jpg",
    "2026-11--i-love-boosters": "https://image.tmdb.org/t/p/w780/4pNKIUFy7tkZiBx0rnSmG9ysRy.jpg",
    "2026-11--rosebush-pruning": "https://image.tmdb.org/t/p/w780/rsHEVjzxU8cxz1sm3vboj99daNv.jpg",
    "2026-11--fatherland": "https://image.tmdb.org/t/p/w780/oNejN1l69nBF8LdQwy5FkAQZT44.jpg"
}

with open('data/revista.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for slug, url in posters_para_baixar.items():
    tmp_path = f"/tmp/{slug}.jpg"
    cmd = [
        "curl", "-s", "-L",
        "-A", "FaixaOcultaBot/1.0 (contact@faixaoculta.com)",
        url, "-o", tmp_path
    ]
    res = subprocess.run(cmd)
    if res.returncode != 0 or not os.path.exists(tmp_path) or os.path.getsize(tmp_path) < 1000:
        print(f"Erro ao baixar {slug} de {url}")
        continue
    
    try:
        im = Image.open(tmp_path).convert('RGB')
        # Calcular hash do arquivo baixado
        with open(tmp_path, 'rb') as f_tmp:
            h = hashlib.md5(f_tmp.read()).hexdigest()
        dest_filename = f"capas/{h}.jpg"
        im.save(dest_filename, 'JPEG', quality=95)
        
        # Atualizar no dicionario
        if slug in d['cine_itens']:
            d['cine_itens'][slug]['capa'] = dest_filename
            print(f"Atualizado {slug} -> {dest_filename}")
        else:
            print(f"Slug {slug} não encontrado em cine_itens")
    except Exception as e:
        print(f"Erro ao processar imagem para {slug}: {e}")

with open('data/revista.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("\nVerificando duplicatas restantes em cine_itens 2026-11...")
capas_cine = {}
for k, it in d.get('cine_itens', {}).items():
    if it.get('edicao') == '2026-11':
        c = it.get('capa')
        capas_cine.setdefault(c, []).append((k, it.get('titulo')))

dups = {c: itens for c, itens in capas_cine.items() if len(itens) > 1}
if not dups:
    print("Sucesso absoluto! ZERO capas duplicadas na safra de cinema de 2026-11!")
else:
    print(f"Ainda restam {len(dups)} capas duplicadas:")
    for c, itens in dups.items():
        print(f"  {c}: {itens}")
