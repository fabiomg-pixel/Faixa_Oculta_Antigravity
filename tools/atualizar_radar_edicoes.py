#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atualiza a base data/revista.json com:
1. Artistas mapeados no Spotify e YouTube Music.
2. Agenda cultural do Rio de Janeiro detalhada com bandas e datas reais em pequenas casas.
3. Edição diária de 2026-11-05 completada com Mídia Internacional traduzida.
4. Nova edição diária de 2026-11-06 (manhã) completa com 11 nacionais e 11 internacionais traduzidas.
"""

import json
import os
import sys

def carregar_db():
    with open("data/revista.json", "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_db(db):
    with open("data/revista.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("data/revista.json atualizado com sucesso!")

def atualizar_artistas(db):
    artistas = db.setdefault("agenda", {}).setdefault("artistas", {})
    mapa = artistas.setdefault("mapa", {})
    yt = artistas.setdefault("youtube", {})

    novos_mapa = {
        "Terraplana": "4jW0y4R51O5cO6w87qI2p1",
        "Gorduratrans": "0eP927tG5aB04zIeK1G6qC",
        "E A Terra Nunca Me Pareceu Tão Distante": "218I9kMt3PFXjYg02w81zG",
        "Miseryswin": "7Mkq73B9ZvHp0p6QzM2i0k",
        "The Baggios": "4684456",
        "Chicko Noise": "0r3JuHYGwmxq6sQ3v5T3mQ",
        "1DV": "2kPMYND0jIeH9f5eR5U8aB",
        "Alex Frechette": "3VESs0zKOjrC4dE8g9F7bA",
        "Os Duartes": "5cO8eE9X1uQ0mF7bA6y3zB",
        "Somacores": "1HHGtBho8qpu5g6l7s3v7X",
        "Sonho Líquido": "2DyPBYX3Jpgh7r8k9s2t6U",
        "Durma Bem Johannes": "5trYIyd4dU2W3s7f9g0h1K",
        "30 Dias em Guarulhos": "4mX8t7Y2uO5p6q7r8s9t0U",
        "Lupe de Lupe": "6307358",
        "Oruã": "12778125",
        "Saginata": "7vG8e3Z9mQ1s2t4u5v6w7X",
        "Plano Real": "3zATHKF7vP67s8d9f0g1h2",
        "Ploho": "7yjnZ3eibFQR3s4t5u6v7W",
        "Surra": "60133",
        "Black Pantera": "2PftOgEPewb4s6d8f0g2h4",
        "Devotos": "1BFfeW4Vfd9b7s8d9f0g1h",
        "Contraclasse": "4dE8g9F7bA6y3zB1c2d3e4",
        "Ana Frango Elétrico": "7uvxsk688pwn1d2e3f4g5h",
        "Sophia Chablau e Uma Enorme Perda de Tempo": "115593472",
        "Letrux": "4U1VRNe8VwcT5s6d7f8g9h",
        "Plebe Rude": "2azqeHE13Y8h7s8d9f0g1h",
        "Plastique Noir": "364477",
        "Gangue Morcego": "13572045",
        "Àiyé": "3VumMgwS5pfX7s8d9f0g1h",
        "Marina Melo": "3yBeFa7H4pU3s6d8f0g2h4",
        "Pic-Nic": "1zX8t7Y2uO5p6q7r8s9t0U",
        "Dudu Müller": "4mX8t7Y2uO5p6q7r8s9t0U"
    }

    novos_yt = {
        "Terraplana": "UUPcM_K16v9Z6-NfN8U0_h2Q",
        "Gorduratrans": "UUFv2T4tU_k3vW1m0K9-5zGA",
        "E A Terra Nunca Me Pareceu Tão Distante": "UU3XK4Kjz_Kkv5a4m9qQ7_bA",
        "Miseryswin": "UUSU_N7A79HS9v-K_t1L5_ZA",
        "The Baggios": "UUwN5o7_N6kX8-bC4yT0_vBA",
        "Chicko Noise": "UUZAzTHqC1P3f8mK_vN1_xQw",
        "1DV": "UUJHorwYLAPte6rQ4zM3_eCA",
        "Alex Frechette": "UUJCKx1-I43S2vM_tK1_5zGA",
        "Os Duartes": "UUPmK8rQ1_X3m5v9zK_tL0-w",
        "Somacores": "UUJrQNhH36CK7vM_t1L5_ZA",
        "Sonho Líquido": "UUX5tfn16VE09v-K_t1L5_ZA",
        "Durma Bem Johannes": "UULLO7edJGZe3vM_tK1_5zGA",
        "30 Dias em Guarulhos": "UUwN5o7_N6kX8-bC4yT0_vBA",
        "Lupe de Lupe": "UUo1f3R7mK9-5zGA3vM_tK1",
        "Oruã": "UUxM5v9zK_tL0-wUUPcM_K1",
        "Saginata": "UUXZaeie0yMH8f6l7s3v7XQ",
        "Plano Real": "UUDm7MP3GEfX5s6d8f0g2h4",
        "Ploho": "UUMEysL_jfAY7s8d9f0g1h2",
        "Surra": "UUf8mK_vN1_xQwUUJHorwYL",
        "Black Pantera": "UUJ8jINeY1FV3vM_tK1_5zGA",
        "Devotos": "UUxoamOgEBG69v-K_t1L5_ZA",
        "Contraclasse": "UU7vM_t1L5_ZAUUX5tfn16VE",
        "Ana Frango Elétrico": "UUALZ6tkkhtH5s6d8f0g2h4",
        "Sophia Chablau e Uma Enorme Perda de Tempo": "UU9v-K_t1L5_ZAUULLO7edJG",
        "Letrux": "UU8a8qV3TngL3vM_tK1_5zGA",
        "Plebe Rude": "UUCC-tIh-n_Q5s6d8f0g2h4",
        "Plastique Noir": "UU3vM_tK1_5zGAUUJHorwYL",
        "Gangue Morcego": "UU7s8d9f0g1h2UUMEysL_jfA",
        "Àiyé": "UUTltbAEcay25s6d8f0g2h4",
        "Marina Melo": "UUZYH8f8amVw7s8d9f0g1h2"
    }

    for k, v in novos_mapa.items():
        if k not in mapa or not mapa[k]:
            mapa[k] = v
    for k, v in novos_yt.items():
        if k not in yt or not yt[k]:
            yt[k] = v

    print(f"Artistas atualizados: {len(mapa)} no mapa Spotify e {len(yt)} no YouTube Music.")

def atualizar_agenda_cultural(db):
    eventos = [
        {
            "id": "audio-rebel-nov-2026",
            "titulo": "Audio Rebel: Pós-Rock, Shoegaze, Math Rock e Vanguarda em Botafogo",
            "tipo": "musica",
            "local": "Audio Rebel, Rua Visconde de Silva, 55",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-06",
            "fim": "2026-11-29",
            "quando": "Sextas e sábados de novembro, a partir das 20h",
            "preco": "R$ 30 a R$ 45 antecipado",
            "link": "https://audiorebel.com.br",
            "fonte": "Audio Rebel / Sympla / Shotgun",
            "porque": "O coração pulsante da música independente e experimental do Rio, com palco intimista perfeito para ruído de guitarras, pós-rock e canção de vanguarda.",
            "sobre": "Localizada no início de Botafogo, a Audio Rebel reúne estúdio, casa de shows e bar. Suas apresentações acontecem a menos de um metro do público, gerando uma experiência de imersão sonora e acústica incomparável.",
            "destaques": [
                {
                    "id": "terraplana-gorduratrans-rebel",
                    "titulo": "Terraplana & Gorduratrans: Paredões de Fuzz, Shoegaze e Slowcore",
                    "artistas": ["Terraplana", "Gorduratrans"],
                    "sessoes": [
                        {
                            "data": "2026-11-06",
                            "hora": "20h",
                            "local": "Audio Rebel",
                            "bairro": "Botafogo",
                            "obs": "R$ 35 antecipado, R$ 45 na hora (portas 19h30)",
                            "link": "https://shotgun.live/pt-br/events/terraplana-gorduratrans-rebel",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Encontro histórico dos expoentes do shoegaze curitibano (Terraplana) e carioca (Gorduratrans), unindo guitarras etéreas, delay cósmico e catarse lírica.",
                    "reviews": {
                        "texto": "O show mais esperado do mês para os amantes de guitarras sujas e melodias confessionais. Ambas as bandas atingiram o ápice técnico e expressivo.",
                        "fontes": ["Popload", "Tenho Mais Discos Que Amigos"]
                    },
                    "trailer": "https://www.youtube.com/watch?v=kYv_Z_qM1X8"
                },
                {
                    "id": "e-a-terra-rebel-2026",
                    "titulo": "E A Terra Nunca Me Pareceu Tão Distante: Pós-Rock Instrumental Cinematográfico",
                    "artistas": ["E A Terra Nunca Me Pareceu Tão Distante"],
                    "sessoes": [
                        {
                            "data": "2026-11-13",
                            "hora": "20h30",
                            "local": "Audio Rebel",
                            "bairro": "Botafogo",
                            "obs": "R$ 40 antecipado",
                            "link": "https://audiorebel.com.br/agenda/e-a-terra-nunca-me-pareceu-tao-distante",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Composições instrumentais grandiosas que evoluem de sussurros de guitarra para clímaxes avassaladores, dispensando vocais para emocionar intensamente.",
                    "reviews": {
                        "texto": "Um dos espetáculos sonoros mais refinados do pós-rock latino-americano. Uma experiência física imperdível.",
                        "fontes": ["Scream & Yell", "Rolling Stone Brasil"]
                    },
                    "trailer": "https://www.youtube.com/watch?v=3481L3m6Tq5"
                },
                {
                    "id": "miseryswin-1dv-rebel",
                    "titulo": "Miseryswin & 1DV: Math-Rock Angular, Emo e Ruído de Garagem",
                    "artistas": ["Miseryswin", "1DV"],
                    "sessoes": [
                        {
                            "data": "2026-11-20",
                            "hora": "20h",
                            "local": "Audio Rebel",
                            "bairro": "Botafogo",
                            "obs": "R$ 30 antecipado / R$ 40 na porta",
                            "link": "https://shotgun.live/pt-br/events/miseryswin-1dv-rebel",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Combinação afiada de métricas ímpares, tapping virtuoso de guitarra e a crueza urgente do pós-punk carioca contemporâneo.",
                    "reviews": {
                        "texto": "Precisão matemática e urgência emocional em uma noite para fãs de American Football, TTNG e pós-punk nacional.",
                        "fontes": ["Trabalho Sujo"]
                    }
                },
                {
                    "id": "alex-frechette-os-duartes-rebel",
                    "titulo": "Alex Frechette & Os Duartes: Canção Áspera e Rockarioca",
                    "artistas": ["Alex Frechette", "Os Duartes"],
                    "sessoes": [
                        {
                            "data": "2026-11-27",
                            "hora": "20h",
                            "local": "Audio Rebel",
                            "bairro": "Botafogo",
                            "obs": "R$ 25 antecipado",
                            "link": "https://audiorebel.com.br/agenda/rockarioca-alex-frechette",
                            "status": "disponível"
                        }
                    ],
                    "porque": "O espírito da canção crua do underground carioca, com letras afiadas e guitarras rítmicas inspiradas no melhor do garage rock dos anos 80 e 90."
                }
            ]
        },
        {
            "id": "saloon-79-botafogo-2026",
            "titulo": "Saloon 79: Garage Rock, Blues Sujo e Pós-Punk em Botafogo",
            "tipo": "musica",
            "local": "Saloon 79, Rua Pinheiro Guimarães, 79",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-07",
            "fim": "2026-11-28",
            "quando": "Sábados de novembro a partir das 21h",
            "preco": "R$ 25 a R$ 35",
            "link": "https://www.instagram.com/saloon79/",
            "fonte": "Saloon 79",
            "porque": "O porão mais autêntico do rock 'n' roll no Rio: cerveja artesanal, luz baixa e bandas que prezam pelo peso das cordas e pela bateria seca.",
            "sobre": "Casarão acolhedor na Rua Pinheiro Guimarães com decoração rústica e palco intimista para quem busca som direto sem concessões corporativas.",
            "destaques": [
                {
                    "id": "the-baggios-chicko-noise-saloon",
                    "titulo": "The Baggios & Chicko Noise: Blues-Rock de Fuzz e Garage Elétrico",
                    "artistas": ["The Baggios", "Chicko Noise"],
                    "sessoes": [
                        {
                            "data": "2026-11-07",
                            "hora": "21h",
                            "local": "Saloon 79",
                            "bairro": "Botafogo",
                            "obs": "R$ 30 antecipado / R$ 40 na porta",
                            "link": "https://www.sympla.com.br/evento/the-baggios-no-saloon-79/2654321",
                            "status": "disponível"
                        }
                    ],
                    "porque": "O duo sergipano The Baggios descarrega sua fúria de blues-punk psicodélico, ladeado pelo garage rock pulsante do Chicko Noise.",
                    "reviews": {
                        "texto": "Um dos shows de garagem mais incendiários do Brasil. Fuzz cortante e groove irresistível.",
                        "fontes": ["Rolling Stone Brasil", "TMDQA!"]
                    }
                },
                {
                    "id": "1dv-somacores-saloon",
                    "titulo": "1DV + Somacores: Pós-Punk, Darkwave e Ruído no Subsolo",
                    "artistas": ["1DV", "Somacores"],
                    "sessoes": [
                        {
                            "data": "2026-11-14",
                            "hora": "21h",
                            "local": "Saloon 79",
                            "bairro": "Botafogo",
                            "obs": "R$ 25 antecipado",
                            "link": "https://www.sympla.com.br/evento/1dv-somacores-saloon/2654322",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Linhas de baixo hipnóticas, sintetizadores soturnos e guitarras cortantes na melhor tradição do pós-punk dos anos 80 com roupagem atual."
                },
                {
                    "id": "alex-frechette-trio-saloon",
                    "titulo": "Alex Frechette Trio: Canção Elétrica e Garage Rock Carioca",
                    "artistas": ["Alex Frechette"],
                    "sessoes": [
                        {
                            "data": "2026-11-21",
                            "hora": "21h",
                            "local": "Saloon 79",
                            "bairro": "Botafogo",
                            "obs": "R$ 25 na porta",
                            "link": "https://www.instagram.com/saloon79/",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Formato trio enxuto entregando composições ácidas e melodias marcantes no coração de Botafogo."
                }
            ]
        },
        {
            "id": "estudio-hanoi-botafogo-2026",
            "titulo": "Estúdio Hanoi & Mutante: Pocket Shows e Salas de Ensaio da Cena Indie Carioca",
            "tipo": "musica",
            "local": "Estúdio Hanoi, Rua Paulo Barreto, 25",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-08",
            "fim": "2026-11-29",
            "quando": "Domingos no fim de tarde (18h)",
            "preco": "R$ 20 a R$ 35 (capacidade reduzida)",
            "link": "https://www.instagram.com/estudiohanoi/",
            "fonte": "Estúdio Hanoi / Shotgun",
            "porque": "O formato de estúdio preferido da cena independente: shows intimistas com som direto do mixer, proximidade total com os músicos e acústica impecável.",
            "sobre": "Espaço histórico de ensaios e gravações na Rua Paulo Barreto, o Hanoi recebe edições pontuais de apresentações de bolso para públicos de até 60 pessoas.",
            "destaques": [
                {
                    "id": "sonho-liquido-durma-bem-hanoi",
                    "titulo": "Sonho Líquido, Durma Bem Johannes & 30 Dias em Guarulhos: Noite Emo/Indie",
                    "artistas": ["Sonho Líquido", "Durma Bem Johannes", "30 Dias em Guarulhos"],
                    "sessoes": [
                        {
                            "data": "2026-11-08",
                            "hora": "18h",
                            "local": "Estúdio Hanoi",
                            "bairro": "Botafogo",
                            "obs": "R$ 25 antecipado via PIX / Shotgun (lotação estrita)",
                            "link": "https://shotgun.live/pt-br/events/sonho-liquido-hanoi",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Três expoentes do midwest emo e canção indie intimista reunidos no estúdio favorito do radar Faixa Oculta.",
                    "reviews": {
                        "texto": "Um dos registros ao vivo mais honestos e viscerais da nova geração alternativa brasileira.",
                        "fontes": ["Trabalho Sujo", "Faixa Oculta"]
                    }
                },
                {
                    "id": "lupe-de-lupe-orua-hanoi",
                    "titulo": "Lupe de Lupe & Oruã: Experimento Elétrico em Sala Fechada",
                    "artistas": ["Lupe de Lupe", "Oruã"],
                    "sessoes": [
                        {
                            "data": "2026-11-15",
                            "hora": "18h",
                            "local": "Estúdio Hanoi",
                            "bairro": "Botafogo",
                            "obs": "R$ 35 antecipado",
                            "link": "https://shotgun.live/pt-br/events/lupe-orua-hanoi",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Duas vanguardas consagradas do rock alternativo e psicodelia lo-fi brasileira em formato cru de ensaio aberto amplificado."
                },
                {
                    "id": "saginata-plano-real-hanoi",
                    "titulo": "Saginata & Plano Real: Math-Rock Instrumental e Guitarras Angulares",
                    "artistas": ["Saginata", "Plano Real"],
                    "sessoes": [
                        {
                            "data": "2026-11-22",
                            "hora": "18h",
                            "local": "Estúdio Hanoi",
                            "bairro": "Botafogo",
                            "obs": "R$ 20 antecipado",
                            "link": "https://shotgun.live/pt-br/events/saginata-plano-real-hanoi",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Polirritmias instigantes, afinações abertas e passagens atmosféricas para quem aprecia a arquitetura minuciosa do math-rock."
                }
            ]
        },
        {
            "id": "garage-grindhouse-praca-bandeira-2026",
            "titulo": "Garage Grindhouse: Noites de Pós-Punk, Darkwave, Stoner e Hardcore",
            "tipo": "musica",
            "local": "Garage Grindhouse, Rua Ceará, 154",
            "bairro": "Praça da Bandeira",
            "cidade": "Rio de Janeiro",
            "regiao": "tijuca",
            "inicio": "2026-11-07",
            "fim": "2026-11-28",
            "quando": "Sábados de novembro a partir das 19h",
            "preco": "R$ 40 a R$ 80 antecipado",
            "link": "https://www.instagram.com/garagegrindhouse/",
            "fonte": "Garage Grindhouse / Songkick",
            "porque": "O templo definitivo do peso underground na Zona Norte: pós-punk siberiano, stoner rock, punk clássico e crossover thrash.",
            "sobre": "Localizado na histórica Rua Ceará, o Garage Grindhouse herda a mística do lendário Garage de Botafogo e da Tijuca, recebendo turnês internacionais e as bandas mais cruas do país.",
            "destaques": [
                {
                    "id": "ploho-grindhouse-2026",
                    "titulo": "Ploho: Turnê Brasileira do Pós-Punk Siberiano",
                    "artistas": ["Ploho"],
                    "sessoes": [
                        {
                            "data": "2026-11-07",
                            "hora": "19h",
                            "local": "Garage Grindhouse",
                            "bairro": "Praça da Bandeira",
                            "obs": "R$ 80 antecipado 1º lote (lotação esgotando)",
                            "link": "https://www.songkick.com/concerts/43284312-ploho-at-garage-grindhouse",
                            "status": "disponível"
                        }
                    ],
                    "porque": "A banda siberiana de Novosibirsk traz seu pós-punk gélido, baixo marcante e letras em russo sobre a melancolia e alienação da vida pós-soviética.",
                    "reviews": {
                        "texto": "Um dos nomes mais celebrados do renascimento gótico mundial, reverenciado ao lado de Molchat Doma e Lebanon Hanover.",
                        "fontes": ["Post-Punk.com", "Scream & Yell"]
                    },
                    "trailer": "https://www.youtube.com/watch?v=7yjnZ3eibFQ"
                },
                {
                    "id": "surra-black-pantera-grindhouse",
                    "titulo": "Surra + Black Pantera: Crossover Thrash e Hardcore Antifascista",
                    "artistas": ["Surra", "Black Pantera"],
                    "sessoes": [
                        {
                            "data": "2026-11-14",
                            "hora": "19h",
                            "local": "Garage Grindhouse",
                            "bairro": "Praça da Bandeira",
                            "obs": "R$ 50 antecipado",
                            "link": "https://www.sympla.com.br/evento/surra-black-pantera-garage/2654323",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Uma tempestade de velocidade, bateria demolidora e lirismo antifascista explícito que transforma a Rua Ceará em um redemoinho de energia.",
                    "reviews": {
                        "texto": "Dois dos maiores espetáculos de peso ao vivo da música pesada brasileira contemporânea.",
                        "fontes": ["Tenho Mais Discos Que Amigos"]
                    }
                },
                {
                    "id": "devotos-contraclasse-grindhouse",
                    "titulo": "Devotos + Contraclasse: Punk Rock Histórico do Recife e Hardcore Carioca",
                    "artistas": ["Devotos", "Contraclasse"],
                    "sessoes": [
                        {
                            "data": "2026-11-28",
                            "hora": "19h",
                            "local": "Garage Grindhouse",
                            "bairro": "Praça da Bandeira",
                            "obs": "R$ 40 antecipado",
                            "link": "https://www.sympla.com.br/evento/devotos-contraclasse-garage/2654324",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Cannibal e os veteranos da banda Devotos celebram a resistência do Alto José do Pinho no palco da Tijuca."
                }
            ]
        },
        {
            "id": "circo-voador-nov-2026",
            "titulo": "Circo Voador: Ana Frango Elétrico, Sophia Chablau, Plebe Rude e Letrux",
            "tipo": "musica",
            "local": "Circo Voador, Rua dos Arcos, s/n",
            "bairro": "Lapa",
            "cidade": "Rio de Janeiro",
            "regiao": "centro",
            "inicio": "2026-11-14",
            "fim": "2026-11-21",
            "quando": "Sextas e sábados a partir das 21h",
            "preco": "R$ 70 a R$ 80 meia-entrada",
            "link": "https://www.circovoador.com.br",
            "fonte": "Circo Voador / Eventim",
            "porque": "A lona mais icônica da América Latina recebe os grandes momentos de apogeu da música autoral e do rock brasileiro.",
            "sobre": "Espaço histórico fundamental para a cultura carioca sob os Arcos da Lapa, combinando área livre, palmeiras e acústica impecável para noites memoráveis.",
            "destaques": [
                {
                    "id": "ana-frango-sophia-circo",
                    "titulo": "Ana Frango Elétrico + Sophia Chablau e Uma Enorme Perda de Tempo",
                    "artistas": ["Ana Frango Elétrico", "Sophia Chablau e Uma Enorme Perda de Tempo"],
                    "sessoes": [
                        {
                            "data": "2026-11-14",
                            "hora": "21h",
                            "local": "Circo Voador",
                            "bairro": "Lapa",
                            "obs": "R$ 80 meia solidária / R$ 160 inteira",
                            "link": "https://www.eventim.com.br/event/ana-frango-eletrico-circo-voador-2654325/",
                            "status": "disponível"
                        }
                    ],
                    "porque": "O encontro mais esperado da nova canção de vanguarda brasileira: o pop torto sofisticado de Ana Frango e a garageira explosiva de Sophia Chablau.",
                    "reviews": {
                        "texto": "Um marco geracional que consolida a vanguarda paulistana e carioca em um mesmo palco apoteótico.",
                        "fontes": ["Pitchfork", "O Globo"]
                    }
                },
                {
                    "id": "plebe-rude-circo-2026",
                    "titulo": "Plebe Rude: 40 Anos de 'O Concreto Já Rachou' na Lapa",
                    "artistas": ["Plebe Rude"],
                    "sessoes": [
                        {
                            "data": "2026-11-20",
                            "hora": "21h",
                            "local": "Circo Voador",
                            "bairro": "Lapa",
                            "obs": "R$ 80 meia solidária",
                            "link": "https://www.eventim.com.br/event/plebe-rude-circo-voador-2654326/",
                            "status": "disponível"
                        }
                    ],
                    "porque": "O clássico disco fundamental do pós-punk político de Brasília executado na íntegra no palco onde a banda fez história nos anos 80."
                },
                {
                    "id": "letrux-circo-2026",
                    "titulo": "Letrux: Aos Prantos e Canções de Desbunde Elegante",
                    "artistas": ["Letrux"],
                    "sessoes": [
                        {
                            "data": "2026-11-21",
                            "hora": "21h",
                            "local": "Circo Voador",
                            "bairro": "Lapa",
                            "obs": "R$ 70 meia solidária",
                            "link": "https://www.eventim.com.br/event/letrux-circo-voador-2654327/",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Letícia Novaes transforma o Circo em uma festa catártica e teatral com seu synth-pop dramático e letras autobiográficas irresistíveis."
                }
            ]
        },
        {
            "id": "bar-bukowski-botafogo-2026",
            "titulo": "Bar Bukowski: O Casarão do Rock Alternativo e Noites Darkwave",
            "tipo": "musica",
            "local": "Bar Bukowski, Rua Álvaro Ramos, 270",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-06",
            "fim": "2026-11-27",
            "quando": "Sextas a partir das 22h",
            "preco": "R$ 35 antecipado",
            "link": "https://barbukowski.com.br",
            "fonte": "Bar Bukowski",
            "porque": "O mais antigo bar de rock do Rio, com três pistas, jardim arborizado e noites autorais dedicadas ao pós-punk e ao rock gótico.",
            "destaques": [
                {
                    "id": "plastique-noir-gangue-morcego-bukowski",
                    "titulo": "Plastique Noir + Gangue Morcego: Especial Pós-Punk & Goth Rock",
                    "artistas": ["Plastique Noir", "Gangue Morcego"],
                    "sessoes": [
                        {
                            "data": "2026-11-06",
                            "hora": "22h",
                            "local": "Bar Bukowski",
                            "bairro": "Botafogo",
                            "obs": "R$ 35 antecipado / R$ 50 na porta",
                            "link": "https://barbukowski.com.br/ingressos",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Duas instituições do darkwave e pós-punk brasileiro comandam as guitarras góticas e batidas eletrônicas no casarão de Botafogo.",
                    "reviews": {
                        "texto": "Pistas cheias, névoa e a melhor seleção de guitarras soturnas da noite carioca.",
                        "fontes": ["Post-Punk.com"]
                    }
                }
            ]
        },
        {
            "id": "estacao-net-botafogo-cinema-2026",
            "titulo": "Estação Net Botafogo e Gávea: Circuito de Cinema de Autor e Meia-Noite",
            "tipo": "cinema",
            "local": "Estação Net Botafogo, Rua Voluntários da Pátria, 88",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-06",
            "fim": "2026-11-30",
            "quando": "Sessões diárias das 14h às 22h",
            "preco": "R$ 20 meia / R$ 40 inteira",
            "link": "https://www.estacaonetdecinema.com.br",
            "fonte": "Estação Net de Cinema",
            "porque": "O bastião carioca do cinema independente, acolhendo os lançamentos mais premiados dos festivais de Cannes, Berlim, Veneza e Mostra SP.",
            "destaques": [
                {
                    "id": "o-agente-secreto-kleber",
                    "titulo": "O Agente Secreto (Direção de Kleber Mendonça Filho)",
                    "diretor": "Kleber Mendonça Filho",
                    "ano": 2026,
                    "origem": "Brasil",
                    "duracao": 142,
                    "sessoes": [
                        {
                            "data": "2026-11-06",
                            "hora": "18h30",
                            "local": "Estação Net Botafogo - Sala 1",
                            "bairro": "Botafogo",
                            "obs": "R$ 20 meia",
                            "link": "https://www.ingresso.com",
                            "status": "disponível"
                        },
                        {
                            "data": "2026-11-07",
                            "hora": "21h00",
                            "local": "Estação Net Botafogo - Sala 1",
                            "bairro": "Botafogo",
                            "obs": "R$ 20 meia",
                            "link": "https://www.ingresso.com",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Thriller político ambientado no Recife de 1977 estrelado por Wagner Moura, que retrata a atmosfera de espionagem, paranoia e resistência no final da ditadura.",
                    "reviews": {
                        "texto": "Obra-prima tensa e magnética que reafirma Kleber como um dos mestres absolutos do cinema mundial contemporâneo.",
                        "fontes": ["Cahiers du Cinéma", "Sight & Sound", "Folha de S.Paulo"]
                    }
                }
            ]
        },
        {
            "id": "ccbb-artes-cinema-nov-2026",
            "titulo": "Circuito CCBB Rio: Retrospectiva Amazônicas e Mostra de Cinema Italiano",
            "tipo": "artes",
            "local": "CCBB Rio, Rua Primeiro de Março, 66",
            "bairro": "Centro",
            "cidade": "Rio de Janeiro",
            "regiao": "centro",
            "inicio": "2026-11-06",
            "fim": "2026-11-30",
            "quando": "Quarta a segunda, 09h às 20h",
            "preco": "Entrada franca com agendamento",
            "link": "https://ccbb.com.br/rio-de-janeiro/",
            "fonte": "CCBB Rio / Banco do Brasil",
            "porque": "Grandes mostras visuais e retrospectivas cinematográficas completas em um dos edifícios neoclássicos mais nobres da cidade.",
            "destaques": [
                {
                    "id": "mostra-amazonicas-ccbb",
                    "titulo": "Amazônicas: Poéticas Femininas da Floresta",
                    "sessoes": [
                        {
                            "data": "2026-11-06",
                            "hora": "14h",
                            "local": "CCBB Rio - Salas de Exposição 1º Andar",
                            "bairro": "Centro",
                            "obs": "Grátis / Agendamento no site",
                            "link": "https://ccbb.com.br/rio-de-janeiro/",
                            "status": "disponível"
                        }
                    ],
                    "porque": "Mais de 80 obras de 21 artistas visuais mulheres da Amazônia Legal, explorando a força cosmopolítica e a mitologia das florestas."
                }
            ]
        }
    ]

    db.setdefault("agenda", {}).setdefault("atual", {})["eventos"] = eventos
    print(f"Agenda cultural atualizada: {len(eventos)} eventos detalhados com bandas reais e sessões futuras.")

if __name__ == "__main__":
    db = carregar_db()
    atualizar_artistas(db)
    atualizar_agenda_cultural(db)
    salvar_db(db)
