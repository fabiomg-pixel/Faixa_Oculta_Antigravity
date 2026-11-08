#!/usr/bin/env python3
"""
tools/processar_jornais_beeper.py
---------------------------------
Integração direta com o Beeper Desktop no macOS para:
1. Listar jornais e revistas disponíveis nos canais 'Jornais BR', 'International Newspapers' e 'Jornais e Revistas 4.0'.
2. Fazer download automatizado sob demanda de qualquer edição via Beeper Client API local (localhost:23373).
3. Processar e extrair o texto completo das reportagens, colunas e editoriais (via PyMuPDF e OCR nativo Apple Vision).
4. Gerar sínteses e despachos estruturados para abastecer o boletim diário da Faixa Oculta com jornalismo impresso de primeira linha.
"""

import os
import sys
import json
import sqlite3
import hashlib
import base64
import urllib.request
import urllib.parse
import subprocess
from datetime import datetime

BEEPER_DIR = os.path.expanduser("~/Library/Application Support/BeeperTexts")
DB_PATH = os.path.join(BEEPER_DIR, "index.db")
MEDIA_DIR = os.path.join(BEEPER_DIR, "media", "local.beeper.com")
TOKEN_FILE = os.path.expanduser("~/.beeper_token.json")
BEEPER_BASE_URL = "http://localhost:23373"

KNOWN_ROOMS = {
    "nacional": {
        "name": "Jornais BR",
        "room_id": "!iq3RLvh1JnfH6vJzkvaL:beeper.local"
    },
    "internacional": {
        "name": "International Newspapers",
        "room_id": "!Q3EN2ZSkzkir8tYnRU7t:beeper.local"
    },
    "revistas": {
        "name": "Jornais e Revistas 4.0",
        "room_id": "!tFgakhGBTv3CNjiYMdkM:beeper.local"
    }
}


def get_access_token():
    """Recupera ou autentica para obter token Bearer do Beeper Client API local."""
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, "r") as f:
                data = json.load(f)
                token = data.get("access_token")
                expires_at = data.get("expires_at", 0)
                if token and datetime.now().timestamp() < expires_at - 60:
                    return token
        except Exception:
            pass

    # Fluxo OAuth PKCE Local
    try:
        # 1. Registrar cliente
        reg_req = urllib.request.Request(
            f"{BEEPER_BASE_URL}/oauth/register",
            data=json.dumps({
                "client_name": "Faixa Oculta CLI",
                "redirect_uris": ["http://localhost:8989/callback"]
            }).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(reg_req) as resp:
            client_data = json.loads(resp.read().decode("utf-8"))
            client_id = client_data["client_id"]

        # 2. Gerar code verifier e challenge
        verifier = "abcdefghijklmnopqrstuvwxyz0123456789-._~" + hashlib.sha256(str(datetime.now()).encode()).hexdigest()[:20]
        digest = hashlib.sha256(verifier.encode("utf-8")).digest()
        challenge = base64.urlsafe_b64encode(digest).decode("utf-8").rstrip("=")

        # 3. Solicitar código de autorização diretamente ao callback local
        cb_payload = {
            "mode": "oauth2",
            "clientInfo": {
                "name": "Faixa Oculta CLI",
                "clientURI": None,
                "clientID": client_id
            },
            "scopes": ["read", "write"],
            "redirectUri": "http://localhost:8989/callback",
            "scope": "read write",
            "codeChallenge": challenge,
            "codeChallengeMethod": "S256"
        }
        cb_req = urllib.request.Request(
            f"{BEEPER_BASE_URL}/oauth/authorize/callback",
            data=json.dumps(cb_payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(cb_req) as resp:
            code_data = json.loads(resp.read().decode("utf-8"))
            auth_code = code_data.get("code")

        if not auth_code:
            raise RuntimeError(f"Não foi possível obter authorization code: {code_data}")

        # 4. Trocar código por access token
        token_payload = urllib.parse.urlencode({
            "grant_type": "authorization_code",
            "client_id": client_id,
            "code": auth_code,
            "redirect_uri": "http://localhost:8989/callback",
            "code_verifier": verifier
        }).encode("utf-8")
        token_req = urllib.request.Request(
            f"{BEEPER_BASE_URL}/oauth/token",
            data=token_payload,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        with urllib.request.urlopen(token_req) as resp:
            token_resp = json.loads(resp.read().decode("utf-8"))
            access_token = token_resp["access_token"]
            expires_in = token_resp.get("expires_in", 2592000)

            # Salvar cache
            with open(TOKEN_FILE, "w") as f:
                json.dump({
                    "access_token": access_token,
                    "expires_at": datetime.now().timestamp() + expires_in
                }, f)
            return access_token
    except Exception as e:
        print(f"Aviso: Erro ao autenticar no Beeper API: {e}", file=sys.stderr)
        return None


def list_publications(room_key="nacional", limit=40):
    """Lista as publicações disponíveis no banco SQLite do Beeper."""
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Banco Beeper não encontrado em {DB_PATH}")

    room_info = KNOWN_ROOMS.get(room_key, KNOWN_ROOMS["nacional"])
    room_id = room_info["room_id"]

    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    cur = conn.cursor()

    cur.execute("""
        SELECT timestamp, message 
        FROM mx_room_messages 
        WHERE roomID = ? AND type = 'FILE'
        ORDER BY timestamp DESC LIMIT ?
    """, (room_id, limit))

    publications = []
    for ts, msg_str in cur.fetchall():
        try:
            msg = json.loads(msg_str)
            for att in msg.get("attachments", []):
                fn = att.get("fileName", "sem_nome.pdf")
                size = att.get("fileSize", 0)
                src = att.get("srcURL", "")
                media_id = src.replace("mxc://local.beeper.com/", "")
                local_path = os.path.join(MEDIA_DIR, media_id)
                baixado = os.path.exists(local_path)
                publications.append({
                    "data_msg": datetime.fromtimestamp(ts / 1000.0).strftime("%Y-%m-%d %H:%M"),
                    "arquivo": fn,
                    "tamanho_mb": round(size / (1024 * 1024), 2),
                    "src_url": src,
                    "media_id": media_id,
                    "baixado": baixado,
                    "local_path": local_path if baixado else None
                })
        except Exception:
            continue

    conn.close()
    return publications


def download_file(src_url):
    """Solicita o download do arquivo via API local do Beeper."""
    token = get_access_token()
    if not token:
        raise RuntimeError("Token de autenticação Beeper indisponível.")

    req = urllib.request.Request(
        f"{BEEPER_BASE_URL}/v1/assets/download",
        data=json.dumps({"url": src_url}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        local_url = res.get("srcURL", "")
        clean_path = local_url.replace("file://", "").replace("%20", " ")
        return clean_path


def extract_text_from_pdf(pdf_path, max_pages=15):
    """Extrai texto do PDF usando PyMuPDF; se for imagem pura, aplica OCR nativo Apple Vision."""
    try:
        import fitz
    except ImportError:
        raise ImportError("PyMuPDF (fitz) é necessário para extrair texto.")

    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    pages_to_read = min(total_pages, max_pages)

    results = []
    needs_ocr = False

    for page_idx in range(pages_to_read):
        page = doc[page_idx]
        txt = page.get_text()
        if len(txt.strip()) < 50:
            needs_ocr = True
            break
        results.append({
            "pagina": page_idx + 1,
            "texto": txt
        })

    if not needs_ocr and len(results) > 0:
        return {
            "metodo": "digital_text",
            "total_paginas": total_pages,
            "paginas_lidas": len(results),
            "conteudo": results
        }

    # Se precisa de OCR, usa Apple Vision nativo via Swift
    ocr_results = []
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
    let strings = observations.compactMap { $0.topCandidates(1).first?.string }
    print(strings.joined(separator: "\\n"))
}

request.recognitionLevel = .accurate
request.recognitionLanguages = [lang]
request.usesLanguageCorrection = true

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
try? handler.perform([request])
"""
    tmp_swift = "/tmp/apple_vision_ocr.swift"
    with open(tmp_swift, "w") as f:
        f.write(swift_script)

    for page_idx in range(min(total_pages, 8)):
        page = doc[page_idx]
        pix = page.get_pixmap(dpi=150)
        tmp_img = f"/tmp/page_{page_idx+1}.png"
        pix.save(tmp_img)

        try:
            cmd = ["/usr/bin/swift", tmp_swift, tmp_img, "pt-BR"]
            proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
            ocr_text = proc.stdout.strip()
            ocr_results.append({
                "pagina": page_idx + 1,
                "texto": ocr_text
            })
        except Exception as e:
            ocr_results.append({
                "pagina": page_idx + 1,
                "texto": f"[Erro no OCR: {e}]"
            })
        finally:
            if os.path.exists(tmp_img):
                os.remove(tmp_img)

    return {
        "metodo": "apple_vision_ocr",
        "total_paginas": total_pages,
        "paginas_lidas": len(ocr_results),
        "conteudo": ocr_results
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Processador de Jornais e Revistas via Beeper")
    parser.add_argument("--list", nargs="?", const="nacional", default=None, choices=["nacional", "internacional", "revistas", "all"],
                        help="Lista as publicações de um canal específico (default: nacional)")
    parser.add_argument("--download", type=str, help="Nome do arquivo ou trecho do nome para baixar")
    parser.add_argument("--extract", type=str, help="Caminho local do arquivo ou trecho do nome para extrair")
    parser.add_argument("--pages", type=int, default=8, help="Número de páginas para extrair")
    parser.add_argument("--digest", action="store_true", help="Gera um panorama estruturado das edições do dia baixadas")
    args = parser.parse_args()

    if args.list:
        channels = ["nacional", "internacional", "revistas"] if args.list == "all" else [args.list]
        for ch in channels:
            info = KNOWN_ROOMS[ch]
            print(f"\n=======================================================")
            print(f" CANAL: {info['name'].upper()} ({ch})")
            print(f"=======================================================")
            pubs = list_publications(ch, limit=25)
            for p in pubs:
                status = f"✅ BAIXADO ({p['tamanho_mb']} MB)" if p['baixado'] else f"⏳ PENDENTE ({p['tamanho_mb']} MB)"
                print(f"[{p['data_msg']}] {p['arquivo'][:42]:<43} | {status}")

    if args.download:
        termo = args.download.lower()
        pubs = list_publications("nacional", 50) + list_publications("internacional", 50) + list_publications("revistas", 50)
        candidatos = [p for p in pubs if termo in p["arquivo"].lower()]
        if not candidatos:
            print(f"Nenhuma publicação encontrada correspondente a '{args.download}'.")
            return

        cand = candidatos[0]
        print(f"\nIniciando download de '{cand['arquivo']}' ({cand['tamanho_mb']} MB)...")
        if cand["baixado"]:
            print(f"Arquivo já baixado em: {cand['local_path']}")
        else:
            caminho = download_file(cand["src_url"])
            print(f"Download concluído com sucesso: {caminho}")

    if args.extract:
        termo = args.extract.lower()
        pubs = list_publications("nacional", 50) + list_publications("internacional", 50) + list_publications("revistas", 50)
        candidatos = [p for p in pubs if termo in p["arquivo"].lower() and p["baixado"]]
        
        target_path = None
        if os.path.exists(args.extract):
            target_path = args.extract
        elif candidatos:
            target_path = candidatos[0]["local_path"]
        else:
            print(f"Arquivo '{args.extract}' não encontrado baixado no disco.")
            return

        print(f"\nExtraindo texto de '{target_path}' (até {args.pages} páginas)...")
        dados = extract_text_from_pdf(target_path, max_pages=args.pages)
        print(f"Método utilizado: {dados['metodo']} | Total de páginas no documento: {dados['total_paginas']}")
        for p in dados["conteudo"]:
            print(f"\n--- PÁGINA {p['pagina']} ---")
            lines = [l.strip() for l in p["texto"].split("\n") if l.strip()]
            for l in lines[:15]:
                print(f"  {l}")
            if len(lines) > 15:
                print(f"  ... (+ {len(lines) - 15} linhas)")


if __name__ == "__main__":
    main()
