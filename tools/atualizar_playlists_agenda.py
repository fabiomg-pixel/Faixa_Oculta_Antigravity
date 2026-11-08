#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atualizador e Gerador de Playlists da Agenda Cultural (Faixa Oculta / Radar Rio).

Cadência Oficial:
- Início da semana (segunda-feira): atualiza a playlist 'semana' (shows dos próximos 7 dias).
- Início do mês (dia 01): atualiza a playlist 'trinta' (shows dos próximos 30 dias / mês).
- As playlists do período anterior são arquivadas automaticamente em 'anteriores'.
- Mantém o histórico, artistas mapeados e observações curatoriais.

Uso:
  python3 tools/atualizar_playlists_agenda.py [--modo {auto,semana,mensal,forcar}]
"""

import argparse
import datetime
import json
import os
import sys

REVISTA_JSON = "data/revista.json"

MESES_PT = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}


def obter_agora():
    # Fuso horário oficial do Brasil (BRT: UTC-3)
    tz = datetime.timezone(datetime.timedelta(hours=-3))
    return datetime.datetime.now(tz)


def carregar_dados():
    if not os.path.exists(REVISTA_JSON):
        raise FileNotFoundError(f"Arquivo {REVISTA_JSON} não encontrado.")
    with open(REVISTA_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(REVISTA_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    print(f"[{obter_agora().strftime('%Y-%m-%d %H:%M:%S')}] {REVISTA_JSON} atualizado com sucesso!")


def extrair_artistas_periodo(eventos, dt_inicio, dt_fim):
    """Extrai os artistas que possuem sessões ou shows marcados entre dt_inicio e dt_fim."""
    artistas = []
    vistos = set()

    for ev in eventos:
        # 1. Checa os destaques do evento
        for pick in ev.get("destaques", []):
            pick_artistas = [str(a).strip() for a in pick.get("artistas") or [] if str(a).strip()]
            match = False
            for s in pick.get("sessoes", []):
                s_data = s.get("data")
                if s_data:
                    try:
                        s_dt = datetime.date.fromisoformat(s_data)
                        if dt_inicio <= s_dt <= dt_fim:
                            match = True
                            break
                    except Exception:
                        pass
            if match:
                for a in pick_artistas:
                    if a not in vistos:
                        vistos.add(a)
                        artistas.append(a)

        # 2. Checa as sessões em 'dias'
        for dia in ev.get("dias", []):
            d_data = dia.get("data")
            if d_data:
                try:
                    d_dt = datetime.date.fromisoformat(d_data)
                    if dt_inicio <= d_dt <= dt_fim:
                        for a in dia.get("artistas") or []:
                            a_str = str(a).strip()
                            if a_str and a_str not in vistos:
                                vistos.add(a_str)
                                artistas.append(a_str)
                except Exception:
                    pass

        # 3. Se for evento guarda-chuva no intervalo com artistas no topo
        ev_datas = []
        for s in ev.get("dias", []):
            if s.get("data"):
                try:
                    ev_datas.append(datetime.date.fromisoformat(s["data"]))
                except Exception:
                    pass
        for pick in ev.get("destaques", []):
            for s in pick.get("sessoes", []):
                if s.get("data"):
                    try:
                        ev_datas.append(datetime.date.fromisoformat(s["data"]))
                    except Exception:
                        pass
        if any(dt_inicio <= d <= dt_fim for d in ev_datas):
            for a in ev.get("artistas") or []:
                a_str = str(a).strip()
                if a_str and a_str not in vistos:
                    vistos.add(a_str)
                    artistas.append(a_str)

    return artistas


def arquivar_se_necessario(anteriores, pl_atual, chave_tipo):
    """Arquiva uma playlist em 'anteriores' se ela já não estiver registrada."""
    if not pl_atual or not isinstance(pl_atual, dict):
        return
    url = pl_atual.get("url")
    nome = pl_atual.get("nome")
    if not url or not nome:
        return

    # Verifica se já existe em anteriores com mesmo nome ou mesma url
    ja_existe = any(
        ant.get("url") == url and ant.get("nome") == nome
        for ant in anteriores if isinstance(ant, dict)
    )
    if not ja_existe:
        anteriores.append({
            "nome": nome,
            "url": url
        })
        print(f"Playlist arquivada em 'anteriores': {nome} ({url})")


def calcular_intervalo_semana(agora):
    """Calcula a janela da semana.
    Se for domingo (weekday 6), abrange de hoje até o próximo domingo (8 dias)
    para contemplar os shows deste domingo e da semana inteira.
    Se for segunda (weekday 0) ou outro dia da semana, vai da segunda ao domingo seguinte.
    """
    hoje = agora.date()
    if hoje.weekday() == 6:  # Domingo
        dt_inicio = hoje
        dt_fim = hoje + datetime.timedelta(days=7)
    else:
        # Segunda-feira da semana atual
        dt_inicio = hoje - datetime.timedelta(days=hoje.weekday())
        dt_fim = dt_inicio + datetime.timedelta(days=6)
    return dt_inicio, dt_fim


def calcular_intervalo_trinta(agora):
    """Calcula a janela mensal / 30 dias a partir do início do mês ou de hoje."""
    hoje = agora.date()
    # Primeiro dia do mês atual
    dt_inicio = datetime.date(hoje.year, hoje.month, 1)
    # Fim do mês atual
    if hoje.month == 12:
        ultimo_dia = datetime.date(hoje.year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        ultimo_dia = datetime.date(hoje.year, hoje.month + 1, 1) - datetime.timedelta(days=1)
    dt_fim = ultimo_dia
    return dt_inicio, dt_fim


def precisa_atualizar_semana(semana_atual, dt_inicio, dt_fim):
    """Verifica se a playlist semanal está defasada ou expirada."""
    if not semana_atual or not isinstance(semana_atual, dict):
        return True
    intervalo = semana_atual.get("intervalo", "")
    if not intervalo or " a " not in intervalo:
        return True
    try:
        fim_str = intervalo.split(" a ")[1].strip()
        fim_dt = datetime.date.fromisoformat(fim_str)
        # Se a data de fim do intervalo já passou em relação à data inicial esperada
        if fim_dt < dt_inicio:
            return True
    except Exception:
        return True
    return False


def precisa_atualizar_trinta(trinta_atual, dt_inicio, dt_fim):
    """Verifica se a playlist mensal/30 dias está defasada."""
    if not trinta_atual or not isinstance(trinta_atual, dict):
        return True
    intervalo = trinta_atual.get("intervalo", "")
    if not intervalo or " a " not in intervalo:
        return True
    try:
        fim_str = intervalo.split(" a ")[1].strip()
        fim_dt = datetime.date.fromisoformat(fim_str)
        if fim_dt < dt_inicio:
            return True
    except Exception:
        return True
    return False


def executar_atualizacao(modo="auto"):
    dados = carregar_dados()
    ag = dados.setdefault("agenda", {}).setdefault("atual", {})
    eventos = ag.get("eventos", [])

    playlists = ag.setdefault("playlists", {})
    anteriores = playlists.setdefault("anteriores", [])
    semana_atual = playlists.get("semana", {})
    trinta_atual = playlists.get("trinta", {})

    agora = obter_agora()
    dt_sem_inicio, dt_sem_fim = calcular_intervalo_semana(agora)
    dt_tri_inicio, dt_tri_fim = calcular_intervalo_trinta(agora)

    atualizou_semana = False
    atualizou_trinta = False

    # Condições para semana:
    # modo == forcar, modo == semana, ou hoje é segunda (weekday 0), ou hoje é domingo à noite,
    # ou o intervalo anterior já expirou.
    expirou_semana = precisa_atualizar_semana(semana_atual, dt_sem_inicio, dt_sem_fim)
    deve_atualizar_semana = (
        modo in ("forcar", "semana") or
        expirou_semana or
        (agora.date().weekday() == 0 and agora.hour >= 5)
    )

    # Condições para mensal/30 dias:
    # modo == forcar, modo == mensal, ou hoje é dia 01 do mês, ou expirou.
    expirou_trinta = precisa_atualizar_trinta(trinta_atual, dt_tri_inicio, dt_tri_fim)
    deve_atualizar_trinta = (
        modo in ("forcar", "mensal") or
        expirou_trinta or
        (agora.date().day == 1 and agora.hour >= 5)
    )

    if deve_atualizar_semana:
        print(f"Atualizando playlist SEMANAL ({dt_sem_inicio.strftime('%d/%m')} a {dt_sem_fim.strftime('%d/%m')})...")
        artistas_semana = extrair_artistas_periodo(eventos, dt_sem_inicio, dt_sem_fim)

        # Se houver versão anterior defasada, arquiva
        if semana_atual and semana_atual.get("intervalo") != f"{dt_sem_inicio.isoformat()} a {dt_sem_fim.isoformat()}":
            arquivar_se_necessario(anteriores, semana_atual, "semana")

        nome_semana = f"Radar Rio {dt_sem_inicio.strftime('%d/%m')} a {dt_sem_fim.strftime('%d/%m')}"
        nome_pedido = f"Radar — Esta semana ({dt_sem_inicio.strftime('%d/%m')} a {dt_sem_fim.strftime('%d/%m')})"

        # Preserva URL da playlist do Spotify existente ou canal
        url_spotify = semana_atual.get("url") if semana_atual else None
        if not url_spotify:
            url_spotify = "https://open.spotify.com/playlist/06GrfoezeKegLWspFf4XpU"

        playlists["semana"] = {
            "artistas": artistas_semana,
            "intervalo": f"{dt_sem_inicio.isoformat()} a {dt_sem_fim.isoformat()}",
            "nome": nome_semana,
            "nomePedido": nome_pedido,
            "obs": f"Shows em Botafogo, Lapa, Tijuca e Centro reunindo {len(artistas_semana)} atrações da semana.",
            "url": url_spotify,
            "url_yt": f"https://music.youtube.com/search?q={nome_semana.replace(' ', '+')}"
        }
        atualizou_semana = True

    if deve_atualizar_trinta:
        nome_mes = MESES_PT.get(dt_tri_inicio.month, "")
        print(f"Atualizando playlist MENSAL ({nome_mes} {dt_tri_inicio.year})...")
        artistas_trinta = extrair_artistas_periodo(eventos, dt_tri_inicio, dt_tri_fim)

        # Se houver versão anterior defasada, arquiva
        if trinta_atual and trinta_atual.get("intervalo") != f"{dt_tri_inicio.isoformat()} a {dt_tri_fim.isoformat()}":
            arquivar_se_necessario(anteriores, trinta_atual, "trinta")

        nome_trinta = f"Radar Próximos 30 Dias ({nome_mes} {dt_tri_inicio.year})"
        nome_pedido = f"Radar — Próximos 30 dias ({nome_mes} {dt_tri_inicio.year})"

        url_spotify_30 = trinta_atual.get("url") if trinta_atual else None
        if not url_spotify_30:
            url_spotify_30 = "https://open.spotify.com/playlist/3Sns4qN1JetINCJmplCljB"

        playlists["trinta"] = {
            "artistas": artistas_trinta,
            "intervalo": f"{dt_tri_inicio.isoformat()} a {dt_tri_fim.isoformat()}",
            "nome": nome_trinta,
            "nomePedido": nome_pedido,
            "obs": f"Panorama completo do mês de {nome_mes} no Rio com {len(artistas_trinta)} bandas e artistas.",
            "url": url_spotify_30,
            "url_yt": f"https://music.youtube.com/search?q={nome_trinta.replace(' ', '+')}"
        }
        atualizou_trinta = True

    if atualizou_semana or atualizou_trinta:
        playlists["em"] = agora.strftime("%Y-%m-%dT%H:%M:%S-03:00")
        total_sem = len(playlists.get("semana", {}).get("artistas", []))
        total_tri = len(playlists.get("trinta", {}).get("artistas", []))
        nome_mes = MESES_PT.get(dt_tri_inicio.month, "")
        playlists["obs"] = (
            f"Edição de {nome_mes} {dt_tri_inicio.year}: {total_tri} bandas em pequenas casas e palcos do Rio "
            f"(Audio Rebel, Saloon 79, Estúdio Hanoi, Garage Grindhouse, Circo Voador). "
            f"Playlist semanal com {total_sem} atrações no período {dt_sem_inicio.strftime('%d/%m')} a {dt_sem_fim.strftime('%d/%m')}. "
            f"Atualização periódica programada para início da semana (semanal) e início do mês (mensal)."
        )
        salvar_dados(dados)
        print("Playlists sincronizadas com sucesso!")
    else:
        print("Playlists já estão dentro da vigência atual. Nenhuma atualização necessária.")


def main():
    parser = argparse.ArgumentParser(description="Atualiza playlists da agenda do Radar Rio")
    parser.add_argument("--modo", choices=["auto", "semana", "mensal", "forcar"], default="auto",
                        help="Modo de execução: auto (verifica cadência), semana (força semanal), mensal (força mensal), forcar (força ambos)")
    args = parser.parse_args()
    executar_atualizacao(args.modo)


if __name__ == "__main__":
    main()
