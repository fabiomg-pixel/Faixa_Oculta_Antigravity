#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utilitário de padronização, compressão sem perda perceptível e higienização de mídias da Faixa Oculta.

1. Converte capas fora do padrão (`capas/*.png`, `capas/mag_*.jpg`, `capas/pap_*.jpg`, hashes curtos)
   em `capas/<md5_32_hex>.jpg` compatíveis com `safeUrl` e atualiza `data/revista.json`.
2. Redimensiona e comprime capas pesadas (> 220 KB ou dimensão > 1000px) em JPEG RGB progressivo (`quality=84`).
3. Arquiva capas órfãs (não referenciadas em `data/revista.json` nem em `tools/`), áudios órfãos e backups `.zip`
   na pasta privada do Google Drive (`~/Library/CloudStorage/.../Meu Drive/Faixa Oculta PDFs/`), preservando 100% do histórico fora do Git.
"""

import glob
import hashlib
import io
import json
import os
import re
import shutil
from PIL import Image

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CAPAS_DIR = os.path.join(ROOT_DIR, "capas")
AUDIOS_DIR = os.path.join(ROOT_DIR, "audios")
REVISTA_JSON = os.path.join(ROOT_DIR, "data", "revista.json")
DRIVE_ARCHIVE = os.environ.get("FAIXA_PDF_ARCHIVE_DIR") or os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-fabiomg@biof.ufrj.br/Meu Drive/Faixa Oculta PDFs"
)

SAFE_CAPA_RE = re.compile(r"^capas/[0-9a-f]{32}\.jpg$")
MAX_DIM = 1000
TARGET_MAX_BYTES = 220 * 1024


def renderizar_jpeg_otimizado(img_path, max_dim=MAX_DIM, quality=84):
    with Image.open(img_path) as im:
        if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
            bg = Image.new("RGB", im.size, (243, 238, 228))
            rgba = im.convert("RGBA")
            bg.paste(rgba, mask=rgba.split()[3])
            rgb = bg
        else:
            rgb = im.convert("RGB")

        w, h = rgb.size
        if max(w, h) > max_dim:
            rgb.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)

        buf = io.BytesIO()
        rgb.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True)
        return buf.getvalue()


def padronizar_capas_no_json(db):
    raw = json.dumps(db, ensure_ascii=False)
    refs = sorted(set(re.findall(r'capas/[^"\'\s\\]+', raw)))
    substituicoes = {}

    # Garantir também a capa estática do Le Monde usada pelo coletor RSS
    lemonde_png = os.path.join(ROOT_DIR, "capas", "lemonde_capa.png")
    if os.path.exists(lemonde_png) and "capas/lemonde_capa.png" not in refs:
        refs.append("capas/lemonde_capa.png")

    for ref in refs:
        if SAFE_CAPA_RE.match(ref):
            continue
        src_abs = os.path.join(ROOT_DIR, ref)
        if not os.path.exists(src_abs):
            continue
        if ref == "capas/lemonde_capa.png":
            novo_hash = hashlib.md5(b"lemonde-capa-oficial").hexdigest()
        else:
            novo_hash = hashlib.md5(ref.encode("utf-8")).hexdigest()
        novo_rel = f"capas/{novo_hash}.jpg"
        novo_abs = os.path.join(ROOT_DIR, novo_rel)
        if not os.path.exists(novo_abs):
            dados_jpg = renderizar_jpeg_otimizado(src_abs, max_dim=MAX_DIM, quality=85)
            with open(novo_abs, "wb") as f:
                f.write(dados_jpg)
        substituicoes[ref] = novo_rel

    if substituicoes:
        def _trocar(obj):
            if isinstance(obj, dict):
                return {k: _trocar(v) for k, v in obj.items()}
            if isinstance(obj, list):
                return [_trocar(x) for x in obj]
            if isinstance(obj, str) and obj in substituicoes:
                return substituicoes[obj]
            return obj

        db = _trocar(db)

    return db, substituicoes


def comprimir_capas_existentes():
    from concurrent.futures import ThreadPoolExecutor

    candidatos = []
    for fn in sorted(os.listdir(CAPAS_DIR)):
        if fn.startswith(".") or not fn.lower().endswith(".jpg"):
            continue
        p = os.path.join(CAPAS_DIR, fn)
        sz_antes = os.path.getsize(p)
        if sz_antes > TARGET_MAX_BYTES:
            candidatos.append((fn, p, sz_antes))

    def _proc(item):
        fn, p, sz_antes = item
        try:
            novo_bytes = renderizar_jpeg_otimizado(p, max_dim=MAX_DIM, quality=84)
            if len(novo_bytes) > 3072 and len(novo_bytes) < sz_antes * 0.92:
                with open(p, "wb") as f:
                    f.write(novo_bytes)
                return 1, (sz_antes - len(novo_bytes))
        except Exception as e:
            print(f"  [Aviso] Falha ao comprimir {fn}: {e}", flush=True)
        return 0, 0

    recomp = 0
    economizado = 0
    if candidatos:
        with ThreadPoolExecutor(max_workers=8) as pool:
            for r, ec in pool.map(_proc, candidatos):
                recomp += r
                economizado += ec
    return recomp, economizado


def coletar_referencias_protegidas(raw_revista):
    protegidas = set(re.findall(r'capas/([A-Za-z0-9_.\-]+)', raw_revista))
    for padrao in ("tools/*.py", "tools/*.json"):
        for arq in glob.glob(os.path.join(ROOT_DIR, padrao)):
            try:
                txt = open(arq, "r", encoding="utf-8", errors="ignore").read()
                protegidas.update(re.findall(r'capas/([A-Za-z0-9_.\-]+)', txt))
            except Exception:
                pass
    return protegidas


def _mover_rapido(src, dst):
    try:
        os.replace(src, dst)
    except OSError:
        shutil.move(src, dst)


def arquivar_orfaos(raw_revista):
    usa_drive = os.path.isdir(os.path.dirname(DRIVE_ARCHIVE))
    dest_capas = os.path.join(DRIVE_ARCHIVE, "Capas_Orfas")
    dest_audios = os.path.join(DRIVE_ARCHIVE, "Audios_Historico")
    dest_backups = os.path.join(DRIVE_ARCHIVE, "Backups_Codigo")
    if usa_drive:
        for d in (dest_capas, dest_audios, dest_backups):
            os.makedirs(d, exist_ok=True)

    protegidas = coletar_referencias_protegidas(raw_revista)
    capas_movidas = 0
    bytes_capas_mov = 0
    for fn in sorted(os.listdir(CAPAS_DIR)):
        if fn.startswith("."):
            continue
        if fn not in protegidas:
            src = os.path.join(CAPAS_DIR, fn)
            sz = os.path.getsize(src)
            if usa_drive:
                _mover_rapido(src, os.path.join(dest_capas, fn))
            else:
                os.remove(src)
            capas_movidas += 1
            bytes_capas_mov += sz

    audios_ref = set(re.findall(r'audios/([A-Za-z0-9_.\-]+\.mp3)', raw_revista))
    audios_movidos = 0
    bytes_audios_mov = 0
    if os.path.isdir(AUDIOS_DIR):
        for fn in sorted(os.listdir(AUDIOS_DIR)):
            if fn.startswith("."):
                continue
            if fn not in audios_ref:
                src = os.path.join(AUDIOS_DIR, fn)
                sz = os.path.getsize(src)
                if usa_drive:
                    _mover_rapido(src, os.path.join(dest_audios, fn))
                else:
                    os.remove(src)
                audios_movidos += 1
                bytes_audios_mov += sz

    zips_movidos = []
    for zp in glob.glob(os.path.join(ROOT_DIR, "faixa_oculta_*.zip")):
        fn = os.path.basename(zp)
        sz = os.path.getsize(zp)
        if usa_drive:
            _mover_rapido(zp, os.path.join(dest_backups, fn))
            zips_movidos.append((fn, sz))

    return {
        "capas_movidas": capas_movidas,
        "bytes_capas_mov": bytes_capas_mov,
        "audios_movidos": audios_movidos,
        "bytes_audios_mov": bytes_audios_mov,
        "zips_movidos": zips_movidos,
    }


def main():
    print("=== OTIMIZAÇÃO DE MÍDIAS · FAIXA OCULTA ===", flush=True)
    with open(REVISTA_JSON, "r", encoding="utf-8") as f:
        db = json.load(f)

    db, subs = padronizar_capas_no_json(db)
    if subs:
        with open(REVISTA_JSON, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
    print(f"  [OK] Capas fora do padrão convertidas para MD5 .jpg: {len(subs)}", flush=True)

    raw_novo = json.dumps(db, ensure_ascii=False)
    arq = arquivar_orfaos(raw_novo)
    print(f"  [OK] Capas órfãs arquivadas no Drive : {arq['capas_movidas']} (-{arq['bytes_capas_mov']/1024/1024:.2f} MB)", flush=True)
    print(f"  [OK] Áudios órfãos arquivados no Drive: {arq['audios_movidos']} (-{arq['bytes_audios_mov']/1024/1024:.2f} MB)", flush=True)
    if arq["zips_movidos"]:
        tot_z = sum(s for _, s in arq["zips_movidos"])
        print(f"  [OK] Backups .zip movidos para o Drive: {len(arq['zips_movidos'])} (-{tot_z/1024/1024:.2f} MB)", flush=True)

    recomp, econ = comprimir_capas_existentes()
    print(f"  [OK] Capas pesadas recomprimidas (<=1000px, JPEG progressivo): {recomp} arquivos (-{econ/1024/1024:.2f} MB)", flush=True)

    restantes_capas = [os.path.getsize(os.path.join(CAPAS_DIR, c)) for c in os.listdir(CAPAS_DIR) if not c.startswith(".")]
    restantes_audios = [os.path.getsize(os.path.join(AUDIOS_DIR, a)) for a in os.listdir(AUDIOS_DIR) if not a.startswith(".")]
    print(f"  [FINAL] capas/: {len(restantes_capas)} arquivos ({sum(restantes_capas)/1024/1024:.2f} MB)", flush=True)
    print(f"  [FINAL] audios/: {len(restantes_audios)} arquivos ({sum(restantes_audios)/1024/1024:.2f} MB)", flush=True)


if __name__ == "__main__":
    main()
