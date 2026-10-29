#!/usr/bin/env python3
"""Sentinela da Faixa Oculta / Radar Cultural.

Executado via launchd no macOS sempre que o computador estiver ativo.
Verifica se o GitHub Actions já gerou e publicou o boletim do turno atual.
Se já estiver no ar, encerra imediatamente sem fazer nada.
Se a nuvem não tiver rodado (ou falhado), dispara o workflow via GitHub CLI.
"""

import sys
import os
import json
import time
import ssl
import urllib.request
import datetime
import subprocess

LOCK_FILE = "/tmp/faixaoculta_sentinela.lock"
COOLDOWN_SEGUNDOS = 900  # 15 minutos de intervalo entre disparos manuais
REPO = "fabiomg-pixel/Faixa_Oculta_Antigravity"
WORKFLOW = "atualizar_radar.yml"
SITE_JSON = "https://fabiomg-pixel.github.io/Faixa_Oculta_Antigravity/data/revista.json"

GH_BIN = "/opt/homebrew/bin/gh"
if not os.path.exists(GH_BIN):
    GH_BIN = "/usr/local/bin/gh"


def log(msg):
    agora_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{agora_str}] [Sentinela] {msg}", flush=True)


def obter_turno_esperado():
    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    data_iso = agora.strftime("%Y-%m-%d")
    hora = agora.hour

    # Janela da manhã: verifica a partir das 06h00 até 16h59
    if 6 <= hora < 17:
        return data_iso, "manha"

    # Janela da noite: verifica a partir das 18h00 até 23h59
    if hora >= 18:
        return f"{data_iso}-noite", "noite"

    # Antes das 05h00 da madrugada: turno da noite do dia anterior
    if hora < 5:
        ontem = (agora - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        return f"{ontem}-noite", "noite"

    # Entre 05h00-05h59 ou 17h00-17h59: janela em que a nuvem está rodando o cron
    return None, None


def verificar_site_publicado(doc_id):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(
        f"{SITE_JSON}?t={int(time.time())}",
        headers={"User-Agent": "FaixaOculta-Sentinela/1.0", "Cache-Control": "no-cache"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            dados = json.loads(r.read().decode("utf-8"))
        dias = dados.get("dias", {})
        return doc_id in dias
    except Exception as e:
        log(f"Aviso ao consultar GitHub Pages ({e}). Consultando arquivo local de fallback...")
        local_path = os.path.expanduser(
            "~/Library/CloudStorage/GoogleDrive-fabiomg@biof.ufrj.br/Meu Drive/Antigravity/Radar Cultural/data/revista.json"
        )
        if os.path.exists(local_path):
            try:
                with open(local_path, "r", encoding="utf-8") as f:
                    local_dados = json.load(f)
                return doc_id in local_dados.get("dias", {})
            except Exception:
                pass
        return False


def ja_disparado_recentemente():
    if not os.path.exists(LOCK_FILE):
        return False
    try:
        mtime = os.path.getmtime(LOCK_FILE)
        if time.time() - mtime < COOLDOWN_SEGUNDOS:
            return True
    except Exception:
        pass
    return False


def marcar_disparo():
    try:
        with open(LOCK_FILE, "w") as f:
            f.write(str(time.time()))
    except Exception:
        pass


def disparar_nuvem():
    if not os.path.exists(GH_BIN):
        log(f"Erro: binário gh não encontrado em {GH_BIN}.")
        return False

    cmd = [GH_BIN, "workflow", "run", WORKFLOW, "--repo", REPO]
    log(f"Executando: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        log(f"Sucesso: GitHub Actions disparado na nuvem! Saída: {res.stdout.strip()}")
        marcar_disparo()
        return True
    else:
        log(f"Falha ao disparar GitHub Actions: {res.stderr.strip()}")
        return False


def main():
    doc_id, turno = obter_turno_esperado()
    if not doc_id:
        log("Fora do horário de checagem do sentinela (nuvem está no período de apuração programada).")
        return

    log(f"Verificando se edição esperada [{doc_id}] ({turno}) já está publicada...")

    if verificar_site_publicado(doc_id):
        log(f"OK: Edição [{doc_id}] já está publicada e acessível no ar. Nada a fazer.")
        return

    log(f"ATENÇÃO: Edição [{doc_id}] NÃO foi encontrada no ar.")

    if ja_disparado_recentemente():
        log(f"Disparo já solicitado nos últimos {COOLDOWN_SEGUNDOS // 60} minutos. Aguardando a nuvem concluir.")
        return

    log("Acionando GitHub Actions na nuvem para apurar e publicar imediatamente...")
    disparar_nuvem()


if __name__ == "__main__":
    main()
