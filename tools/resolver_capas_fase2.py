import json, os, subprocess, urllib.parse, time
from PIL import Image

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

MAPA = {
    'capas/1385b17002a71304003b7382ac1e63e1.jpg': [('en', 'La_chimera'), ('it', 'La_chimera')],
    'capas/1e9191fc22a4d922a5a860f2045d6877.jpg': [('openlibrary', 'A Visao em Parafuso Manoel de Barros'), ('pt', 'Manoel_de_Barros')],
    'capas/22eaa8c38d7d5ac3c58cd5c7f1e2ab04.jpg': [('en', 'The_Girl_with_the_Needle')],
    'capas/26e99066eb6a7bc6359f88978efba37e.jpg': [('pt', 'Retratos_Fantasmas'), ('en', 'Pictures_of_Ghosts')],
    'capas/39ef428bd22c8eb18d4152339772a829.jpg': [('deezer', 'Jucara Marcal Caderno de Composicao'), ('deezer', 'Jucara Marcal')],
    'capas/3e73aac8ab5680338200857b5295e345.jpg': [('en', 'Emilia_Pérez'), ('fr', 'Emilia_Pérez')],
    'capas/47fb8cf21127a7dc3cb9ab22272a38d1.jpg': [('deezer', 'Iggy Pop Post Pop Depression'), ('en', 'Post_Pop_Depression')],
    'capas/4afdae3808926907ea71e3128698e087.jpg': [('en', 'Anatomy_of_a_Fall'), ('fr', 'Anatomie_d%27une_chute')],
    'capas/505a32057542d18eafe3d2dfc454162b.jpg': [('deezer', 'Negro Leo Desejo do Labirinto'), ('deezer', 'Negro Leo')],
    'capas/58670ebdc21b6abc206a7cb2bebbe7b3.jpg': [('en', 'Happy_as_Lazzaro'), ('it', 'Lazzaro_felice')],
    'capas/64968caf8aa0c315750a57caf6a04689.jpg': [('en', 'The_Sympathizer_(miniseries)')],
    'capas/66470d3237ff2f562147f592072e176c.jpg': [('en', 'Happening_(film)'), ('fr', 'L%27Événement_(film)')],
    'capas/69a6ddeabdb85f7a986ce25b8c41f70c.jpg': [('en', 'There_Is_No_Evil')],
    'capas/6fa073eda6653f259097132ff2ffb432.jpg': [('en', 'The_Lives_of_Others'), ('de', 'Das_Leben_der_Anderen')],
    'capas/72647e941dc7c584380bef229d927018.jpg': [('en', 'Furiosa:_A_Mad_Max_Saga'), ('pt', 'Furiosa:_Uma_Saga_Mad_Max')],
    'capas/8229a4a72ea1fbff47a7ad78f7f6c0fe.jpg': [('pt', 'Bacurau_(filme)'), ('en', 'Bacurau')],
    'capas/8575f2af92c349adfa688b1932a29f16.jpg': [('en', 'Slow_Horses')],
    'capas/8894f4363929c5160bbdce2671dd01e8.jpg': [('en', 'Dune:_Part_Two')],
    'capas/8ced05c1e108274bf9d064542ed9111f.jpg': [('deezer', 'Whitelands Sun-Bleached Noise'), ('deezer', 'Whitelands')],
    'capas/8f6812fede13ce714a3cd293afef8219.jpg': [('es', 'Cien_años_de_soledad_(serie_de_televisión)'), ('en', 'One_Hundred_Years_of_Solitude_(TV_series)')],
    'capas/92fd062a5bf015803448eb35eca7a2ba.jpg': [('en', 'Mickey_17')],
    'capas/94f5a1ed54a81b7bfe2cc5cb02dd948e.jpg': [('en', 'Toni_Erdmann')],
    'capas/98b41b86d380b77ec3e65557cde1d456.jpg': [('pt', 'Cabra_Marcado_para_Morrer'), ('en', 'Twenty_Years_Later')],
    'capas/994fed4218b5c88e95038d1ab8b64df8.jpg': [('en', 'Green_Border')],
    'capas/a4ec9dac07633d1f082398c321872a78.jpg': [('en', 'Megalopolis_(film)')],
    'capas/b91daa855875ef0854afedb860d46dd3.jpg': [('en', 'Do_Not_Expect_Too_Much_from_the_End_of_the_World')],
    'capas/bdf90e3f73efb55208158e21a806541c.jpg': [('en', 'Motel_Destino'), ('pt', 'Motel_Destino')],
    'capas/e18dbc135c0addb4b5710e67376ad07f.jpg': [('pt', 'O_Som_ao_Redor'), ('en', 'Neighboring_Sounds')],
    'capas/e681e40cc8d0ab5a98f7287f88790717.jpg': [('pt', 'Vidas_Secas_(filme)'), ('en', 'Barren_Lives_(film)')],
    'capas/eaafe4a8269e9ffff3c77e3637f98636.jpg': [('en', 'Baby_Reindeer_(TV_series)'), ('en', 'Baby_Reindeer')],
    'capas/ebf6c3749385eac62333800288835818.jpg': [('en', 'Evil_Does_Not_Exist')],
    'capas/f327729b0bb1ce1a6e9df5cf2cb7c6be.jpg': [('en', 'Challengers_(film)')],
    'capas/fc507519d843a204d53c434a291983a5.jpg': [('openlibrary', "The Panda's Thumb Stephen Jay Gould"), ('en', "The_Panda%27s_Thumb_(book)")],
    'capas/fe9f83798a0a978852084b5a744aaac9.jpg': [('en', 'The_Room_Next_Door')]
}

def download_img(url, dest_path):
    if not url: return False
    tmp = dest_path + ".tmp"
    cmd = ["curl", "-s", "-L", "--max-time", "15", "-A", UA, "-o", tmp, url]
    r = subprocess.run(cmd)
    if r.returncode == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 3000:
        try:
            im = Image.open(tmp)
            im.verify()
            os.replace(tmp, dest_path)
            return True
        except Exception:
            if os.path.exists(tmp): os.remove(tmp)
            return False
    if os.path.exists(tmp): os.remove(tmp)
    return False

def resolver_item(dest, regras):
    for tipo, query in regras:
        if tipo in ['en', 'pt', 'fr', 'it', 'es', 'de']:
            url = f"https://{tipo}.wikipedia.org/api/rest_v1/page/summary/{query}"
            res = subprocess.run(["curl", "-s", "-A", UA, url], capture_output=True, text=True)
            try:
                d = json.loads(res.stdout)
                img = d.get('originalimage', {}).get('source') or d.get('thumbnail', {}).get('source')
                if img and download_img(img, dest):
                    return img
            except Exception:
                pass
        elif tipo == 'deezer':
            url = f"https://api.deezer.com/search/album?q={urllib.parse.quote(query)}"
            res = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
            try:
                d = json.loads(res.stdout).get('data', [])
                if d:
                    img = d[0].get('cover_xl') or d[0].get('cover_big') or d[0].get('cover_medium')
                    if img and download_img(img, dest):
                        return img
            except Exception:
                pass
        elif tipo == 'openlibrary':
            url = f"https://openlibrary.org/search.json?q={urllib.parse.quote(query)}&limit=3"
            res = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
            try:
                docs = json.loads(res.stdout).get('docs', [])
                for doc in docs:
                    cov = doc.get('cover_i')
                    if cov:
                        img = f"https://covers.openlibrary.org/b/id/{cov}-L.jpg"
                        if download_img(img, dest):
                            return img
            except Exception:
                pass
    return None

def main():
    print(f"Resolvendo os {len(MAPA)} itens restantes...")
    sucessos = 0
    falhas = []
    for dest, regras in MAPA.items():
        print(f"Resolvendo {dest} ... ", end="", flush=True)
        img = resolver_item(dest, regras)
        if img:
            print(f"SUCESSO! ({img[:45]}...)")
            sucessos += 1
        else:
            print("FALHOU.")
            falhas.append(dest)
        time.sleep(0.1)

    print(f"\nFinal: {sucessos} / {len(MAPA)} resolvidos.")
    print("Falhas:", falhas)

if __name__ == '__main__':
    main()
