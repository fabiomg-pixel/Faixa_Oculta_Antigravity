#!/usr/bin/env python3
"""Orquestrador na nuvem da Faixa Oculta.

Gerencia os ciclos editoriais solicitados via GitHub Actions:
- Boletim Diário (Manhã e Noite - Todos os dias)
- Revista da Semana (Quinta-feira à noite - 20h00 BRT)
- Revista de Cultura (Música, Filmes e Livros - Todo dia 01)
"""

import os
import sys
import datetime
import subprocess

def log(msg):
    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    print(f"[{agora.strftime('%Y-%m-%d %H:%M:%S BRT')}] [Orquestrador] {msg}", flush=True)

def executar_script(script_path, extra_args=None):
    cmd = [sys.executable, script_path] + (extra_args or [])
    log(f"--- Executando: {' '.join(cmd)} ---")
    res = subprocess.run(cmd, check=False)
    if res.returncode != 0:
        log(f"Aviso: {script_path} finalizou com código {res.returncode}")
        return False
    log(f"--- Concluído com sucesso: {script_path} ---")
    return True

def main():
    rotina = os.environ.get("ROTINA_SOLICITADA", "auto").strip().lower()
    extra_args = [a for a in sys.argv[1:] if a.startswith("--")]
    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    dia_semana = agora.weekday()  # Segunda=0, Terça=1, Quarta=2, Quinta=3, Sexta=4, Sábado=5, Domingo=6
    dia_mes = agora.day
    hora = agora.hour

    log(f"Iniciando orquestração. Modo: '{rotina}'. Horário local: {agora.strftime('%A, %d/%m/%Y %H:%M')}")

    if rotina == "boletim":
        executar_script("tools/boletim_nuvem.py", extra_args)
        executar_script("tools/gerar_audio_boletim.py", extra_args)
    elif rotina == "revista_semana":
        executar_script("tools/revista_semanal.py", extra_args)
    elif rotina == "cultura_mensal":
        executar_script("tools/cultura_mensal.py", extra_args)
    elif rotina == "tudo":
        executar_script("tools/boletim_nuvem.py", extra_args)
        executar_script("tools/gerar_audio_boletim.py", extra_args)
        executar_script("tools/revista_semanal.py", extra_args)
        executar_script("tools/cultura_mensal.py", extra_args)
    elif rotina == "auto":
        # 1. Boletim Diário roda em todas as chamadas
        executar_script("tools/boletim_nuvem.py", extra_args)
        executar_script("tools/gerar_audio_boletim.py", extra_args)

        # 2. Revista da Semana: Quinta-feira a partir das 18h BRT
        if dia_semana == 3 and hora >= 18:
            log("Quinta-feira à noite detectada: compilando Revista Semanal ampliada...")
            executar_script("tools/revista_semanal.py", extra_args)

        # 3. Cultura do Mês: Todo dia 01
        if dia_mes == 1:
            log("Dia 01 do mês detectado: atualizando edições de Música, Filmes e Livros...")
            executar_script("tools/cultura_mensal.py", extra_args)
    else:
        log(f"Rotina desconhecida: '{rotina}'. Executando boletim diário padrão.")
        executar_script("tools/boletim_nuvem.py", extra_args)

if __name__ == "__main__":
    main()
