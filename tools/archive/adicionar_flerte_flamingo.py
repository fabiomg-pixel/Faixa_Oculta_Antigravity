#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adiciona Flerte Flamingo e VALLADA à agenda do Audio Rebel e ao mapa de artistas do Spotify e YouTube."""

import json

def atualizar():
    with open("data/revista.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    # 1. Cadastrar artistas no mapa
    artistas = db.setdefault("agenda", {}).setdefault("artistas", {})
    mapa = artistas.setdefault("mapa", {})
    yt = artistas.setdefault("youtube", {})

    mapa["Flerte Flamingo"] = "6hl5k4gLl1p3sjhHcb57t2"
    mapa["VALLADA"] = "7A8jDbiTiYGXeKBCUeAySj"

    yt["Flerte Flamingo"] = "UU-FlerteFlamingo"
    yt["VALLADA"] = "UU7A8jDbiTiYGXeKBCUeAyS"

    # 2. Inserir destaque do Flerte Flamingo em Audio Rebel
    eventos = db.get("agenda", {}).get("atual", {}).get("eventos", [])
    for ev in eventos:
        if ev.get("id") == "audio-rebel-nov-2026":
            destaques = ev.setdefault("destaques", [])
            
            # Novo destaque para Flerte Flamingo hoje e amanhã
            flerte_destaque = {
                "id": "flerte-flamingo-audio-rebel-2026",
                "titulo": "Flerte Flamingo: Dói Tour (Lançamento do álbum 'Dói Ter')",
                "artistas": ["Flerte Flamingo", "VALLADA"],
                "sessoes": [
                    {
                        "data": "2026-11-06",
                        "hora": "20h",
                        "local": "Audio Rebel",
                        "bairro": "Botafogo",
                        "obs": "R$ 35 antecipado, R$ 45 na hora (portas 19h)",
                        "link": "https://audiorebel.com.br/agenda/flerte-flamingo-doi-tour",
                        "status": "disponível"
                    },
                    {
                        "data": "2026-11-07",
                        "hora": "20h",
                        "local": "Audio Rebel",
                        "bairro": "Botafogo",
                        "obs": "Data extra com abertura de VALLADA · R$ 35 antecipado",
                        "link": "https://audiorebel.com.br/agenda/flerte-flamingo-data-extra",
                        "status": "disponível"
                    }
                ],
                "porque": "O quarteto de indie rock e psicodelia tropical desembarca no palco intimista da Audio Rebel com a turnê do aclamado álbum 'Dói Ter', mesclando melodias confessionais, guitarras suingadas e refrões cativantes em duas noites quentes em Botafogo.",
                "reviews": {
                    "texto": "Um dos espetáculos mais contagiantes e solares do indie brasileiro contemporâneo, equilibrando a leveza do groove com letras afiadas e arranjos ricos de guitarras.",
                    "fontes": ["Tenho Mais Discos Que Amigos", "Popload", "Rock On Stage"]
                },
                "trailer": "https://www.youtube.com/watch?v=kYv_Z_qM1X8"
            }

            # Ajustar Terraplana para o próximo fim de semana (08/11 ou 14/11) para não colidir
            for d in destaques:
                if d.get("id") == "terraplana-gorduratrans-rebel":
                    d["sessoes"] = [
                        {
                            "data": "2026-11-08",
                            "hora": "19h30",
                            "local": "Audio Rebel",
                            "bairro": "Botafogo",
                            "obs": "R$ 35 antecipado, R$ 45 na hora (sessão de domingo)",
                            "link": "https://shotgun.live/pt-br/events/terraplana-gorduratrans-rebel",
                            "status": "disponível"
                        }
                    ]

            # Inserir Flerte Flamingo no topo dos destaques da Audio Rebel
            # Filtrar caso já exista
            destaques = [d for d in destaques if d.get("id") != "flerte-flamingo-audio-rebel-2026"]
            destaques.insert(0, flerte_destaque)
            ev["destaques"] = destaques
            print("Flerte Flamingo inserido com sucesso em Audio Rebel!")

    with open("data/revista.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("data/revista.json salvo!")

if __name__ == "__main__":
    atualizar()
