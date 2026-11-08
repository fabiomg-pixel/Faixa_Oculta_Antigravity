#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Orquestrador Central de Atualizações da Faixa Oculta (Local & Nuvem).

Coordena na ordem correta todas as rotinas automatizadas:
1. Boletim Diário (Manhã e Noite — Todos os dias via tools/boletim_nuvem.py)
2. Jornais do Dia no Modo Leitor (via tools/processar_jornais_beeper.py --perfil diario)
3. Boletim em Áudio Integral (via tools/gerar_audio_boletim.py)
4. Revista da Semana (Quintas-feiras à noite >= 18h BRT ou Sextas pela manhã)
5. Cultura Mensal: Música, Cinema, Livros e Agenda Rio (Dia 01 de cada mês)
6. Playlists da Agenda Cultural do Rio (Segundas-feiras e Dia 01)
"""

import os
import sys
import json
import datetime
import subprocess


def rodar_script(caminho_script, args=None):
    cmd = [sys.executable, caminho_script] + (args or [])
    print(f"\n>>> Executando: {' '.join(cmd)}")
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print(f"Aviso: {caminho_script} retornou código {res.returncode}")
    return res.returncode == 0


def main():
    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    data_iso = agora.strftime("%Y-%m-%d")
    mes_iso = agora.strftime("%Y-%m")
    dia_semana = agora.weekday()  # 0=Seg, 1=Ter, 2=Qua, 3=Qui, 4=Sex, 5=Sáb, 6=Dom
    dia_mes = agora.day
    hora = agora.hour

    forcar = os.environ.get("FORCAR_EXECUCAO", "").strip().lower() in ("1", "true", "sim") or "--forcar" in sys.argv
    extra_args = ["--forcar"] if forcar else []

    print("=================================================================")
    print(f" ORQUESTRADOR FAIXA OCULTA · {data_iso} ({agora.strftime('%H:%M')} BRT)")
    print(f" Dia da semana: {dia_semana} | Dia do mês: {dia_mes} | Forçar: {forcar}")
    print("=================================================================")

    # 1. BOLETIM DIÁRIO (Roda sempre: manhã e noite)
    print("\n[1/6] Verificando Boletim Diário (Notícias Clássicas Nacionais + Internacionais)...")
    rodar_script("tools/boletim_nuvem.py", extra_args)

    # 2. JORNAIS DO DIA NO MODO LEITOR (Roda APÓS o boletim para injetar destaques, editoriais e reportagens na edição criada)
    print("\n[2/6] Processando Jornais do Dia para o Modo Leitor (Beeper / Curadoria)...")
    rodar_script("tools/processar_jornais_beeper.py", ["--perfil", "diario", "--pages", "15"])

    # 3. ÁUDIO DO BOLETIM DIÁRIO (Gera narração em áudio da edição integral do turno atual)
    print("\n[3/8] Gerando/Verificando Áudio Narrado do Boletim Diário...")
    turno_id = data_iso if hora < 17 else f"{data_iso}-noite"
    rodar_script("tools/gerar_audio_boletim.py", ["--dia", turno_id] + extra_args)

    # Carregar banco para verificar se edições semanais/mensais já constam
    try:
        with open("data/revista.json", "r", encoding="utf-8") as f:
            db = json.load(f)
    except Exception as e:
        print(f"Erro ao ler data/revista.json: {e}")
        sys.exit(1)

    # 4. REVISTA DA SEMANA (Quinta à noite >= 18h ou Sexta-feira)
    eh_janela_semanal = (dia_semana == 3 and hora >= 18) or (dia_semana == 4)
    if eh_janela_semanal or forcar:
        print("\n[4/8] Janela da Revista da Semana ativa! Processando revistas semanais e compilação...")
        rodar_script("tools/processar_jornais_beeper.py", ["--perfil", "semana", "--pages", "12"])
        rodar_script("tools/revista_semanal.py", extra_args)
    else:
        print("\n[4/8] Revista da Semana: fora da janela de quinta à noite / sexta (mantendo edição atual).")

    # 5. CULTURA MENSAL (Todo dia 01 do mês ou se o mês atual ainda não existir em edicoes)
    falta_mes_atual = mes_iso not in db.get("edicoes", {})
    if dia_mes == 1 or falta_mes_atual:
        print(f"\n[5/8] Janela da Cultura Mensal ({mes_iso}) ativa! Verificando safra de Música, Cinema, Livros e Agenda...")
        rodar_script("tools/processar_jornais_beeper.py", ["--perfil", "cultura", "--pages", "12"])
        rodar_script("tools/cultura_mensal.py", extra_args)
    else:
        print(f"\n[5/8] Cultura Mensal ({mes_iso}): edição do mês já publicada e íntegra.")

    # 6. PLAYLISTS DA AGENDA DO RIO (Início da semana [segunda-feira] e início do mês [dia 01])
    if dia_semana == 0 or dia_mes == 1 or forcar:
        print("\n[6/8] Atualizando Playlists da Agenda Cultural do Rio (cadência oficial de início de semana/mês)...")
        modo_pl = "forcar" if forcar else "auto"
        rodar_script("tools/atualizar_playlists_agenda.py", ["--modo", modo_pl])
    else:
        print("\n[6/8] Playlists da Agenda: mantendo playlists da semana e do mês atuais.")

    # 7. PARTICIONAMENTO DE DADOS V2 (Gera data/boot.json ~145 KB + shards em data/dias, data/semanas e data/cultura)
    print("\n[7/8] Gerando Manifesto de Boot Rápido (data/boot.json) e Shards da Arquitetura v2...")
    rodar_script("tools/particionar_dados_v2.py")

    # 8. QUALITY GATE PRÉ-PUBLICAÇÃO (Valida 100% dos critérios editoriais)
    print("\n[8/8] Executando Quality Gate Pré-Publicação (tools/validar_edicao.py)...")
    rodar_script("tools/validar_edicao.py")

    # Sincronização final garantida de index.html a partir de pagina.html
    try:
        with open("pagina.html", "r", encoding="utf-8") as f:
            src = f.read()
        skeleton_head = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
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
            if src.lstrip().lower().startswith("<!doctype"):
                f.write(src)
            else:
                f.write(skeleton_head + src + skeleton_tail)
    except Exception as e:
        print(f"Aviso ao sincronizar index.html: {e}")

    print("\n=================================================================")
    print(" ORQUESTRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=================================================================")


if __name__ == "__main__":
    main()
