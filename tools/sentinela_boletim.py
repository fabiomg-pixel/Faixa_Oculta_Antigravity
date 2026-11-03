#!/usr/bin/env python3
"""Sentinela da Faixa Oculta / Radar Cultural.

Regra de ouro: A prioridade é rodar por aqui (localmente no Mac). Se atrasar, roda online.
Executado via launchd no macOS sempre que o computador estiver ativo ou ao abrir a tampa.

Fluxo:
1. Verifica se a edição esperada do turno atual já está publicada no ar (GitHub Pages).
2. Se já estiver no ar: apenas sincroniza a pasta local do repositório (git pull) e encerra.
3. Se NÃO estiver no ar:
   - Prioridade 1: Executa a apuração e geração LOCALMENTE no Mac com Python e Gemini.
   - Monta o site, commita e faz o push para o GitHub Pages.
   - Se a execução local concluir com sucesso, tudo resolvido diretamente pelo computador!
   - Se houver falha local (ex: sem conexão de rede momentânea no Mac):
     - Prioridade 2 (salvaguarda): Aciona o GitHub Actions para rodar online.
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
COOLDOWN_SEGUNDOS = 600  # 10 minutos de intervalo entre tentativas locais
REPO = "fabiomg-pixel/Faixa_Oculta_Antigravity"
WORKFLOW = "atualizar_radar.yml"
SITE_JSON = "https://fabiomg-pixel.github.io/Faixa_Oculta_Antigravity/data/revista.json"

WORKSPACE_DIR = os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-fabiomg@biof.ufrj.br/Meu Drive/Antigravity/Radar Cultural"
)

PYTHON_BIN = "/usr/local/bin/python3"
if not os.path.exists(PYTHON_BIN):
    PYTHON_BIN = sys.executable

GH_BIN = "/opt/homebrew/bin/gh"
if not os.path.exists(GH_BIN):
    GH_BIN = "/usr/local/bin/gh"

GIT_BIN = "/usr/bin/git"


def obter_chave_gemini():
    """Carrega chave do ambiente ou dos arquivos protegidos ~/.faixaoculta/.env ou ~/.env."""
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ.get("GEMINI_API_KEY")
    for env_file in [os.path.expanduser("~/.faixaoculta/.env"), os.path.expanduser("~/.env")]:
        if os.path.exists(env_file):
            try:
                with open(env_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("GEMINI_API_KEY="):
                            return line.split("=", 1)[1].strip().strip('"').strip("'")
            except Exception:
                pass
    return None


def log(msg):
    agora_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{agora_str}] [Sentinela Local] {msg}", flush=True)


def obter_turno_esperado():
    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    data_iso = agora.strftime("%Y-%m-%d")
    hora = agora.hour

    # Janela da manhã: verifica a partir das 05h00 até 16h59
    if 5 <= hora < 17:
        return data_iso, "manha"

    # Janela da noite: verifica a partir das 17h00 até 23h59
    if hora >= 17:
        return f"{data_iso}-noite", "noite"

    # Madrugada antes das 05h00: turno da noite anterior
    ontem = (agora - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    return f"{ontem}-noite", "noite"


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
        local_path = os.path.join(WORKSPACE_DIR, "data/revista.json")
        if os.path.exists(local_path):
            try:
                with open(local_path, "r", encoding="utf-8") as f:
                    local_dados = json.load(f)
                return doc_id in local_dados.get("dias", {})
            except Exception:
                pass
        return False


def sincronizar_repositorio_local():
    """Mantém a pasta local no Google Drive sincronizada com a nuvem."""
    if not os.path.exists(WORKSPACE_DIR):
        return
    try:
        subprocess.run([GIT_BIN, "-C", WORKSPACE_DIR, "pull", "--ff-only"], capture_output=True, timeout=20)
    except Exception:
        pass


def ja_executado_recentemente():
    if not os.path.exists(LOCK_FILE):
        return False
    try:
        mtime = os.path.getmtime(LOCK_FILE)
        if time.time() - mtime < COOLDOWN_SEGUNDOS:
            return True
    except Exception:
        pass
    return False


def marcar_execucao():
    try:
        with open(LOCK_FILE, "w") as f:
            f.write(str(time.time()))
    except Exception:
        pass


def executar_localmente(turno):
    """Executa a apuração e publicação localmente no Mac (Prioridade 1 - 'por aqui')."""
    if not os.path.exists(WORKSPACE_DIR):
        log(f"Erro: diretório do projeto não encontrado em {WORKSPACE_DIR}")
        return False

    log(f"Iniciando apuração editorial no Mac ({turno})...")
    marcar_execucao()

    # 1. Sincroniza antes de começar
    sincronizar_repositorio_local()

    # 2. Executa o orquestrador local
    env = os.environ.copy()
    chave = obter_chave_gemini()
    if chave:
        env["GEMINI_API_KEY"] = chave
    env["ROTINA_SOLICITADA"] = "auto"

    script = os.path.join(WORKSPACE_DIR, "tools/orquestrador_nuvem.py")
    cmd = [PYTHON_BIN, script]

    log(f"Executando comando local: {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=WORKSPACE_DIR, env=env, capture_output=True, text=True, timeout=300)
    if res.returncode != 0:
        log(f"Erro na execução local: {res.stderr.strip() or res.stdout.strip()}")
        return False

    log("Orquestrador local concluiu com sucesso! Commitando e publicando no GitHub Pages...")

    # 3. Git add, commit e push
    subprocess.run([GIT_BIN, "-C", WORKSPACE_DIR, "add", "data/revista.json", "index.html", "pagina.html", "audios/", "capas/"], check=False)
    subprocess.run(
        [GIT_BIN, "-C", WORKSPACE_DIR, "commit", "-m", f"Atualização editorial executada localmente no Mac ({turno}) [skip ci]"],
        check=False
    )
    push_res = subprocess.run([GIT_BIN, "-C", WORKSPACE_DIR, "push", "origin", "main"], capture_output=True, text=True, timeout=40)
    if push_res.returncode == 0:
        log("SUCESSO: Apuração gerada localmente e enviada ao GitHub Pages com sucesso!")
        return True
    else:
        log(f"Aviso no git push: {push_res.stderr.strip()}")
        return False


def disparar_nuvem():
    """Aciona o GitHub Actions na nuvem (Prioridade 2 - 'se atrasar, roda online')."""
    if not os.path.exists(GH_BIN):
        log(f"Erro: binário gh não encontrado em {GH_BIN}.")
        return False

    cmd = [GH_BIN, "workflow", "run", WORKFLOW, "--repo", REPO]
    log(f"Executando disparo na nuvem: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if res.returncode == 0:
        log(f"Sucesso: GitHub Actions disparado na nuvem! Saída: {res.stdout.strip()}")
        marcar_execucao()
        return True
    else:
        log(f"Falha ao disparar GitHub Actions: {res.stderr.strip()}")
        return False


def main():
    doc_id, turno = obter_turno_esperado()
    log(f"Checagem do sentinela: turno atual [{doc_id}] ({turno})...")

    if verificar_site_publicado(doc_id):
        log(f"OK: Edição [{doc_id}] já está publicada e acessível no ar. Nada a fazer.")
        sincronizar_repositorio_local()
        return

    log(f"Edição [{doc_id}] ainda NÃO está no ar.")

    if ja_executado_recentemente():
        log(f"Execução já solicitada recentemente (cooldown de {COOLDOWN_SEGUNDOS // 60}m). Aguardando conclusão.")
        return

    # Prioridade 1: Roda por aqui (Localmente no Mac)
    log(">> PRIORIDADE 1: Executando apuração por aqui (localmente no Mac)...")
    sucesso_local = executar_localmente(turno)
    if sucesso_local:
        return

    # Prioridade 2: Se falhar localmente ou atrasar, aciona online
    log(">> PRIORIDADE 2: Execução local indisponível. Acionando GitHub Actions online como salvaguarda...")
    disparar_nuvem()


if __name__ == "__main__":
    main()
