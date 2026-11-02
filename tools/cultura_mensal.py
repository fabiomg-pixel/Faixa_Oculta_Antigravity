#!/usr/bin/env python3
"""Gerador e atualizador mensal da Revista Cultural (Música, Cinema, Livros e Agenda Cultural).

Executado todo dia 01 do mês às 06h00 BRT (09h00 UTC) ou sob demanda.
Produz a edição integral de:
- Revista de Música (edicoes['AAAA-MM'], itens, guias)
- Revista de Cinema (cine_edicoes['AAAA-MM'], cine_itens, cine_guias)
- Revista de Livros (livro_edicoes['AAAA-MM'], livro_itens, livro_guias)
- Agenda Cultural atualizada do Rio (rock, underground, cena independente, mostras)
"""

import os
import sys
import json
import datetime

SKELETON_HEAD = """<!doctype html>
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
SKELETON_TAIL = "\n</body>\n</html>\n"


def montar_cultura_novembro_2026():
    mes_id = "2026-11"
    mes_rotulo = "nov 2026"
    data_ed = "2026-11-01"
    num_ed = 2

    # ==========================================
    # 1. MÚSICA (Nº 2 · Novembro 2026)
    # ==========================================
    musica_edicao = {
        "id": mes_id,
        "numero": num_ed,
        "mes": mes_rotulo,
        "data": data_ed,
        "manchete": "Guitarras de garage, poesia áspera e o pulso da cena independente",
        "editorial": "A edição de novembro do Radar Musical mergulha nas texturas orgânicas e na fricção das guitarras: da visceralidade melódica de MJ Lenderman e Dry Cleaning aos ecos do shoegaze britânico do Whitelands, abrindo espaço para a coragem harmônica da vanguarda brasileira com Juçara Marçal, Thais Nicodemo e Ana Frango Elétrico. Uma safra curada para quem busca música viva, sem pasteurização de algoritmo.",
        "layout": [
            {"tipo": "secao", "secao": "radar"},
            {"tipo": "guia", "id": "guia-pos-punk-indie-2026"},
            {"tipo": "secao", "secao": "descobertas"},
            {"tipo": "guia", "id": "guia-shoegaze-reverb-2026"},
            {"tipo": "secao", "secao": "brasil"},
            {"tipo": "guia", "id": "guia-vanguarda-paulista-carioca-2026"},
            {"tipo": "secao", "secao": "breve"}
        ]
    }

    musica_itens = {
        "2026-11--mj-lenderman-manning-fireworks": {
            "id": "2026-11--mj-lenderman-manning-fireworks",
            "edicao": mes_id,
            "ordem": 1,
            "secao": "radar",
            "destaque": True,
            "artista": "MJ Lenderman",
            "album": "Manning Fireworks",
            "ano": 2024,
            "genero": "indie rock / alt-country",
            "olho": "Guitarras cruas, lirismo agridoce e refrões tortos que confirmam o compositor da Carolina do Norte como a voz mais singular do indie rock americano contemporâneo.",
            "texto": "Com Manning Fireworks, MJ Lenderman (também guitarrista do Wednesday) equilibra com precisão rara o humor autodepreciativo, a vulnerabilidade e os amplificadores valvulados no limite do feedback. Cada faixa parece uma história curta contada no balcão de um bar esquecido de beira de estrada.",
            "faixas": ["Manning Fireworks", "Joker Lips", "Wristwatch", "She's Leaving You", "Bark at the Moon"],
            "onde": "Bandcamp, Spotify, Apple Music"
        },
        "2026-11--dry-cleaning-new-long-walk": {
            "id": "2026-11--dry-cleaning-new-long-walk",
            "edicao": mes_id,
            "ordem": 2,
            "secao": "radar",
            "artista": "Dry Cleaning",
            "album": "New Long Walk",
            "ano": 2026,
            "genero": "pós-punk / spoken word / art-rock",
            "olho": "O quarteto do sul de Londres afia ainda mais suas linhas de baixo elásticas e guitarras cortantes em diálogo com a voz inexpressiva e hipnótica de Florence Shaw.",
            "texto": "Registrado com produção analógica, New Long Walk transforma o tédio urbano e os fragmentos de conversas cotidianas em crônicas de absurdo e elegância. O diálogo entre a rítmica marcial de Tom Dowse e os devaneios de Florence cria uma tensão viciante do início ao fim.",
            "faixas": ["Gary Ashby", "Anna Calls From the Arctic", "Don't Press Me", "Hot Penny Day"],
            "onde": "4AD, Spotify, Apple Music"
        },
        "2026-11--whitelands-sun-bleached-noise": {
            "id": "2026-11--whitelands-sun-bleached-noise",
            "edicao": mes_id,
            "ordem": 3,
            "secao": "descobertas",
            "artista": "Whitelands",
            "album": "Sun-Bleached Noise",
            "ano": 2026,
            "genero": "shoegaze / dream-pop / ethereal wave",
            "olho": "Camadas espessas de chorus e distorção com sensibilidade pop luminosa na melhor tradição de Cocteau Twins e Slowdive.",
            "texto": "Formado em Londres, o Whitelands injeta frescor e diversidade na cena shoegaze britânica. Suas canções flutuam entre o peso físico das guitarras e harmonias vocais etéreas que envolvem o ouvinte sem sufocar.",
            "faixas": ["Setting Sun", "The Prophet & I", "Tell Me About It", "Cheer"],
            "onde": "Sonic Cathedral, Spotify, Bandcamp"
        },
        "2026-11--jucara-marcal-caderno-composicao": {
            "id": "2026-11--jucara-marcal-caderno-composicao",
            "edicao": mes_id,
            "ordem": 4,
            "secao": "brasil",
            "artista": "Juçara Marçal & Thais Nicodemo",
            "album": "Caderno de Composição",
            "ano": 2026,
            "genero": "vanguarda paulista / canção contemporânea",
            "olho": "Voz e piano despontam como forças vulcânicas recriando canções raras de Itamar Assumpção, Negro Léo e temas autorais.",
            "texto": "Um dos registros mais densos e comoventes da música brasileira em 2026. A pianista Thais Nicodemo explora técnicas estendidas e harmonias arrojadas enquanto Juçara imprime a dramaticidade cortante que a consagrou no Metá Metá.",
            "faixas": ["Sem Nome", "Ladeira da Memória", "Fogo no Prato", "Canto Noturno"],
            "onde": "QTV Selo, Spotify, Apple Music"
        },
        "2026-11--ana-frango-eletrico-ao-vivo-caixa": {
            "id": "2026-11--ana-frango-eletrico-ao-vivo-caixa",
            "edicao": mes_id,
            "ordem": 5,
            "secao": "brasil",
            "artista": "Ana Frango Elétrico",
            "album": "Me Chama de Gato Que Eu Sou Sua (Edição Expandida)",
            "ano": 2025,
            "genero": "boogie carioca / sophisti-pop / indie MPB",
            "olho": "Metais aveludados, groove dos anos 70 e ironia carioca em arranjos que dialogam com Marcos Valle e Steely Dan.",
            "texto": "Após turnês consagradas na Europa e no Japão, a multi-instrumentista carioca apresenta novas versões ao vivo gravadas no Rio de Janeiro, reafirmando seu papel como uma das produtoras e compositoras mais brilhantes da sua geração.",
            "faixas": ["Electric Fish", "Dela", "Boy of Bebop", "Insista em Mim", "Camelo Azul"],
            "onde": "Selo Risco, Spotify, Apple Music"
        },
        "2026-11--fontaines-dc-romance": {
            "id": "2026-11--fontaines-dc-romance",
            "edicao": mes_id,
            "ordem": 6,
            "secao": "breve",
            "artista": "Fontaines D.C.",
            "album": "Romance",
            "ano": 2024,
            "genero": "pós-punk / rock alternativo",
            "olho": "Os dublinenses abraçam a grandiosidade sombria do rock dos anos 90 sem perder a fúria poética de Grian Chatten.",
            "texto": "Produzido por James Ford, Romance expande o território sônico da banda para territórios industriais, trip-hop e grunge apocalíptico.",
            "faixas": ["Starburster", "Favourite", "Here's the Thing", "In the Modern World"],
            "onde": "XL Recordings, Spotify"
        }
    }

    musica_guias = {
        "guia-pos-punk-indie-2026": {
            "id": "guia-pos-punk-indie-2026",
            "edicao": mes_id,
            "tipo": "roteiro de audição",
            "titulo": "As novas guitarras do pós-punk e indie rock",
            "subtitulo": "Quatro discos recentes que provam a vitalidade do rock alternativo contemporâneo.",
            "albuns": [
                {
                    "artista": "MJ Lenderman",
                    "album": "Manning Fireworks",
                    "ano": 2024,
                    "estilo": "alt-country / garage",
                    "nota": "O disco que redefiniu a postura das guitarras no indie recente."
                },
                {
                    "artista": "Dry Cleaning",
                    "album": "New Long Walk",
                    "ano": 2026,
                    "estilo": "spoken word / pós-punk",
                    "nota": "Linhas de baixo envolventes e poesia mordaz britânica."
                },
                {
                    "artista": "Geese",
                    "album": "3D Country",
                    "ano": 2023,
                    "estilo": "art-punk / blues-rock",
                    "nota": "Energia maníaca e vocais teatrais à la New York pós-punk."
                },
                {
                    "artista": "Wednesday",
                    "album": "Rat Saw God",
                    "ano": 2023,
                    "estilo": "indie rock / noise country",
                    "nota": "Histórias do sul dos EUA banhadas em feedback e ternura."
                }
            ]
        },
        "guia-shoegaze-reverb-2026": {
            "id": "guia-shoegaze-reverb-2026",
            "edicao": mes_id,
            "tipo": "paisagens sonoras",
            "titulo": "Mergulho em reverb: a renascença shoegaze",
            "subtitulo": "De Londres a Tóquio, bandas jovens reinventam as muralhas sonoras dos anos 90.",
            "albuns": [
                {
                    "artista": "Whitelands",
                    "album": "Sun-Bleached Noise",
                    "ano": 2026,
                    "estilo": "dream-pop / shoegaze",
                    "nota": "Canções ensolaradas sob camadas generosas de efeito e eco."
                },
                {
                    "artista": "Slowdive",
                    "album": "everything is alive",
                    "ano": 2023,
                    "estilo": "ambient shoegaze",
                    "nota": "A maturidade impecável dos mestres do gênero."
                },
                {
                    "artista": "Luster",
                    "album": "Dopamine",
                    "ano": 2025,
                    "estilo": "heavy shoegaze / post-metal",
                    "nota": "Riffs colossais com afinações graves e dinâmica hipnótica."
                }
            ]
        },
        "guia-vanguarda-paulista-carioca-2026": {
            "id": "guia-vanguarda-paulista-carioca-2026",
            "edicao": mes_id,
            "tipo": "cena nacional",
            "titulo": "Invenção e coragem na música brasileira",
            "subtitulo": "Artistas que desafiam fórmulas fáceis e honram a tradição experimental do país.",
            "albuns": [
                {
                    "artista": "Juçara Marçal & Thais Nicodemo",
                    "album": "Caderno de Composição",
                    "ano": 2026,
                    "estilo": "vanguarda / canção",
                    "nota": "Voz visceral e piano estendido em temas de alta voltagem."
                },
                {
                    "artista": "Ana Frango Elétrico",
                    "album": "Me Chama de Gato Que Eu Sou Sua",
                    "ano": 2023,
                    "estilo": "boogie / sophisti-pop",
                    "nota": "Produção sofisticada e exuberância rítmica carioca."
                },
                {
                    "artista": "Negro Léo",
                    "album": "Desejo do Labirinto",
                    "ano": 2024,
                    "estilo": "free funk / canção torta",
                    "nota": "O pensador mais iconoclasta da canção contemporânea no Rio."
                }
            ]
        }
    }

    # ==========================================
    # 2. CINEMA (Nº 2 · Novembro 2026)
    # ==========================================
    cine_edicao = {
        "id": mes_id,
        "numero": num_ed,
        "mes": mes_rotulo,
        "data": data_ed,
        "manchete": "Memória política, silêncio e o melhor do cinema de autor nas telas do Rio",
        "editorial": "Novembro no circuito cinematográfico carioca celebra o retorno da força autoral: das salas de rua do Estação Net Botafogo às mostras do CCBB e novidades do streaming qualificado. O grande destaque é 'O Agente Secreto', o novo thriller histórico de Kleber Mendonça Filho com Wagner Moura, ladeado por obras de câmara de Christian Petzold, restaurações raras e minisséries que desafiam a narrativa convencional.",
        "layout": [
            {"tipo": "secao", "secao": "cartaz"},
            {"tipo": "guia", "id": "guia-cine-mostras-rio-2026"},
            {"tipo": "secao", "secao": "achados"},
            {"tipo": "secao", "secao": "brasil"},
            {"tipo": "secao", "secao": "series"}
        ]
    }

    cine_itens = {
        "2026-11--o-agente-secreto": {
            "id": "2026-11--o-agente-secreto",
            "edicao": mes_id,
            "ordem": 1,
            "secao": "cartaz",
            "destaque": True,
            "titulo": "O Agente Secreto",
            "autor": "Kleber Mendonça Filho",
            "ano": 2026,
            "tipo": "filme",
            "genero": "thriller político / drama de época",
            "pais": "Brasil / França",
            "tempo": "148 min",
            "olho": "Wagner Moura vive um professor universitário e pesquisador de tecnologia que foge de São Paulo para o Recife em 1977, cercado pela paranoia da ditadura militar.",
            "texto": "Vencedor de direção e atuação em festivais internacionais, o novo longa de Kleber Mendonça Filho é uma aula magna de reconstrução de época e tensão psicológica. Ao focar no ambiente acadêmico e na vigilância cotidiana de vizinhança, o filme constrói uma metáfora cortante sobre as feridas abertas da história brasileira.",
            "onde": "Em cartaz no Estação Net Botafogo, Estação Net Gávea e Reserva Cultural",
            "fonte": "https://pt.wikipedia.org/wiki/O_Agente_Secreto_(filme)"
        },
        "2026-11--mirrors-no-3": {
            "id": "2026-11--mirrors-no-3",
            "edicao": mes_id,
            "ordem": 2,
            "secao": "achados",
            "titulo": "Mirrors No. 3",
            "autor": "Christian Petzold",
            "ano": 2026,
            "tipo": "filme",
            "genero": "drama / mistério psicológico",
            "pais": "Alemanha",
            "tempo": "104 min",
            "olho": "Com Paula Beer, Petzold conclui sua trilogia sobre elementos naturais com uma reflexão magnética sobre culpa, reencontros e arquitetura berlinense.",
            "texto": "Filmado com a costumeira economia de gestos e rigor visual de Petzold, Mirrors No. 3 investiga o luto e a farsa das identidades burguesas. Uma obra de câmara que cresce a cada silêncio.",
            "onde": "MUBI / Aluguel digital no Apple TV e Google Play",
            "fonte": "https://en.wikipedia.org/wiki/Christian_Petzold_(director)"
        },
        "2026-11--retirantes-da-seca-restauracao": {
            "id": "2026-11--retirantes-da-seca-restauracao",
            "edicao": mes_id,
            "ordem": 3,
            "secao": "brasil",
            "titulo": "Vidas Secas (Cópia Restaurada em 4K)",
            "autor": "Nelson Pereira dos Santos",
            "ano": 2026,
            "tipo": "filme",
            "genero": "clássico do Cinema Novo / drama",
            "pais": "Brasil",
            "tempo": "103 min",
            "olho": "A obra-prima baseada em Graciliano Ramos ganha nova vida em restauração fotoquímica e digital supervisionada pela Cinemateca Brasileira.",
            "texto": "A luz estourada de Luiz Carlos Barreto e o som árido dos passos no chão crestado voltam às telas dos cinemas de rua cariocas, reafirmando por que este é um dos pilares estéticos fundamentais da identidade cinematográfica do país.",
            "onde": "Sessões especiais na Cinemateca do MAM e Estação Net Botafogo",
            "fonte": "https://cinemateca.org.br"
        },
        "2026-11--ripley-minisserie": {
            "id": "2026-11--ripley-minisserie",
            "edicao": mes_id,
            "ordem": 4,
            "secao": "series",
            "titulo": "Ripley",
            "autor": "Steven Zaillian",
            "ano": 2024,
            "tipo": "serie",
            "genero": "minissérie noir / thriller de câmara",
            "pais": "EUA",
            "tempo": "8 episódios (série limitada)",
            "olho": "Fotografia deslumbrante em preto e branco de Robert Elswit e atuação contida de Andrew Scott adaptando o romance clássico de Patricia Highsmith.",
            "texto": "Ao contrário das adaptações solares anteriores, o Ripley de Zaillian é gélido, meticuloso e claustrofóbico. Cada enquadramento parece uma gravura de Caravaggio, transformando a falsificação e o assassinato em estudos de solidão e vaidade.",
            "onde": "Netflix / Disponível em 4K HDR",
            "fonte": "https://www.netflix.com/title/81604292"
        }
    }

    cine_guias = {
        "guia-cine-mostras-rio-2026": {
            "id": "guia-cine-mostras-rio-2026",
            "edicao": mes_id,
            "tipo": "circuito de salas",
            "titulo": "Salas de rua e festivais imperdíveis no Rio em novembro",
            "subtitulo": "Três experiências de tela grande para fugir dos multiplex de shopping.",
            "filmes": [
                {
                    "titulo": "O Agente Secreto",
                    "autor": "Kleber Mendonça Filho",
                    "ano": 2026,
                    "genero": "thriller político",
                    "onde": "Estação Net Botafogo (Rua Voluntários da Pátria, 88)",
                    "nota": "Ver numa sala de rua com plateia atenta potencializa cada detalhe sonoro e tensão política da obra."
                },
                {
                    "titulo": "Festival de Cinema Italiano no CCBB",
                    "autor": "Mostra Retrospectiva",
                    "ano": 2026,
                    "genero": "clássicos e inéditos",
                    "onde": "CCBB Rio (Rua Primeiro de Março, 66)",
                    "nota": "Ingressos a R$ 10 para ver cópias restauradas do neorrealismo e novas vozes do cinema peninsular."
                },
                {
                    "titulo": "Sessão da Meia-Noite no Estação Net",
                    "autor": "Cinema Cult e Ficção Científica",
                    "ano": 2026,
                    "genero": "cult / meia-noite",
                    "onde": "Estação Net Botafogo (Sextas e sábados às 23h59)",
                    "nota": "O mais tradicional programa noturno carioca com clássicos do terror, sci-fi e pós-punk."
                }
            ]
        }
    }

    # ==========================================
    # 3. LIVROS (Nº 2 · Novembro 2026)
    # ==========================================
    livro_edicao = {
        "id": mes_id,
        "numero": num_ed,
        "mes": mes_rotulo,
        "data": data_ed,
        "manchete": "Ciência como ensaio vivo, memórias da biologia e o melhor da literatura curta",
        "editorial": "Na edição de novembro da Revista de Livros, a curadoria foge das listas comerciais de marketing para selecionar obras que unem precisão conceitual e beleza de prosa: de ensaios fundamentais sobre neurobiologia, evolução e sistemas vivos à literatura brasileira de fôlego e achados de pequenas editoras independentes.",
        "layout": [
            {"tipo": "secao", "secao": "lancamentos"},
            {"tipo": "guia", "id": "guia-ensaios-biologia-mente-2026"},
            {"tipo": "secao", "secao": "brasil"},
            {"tipo": "secao", "secao": "ideias"},
            {"tipo": "secao", "secao": "achados"}
        ]
    }

    livro_itens = {
        "2026-11--uma-trama-da-vida-merlin-sheldrake": {
            "id": "2026-11--uma-trama-da-vida-merlin-sheldrake",
            "edicao": mes_id,
            "ordem": 1,
            "secao": "lancamentos",
            "destaque": True,
            "titulo": "A Trama da Vida: Como os Fungos Constroem o Mundo",
            "autor": "Merlin Sheldrake",
            "ano": 2021,
            "tipo": "livro",
            "genero": "não ficção / biologia / ensaio científico",
            "pais": "Reino Unido / Tradução brasileira Fósforo",
            "tempo": "368 págs.",
            "olho": "O micologista britânico revela a inteligência descentralizada dos fungos e as redes subterrâneas que conectam ecossistemas inteiros.",
            "texto": "Um livro que transforma radicalmente nossa compreensão sobre individualidade biológica, simbiose e cooperação na natureza. Com prosa sensorial e rigor laboratorial impecável, Sheldrake mostra que a vida não é uma competição de organismos isolados, mas uma rede intrincada de relações ecológicas.",
            "onde": "Editora Fósforo / Livrarias e e-book",
            "fonte": "https://www.fosforoeditora.com.br"
        },
        "2026-11--o-homem-que-confundiu-sua-mulher-oliver-sacks": {
            "id": "2026-11--o-homem-que-confundiu-sua-mulher-oliver-sacks",
            "edicao": mes_id,
            "ordem": 2,
            "secao": "ideias",
            "titulo": "O Homem Que Confundiu Sua Mulher Com um Chapéu",
            "autor": "Oliver Sacks",
            "ano": 2023,
            "ano_original": 1985,
            "tipo": "livro",
            "genero": "neurologia / ensaio clínico / literatura",
            "pais": "Reino Unido / Brasil (Cia das Letras)",
            "tempo": "288 págs.",
            "olho": "Relatos clínicos inesquecíveis que investigam os mistérios da percepção, da memória e da identidade humana sob lesões cerebrais.",
            "texto": "O clássico atemporal que fundou a neurologia narrativa. Sacks aborda seus pacientes não como casos anômalos a serem descritos friamente, mas como seres humanos inteiros lutando para preservar o significado de suas vidas diante de labirintos perceptivos.",
            "onde": "Companhia das Letras / Livrarias e Kindle",
            "fonte": "https://www.companhiadasletras.com.br"
        },
        "2026-11--salvar-o-fogo-itamar-vieira-junior": {
            "id": "2026-11--salvar-o-fogo-itamar-vieira-junior",
            "edicao": mes_id,
            "ordem": 3,
            "secao": "brasil",
            "titulo": "Salvar o Fogo",
            "autor": "Itamar Vieira Junior",
            "ano": 2023,
            "tipo": "livro",
            "genero": "ficção brasileira contemporânea / romance",
            "pais": "Brasil",
            "tempo": "320 págs.",
            "olho": "Nas margens do rio Paraguaçu, na Bahia, laços familiares, opressão agrária e espiritualidade ancestral colidem em prosa caudalosa.",
            "texto": "Segundo romance da trilogia iniciada com Torto Arado, Salvar o Fogo confirma a maestria de Itamar Vieira Junior em capturar a dicotomia entre a violência secular da posse da terra e a dignidade resistente das comunidades ribeirinhas.",
            "onde": "Todavia Editora / Livrarias",
            "fonte": "https://todavialivros.com.br"
        },
        "2026-11--a-visao-em-parafuso-manoel-de-barros": {
            "id": "2026-11--a-visao-em-parafuso-manoel-de-barros",
            "edicao": mes_id,
            "ordem": 4,
            "secao": "achados",
            "titulo": "Gramática Expositiva do Chão (Poesia Quase Toda)",
            "autor": "Manoel de Barros",
            "ano": 2024,
            "tipo": "livro",
            "genero": "poesia / ensaio sobre a linguagem",
            "pais": "Brasil",
            "tempo": "240 págs.",
            "olho": "A celebração das coisas desimportantes, dos caramujos, dos vermes e da infância como postura epistemológica diante do mundo.",
            "texto": "Relendo Manoel de Barros, compreende-se por que a observação minuciosa do chão e dos seres ínfimos é parente direta da melhor postura científica naturalista.",
            "onde": "Alfaguara / Livrarias",
            "fonte": "https://www.companhiadasletras.com.br"
        }
    }

    livro_guias = {
        "guia-ensaios-biologia-mente-2026": {
            "id": "guia-ensaios-biologia-mente-2026",
            "edicao": mes_id,
            "tipo": "leituras de fôlego",
            "titulo": "Biologia, mente e natureza como literatura de ensaio",
            "subtitulo": "Três obras magistrais que cruzam o rigor experimental com a beleza da prosa.",
            "livros": [
                {
                    "titulo": "A Trama da Vida",
                    "autor": "Merlin Sheldrake",
                    "ano": 2021,
                    "genero": "micologia e redes ecológicas",
                    "onde": "Editora Fósforo",
                    "nota": "Uma viagem fascinante pela inteligência das redes fúngicas subterrâneas."
                },
                {
                    "titulo": "O Homem Que Confundiu Sua Mulher Com um Chapéu",
                    "autor": "Oliver Sacks",
                    "ano": 1985,
                    "genero": "neurociência e ensaio humano",
                    "onde": "Companhia das Letras",
                    "nota": "O livro basilar sobre a fragilidade e a beleza da mente humana."
                },
                {
                    "titulo": "A Montanha Viva",
                    "autor": "Nan Shepherd",
                    "ano": 1977,
                    "genero": "observação naturalista e montanhismo",
                    "onde": "Cosac Naify / Ubu",
                    "nota": "O relato sensorial definitivo sobre caminhar e contemplar o platô escocês."
                }
            ]
        }
    }

    # ==========================================
    # 4. AGENDA CULTURAL DO RIO (Rock, Indie, Underground, Cinema de Autor)
    # ==========================================
    agenda_eventos = [
        {
            "id": "saloon-79-botafogo-2026",
            "titulo": "Saloon 79: Noites de Garage Rock, Indie e Pós-Punk em Botafogo",
            "tipo": "musica",
            "local": "Saloon 79, Rua Pinheiro Guimarães, 79",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-05",
            "fim": "2026-11-28",
            "quando": "Quintas, sextas e sábados a partir das 20h",
            "preco": "R$ 25 a R$ 40",
            "afinidade": 5,
            "adicionadoEm": "2026-11-01",
            "fonte": "Saloon 79",
            "link": "https://www.instagram.com/saloon79/",
            "sobre": "Um dos redutos mais autênticos do rock independente carioca. Chope artesanal gelado, som cru nos amplificadores e noites dedicadas ao garage rock, pós-punk e bandas autorais do circuito do Rio.",
            "porque": "Para quem gosta de rock sem firula: ambiente descontraído em Botafogo, som alto e programação que valoriza bandas independentes autorais cariocas.",
            "destaques": [
                {
                    "id": "saloon-garage-night",
                    "titulo": "Sexta de Garage Rock e Indie Autoral",
                    "local": "Saloon 79",
                    "bairro": "Botafogo",
                    "sessoes": [
                        {"data": "2026-11-06", "hora": "21h", "local": "Saloon 79", "bairro": "Botafogo", "obs": "Abertura dos portões 20h", "status": "disponível"},
                        {"data": "2026-11-07", "hora": "21h", "local": "Saloon 79", "bairro": "Botafogo", "obs": "Noite Pós-Punk & Indie", "status": "disponível"},
                        {"data": "2026-11-13", "hora": "21h", "local": "Saloon 79", "bairro": "Botafogo", "obs": "Bandas autorais", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": "garage-grindhouse-praca-bandeira-2026",
            "titulo": "Garage Grindhouse: Noites de Underground, Pós-Punk, Stoner e Hardcore",
            "tipo": "musica",
            "local": "Garage Grindhouse, Rua Ceará, 154",
            "bairro": "Praça da Bandeira",
            "cidade": "Rio de Janeiro",
            "regiao": "tijuca",
            "inicio": "2026-11-06",
            "fim": "2026-11-29",
            "quando": "Sextas e sábados, 20h",
            "preco": "R$ 30 a R$ 50",
            "afinidade": 5,
            "adicionadoEm": "2026-11-01",
            "fonte": "Garage Grindhouse",
            "link": "https://www.instagram.com/garagegrindhouse/",
            "sobre": "O epicentro da lendária Rua Ceará na Praça da Bandeira. Palco sagrado do underground carioca recebendo bandas de pós-punk, stoner rock, doom e hardcore nacional e internacional.",
            "porque": "A cena independente mais pesada e fiel da cidade, herdeira direta da história do Garage Rock Bar dos anos 90.",
            "destaques": [
                {
                    "id": "grindhouse-ploho-pospunk",
                    "titulo": "Noite Especial: Pós-Punk Siberiano (Ploho) e Cena Underground",
                    "local": "Garage Grindhouse",
                    "bairro": "Praça da Bandeira",
                    "sessoes": [
                        {"data": "2026-11-07", "hora": "20h", "local": "Garage Grindhouse", "bairro": "Praça da Bandeira", "obs": "Turnê Ploho + bandas de abertura", "status": "disponível"},
                        {"data": "2026-11-14", "hora": "20h", "local": "Garage Grindhouse", "bairro": "Praça da Bandeira", "obs": "Noite Stoner Rock e Fuzz", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": "bar-bukowski-botafogo-2026",
            "titulo": "Bar Bukowski: O Casarão do Rock Alternativo e Noites Indie",
            "tipo": "musica",
            "local": "Bar Bukowski, Rua Álvaro Ramos, 270",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-06",
            "fim": "2026-11-28",
            "quando": "Sextas e sábados, 21h às 05h",
            "preco": "R$ 40 a R$ 60",
            "afinidade": 5,
            "adicionadoEm": "2026-11-01",
            "fonte": "Bar Bukowski",
            "link": "https://www.barbukowski.com.br/",
            "sobre": "O mais clássico refúgio do rock no Rio, ocupando um casarão histórico de dois andares com pista aberta, quintal arborizado e três pistas dedicadas ao rock alternativo, grunge, britpop e pós-punk.",
            "porque": "Para dançar e ouvir The Smiths, Pixies, Arctic Monkeys, Joy Division e clássicos do rock madrugada adentro em Botafogo.",
            "destaques": [
                {
                    "id": "bukowski-fim-de-semana",
                    "titulo": "Noites Clássicas do Casarão: Indie 90/00, Grunge e Rock Britânico",
                    "local": "Bar Bukowski",
                    "bairro": "Botafogo",
                    "sessoes": [
                        {"data": "2026-11-06", "hora": "21h", "local": "Bar Bukowski", "bairro": "Botafogo", "obs": "Três pistas e área externa", "status": "disponível"},
                        {"data": "2026-11-07", "hora": "21h", "local": "Bar Bukowski", "bairro": "Botafogo", "obs": "Dose dupla até meia-noite", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": "audio-rebel-nov-2026",
            "titulo": "Temporada Audio Rebel: Pós-Rock, Shoegaze, Math Rock e Cena Independente",
            "tipo": "musica",
            "local": "Audio Rebel, Rua Visconde de Silva, 55",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-04",
            "fim": "2026-11-28",
            "quando": "Quartas a sábados, 19h e 20h",
            "preco": "R$ 25 a R$ 40",
            "afinidade": 5,
            "adicionadoEm": "2026-11-01",
            "fonte": "Audio Rebel",
            "link": "https://www.instagram.com/audiorebel/",
            "sobre": "Meca da vanguarda e experimentação no Rio: noites de shoegaze, pós-rock acústico, jazz livre e lançamentos de selos independentes cariocas como a QTV.",
            "porque": "A experiência de ouvir música ao vivo a dois metros dos amplificadores com uma comunidade apaixonada por experimentação sonora.",
            "destaques": [
                {
                    "id": "rebel-shows-nov",
                    "titulo": "Sessões Íntimas de Vanguarda e Ruído",
                    "local": "Audio Rebel",
                    "bairro": "Botafogo",
                    "sessoes": [
                        {"data": "2026-11-06", "hora": "20h", "local": "Audio Rebel", "bairro": "Botafogo", "obs": "Noite Instrumental e Pós-Rock", "status": "disponível"},
                        {"data": "2026-11-07", "hora": "20h", "local": "Audio Rebel", "bairro": "Botafogo", "obs": "Shoegaze Carioca", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": "estudio-hanoi-botafogo-2026",
            "titulo": "Estúdio Hanoi e Pequenos Estúdios: Shows de Bolso da Cena Indie Carioca",
            "tipo": "musica",
            "local": "Estúdio Hanoi (Rua Paulo Barreto, 25) e Estúdio Mutante",
            "bairro": "Botafogo",
            "cidade": "Rio de Janeiro",
            "regiao": "zona_sul",
            "inicio": "2026-11-05",
            "fim": "2026-11-28",
            "quando": "Quintas a sábados à noite, 19h30",
            "preco": "R$ 20 a R$ 35",
            "afinidade": 5,
            "adicionadoEm": "2026-11-01",
            "fonte": "Cena Independente Botafogo",
            "link": "https://www.instagram.com/estudiohanoi/",
            "sobre": "Salas de gravação e ensaio que abrem suas portas para apresentações de bolso de 30 a 50 pessoas, com chope gelado e lançamentos de singles autorais.",
            "porque": "O coração da produção independente carioca onde as novas canções são testadas antes dos palcos maiores.",
            "destaques": [
                {
                    "id": "hanoi-pocket",
                    "titulo": "Pocket Shows de Bolso: Voz, Guitarra e Pedais",
                    "local": "Estúdio Hanoi",
                    "bairro": "Botafogo",
                    "sessoes": [
                        {"data": "2026-11-06", "hora": "19h30", "local": "Estúdio Hanoi", "bairro": "Botafogo", "obs": "Lançamento de single", "status": "disponível"},
                        {"data": "2026-11-07", "hora": "19h30", "local": "Estúdio Hanoi", "bairro": "Botafogo", "obs": "Pocket show intimista", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": "circo-voador-nov-2026",
            "titulo": "Circo Voador: Plebe Rude, MARO, Silva e Novos Nomes da Cena Independente",
            "tipo": "musica",
            "local": "Circo Voador, Rua dos Arcos, s/n",
            "bairro": "Lapa",
            "cidade": "Rio de Janeiro",
            "regiao": "centro",
            "inicio": "2026-11-06",
            "fim": "2026-11-28",
            "quando": "Sextas e sábados, abertura 20h",
            "preco": "R$ 70 a R$ 140",
            "afinidade": 5,
            "adicionadoEm": "2026-11-01",
            "fonte": "Circo Voador",
            "link": "https://www.circovoador.com.br",
            "sobre": "A lona mais famosa do país em novembro: rock nacional com Plebe Rude tocando clássicos políticos, a portuguesa MARO e encontros da cena independente carioca.",
            "porque": "A energia inigualável de ver grandes shows ao ar livre sob os Arcos da Lapa.",
            "destaques": [
                {
                    "id": "circo-plebe-rude",
                    "titulo": "Plebe Rude: O Concreto Já Rachou e Clássicos Políticos do Rock",
                    "local": "Circo Voador",
                    "bairro": "Lapa",
                    "sessoes": [
                        {"data": "2026-11-07", "hora": "21h", "local": "Circo Voador", "bairro": "Lapa", "obs": "Abertura dos portões 20h", "status": "disponível"}
                    ]
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
            "inicio": "2026-11-01",
            "fim": "2026-11-30",
            "quando": "Todos os dias, 14h às 23h59",
            "preco": "R$ 36 (inteira) e R$ 18 (meia / segunda no cinema)",
            "afinidade": 5,
            "adicionadoEm": "2026-11-01",
            "fonte": "Grupo Estação",
            "link": "https://grupoestacao.com.br",
            "sobre": "O cinema de rua mais vivo do Rio, com as sessões de arte, pré-estreias internacionais premiadas em festivais e as cultuadas sessões de meia-noite dedicadas ao cinema cult e rock.",
            "porque": "Patrimônio cultural carioca indispensável para quem ama ver cinema em tela grande com café e conversa na calçada.",
            "destaques": [
                {
                    "id": "estacao-o-agente-secreto",
                    "titulo": "O Agente Secreto (Kleber Mendonça Filho) e Mostras Especiais",
                    "local": "Estação Net Botafogo",
                    "bairro": "Botafogo",
                    "sessoes": [
                        {"data": "2026-11-06", "hora": "18h30", "local": "Estação Net Botafogo", "bairro": "Botafogo", "obs": "Sessão principal", "status": "disponível"},
                        {"data": "2026-11-07", "hora": "20h30", "local": "Estação Net Botafogo", "bairro": "Botafogo", "obs": "Debate pós-sessão", "status": "disponível"},
                        {"data": "2026-11-07", "hora": "23h59", "local": "Estação Net Botafogo", "bairro": "Botafogo", "obs": "Sessão da Meia-Noite", "status": "disponível"}
                    ]
                }
            ]
        },
        {
            "id": "ccbb-artes-cinema-nov-2026",
            "titulo": "Circuito CCBB Rio: Festival Italiano, Mostra Amazônicas e Artes Visuais",
            "tipo": "cinema",
            "local": "CCBB Rio, Rua Primeiro de Março, 66",
            "bairro": "Centro",
            "cidade": "Rio de Janeiro",
            "regiao": "centro",
            "inicio": "2026-11-01",
            "fim": "2026-11-30",
            "quando": "Quarta a segunda, 9h às 20h",
            "preco": "R$ 10 (cinema) e exposições gratuitas",
            "afinidade": 5,
            "adicionadoEm": "2026-11-01",
            "fonte": "CCBB Rio",
            "link": "https://ccbb.com.br/rio-de-janeiro/programacao/",
            "sobre": "Cinema I e II em plena efervescência com mostras internacionais retrospectivas e grandes exposições nas galerias do Centro.",
            "porque": "Programação de altíssimo nível no Centro histórico por preços populares e acesso impecável.",
            "destaques": [
                {
                    "id": "ccbb-cinema-italiano",
                    "titulo": "Mostra de Cinema Italiano: Clássicos e Contemporâneos",
                    "local": "CCBB Rio – Cinema I",
                    "bairro": "Centro",
                    "sessoes": [
                        {"data": "2026-11-06", "hora": "18h", "local": "CCBB Rio", "bairro": "Centro", "obs": "Cópia restaurada", "status": "disponível"},
                        {"data": "2026-11-08", "hora": "17h", "local": "CCBB Rio", "bairro": "Centro", "obs": "Sessão dominical", "status": "disponível"}
                    ]
                }
            ]
        }
    ]

    return {
        "musica_edicao": musica_edicao,
        "musica_itens": musica_itens,
        "musica_guias": musica_guias,
        "cine_edicao": cine_edicao,
        "cine_itens": cine_itens,
        "cine_guias": cine_guias,
        "livro_edicao": livro_edicao,
        "livro_itens": livro_itens,
        "livro_guias": livro_guias,
        "agenda_eventos": agenda_eventos
    }


def main():
    print("=== INICIANDO ATUALIZAÇÃO DA REVISTA CULTURAL (NOVEMBRO 2026) ===")
    revista_path = "data/revista.json"

    with open(revista_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    dados = montar_cultura_novembro_2026()
    mes_id = "2026-11"

    # 1. Música
    db.setdefault("edicoes", {})[mes_id] = dados["musica_edicao"]
    for k, v in dados["musica_itens"].items():
        db.setdefault("itens", {})[k] = v
    for k, v in dados["musica_guias"].items():
        db.setdefault("guias", {})[k] = v

    # 2. Cinema
    db.setdefault("cine_edicoes", {})[mes_id] = dados["cine_edicao"]
    for k, v in dados["cine_itens"].items():
        db.setdefault("cine_itens", {})[k] = v
    for k, v in dados["cine_guias"].items():
        db.setdefault("cine_guias", {})[k] = v

    # 3. Livros
    db.setdefault("livro_edicoes", {})[mes_id] = dados["livro_edicao"]
    for k, v in dados["livro_itens"].items():
        db.setdefault("livro_itens", {})[k] = v
    for k, v in dados["livro_guias"].items():
        db.setdefault("livro_guias", {})[k] = v

    # 4. Agenda Cultural
    if "agenda" not in db:
        db["agenda"] = {}
    if "atual" not in db["agenda"]:
        db["agenda"]["atual"] = {}
    db["agenda"]["atual"]["eventos"] = dados["agenda_eventos"]

    with open(revista_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    with open("pagina.html", "r", encoding="utf-8") as f:
        src = f.read()

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(SKELETON_HEAD + src + SKELETON_TAIL)

    print(f"=== SUCESSO: Cultura Mensal de {mes_id} atualizada com Música, Cinema, Livros e Agenda Rock/Underground! ===")


if __name__ == "__main__":
    main()
