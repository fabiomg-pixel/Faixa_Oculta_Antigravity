# -*- coding: utf-8 -*-
"""Dados editoriais de Cinema e Séries para a edição Nº 2 (Novembro 2026).
Contém 34 filmes/séries nas seções editoriais e 3 guias temáticos completos (15 filmes nos guias).
"""

CINE_EDICAO = {
    "id": "2026-11",
    "numero": 2,
    "mes": "Novembro de 2026",
    "data": "2026-11-01",
    "manchete": "Memória política, silêncio e o melhor do cinema de autor nas telas do Rio",
    "editorial": (
        "Novembro no circuito cinematográfico carioca celebra o retorno da força autoral: das salas de rua do Estação Net "
        "às plataformas de streaming de acervo, a safra deste mês coloca o cinema como instrumento de fricção histórica e sensorial. "
        "Na matéria de capa, 'O Agente Secreto' de Kleber Mendonça Filho resgata a paranoia e a resistência civil no Recife de 1977, "
        "cercado pelo triunfo arrebatador de 'Anora' (Sean Baker) em Cannes, a coragem política clandestina de 'A Semente do Figo Sagrado' "
        "(Mohammad Rasoulof) e a restauração luminosa em 4K de 'Vidas Secas' de Nelson Pereira dos Santos. Uma seleção densa e indispensável."
    ),
    "layout": [
        {"tipo": "secao", "secao": "cartaz"},
        {"tipo": "guia", "id": "guia-kleber-cinema-nordeste-2026"},
        {"tipo": "secao", "secao": "achados"},
        {"tipo": "guia", "id": "guia-suspense-politico-resistencia-2026"},
        {"tipo": "secao", "secao": "series"},
        {"tipo": "secao", "secao": "brasil"},
        {"tipo": "guia", "id": "guia-cinema-autoral-europeu-2026"},
        {"tipo": "secao", "secao": "pop"},
        {"tipo": "secao", "secao": "breve"}
    ]
}

CINE_ITENS = {
    # --- SEÇÃO EM CARTAZ ---
    "2026-11--o-agente-secreto": {
        "id": "2026-11--o-agente-secreto",
        "edicao": "2026-11",
        "ordem": 1,
        "secao": "cartaz",
        "destaque": True,
        "titulo": "O Agente Secreto",
        "titulo_original": "O Agente Secreto",
        "autor": "Kleber Mendonça Filho",
        "ano": 2025,
        "pais": "Brasil, França, Alemanha",
        "tempo": "2h 38min",
        "genero": "thriller político / drama histórico",
        "tipo": "filme",
        "onde": "Circuito de cinema (Estação Net Rio, Cine Odeon, IMS)",
        "imdb": "tt27847051",
        "trailer_url": "https://www.youtube.com/results?search_query=O+Agente+Secreto+Kleber+Mendonca+Filho+trailer",
        "olho": "Wagner Moura e Kleber Mendonça Filho recriam o Recife de 1977 num thriller sufocante sobre vigilância, tecnologia arcaica e resistência civil.",
        "texto": "Vencedor de Direção e Melhor Ator em Cannes, o novo longa do diretor de Aquarius e Bacurau é uma obra-prima sobre as cicatrizes da ditadura.",
        "resenha": [
            "Em 1977, no auge do governo Geisel, o Recife é uma cidade onde a umidade tropical parece condensar o medo institucionalizado. Marcelo (Wagner Moura), um professor universitário e especialista em computação e telecomunicações formado em São Paulo, retorna à capital pernambucana em fuga de um passado misterioso. Ele aceita um trabalho discreto de consultoria para o setor público, mas logo descobre que se tornou peça central numa teia de escutas clandestinas, dossiês e vigilância militar.",
            "Kleber Mendonça Filho constrói a narrativa com a maestria arquitetônica que já é sua marca registrada: as frestas das janelas de cobogó, os sons de fitas de rolo girando em gravadores alemães, o ronco surdo dos carros Opala pretos estacionados nas esquinas e os cortes abruptos entre a banalidade do Carnaval de rua e a violência sumária dos porões do DOI-CODI.",
            "Wagner Moura entrega uma de suas atuações mais sutis e contidas: em vez do herói inflamado, seu Marcelo é um homem comum paralisado pela desconfiança mútua, onde qualquer vizinho ou garçom pode ser um informante a serviço do regime. O elenco estelar conta ainda com Maria Fernanda Cândido e Gabriel Leone, capturados pela fotografia granulada em 35mm de Evgenia Alexandrova.",
            "Um monumento cinematográfico indispensável que resgata a memória política brasileira sem recorrer a panfletarismos, fazendo do suspense histórico uma experiência sensorial de imensa relevância ética."
        ],
        "ponte": "Aquarius, Bacurau, A Conversação (Francis Ford Coppola) e O Homem do Meio (Jean-Pierre Melville).",
        "recepcao": "Prêmio de Melhor Direção e Melhor Ator para Wagner Moura no Festival de Cannes 2025; ovacionado pela crítica internacional."
    },
    "2026-11--anora": {
        "id": "2026-11--anora",
        "edicao": "2026-11",
        "ordem": 2,
        "secao": "cartaz",
        "titulo": "Anora",
        "titulo_original": "Anora",
        "autor": "Sean Baker",
        "ano": 2024,
        "pais": "EUA",
        "tempo": "2h 19min",
        "genero": "comédia dramática / romance",
        "tipo": "filme",
        "onde": "Cinemas e plataformas digitais (Apple TV, Google Play)",
        "imdb": "tt27949392",
        "trailer_url": "https://www.youtube.com/results?search_query=Anora+Sean+Baker+trailer",
        "olho": "Palma de Ouro em Cannes 2024, a fábula frenética de Sean Baker sobre uma stripper de Brighton Beach que se casa com o filho de um oligarca russo.",
        "texto": "Mikey Madison entrega uma performance vulcânica numa montanha-russa entre a comédia screwball e o choque brutal de classes.",
        "resenha": [
            "Sean Baker há muito se estabeleceu como o cronista mais generoso e implacável das margens do sonho americano em filmes como Tangerine, Projeto Flórida e Red Rocket. Em Anora, consagrado com a Palma de Ouro unânime no Festival de Cannes, ele eleva sua estética a um novo patamar de virtuosismo narrativo e energia rítmica.",
            "Anora (Mikey Madison), carinhosamente chamada de Ani, trabalha numa casa noturna de strippers no Brooklyn e atende Vanya, o filho mimado e inconsequente de um magnata russo. O que começa como uma fantasia de conto de fadas em Las Vegas rapidamente se transforma numa caçada histérica e tragicômica quando os pais do garoto enviam capangas para anular a união a qualquer custo.",
            "A grande virada do filme acontece na extraordinária sequência de invasão da mansão de Vanya, que dura quase quarenta minutos de pura farsa teatral e coreografia física, onde capangas atrapalhados e uma noiva indomável transformam o luxo em praça de guerra.",
            "O final, silencioso e devastador no banco de trás de um carro sob a neve de Coney Island, ancora a comédia no desamparo econômico da classe trabalhadora com uma delicadeza que corta como lâmina."
        ],
        "ponte": "Projeto Flórida, Tangerine, Uma Linda Mulher e o cinema dos irmãos Safdie.",
        "recepcao": "Palma de Ouro no Festival de Cannes 2024; amplo favoritismo nas premiações de cinema autoral do ano."
    },
    "2026-11--a-semente-do-figo-sagrado": {
        "id": "2026-11--a-semente-do-figo-sagrado",
        "edicao": "2026-11",
        "ordem": 3,
        "secao": "cartaz",
        "titulo": "A Semente do Figo Sagrado",
        "titulo_original": "The Seed of the Sacred Fig",
        "autor": "Mohammad Rasoulof",
        "ano": 2024,
        "pais": "Irã, Alemanha, França",
        "tempo": "2h 48min",
        "genero": "thriller político / drama familiar",
        "tipo": "filme",
        "onde": "Salas de cinema de arte e MUBI",
        "imdb": "tt32187762",
        "trailer_url": "https://www.youtube.com/results?search_query=The+Seed+of+the+Sacred+Fig+trailer",
        "olho": "Filmado na clandestinidade antes da fuga a pé do diretor pelo Curdistão, o filme disseca a paranoia teocrática dentro de uma família em Teerã.",
        "texto": "Prêmio Especial do Júri em Cannes, este suspense claustrofóbico transforma uma arma desaparecida numa autópsia do patriarcado autoritário.",
        "resenha": [
            "A história dos bastidores de A Semente do Figo Sagrado é por si só um testamento heroico à liberdade de criação: condenado a oito anos de prisão e açoitamento pela teocracia iraniana, o cineasta Mohammad Rasoulof filmou este longa em absoluto segredo em apartamentos de Teerã e fugiu a pé através das montanhas da fronteira turca dias antes da estreia mundial em Cannes.",
            "A trama acompanha Iman, um jurista leal ao regime que acaba de ser promovido a juiz de instrução no Tribunal Revolucionário de Teerã, coincidindo com a explosão dos protestos femininos do movimento 'Mulher, Vida, Liberdade'. Enquanto a repressão assassina jovens nas ruas, a tensão invade sua própria casa quando suas duas filhas universitárias e sua esposa começam a questionar suas decisões.",
            "Quando a arma funcional que o tribunal entregou a Iman desaparece misteriosamente de sua gaveta, a paranoia paterna atinge o ápice da loucura inquisitorial, transformando o patriarca num tirano doméstico que submete a própria família a interrogatórios humilhantes.",
            "Um dos filmes políticos mais corajosos, urgentes e cinematograficamente potentes do século XXI."
        ],
        "ponte": "Não Há Mal Algum (Mohammad Rasoulof), Uma Separação (Asghar Farhadi) e O Conformista (Bernardo Bertolucci).",
        "recepcao": "Prêmio Especial do Júri e Prêmio FIPRESCI em Cannes 2024; representante da Alemanha no Oscar."
    },
    "2026-11--o-quarto-ao-lado": {
        "id": "2026-11--o-quarto-ao-lado",
        "edicao": "2026-11",
        "ordem": 4,
        "secao": "cartaz",
        "titulo": "O Quarto ao Lado",
        "titulo_original": "The Room Next Door",
        "autor": "Pedro Almodóvar",
        "ano": 2024,
        "pais": "Espanha, EUA",
        "tempo": "1h 47min",
        "genero": "drama / melodrama reflexivo",
        "tipo": "filme",
        "onde": "Cinemas (circuito Estação Net) e plataformas digitais",
        "imdb": "tt31006124",
        "trailer_url": "https://www.youtube.com/results?search_query=The+Room+Next+Door+Almodovar+trailer",
        "olho": "Tilda Swinton e Julianne Moore brilham na estreia de Almodóvar em língua inglesa, laureada com o Leão de Ouro no Festival de Veneza.",
        "texto": "Uma meditação luminosa sobre a amizade feminina, a dignidade da morte e as cores do outono em uma casa nas montanhas de Nova York.",
        "resenha": [
            "Após décadas reinando em Madri, Pedro Almodóvar finalmente filmou seu primeiro longa-metragem falado em inglês, adaptando o romance 'O Que Você Está Passando', de Sigrid Nunez. O resultado foi a consagração máxima com o cobiçado Leão de Ouro no Festival de Veneza 2024, coroando um filme de sobriedade e maturidade comoventes.",
            "Ingrid (Julianne Moore), uma romancista de autoficção aterrorizada pela ideia da morte, reencontra Martha (Tilda Swinton), uma antiga amiga e ex-correspondente de guerra que agora enfrenta um câncer terminal. Quando Martha decide encerrar a vida em seus próprios termos e pede que Ingrid a acompanhe em uma casa alugada nas florestas do estado de Nova York, o filme se torna um dueto íntimo sobre a coragem e a cumplicidade.",
            "Almodóvar mantém seu refinamento cromático incomparável — vermelhos profundos, amarelos mostarda e verdes florestais assinados pelo diretor de arte Inbal Weinberg —, mas substitui o melodrama histérico por um silêncio digno e afetuoso que reverbera a pintura de Edward Hopper.",
            "Swinton e Moore entregam lições de modulação vocal e presença física, construindo uma elegia à vida que se recusa a ceder ao desespero."
        ],
        "ponte": "Dor e Glória, Fale com Ela, Três Cores: Azul e o cinema de Ingmar Bergman.",
        "recepcao": "Vencedor do Leão de Ouro de Melhor Filme no Festival de Veneza 2024; ovação de 17 minutos de aplausos."
    },
    "2026-11--megalopolis": {
        "id": "2026-11--megalopolis",
        "edicao": "2026-11",
        "ordem": 5,
        "secao": "cartaz",
        "titulo": "Megalópolis",
        "titulo_original": "Megalopolis",
        "autor": "Francis Ford Coppola",
        "ano": 2024,
        "pais": "EUA",
        "tempo": "2h 18min",
        "genero": "ficção científica / fábula dramática / épico",
        "tipo": "filme",
        "onde": "Cinemas (IMAX, Estação Net Rio)",
        "imdb": "tt10128846",
        "trailer_url": "https://www.youtube.com/results?search_query=Megalopolis+Coppola+trailer",
        "olho": "Financiado com US$ 120 milhões do próprio bolso de Coppola, um delírio barroco e visionário sobre a queda da Roma contemporânea.",
        "texto": "Adam Driver interpreta um arquiteto utópico com o poder de parar o tempo em uma Nova Roma decadente dividida por populismo e ganância.",
        "resenha": [
            "Não existe nada no cinema atual que se assemelhe a Megalópolis. Aos 85 anos, tendo vendido parte substancial de seus vinhedos na Califórnia para garantir total independência financeira, Francis Ford Coppola realizou o sonho obsessivo de quatro décadas: um épico filosófico que rejeita todas as convenções do cinema narrativo contemporâneo de estúdio.",
            "Em uma versão futurista e decadente de Nova York chamada Nova Roma, o genial e arrogante arquiteto César Catilina (Adam Driver) sonha em reconstruir a cidade com um material biológico revolucionário chamado Megalon, enfrentando a oposição feroz do corrupto prefeito Franklyn Cicero (Giancarlo Esposito) e a cobiça do banqueiro Crassus (Jon Voight).",
            "O filme transita entre o teatro elisabetano, citações literais de Marco Aurélio e Petrarca, telas divididas experimentais e efeitos visuais expressionistas que desafiam o bom gosto médio. Audrey Plaza rouba todas as cenas no papel da ambiciosa âncora de TV Wow Platinum.",
            "Megalópolis é uma obra monumental e imperfeita, que pulsa com a ambição desmedida de um dos últimos gigantes do cinema autoral que ainda ousa apostar tudo na imaginação."
        ],
        "ponte": "Apocalypse Now, Metrópolis (Fritz Lang), Cidadão Kane e O Fundo do Coração.",
        "recepcao": "Estreia divisiva e histórica em Cannes 2024; abraçado por críticos de vanguarda como um clássico imperfeito e corajoso."
    },
    "2026-11--a-garota-da-agulha": {
        "id": "2026-11--a-garota-da-agulha",
        "edicao": "2026-11",
        "ordem": 6,
        "secao": "cartaz",
        "titulo": "A Garota da Agulha",
        "titulo_original": "Pigen med nålen",
        "autor": "Magnus von Horn",
        "ano": 2024,
        "pais": "Dinamarca, Polônia, Suécia",
        "tempo": "1h 55min",
        "genero": "drama histórico / terror psicológico",
        "tipo": "filme",
        "onde": "Cinemas de arte e MUBI",
        "imdb": "tt31004812",
        "trailer_url": "https://www.youtube.com/results?search_query=The+Girl+with+the+Needle+trailer",
        "olho": "Em preto e branco expressionista deslumbrante, uma Copenhague devastada pós-Primeira Guerra serve de palco para uma fábula macabra sobre maternidade.",
        "texto": "Baseado na aterradora história real de Dagmar Overbye, com performances magnéticas de Vic Carmen Sonne e Trine Dyrholm.",
        "resenha": [
            "Inspirado nos crimes verídicos de Dagmar Overbye na Copenhague de 1919, A Garota da Agulha é uma das experiências estéticas mais perturbadoras e visualmente acachapantes do ano. O diretor sueco Magnus von Horn adota uma fotografia em preto e branco de alto contraste, assinada por Michał Dymek, que evoca tanto o expressionismo alemão de Murnau e Fritz Lang quanto o realismo social cruel de David Lynch em O Homem Elefante.",
            "Karoline (Vic Carmen Sonne) é uma jovem costureira cujo marido foi dado como morto nas trincheiras da Grande Guerra. Grávida e abandonada à miséria nas ruas geladas da capital dinamarquesa, ela encontra abrigo ao lado de Dagmar (Trine Dyrholm), uma mulher mais velha e aparentemente compassiva que opera uma agência clandestina de adoção no sótão de uma loja de doces.",
            "A cumplicidade entre as duas mulheres evolui num crescendo de sombras até Karoline descobrir a verdade sinistra por trás do destino das crianças entregues aos cuidados de Dagmar. O design de som industrial e as texturas táteis transformam cada cena numa pintura angustiante.",
            "Um conto de fadas sombrio e magistral sobre a sobrevivência das mulheres nas margens de uma sociedade hipócrita e arruinada."
        ],
        "ponte": "O Homem Elefante (David Lynch), A Fita Branca (Michael Haneke) e O Vampiro de Düsseldorf.",
        "recepcao": "Compromisso oficial em Cannes 2024; elogiado pelo The Hollywood Reporter e Variety como um triunfo visual sombrio."
    },
    "2026-11--bird": {
        "id": "2026-11--bird",
        "edicao": "2026-11",
        "ordem": 7,
        "secao": "cartaz",
        "titulo": "Bird",
        "titulo_original": "Bird",
        "autor": "Andrea Arnold",
        "ano": 2024,
        "pais": "Reino Unido, França",
        "tempo": "1h 59min",
        "genero": "drama / realismo mágico",
        "tipo": "filme",
        "onde": "Cinemas e plataformas digitais",
        "imdb": "tt27849480",
        "trailer_url": "https://www.youtube.com/results?search_query=Bird+Andrea+Arnold+trailer",
        "olho": "Andrea Arnold retorna à periferia britânica com Barry Keoghan e Franz Rogowski numa colisão mágica entre crueza social e lirismo voador.",
        "texto": "A diretora de American Honey e Fish Tank eleva o cinema da classe trabalhadora com um toque inesperado de fábula fantástica.",
        "resenha": [
            "Andrea Arnold tem um dom incomparável para filmar a aspereza dos subúrbios ingleses sem nunca retirar a dignidade e a pulsão de vida de seus personagens. Em Bird, ambientado na cidade costeira decadente de Gravesend no Kent, ela acompanha Bailey (Nykiya Adams, uma revelação fulgurante de 12 anos), que vive em ocupações com seu jovem pai solteiro Bug (Barry Keoghan, transbordando carisma instável coberto de tatuagens).",
            "Bailey filma gaivotas e o vento nos campos baldios com seu celular para escapar do caos doméstico. Em suas andanças solitárias, ela cruza com Bird (Franz Rogowski), um homem enigmático que veste roupas estranhas, empoleira-se nos telhados e procura desesperadamente por seus pais biológicos.",
            "O encontro entre os dois abre uma fenda mágica na narrativa, onde o realismo social britânico herdeiro de Ken Loach colide com momentos de pura transcendência poética embalados pela trilha de Burial e Fontaines D.C..",
            "Um filme solar, enérgico e comovente que reafirma Andrea Arnold como uma das vozes mais vitais do cinema mundial."
        ],
        "ponte": "Fish Tank, American Honey, Ken Loach e O Labirinto do Fauno.",
        "recepcao": "Ovacionado em sua estreia em Cannes 2024; aplaudido pela química enternecedora entre Keoghan e a jovem Nykiya Adams."
    },
    "2026-11--emilia-perez": {
        "id": "2026-11--emilia-perez",
        "edicao": "2026-11",
        "ordem": 8,
        "secao": "cartaz",
        "titulo": "Emilia Pérez",
        "titulo_original": "Emilia Pérez",
        "autor": "Jacques Audiard",
        "ano": 2024,
        "pais": "França, México",
        "tempo": "2h 12min",
        "genero": "musical / drama policial / thriller",
        "tipo": "filme",
        "onde": "Cinemas e Netflix",
        "imdb": "tt20221436",
        "trailer_url": "https://www.youtube.com/results?search_query=Emilia+Perez+Audiard+trailer",
        "olho": "Prêmio do Júri e Melhor Atriz coletivo em Cannes, o musical ousadíssimo sobre um líder do narcotráfico que transiciona para mulher.",
        "texto": "Karla Sofía Gascón, Zoe Saldaña e Selena Gomez estrelam uma ópera pop eletrizante sobre redenção, identidade e violência.",
        "resenha": [
            "O diretor francês Jacques Audiard (O Profeta, Dheepan) sempre gostou de dinamitar as fronteiras entre os gêneros cinematográficos, mas com Emilia Pérez ele realizou seu salto mortal mais arriscado e triunfal: um melodrama musical cantado em espanhol sobre o submundo dos cartéis mexicanos de drogas.",
            "Rita (Zoe Saldaña) é uma advogada brilhante e subvalorizada na Cidade do México que recebe uma oferta irrecusável: ajudar Juan 'Manitas' Del Monte, o mais temido chefe do narcotráfico do país, a forjar a própria morte e realizar seu sonho secreto de transicionar para o gênero feminino, renascendo como Emilia Pérez (Karla Sofía Gascón).",
            "Anos depois, Emilia retorna sob nova identidade para resgatar sua esposa (Selena Gomez) e seus filhos, tentando compensar a barbárie de seu passado financiando uma ONG dedicada a localizar os corpos dos desaparecidos da guerra do narcotráfico.",
            "Com números musicais arrojados compostos pela cantora francesa Camille e pelo arranjador Clément Ducol, o filme é uma explosão de energia rítmica, ousadia queer e paixão cinematográfica."
        ],
        "ponte": "O Profeta, Tudo Sobre Minha Mãe (Almodóvar), West Side Story e Sicario.",
        "recepcao": "Prêmio do Júri e Prêmio de Melhor Atriz para o quarteto de atrizes em Cannes 2024; indicado oficial da França ao Oscar."
    },

    # --- SEÇÃO ACHADOS & AUTORES ---
    "2026-11--evil-does-not-exist": {
        "id": "2026-11--evil-does-not-exist",
        "edicao": "2026-11",
        "ordem": 9,
        "secao": "achados",
        "titulo": "O Mal Não Existe",
        "titulo_original": "Aku wa sonzai shinai",
        "autor": "Ryusuke Hamaguchi",
        "ano": 2023,
        "pais": "Japão",
        "tempo": "1h 46min",
        "genero": "drama / suspense contemplativo / mistério ecológico",
        "tipo": "filme",
        "onde": "MUBI e plataformas digitais",
        "imdb": "tt28469858",
        "trailer_url": "https://www.youtube.com/results?search_query=Evil+Does+Not+Exist+Hamaguchi+trailer",
        "olho": "Vencedor do Grande Prêmio do Júri no Festival de Veneza, o novo filme do diretor de Drive My Car é uma parábola ecológica enigmática e hipnótica.",
        "texto": "A invasão de um vilarejo rural por um projeto de glamping corporativo desencadeia um conflito silencioso de consequências imprevisíveis.",
        "resenha": [
            "Após o triunfo internacional de Drive My Car, Ryusuke Hamaguchi poderia ter sido absorvido pelo cinema ocidental de grande orçamento. Em vez disso, ele se recolheu às florestas de Nagano ao lado da compositora Eiko Ishibashi para criar O Mal Não Existe, uma obra que começou como um projeto audiovisual para concertos ao vivo e transformou-se num dos suspenses morais mais instigantes do cinema recente.",
            "Takumi e sua filha Hana vivem em perfeita harmonia com o ciclo das estações no vilarejo de Mizubiki, cortando lenha e recolhendo água pura da nascente para o restaurante de macarrão local. O equilíbrio é ameaçado quando uma empresa de entretenimento de Tóquio decide construir um local de acampamento de luxo (glamping) exatamente no curso da nascente, atraindo turistas despreparados e esgoto contaminado.",
            "Hamaguchi filma a reunião comunitária entre os aldeões e os representantes da corporação com uma inteligência dialógica extraordinária: ninguém é vilão caricato, mas as lógicas urbanas e ecológicas colidem de forma irreconciliável.",
            "A música em cordas de Eiko Ishibashi e os planos contemplativos das copas das árvores culminam num desfecho enigmático, chocante e aberto, que ecoa na memória por semanas."
        ],
        "ponte": "Drive My Car, Roda do Destino, Andrei Tarkovsky e o cinema de Kenji Mizoguchi.",
        "recepcao": "Leão de Prata / Grande Prêmio do Júri e Prêmio FIPRESCI no Festival de Veneza; eleito melhor filme do ano pelo BFI/Sight & Sound."
    },
    "2026-11--la-chimera": {
        "id": "2026-11--la-chimera",
        "edicao": "2026-11",
        "ordem": 10,
        "secao": "achados",
        "titulo": "La Chimera",
        "titulo_original": "La Chimera",
        "autor": "Alice Rohrwacher",
        "ano": 2023,
        "pais": "Itália, França, Suíça",
        "tempo": "2h 10min",
        "genero": "comédia dramática / fábula poética",
        "tipo": "filme",
        "onde": "Globoplay / Telecine e Apple TV",
        "imdb": "tt14561712",
        "trailer_url": "https://www.youtube.com/results?search_query=La+Chimera+Alice+Rohrwacher+trailer",
        "olho": "Josh O'Connor e Alice Rohrwacher conduzem uma trupe de saqueadores de tumbas etruscas na Toscana dos anos 1980.",
        "texto": "Filmado em três bitolas analógicas diferentes (35mm, 16mm e Super 8), o longa é uma elegia deslumbrante à memória soterrada.",
        "resenha": [
            "Alice Rohrwacher completa com La Chimera uma trilogia informal sobre a perda da inocência rural italiana iniciada com As Maravilhas e Feliz como Lázaro. Aqui, o protagonista é Arthur (Josh O'Connor, em estado de graça com seu terno de linho amassado), um arqueólogo inglês recém-saído da prisão que possui o dom zahorí de farejar cavidades subterrâneas e túmulos etruscos milenares.",
            "Adotado por uma trupe de 'tombaroli' — jovens maltrapilhos que escavam ilegalmente relíquias sagradas para vendê-las no mercado negro a colecionadores estrangeiros —, Arthur busca algo que o dinheiro não compra: uma passagem mística para reencontrar Beniamina, seu grande amor que partiu para o reino dos mortos.",
            "O filme brilha na convivência com a aristocrática mãe de Beniamina, interpretada pela lendária Isabella Rossellini em uma vila decadente, e com Italia (Carol Duarte), uma imigrante brasileira que estuda canto lírico e traz uma luz terrena à melancolia de Arthur.",
            "Uma celebração pagã e mágica do cinema, onde o riso carnavalesco e a gravidade dos mortos convivem com poesia sem igual."
        ],
        "ponte": "Feliz como Lázaro, Fellini Roma, Pasolini e Carol Duarte.",
        "recepcao": "Competição oficial de Cannes; vencedor de múltiplos prêmios de direção e fotografia na Europa."
    },
    "2026-11--do-not-expect-too-much": {
        "id": "2026-11--do-not-expect-too-much",
        "edicao": "2026-11",
        "ordem": 11,
        "secao": "achados",
        "titulo": "Não Espere Muito do Fim do Mundo",
        "titulo_original": "Nu astepta prea mult de la sfârsitul lumii",
        "autor": "Radu Jude",
        "ano": 2023,
        "pais": "Romênia, Luxemburgo, França, Croácia",
        "tempo": "2h 43min",
        "genero": "comédia satírica / ensaio cinematográfico / meta-cinema",
        "tipo": "filme",
        "onde": "MUBI",
        "imdb": "tt27668696",
        "trailer_url": "https://www.youtube.com/results?search_query=Do+Not+Expect+Too+Much+from+the+End+of+the+World+trailer",
        "olho": "A sátira definitiva sobre o capitalismo de plataforma, trabalho precarizado e vídeos tóxicos de TikTok nas ruas de Bucareste.",
        "texto": "O diretor romeno Radu Jude mistura comédia ácida, arquivos comunistas e humor escatológico numa obra-prima contemporânea.",
        "resenha": [
            "Radu Jude (vencedor do Urso de Ouro em Berlim por Má Sorte no Sexo ou Pornô Acidental) é o cirurgião mais implacável do absurdo moderno. Em Não Espere Muito do Fim do Mundo, ele acompanha Angela (Ilinca Manolache, monumental), uma assistente de produção exausta que dirige 16 horas por dia pelas ruas congestionadas de Bucareste entrevistando operários acidentados para um vídeo corporativo de segurança encomendado por uma multinacional austríaca.",
            "Para não enlouquecer com o cansaço extremo, Angela grava vídeos hilários e abjetos para as redes sociais usando um filtro de homem careca ultraconservador chamado Bobiță, destilando misoginia e conspiracionismo como catarse digital.",
            "Jude intercala a jornada frenética de Angela com trechos em cores de Angela Merge Mai Departe, um filme de propaganda comunista romeno de 1981 sobre uma taxista mulher, criando um diálogo fascinante e doloroso entre duas épocas de exploração do corpo feminino pelo trabalho.",
            "O terceiro ato, filmado em um plano-sequência estático de 40 minutos em preto e branco diante de um galpão industrial, é uma das sequências mais brilhantes e aterrorizantes sobre a crueldade corporativa já filmadas."
        ],
        "ponte": "Má Sorte no Sexo ou Pornô Acidental, Toni Erdmann, Jean-Luc Godard e Ruben Östlund.",
        "recepcao": "Prêmio Especial do Júri no Festival de Locarno; eleito um dos cinco melhores filmes do ano pela Cahiers du Cinéma."
    },
    "2026-11--green-border": {
        "id": "2026-11--green-border",
        "edicao": "2026-11",
        "ordem": 12,
        "secao": "achados",
        "titulo": "A Fronteira Verde",
        "titulo_original": "Zielona granica",
        "autor": "Agnieszka Holland",
        "ano": 2023,
        "pais": "Polônia, França, República Tcheca, Bélgica",
        "tempo": "2h 32min",
        "genero": "drama / thriller humanitário",
        "tipo": "filme",
        "onde": "Plataformas digitais (Apple TV, Google Play, Prime Video)",
        "imdb": "tt27184936",
        "trailer_url": "https://www.youtube.com/results?search_query=Green+Border+Agnieszka+Holland+trailer",
        "olho": "Em preto e branco impiedoso, Agnieszka Holland denuncia a tragédia dos refugiados presos nos pântanos entre a Polônia e Belarus.",
        "texto": "Prêmio Especial do Júri no Festival de Veneza, um manifesto humanitário corajoso que enfrentou a fúria do governo de extrema-direita polonês.",
        "resenha": [
            "A diretora polonesa Agnieszka Holland (Europa Europa, Rastros) nunca teve medo de confrontar os poderes estabelecidos de sua época. Em A Fronteira Verde, ela coloca sua câmera no coração do pântano de Białowieża, na fronteira entre a Polônia e a ditadura de Belarus, onde milhares de refugiados sírios e afegãos são usados como armas humanas num jogo geopolítico sádico.",
            "Enganados pela propaganda de Lukashenko com a promessa de passagem fácil para a União Europeia, famílias inteiras são espancadas pela guarda de fronteira bielorrussa e empurradas através do arame farpado para a Polônia, onde os guardas poloneses os capturam e os jogam de volta na lama, num ciclo infernal de fome, hipotermia e morte.",
            "Holland constrói a narrativa sob quatro perspectivas entrelaçadas: uma família síria em fuga, uma psicóloga polonesa que decide agir ao lado de ativistas voluntários, um jovem guarda de fronteira em crise de consciência e militantes humanitários perseguidos pela polícia.",
            "Um soco no estômago indispensável sobre a hipocrisia das democracias europeias e a urgência de não normalizar a barbárie."
        ],
        "ponte": "Filhos da Esperança, Terra Queimada, Europa Europa e O Pântano.",
        "recepcao": "Prêmio Especial do Júri no Festival de Veneza; alvo de ataques inflamados do antigo governo polonês, transformando-se em símbolo de resistência democrática."
    },
    "2026-11--rotting-in-the-sun": {
        "id": "2026-11--rotting-in-the-sun",
        "edicao": "2026-11",
        "ordem": 13,
        "secao": "achados",
        "titulo": "Rotting in the Sun",
        "titulo_original": "Rotting in the Sun",
        "autor": "Sebastián Silva",
        "ano": 2023,
        "pais": "EUA, México",
        "tempo": "1h 49min",
        "genero": "comédia negra / suspense metaficcional",
        "tipo": "filme",
        "onde": "MUBI",
        "imdb": "tt21069698",
        "trailer_url": "https://www.youtube.com/results?search_query=Rotting+in+the+Sun+Sebastian+Silva+trailer",
        "olho": "O cineasta chileno Sebastián Silva e o comediante Jordan Firstman estrelam uma metassátira cínica sobre a futilidade dos influenciadores digitais.",
        "texto": "Um mistério de humor ácido na Cidade do México que explode quando a faxineira de Silva se vê envolvida num acidente fatal.",
        "resenha": [
            "Sebastián Silva é um mestre da comédia do constrangimento e da neurose urbana em filmes como A Criada e Crystal Fairy. Em Rotting in the Sun, ele leva a autoficção ao limite do escárnio ao interpretar a si mesmo: um cineasta chileno deprimido, viciado em cetamina e obcecado em ler Sobre a Brevidade da Vida de Sêneca enquanto passeia com seu cachorro pela Cidade do México.",
            "Durante uma viagem à praia gay de nudismo de Zicatela em Oaxaca, Silva quase se afoga no mar e é resgatado pelo influencer de redes sociais Jordan Firstman (também interpretando uma versão caricata de si mesmo). Firstman convence Silva a criar uma série cômica juntos, mas quando o influencer chega ao apartamento de Sebastián na Cidade do México para começar a produção, o diretor desapareceu sem deixar vestígios.",
            "O que começa como sátira cultural ao narcisismo de Instagram dá uma guinada radical para o suspense policial quando a leal empregada doméstica de Silva, Vero (Catalina Saavedra, formidável), assume o centro da tela em um jogo tenso de mentiras e dissimulações de classe.",
            "Um filme corrosivo, hilário e perversamente inteligente sobre a superficialidade contemporânea."
        ],
        "ponte": "A Criada (Sebastián Silva), Parasita (Bong Joon-ho), Festim Diabólico (Hitchcock) e Triangle of Sadness.",
        "recepcao": "Aclamação nos festivais de Sundance e Locarno; celebrado pelo humor irreverente e pela coragem metaficcional."
    },
    "2026-11--totem": {
        "id": "2026-11--totem",
        "edicao": "2026-11",
        "ordem": 14,
        "secao": "achados",
        "titulo": "Tótem",
        "titulo_original": "Tótem",
        "autor": "Lila Avilés",
        "ano": 2023,
        "pais": "México, Dinamarca, França",
        "tempo": "1h 35min",
        "genero": "drama familiar / crônica intimista",
        "tipo": "filme",
        "onde": "MUBI e Apple TV",
        "imdb": "tt26210452",
        "trailer_url": "https://www.youtube.com/results?search_query=Totem+Lila+Aviles+trailer",
        "olho": "Pelo olhar de uma menina de sete anos, a diretora mexicana Lila Avilés captura a beleza agridoce de uma festa familiar de despedida.",
        "texto": "Prêmio do Júri Ecumênico no Festival de Berlim, um dos retratos mais enternecedores e luminosos sobre luto e afeto familiar.",
        "resenha": [
            "A diretora mexicana Lila Avilés já havia demonstrado seu domínio milimétrico de espaços confinados em seu aclamado primeiro filme, A Camareira. Em Tótem, ela abre as portas de uma casa familiar caótica na Cidade do México ao longo de um único dia de preparativos para a festa de aniversário de Tona, um jovem pintor com câncer em estágio avançado.",
            "Acompanhamos tudo pelos olhos curiosos e atentos de Sol (Naíma Sentíes), a filha de sete anos de Tona. Enquanto tias, primos e avós cozinham bolos, realizam limpezas espirituais com fumaça para afastar energias ruins e discutem finanças médicas, Sol vaga pelos cômodos observando caracóis, insetos e a fragilidade silenciosa dos adultos.",
            "Avilés filma na proporção clássica de tela 4:3, aproximando os rostos e gerando uma intimidade calorosa que rejeita qualquer sentimentalismo barato. O filme celebra a vida com uma vitalidade desbordante: há risos, canções infantis e abraços desajeitados em meio à dor palpável do adeus.",
            "Uma joia cinematográfica de rara delicadeza humana que toca a alma com suavidade e verdade."
        ],
        "ponte": "O Espírito da Colmeia, Crepúsculo dos Deuses, A Camareira e Roma (Alfonso Cuarón).",
        "recepcao": "Prêmio do Júri Ecumênico no Festival de Berlim 2023; representante oficial do México no Oscar."
    },

    # --- SEÇÃO SÉRIES ---
    "2026-11--ripley": {
        "id": "2026-11--ripley",
        "edicao": "2026-11",
        "ordem": 15,
        "secao": "series",
        "titulo": "Ripley",
        "titulo_original": "Ripley",
        "autor": "Steven Zaillian",
        "ano": 2024,
        "pais": "EUA",
        "tempo": "Minissérie (8 episódios)",
        "genero": "suspense noir / thriller psicológico",
        "tipo": "serie",
        "onde": "Netflix",
        "imdb": "tt11016042",
        "trailer_url": "https://www.youtube.com/results?search_query=Ripley+Netflix+Zaillian+trailer",
        "olho": "Andrew Scott e Robert Elswit criam a adaptação definitiva de Patricia Highsmith em uma aula magistral de preto e branco, tensão e arquitetura italiana.",
        "texto": "Vencedora de múltiplos prêmios Emmy, esta obra-prima formalista transforma o assassinato em estudo sobre luz, sombra e quadros de Caravaggio.",
        "resenha": [
            "Esqueça o charme ensolarado de Jude Law e Matt Damon na versão cinematográfica de Anthony Minghella de 1999. O que o roteirista e diretor Steven Zaillian (A Lista de Schindler, The Night Of) realizou na minissérie Ripley da Netflix é uma das experiências estéticas mais rigorosas, frias e visualmente deslumbrantes da história da televisão contemporânea.",
            "Andrew Scott encarna Tom Ripley com um vazio interior gélido e metódico, operando pequenos golpes de cheque na Nova York chuvosa do início dos anos 1960 até ser contratado por um magnata do transporte marítimo para viajar à Itália e convencer seu filho playboy, Dickie Greenleaf (Johnny Flynn), a retornar para casa. A relação simbiótica e doentia entre Tom, Dickie e Marge Sherwood (Dakota Fanning) é tecida com lentidão calculada.",
            "O verdadeiro espetáculo da série é a fotografia em preto e branco do mestre Robert Elswit (Sangue Negro): cada escadaria em Atrani, cada estátua barroca em Roma, cada reflexo nas águas de Nápoles e Veneza é enquadrado com a precisão de um gravador renascentista. As pinturas sangrentas de Caravaggio tornam-se o espelho moral no qual Ripley contempla seus próprios crimes.",
            "Uma aula definitiva de cinema narrativo em oito capítulos que redefine o padrão visual da era do streaming."
        ],
        "ponte": "O Talentoso Ripley, Cidadão Kane, O Terceiro Homem e Sangue Negro.",
        "recepcao": "Vencedor de múltiplos prêmios Emmy, incluindo Melhor Direção para Steven Zaillian e Melhor Fotografia para Robert Elswit."
    },
    "2026-11--baby-reindeer": {
        "id": "2026-11--baby-reindeer",
        "edicao": "2026-11",
        "ordem": 16,
        "secao": "series",
        "titulo": "Bebê Rena",
        "titulo_original": "Baby Reindeer",
        "autor": "Richard Gadd",
        "ano": 2024,
        "pais": "Reino Unido",
        "tempo": "Minissérie (7 episódios)",
        "genero": "drama psicológico / suspense / comédia negra",
        "tipo": "serie",
        "onde": "Netflix",
        "imdb": "tt13649112",
        "trailer_url": "https://www.youtube.com/results?search_query=Baby+Reindeer+Netflix+trailer",
        "olho": "Richard Gadd adapta seu trauma real com perseguição obsessiva em uma minissérie corajosa que conquistou 6 prêmios Emmy.",
        "texto": "Jessica Gunning assombra no papel de Martha em uma dissecação impiedosa sobre carência afetiva, abuso e cumplicidade moral.",
        "resenha": [
            "Poucas produções causaram um terremoto cultural tão profundo nos últimos anos quanto Bebê Rena. Criada, escrita e protagonizada pelo comediante escocês Richard Gadd, a minissérie baseada em sua peça teatral solo no Edinburgh Fringe rejeita o formato convencional de histórias de perseguição (stalking) para realizar uma autópsia perturbadoramente honesta da cumplicidade da própria vítima em sua descida ao inferno.",
            "Donny Dunn (Gadd) é um aspirante a comediante de stand-up que trabalha atrás do balcão de um pub em Londres. Num dia qualquer, ele oferece uma xícara de chá gratuita a uma mulher solitária e obesa chamada Martha (Jessica Gunning). Esse simples ato de gentileza desencadeia uma obsessão maníaca: Martha envia mais de 41 mil e-mails, 350 horas de mensagens de voz e persegue Donny por anos.",
            "A grande sacada de Gadd é não transformar Martha num monstro bidimensional: ela é doente e perigosa, mas Donny, profundamente ferido por um abuso sexual anterior sofrido nas mãos de um roteirista de TV mais velho, alimenta a adulação de Martha para preencher o vazio de sua autoestima arruinada.",
            "O quarto episódio da série, em que Donny revisita o trauma do estupro, é um dos momentos mais devastadores e honestos já exibidos na televisão mundial."
        ],
        "ponte": "Louca Obsessão (Misery), Fleabag, I May Destroy You e BoJack Horseman.",
        "recepcao": "Consagração total com 6 prêmios Emmy em 2024, incluindo Melhor Minissérie, Roteiro, Ator para Gadd e Atriz Coadjuvante para Gunning."
    },
    "2026-11--disclaimer": {
        "id": "2026-11--disclaimer",
        "edicao": "2026-11",
        "ordem": 17,
        "secao": "series",
        "titulo": "Disclaimer",
        "titulo_original": "Disclaimer",
        "autor": "Alfonso Cuarón",
        "ano": 2024,
        "pais": "Reino Unido, EUA",
        "tempo": "Minissérie (7 episódios)",
        "genero": "suspense psicológico / drama moral",
        "tipo": "serie",
        "onde": "Apple TV+",
        "imdb": "tt16294384",
        "trailer_url": "https://www.youtube.com/results?search_query=Disclaimer+Alfonso+Cuaron+Apple+TV+trailer",
        "olho": "Cate Blanchett, Kevin Kline e Alfonso Cuarón unem forças em um thriller sobre reputação, narrativas concorrentes e culpa soterrada.",
        "texto": "Com fotografia compartilhada por Emmanuel Lubezki e Bruno Delbonnel, a série disseca como as histórias que contamos destroem vidas.",
        "resenha": [
            "O cineasta mexicano Alfonso Cuarón (Roma, Filhos da Esperança, Gravidade) escreveu e dirigiu todos os sete episódios de Disclaimer, adaptando o best-seller de Renée Knight com a escala formal de um longa-metragem de cinema de autor de sete horas de duração exibido em Veneza.",
            "Catherine Ravenscroft (Cate Blanchett, soberba em sua frieza aristocrática) é uma respeitada jornalista investigativa londrina famosa por expor as transgressões de figuras públicas. Sua vida desmorona quando ela recebe pelo correio um livro anônimo intitulado O Estranho Perfeito, apenas para descobrir com horror que a protagonista da história é ela mesma, e que o enredo revela um segredo sombrio de suas férias na Itália há vinte anos que ela jurava estar enterrado para sempre.",
            "O livro foi publicado pelo aposentado Stephen Brigstocke (Kevin Kline em seu melhor papel em décadas), o pai amargurado do rapaz que morreu naquelas mesmas férias, determinado a arruinar Catherine expondo-a para seu marido (Sacha Baron Cohen) e seu filho adulto.",
            "A montagem alternada entre três narradores em vozes gramaticais distintas (primeira, segunda e terceira pessoa) e a iluminação monumental de Lubezki e Delbonnel transformam o suspense em uma reflexão fascinante sobre viés de confirmação e mentiras convenientes."
        ],
        "ponte": "Tár, Anatomia de uma Queda, Roma e Garota Exemplar.",
        "recepcao": "Exibição especial aplaudida no Festival de Veneza 2024; aclamado pela crítica por seu rigor formal e duelo de atuações entre Blanchett e Kline."
    },
    "2026-11--cem-anos-de-solidao": {
        "id": "2026-11--cem-anos-de-solidao",
        "edicao": "2026-11",
        "ordem": 18,
        "secao": "series",
        "titulo": "Cem Anos de Solidão",
        "titulo_original": "Cien años de soledad",
        "autor": "Alex García López, Laura Mora",
        "ano": 2024,
        "pais": "Colômbia",
        "tempo": "Série (16 episódios em 2 partes)",
        "genero": "realismo mágico / drama épico / saga familiar",
        "tipo": "serie",
        "onde": "Netflix",
        "imdb": "tt27878848",
        "trailer_url": "https://www.youtube.com/results?search_query=Cien+anos+de+soledad+Netflix+trailer",
        "olho": "Filmada inteiramente na Colômbia com elenco local e bênção dos filhos de Gabo, a adaptação mais aguardada da literatura latino-americana.",
        "texto": "A fundação mítica de Macondo e a linhagem dos Buendía ganham vida com rigor histórico e deslumbre visual sem precedentes.",
        "resenha": [
            "Durante mais de meio século, Gabriel García Márquez recusou todas as ofertas de Hollywood para adaptar Cem Anos de Solidão ao cinema, sob o argumento inegociável de que o livro precisava ser filmado em espanhol, na Colômbia, e com o tempo necessário que apenas uma série épica de televisão de prestígio poderia comportar. Com a produção executiva de seus filhos Rodrigo e Gonzalo García, essa promessa finalmente se cumpre.",
            "Dirigida pelo cineasta argentino-mexicano Alex García López e pela talentosa diretora colombiana Laura Mora (Os Reis do Mundo), a série recria a lendária aldeia de Macondo desde suas origens, quando José Arcadio Buendía e Úrsula Iguarán desbravaram a selva fugindo de uma maldição ancestral, até a chegada das pedras de gelo trazidas pelo cigano Melquíades.",
            "O elenco formado exclusivamente por atores colombianos, muitos deles não-profissionais garimpados no interior do país, confere às falas a musicalidade exata do espanhol caribenho de Aracataca. A direção de arte e o design de figurino evitaram o pitoresco barato para construir um mundo telúrico onde mariposas amarelas, chuvas de flores e a febre do sono fluem com naturalidade orgânica.",
            "Um triunfo do audiovisual sul-americano que faz jus à maior obra literária do continente."
        ],
        "ponte": "Gabriel García Márquez, Pedro Páramo, Os Reis do Mundo e Fitzcarraldo.",
        "recepcao": "Aguardada como o maior evento cultural televisivo de 2024 na América Latina e no mundo hispânico."
    },
    "2026-11--slow-horses": {
        "id": "2026-11--slow-horses",
        "edicao": "2026-11",
        "ordem": 19,
        "secao": "series",
        "titulo": "Slow Horses",
        "titulo_original": "Slow Horses (Temporada 4)",
        "autor": "Will Smith (showrunner), Mick Herron (livros)",
        "ano": 2024,
        "pais": "Reino Unido",
        "tempo": "Série (6 episódios por temporada)",
        "genero": "espionagem / comédia ácida / suspense",
        "tipo": "serie",
        "onde": "Apple TV+",
        "imdb": "tt10231140",
        "trailer_url": "https://www.youtube.com/results?search_query=Slow+Horses+Season+4+trailer",
        "olho": "Gary Oldman em estado de graça como Jackson Lamb, o chefe nojento, brilhante e beberrão dos espiões rejeitados pelo MI5 britânico.",
        "texto": "A quarta temporada adapta 'Spook Street' com Hugo Weaving no elenco e eleva o humor britânico seco e o suspense de espionagem a patamares magistrais.",
        "resenha": [
            "Slow Horses é, sem sombra de dúvida, a série de espionagem mais consistente, inteligente e deliciosamente cáustica da televisão contemporânea. Ao adaptar os romances da série Slough House de Mick Herron, a produção da Apple TV+ desmontou o mito do agente secreto glamouroso à la James Bond para colocar no centro da cena os burocratas caídos em desgraça do serviço secreto britânico que cometem erros estúpidos e são condenados a carimbar papel em um prédio decrépito perto da estação de Barbican.",
            "Gary Oldman tem aqui um dos papéis de sua vida como Jackson Lamb: um veterano da Guerra Fria de meias furadas, cabelo ensebado e flatulências inoportunas que mascara uma mente tática genial sob uma carapaça de grosseria hilária. Seu desprezo pelos espiões sob seu comando é lendário, mas quando seus 'cavalos lentos' entram na mira de assassinos profissionais, Lamb se revela um predador letal.",
            "A quarta temporada foca na decadência mental do lendário ex-chefe David Cartwright (Jonathan Pryce), avô do agente River Cartwright (Jack Lowden), desencadeando um atentado com bombas em Londres orquestrado por um mercenário impiedoso vivido por Hugo Weaving.",
            "Roteiros sem gordura, diálogos que estalam de sarcasmo britânico e cenas de ação secas e brutais fazem de Slow Horses uma maratona irresistível."
        ],
        "ponte": "O Espião que Sabia Demais (John le Carré), The Wire e O Alfaiate do Panamá.",
        "recepcao": "Aclamação unânime com 98% no Rotten Tomatoes; indicações para Gary Oldman e Jack Lowden nos prêmios Emmy e BAFTA."
    },
    "2026-11--the-sympathizer": {
        "id": "2026-11--the-sympathizer",
        "edicao": "2026-11",
        "ordem": 20,
        "secao": "series",
        "titulo": "O Simpatizante",
        "titulo_original": "The Sympathizer",
        "autor": "Park Chan-wook, Don McKellar",
        "ano": 2024,
        "pais": "EUA, Vietnã, Coreia do Sul",
        "tempo": "Minissérie (7 episódios)",
        "genero": "espionagem satírica / drama histórico / humor negro",
        "tipo": "serie",
        "onde": "Max (HBO)",
        "imdb": "tt14440462",
        "trailer_url": "https://www.youtube.com/results?search_query=The+Sympathizer+HBO+trailer",
        "olho": "Dirigida pelo mestre Park Chan-wook, uma sátira cortante sobre identidade dividida pós-Guerra do Vietnã com Robert Downey Jr. em quatro papéis.",
        "texto": "Adaptação do romance vencedor do Pulitzer de Viet Thanh Nguyen com Hoa Xuande hipnotizante no papel do espião comunista duplo.",
        "resenha": [
            "A Guerra do Vietnã foi contada quase exclusivamente pela ótica dos veteranos e do cinema americano, de Apocalypse Now a Platoon. O Simpatizante inverte essa equação com inteligência satírica avassaladora ao adaptar o romance de estreia de Viet Thanh Nguyen, vencedor do Prêmio Pulitzer em 2016.",
            "O Capitão (Hoa Xuande, uma revelação absoluta) é um espião comunista meio-vietnamita, meio-francês que atua infiltrado no exército do Vietnã do Sul. Quando Saigon cai em abril de 1975, ele é obrigado a fugir para Los Angeles com o General (Toan Le), continuando a espionar a comunidade de refugiados e enviar relatórios codificados para Hanói com tinta invisível.",
            "Os três primeiros episódios dirigidos pelo cineasta sul-coreano Park Chan-wook (Oldboy, Decisão de Partir) são uma exibição de brilhantismo técnico: transições de câmera acrobáticas, humor mordaz e cores vibrantes. Robert Downey Jr. realiza um tour de force ao interpretar quatro representantes distintos do imperialismo ocidental: um agente cínico da CIA, um professor orientalista da UCLA, um congressista republicano linha-dura e um diretor de cinema megalomaníaco que lembra Francis Ford Coppola.",
            "Uma reflexão profunda sobre o exílio, a traição ideológica e a impossibilidade de pertencer plenamente a dois mundos em conflito."
        ],
        "ponte": "Decisão de Partir (Park Chan-wook), Apocalypse Now, O Americano Tranquilo e M.A.S.H..",
        "recepcao": "Aclamado pela crítica americana e asiática; indicação de Robert Downey Jr. ao Emmy."
    },

    # --- SEÇÃO BRASIL ---
    "2026-11--vidas-secas-4k": {
        "id": "2026-11--vidas-secas-4k",
        "edicao": "2026-11",
        "ordem": 21,
        "secao": "brasil",
        "titulo": "Vidas Secas (Restauração 4K)",
        "titulo_original": "Vidas Secas",
        "autor": "Nelson Pereira dos Santos",
        "ano": 2024,
        "pais": "Brasil",
        "tempo": "1h 43min",
        "genero": "drama / clássico do Cinema Novo",
        "tipo": "filme",
        "onde": "Cinemas (Circuito Estação Net / Cinemateca do MAM) e Globoplay",
        "imdb": "tt0057654",
        "trailer_url": "https://www.youtube.com/results?search_query=Vidas+Secas+Nelson+Pereira+dos+Santos+trailer",
        "olho": "A cópia restaurada em 4K da obra fundadora do Cinema Novo devolve à tela a brancura crua do sol do sertão fotografada por Luiz Carlos Barreto.",
        "texto": "Exibida com honras na seção Cannes Classics, a adaptação do romance de Graciliano Ramos é um patrimônio vivo e imorredouro da cultura nacional.",
        "resenha": [
            "Há filmes que o tempo não desgasta, apenas limpa as impurezas para revelar o diamante fundamental que há neles. Lançado originalmente em 1963, Vidas Secas de Nelson Pereira dos Santos sintetizou o lema do Cinema Novo — 'uma câmera na mão e uma ideia na cabeça' — com uma pureza estética e ética que continua a desarmar qualquer espectador.",
            "A nova restauração em 4K realizada pela Cinemateca Brasileira a partir dos negativos originais de 35mm recupera o brilho cegante da luz natural sem refletores capturada pelo diretor de fotografia Luiz Carlos Barreto no sertão de Alagoas. O céu sem nuvens, o estalar das galhas secas sob os pés descalços de Fabiano (Átila Iório) e Sinhá Vitória (Maria Ribeiro) e os passos lentos da cachorra Baleia ganham uma nitidez assombrosa.",
            "Nelson Pereira eliminou qualquer trilha musical convencional, deixando que o som rascante do eixo do carro de boi funcionasse como a única música possível daquele mundo onde o homem é diminuído pela brutalidade climática e pelo jugo dos latifundiários e da polícia.",
            "Rever Vidas Secas em tela grande no Rio de Janeiro é um compromisso cívico com a dignidade da nossa história e a beleza do nosso cinema mais corajoso."
        ],
        "ponte": "Graciliano Ramos, Deus e o Diabo na Terra do Sol, Terra em Transe e O Caminho das Nuvens.",
        "recepcao": "Seleção oficial Cannes Classics 2024; aplaudido de pé por cineastas e preservadores do mundo inteiro."
    },
    "2026-11--motel-destino": {
        "id": "2026-11--motel-destino",
        "edicao": "2026-11",
        "ordem": 22,
        "secao": "brasil",
        "titulo": "Motel Destino",
        "titulo_original": "Motel Destino",
        "autor": "Karim Aïnouz",
        "ano": 2024,
        "pais": "Brasil, França, Alemanha",
        "tempo": "1h 55min",
        "genero": "thriller erótico / noir tropical",
        "tipo": "filme",
        "onde": "Cinemas e plataformas digitais",
        "imdb": "tt28469812",
        "trailer_url": "https://www.youtube.com/results?search_query=Motel+Destino+Karim+Ainouz+trailer",
        "olho": "Neon azul e vermelho, suor e desejo à beira da rodovia cearense na volta de Karim Aïnouz ao cinema de autor rodado no Nordeste.",
        "texto": "Competição oficial de Cannes 2024, o filme traz Fábio Assunção, Nataly Rocha e Iago Xavier num triângulo perigoso de sexo e fuga.",
        "resenha": [
            "Após rodar o drama histórico britânico Firebrand com Alicia Vikander e Jude Law, o cineasta cearense Karim Aïnouz (Madame Satã, A Vida Invisível) sentiu a necessidade urgente de voltar para casa e sujar as mãos com a poeira, o calor e a sensualidade crua do litoral do Ceará. Motel Destino é a materialização desse desejo visceral.",
            "Hélio (o estreante Iago Xavier, de presença magnética), um jovem em fuga de uma gangue da periferia de Fortaleza após uma missão fracassada, encontra refúgio improvável trabalhando como faz-tudo no Motel Destino, um estabelecimento decadente de beira de estrada à beira do mar. Lá, ele se vê enredado numa teia de desejo e violência entre o proprietário violento Elias (Fábio Assunção em atuação ameaçadora) e sua esposa Dayana (Nataly Rocha), uma mulher aprisionada pelo casamento.",
            "A fotografia exuberante de Hélène Louvart banha os quartos de fórmica e espelhos com cores hipersaturadas de néon, criando uma atmosfera que lembra o cinema noir de James M. Cain transposto para as dunas e o vento quente do Nordeste brasileiro.",
            "Um thriller febril e carnal que celebra a juventude, a liberdade dos corpos e o poder de reinvenção contra a opressão."
        ],
        "ponte": "Madame Satã, O Céu de Suely, O Destino Bate à Sua Porta e Corpos Ardentes.",
        "recepcao": "Competição Oficial do Festival de Cannes 2024; aclamado pela crítica brasileira pelo frescor sensorial e atuações elétricas."
    },
    "2026-11--levante": {
        "id": "2026-11--levante",
        "edicao": "2026-11",
        "ordem": 23,
        "secao": "brasil",
        "titulo": "Levante",
        "titulo_original": "Levante",
        "autor": "Lillah Halla",
        "ano": 2023,
        "pais": "Brasil, França, Uruguai",
        "tempo": "1h 39min",
        "genero": "drama / esporte / juventude queer",
        "tipo": "filme",
        "onde": "Globoplay e Apple TV",
        "imdb": "tt26683884",
        "trailer_url": "https://www.youtube.com/results?search_query=Levante+Lillah+Halla+trailer",
        "olho": "Vencedor do Prêmio FIPRESCI na Semana da Crítica de Cannes, a energia contagiante de um time de vôlei queer e a luta pelo direito reprodutivo.",
        "texto": "Sofia (Ayomi Domenica) é uma atleta de 17 anos à beira de uma bolsa profissional que descobre uma gravidez indesejada.",
        "resenha": [
            "O filme de estreia da diretora Lillah Halla chegou como um vendaval no cinema nacional: em vez de tratar a gravidez indesejada e o tema do aborto através da tragédia paralisante, Levante aposta na força coletiva, na cumplicidade do esporte e no afeto queer de uma comunidade que se recusa a abandonar seus pares.",
            "Sofia (Ayomi Domenica, filha do rapper Mano Brown, numa estreia estrondosa) é a capitã talentosa de um time de vôlei juvenil de São Paulo prestes a disputar a final de um campeonato que pode lhe render uma bolsa internacional. Ao descobrir que está grávida num país onde o aborto é criminalizado, ela enfrenta a hostilidade de grupos fundamentalistas que passam a persegui-la dentro e fora das quadras.",
            "O grande trunfo do filme é o elenco coadjuvante que forma o time de vôlei: corpos dissidentes, negros e LGBTQIA+ que treinam juntos, dançam funk nas lajes e criam uma rede de proteção comunitária invencível contra o linchamento moral.",
            "Um filme vibrante, político e energizante, que mostra o cinema jovem brasileiro em seu momento de maior vitalidade e coragem."
        ],
        "ponte": "Retrato de uma Jovem em Chamas, Garotas (Céline Sciamma) e O Acontecimento (Audrey Diwan).",
        "recepcao": "Prêmio FIPRESCI da Crítica Internacional na Semana da Crítica de Cannes; premiado nos festivais de Biarritz e Rio."
    },
    "2026-11--estranho-caminho": {
        "id": "2026-11--estranho-caminho",
        "edicao": "2026-11",
        "ordem": 24,
        "secao": "brasil",
        "titulo": "Estranho Caminho",
        "titulo_original": "Estranho Caminho",
        "autor": "Guto Parente",
        "ano": 2023,
        "pais": "Brasil, Portugal",
        "tempo": "1h 23min",
        "genero": "drama / realismo fantástico / drama familiar",
        "tipo": "filme",
        "onde": "MUBI e plataformas digitais",
        "imdb": "tt27774892",
        "trailer_url": "https://www.youtube.com/results?search_query=Estranho+Caminho+Guto+Parente+trailer",
        "olho": "Grande vencedor do Festival de Tribeca com 4 prêmios principais, o reencontro absurdo e terno entre pai e filho confinados em Fortaleza.",
        "texto": "Lucas Limeira e Carlos Francisco brilham no longa que transforma o confinamento pandêmico em poesia visual sobre o tempo.",
        "resenha": [
            "Guto Parente é um dos cineastas mais inventivos e prolíficos da prolífica cena cinematográfica do Ceará. Em Estranho Caminho, consagrado historicamente no Festival de Tribeca em Nova York (onde levou Melhor Filme Internacional, Roteiro, Fotografia e Ator), ele parte da memória do início da pandemia para construir uma narrativa que ultrapassa qualquer conjuntura para falar sobre laços familiares partidos.",
            "David (Lucas Limeira), um jovem cineasta experimental que vive em Portugal, retorna a Fortaleza em março de 2020 para exibir um curta-metragem num festival. O fechamento repentino do país o impede de voltar a Lisboa, forçando-o a procurar seu pai, Geraldo (Carlos Francisco, de Bacurau e Marte Um), um homem excêntrico e recluso com quem ele não fala há mais de dez anos.",
            "O confinamento forçado no apartamento poeirento de Geraldo transforma-se num espaço de convivência insólita: barulhos estranhos nos encanamentos, objetos que mudam de lugar e conversas tardias sobre os mistérios da física e do cosmos.",
            "Um filme de beleza silenciosa e comovente que resgata a reconciliação entre gerações com delicadeza sem igual."
        ],
        "ponte": "Marte Um, O Som ao Redor, O Clube dos Canibais e Paterson (Jim Jarmusch).",
        "recepcao": "Vencedor dos prêmios de Melhor Longa Internacional, Roteiro, Fotografia e Ator (Carlos Francisco) no Festival de Tribeca 2023."
    },
    "2026-11--sem-coracao": {
        "id": "2026-11--sem-coracao",
        "edicao": "2026-11",
        "ordem": 25,
        "secao": "brasil",
        "titulo": "Sem Coração",
        "titulo_original": "Sem Coração",
        "autor": "Nara Normande, Tião",
        "ano": 2023,
        "pais": "Brasil, França, Itália",
        "tempo": "1h 31min",
        "genero": "drama / amadurecimento / romance juvenil",
        "tipo": "filme",
        "onde": "Netflix e plataformas digitais",
        "imdb": "tt28469800",
        "trailer_url": "https://www.youtube.com/results?search_query=Sem+Coracao+Nara+Normande+Tiao+trailer",
        "olho": "O verão de 1996 no litoral de Alagoas filmado com nostalgia mágica, sensualidade e a dor da passagem para a vida adulta.",
        "texto": "Exibido na seção Orizzonti de Veneza, o longa expande o premiado curta dos diretores com elenco jovem magnético.",
        "resenha": [
            "Ambientado no verão de 1996 na vila de pescadores de Guaxuma, em Alagoas, Sem Coração transporta o espectador para aquele instante frágil e inesquecível em que a infância se desfaz para dar lugar aos enigmas do desejo e da vida adulta. Os diretores Nara Normande e Tião expandiram seu aclamado curta-metragem homônimo de 2014 para criar um dos longas mais sensoriais do cinema nordestino contemporâneo.",
            "Tamara (Maya de Vicq) passa suas últimas semanas na praia com a turma de amigos antes de se mudar para Brasília para cursar o ensino médio. Entre mergulhos no mar verde, partidas de fliperama e festas à beira da fogueira, ela fica fascinada por uma garota local apelidada de 'Sem Coração' (Eduarda Samara), assim chamada por causa de uma cicatriz no peito decorrente de uma cirurgia cardíaca na infância.",
            "A relação que nasce entre as duas garotas de classes sociais distintas é construída por olhares tímidos, toques desajeitados e o fascínio mútuo pelo mar e pelos mistérios da natureza. A fotografia de Evgenia Alexandrova capta a maresia e o sal na pele com beleza pictórica de cinema de arquivo.",
            "Uma obra terna e nostálgica que pulsa com o calor das lembranças de um Brasil analógico que não volta mais."
        ],
        "ponte": "Guaxuma, Águas Claras, O Céu de Suely e Depois de Lúcia.",
        "recepcao": "Estreia mundial no Festival de Veneza 2023 (seção Orizzonti); Melhor Direção e Melhor Fotografia no Festival do Rio."
    },
    "2026-11--retrato-de-um-certo-oriente": {
        "id": "2026-11--retrato-de-um-certo-oriente",
        "edicao": "2026-11",
        "ordem": 26,
        "secao": "brasil",
        "titulo": "Retrato de um Certo Oriente",
        "titulo_original": "Retrato de um Certo Oriente",
        "autor": "Marcelo Gomes",
        "ano": 2024,
        "pais": "Brasil, Itália, Líbano",
        "tempo": "1h 48min",
        "genero": "drama histórico / ensaio poético / adaptação literária",
        "tipo": "filme",
        "onde": "Cinemas (Circuito Estação Net / Cine Joia) e plataformas",
        "imdb": "tt28469822",
        "trailer_url": "https://www.youtube.com/results?search_query=Retrato+de+um+Certo+Oriente+Marcelo+Gomes+trailer",
        "olho": "Marcelo Gomes adapta a obra-prima de Milton Hatoum em uma odisseia visual que une Beirute e a Amazônia nos anos 1940.",
        "texto": "Fotografado em preto e branco magistral, o filme celebra o encontro entre a imigração libanesa e os rios da floresta.",
        "resenha": [
            "O cineasta pernambucano Marcelo Gomes (Cinema, Aspirinas e Urubus, Viajo Porque Preciso, Volto Porque Te Amo) é um dos poetas mais inspirados da geografia afetiva no cinema brasileiro. Em Retrato de um Certo Oriente, ele aceitou o desafio monumental de levar às telas o clássico romance homônimo de Milton Hatoum, construindo uma ponte lírica entre o Mediterrâneo e a floresta amazônica.",
            "Filmado em um preto e branco exuberante que remete às fotografias históricas de época, o filme acompanha Emilie (Wafa'a Celine Halawi), uma jovem católica libanesa que embarca em 1949 em um navio de refugiados rumo ao Brasil ao lado de seu irmão Emir. Durante a viagem, Emilie se apaixona pelo comerciante muçulmano Omar, provocando uma fúria fratricida que culmina numa tragédia antes mesmo da chegada ao porto de Manaus.",
            "Gomes filma a chegada à selva com o olhar de estranhamento e assombro dos imigrantes: as águas escuras do Rio Negro, os cantos de pássaros desconhecidos e o choque cultural transformam Manaus numa Babel tropical onde árabes, indígenas e caboclos reescrevem suas identidades.",
            "Uma celebração audiovisual imensa da miscigenação e da memória que honra a literatura de Hatoum com sensibilidade rara."
        ],
        "ponte": "Milton Hatoum, Cinema Aspirinas e Urubus, Lavoura Arcaica e Dois Irmãos.",
        "recepcao": "Estreia triunfal no Festival Internacional de Cinema de Roterdã 2024; premiado no Festival de Gramado."
    },

    # --- SEÇÃO POP & AUTORAL DE GRANDE ESCALA ---
    "2026-11--duna-parte-2": {
        "id": "2026-11--duna-parte-2",
        "edicao": "2026-11",
        "ordem": 27,
        "secao": "pop",
        "titulo": "Duna: Parte 2",
        "titulo_original": "Dune: Part Two",
        "autor": "Denis Villeneuve",
        "ano": 2024,
        "pais": "EUA, Canadá",
        "tempo": "2h 46min",
        "genero": "ficção científica / épico / aventura",
        "tipo": "filme",
        "onde": "Max (HBO), Apple TV e Prime Video",
        "imdb": "tt15239678",
        "trailer_url": "https://www.youtube.com/results?search_query=Dune+Part+Two+official+trailer",
        "olho": "Denis Villeneuve entrega o ápice da ficção científica moderna: um épico brutal sobre o perigo dos mitos messiânicos e do fanatismo religioso.",
        "texto": "Timothée Chalamet, Zendaya e Austin Butler encabeçam uma experiência cinematográfica avassaladora de escala e design de som.",
        "resenha": [
            "Se o primeiro Duna (2021) preparou o tabuleiro com paciência e elegância arquitetônica, Duna: Parte 2 é a explosão vulcânica da tragédia imaginada por Frank Herbert em 1965. Denis Villeneuve provou categoricamente que é possível fazer cinema de grande escala para os maiores estúdios de Hollywood sem subestimar a inteligência, a sofisticação moral ou o paladar estético do público.",
            "Paul Atreides (Timothée Chalamet em atuação assombrosamente madura) é acolhido pelos Fremen no deserto de Arrakis ao lado de sua mãe Lady Jessica (Rebecca Ferguson). Ao aprender os costumes da areia e apaixonar-se pela guerreira Chani (Zendaya), Paul descobre que não pode conter a profecia messiânica plantada pela ordem Bene Gesserit, que o transforma no messias Muad'Dib à custa de uma guerra santa que promete incendiar o cosmos.",
            "A sequência na arena monocromática de Giedi Prime com o psicopata Feyd-Rautha Harkonnen (Austin Butler irreconhecível e aterrorizante) é uma das realizações visuais mais arrebatadoras da história do cinema de gênero, filmada com câmeras infravermelhas modificadas por Greig Fraser.",
            "Uma obra-prima incontestável do cinema de entretenimento inteligente que já garantiu seu lugar entre os maiores épicos de todos os tempos."
        ],
        "ponte": "Lawrence da Arábia, Apocalypse Now, Blade Runner 2049 e Star Wars (Trilogia Original).",
        "recepcao": "Aclamação crítica global esmagadora; bilheteria de mais de US$ 710 milhões e favorita absoluta às categorias técnicas do Oscar."
    },
    "2026-11--rivais": {
        "id": "2026-11--rivais",
        "edicao": "2026-11",
        "ordem": 28,
        "secao": "pop",
        "titulo": "Rivais",
        "titulo_original": "Challengers",
        "autor": "Luca Guadagnino",
        "ano": 2024,
        "pais": "EUA, Itália",
        "tempo": "2h 11min",
        "genero": "drama / comédia esportiva / romance erótico",
        "tipo": "filme",
        "onde": "Prime Video e Apple TV",
        "imdb": "tt16426418",
        "trailer_url": "https://www.youtube.com/results?search_query=Challengers+Luca+Guadagnino+trailer",
        "olho": "Zendaya, Josh O'Connor e Mike Faist eletrizam a tela num triângulo amoroso em que cada jogada de tênis é puro combate erótico.",
        "texto": "Com trilha eletrônica arrebatadora de Trent Reznor e Atticus Ross, Guadagnino transforma o esporte no melodrama mais sexy do ano.",
        "resenha": [
            "Luca Guadagnino (Me Chame Pelo Seu Nome, Suspiria) é um cineasta do desejo físico e da textura dos corpos em movimento. Em Rivais (Challengers), ele pegou um roteiro afiado de Justin Kuritzkes sobre o circuito profissional de tênis e o transformou em uma ópera eletrônica de suor, cinismo e obsessão triangular.",
            "Tashi Duncan (Zendaya, em sua melhor e mais autoritária performance no cinema) é uma ex-prodígio do tênis cuja carreira foi precocemente encerrada por uma grave lesão no joelho. Casada com Art Donaldson (Mike Faist), um campeão de Grand Slam em crise de confiança a quem ela treina com punho de ferro, Tashi o inscreve num humilde torneio Challenger na periferia de Nova York. Lá, Art descobre que seu adversário na final será Patrick Zweig (Josh O'Connor), seu melhor amigo de adolescência e antigo amante de Tashi.",
            "Guadagnino e o diretor de fotografia Sayombhu Mukdeeprom colocam a câmera dentro da própria bola de tênis, voando sobre a rede entre raquetadas cortadas no ritmo alucinante das batidas de house e techno compostas por Trent Reznor e Atticus Ross.",
            "Um filme pop puríssimo, inteligente e transbordante de vigor carnal que resgata a alegria do cinema de estúdio autoral."
        ],
        "ponte": "Match Point (Woody Allen), Me Chame Pelo Seu Nome, Jules e Jim e A Rede Social.",
        "recepcao": "Sucesso retumbante de público e crítica no mundo inteiro; trilha sonora aclamada como uma das melhores da década."
    },
    "2026-11--furiosa-uma-saga-mad-max": {
        "id": "2026-11--furiosa-uma-saga-mad-max",
        "edicao": "2026-11",
        "ordem": 29,
        "secao": "pop",
        "titulo": "Furiosa: Uma Saga Mad Max",
        "titulo_original": "Furiosa: A Mad Max Saga",
        "autor": "George Miller",
        "ano": 2024,
        "pais": "Austrália, EUA",
        "tempo": "2h 28min",
        "genero": "ação / ficção científica / aventura mitológica",
        "tipo": "filme",
        "onde": "Max (HBO), Apple TV e Prime Video",
        "imdb": "tt12037194",
        "trailer_url": "https://www.youtube.com/results?search_query=Furiosa+A+Mad+Max+Saga+trailer",
        "olho": "Aos 79 anos, George Miller dá mais uma aula definitiva de gramática de ação e mitologia operística no deserto australiano.",
        "texto": "Anya Taylor-Joy e Chris Hemsworth brilham no prelúdio épico que acompanha quinze anos de vingança e sobrevivência no ermo.",
        "resenha": [
            "Depois da perfeição cinética de Estrada da Fúria (2015), muitos duvidavam que George Miller pudesse voltar ao mesmo universo sem se repetir. A resposta veio em Furiosa: Uma Saga Mad Max, que em vez de emular a corrida contínua de dois dias do filme anterior, abraça a estrutura de uma tragédia grega em cinco capítulos cobrindo mais de quinze anos na vida da guerreira do deserto.",
            "Anya Taylor-Joy assume o papel imortalizado por Charlize Theron com uma fúria silenciosa concentrada no olhar, após ser sequestrada ainda criança do Verdejar das Muitas Mães pela horda de motoqueiros liderada pelo carismático e grotesco Dementus (Chris Hemsworth, entregando a melhor e mais desvairada atuação de sua carreira com uma capa vermelha e ursinho de pelúcia pendurado).",
            "A sequência de defesa do caminhão-tanque War Rig contra invasores com parapentes e motocicletas de esteira dura quase vinte minutos de puro balé de engenharia cinematográfica e cortes cirúrgicos comandados pela montadora Eliot Knapman.",
            "Um triunfo do cinema purista de ação e mito que comprova a vitalidade infinita de George Miller."
        ],
        "ponte": "Mad Max: Estrada da Fúria, Ben-Hur, Rastros de Ódio e O Guerreiro da Estrada.",
        "recepcao": "Estreia triunfal no Festival de Cannes 2024 com ovação de pé; aclamado pelos críticos como um clássico instantâneo do cinema de ação."
    },

    # --- SEÇÃO EM BREVE ---
    "2026-11--duna-parte-3": {
        "id": "2026-11--duna-parte-3",
        "edicao": "2026-11",
        "ordem": 30,
        "secao": "breve",
        "titulo": "Duna: Parte 3 (Messias de Duna)",
        "titulo_original": "Dune: Part Three",
        "autor": "Denis Villeneuve",
        "ano": 2026,
        "pais": "EUA, Canadá",
        "tempo": "Previsão: Dezembro de 2026",
        "genero": "ficção científica épica / tragédia política / hard sci-fi",
        "tipo": "filme",
        "onde": "Cinemas (IMAX e Salas Especiais)",
        "imdb": "tt31828376",
        "trailer_url": "https://www.youtube.com/results?search_query=Dune+Part+Three+Denis+Villeneuve+trailer",
        "olho": "Denis Villeneuve conclui sua trilogia colossal adaptando o livro mais sombrio de Frank Herbert sobre a tirania e a desilusão do messianismo.",
        "texto": "O filme acompanha Paul Atreides doze anos após a tomada do trono imperial, confrontando a guerra santa desencadeada em seu nome e as conspirações da Bene Gesserit.",
        "resenha": [
            "O fechamento da trilogia de Denis Villeneuve é um dos acontecimentos cinematográficos mais aguardados da ficção científica mundial. Ao adaptar Messias de Duna, Villeneuve subverte a clássica jornada do herói, expondo o custo humano e espiritual do fanatismo religioso e do controle ecológico.",
            "Timothée Chalamet e Zendaya retornam em atuações mais amadurecidas e trágicas, cercados pela opulência visual de Greig Fraser e o desenho sonoro imersivo de Hans Zimmer. A narrativa abandona o ritmo de aventura espacial para mergulhar em uma tragédia política palaciana de escala galáctica.",
            "Uma experiência obrigatória pensada para as maiores telas e o ápice do sci-fi autoral contemporâneo."
        ],
        "ponte": "Frank Herbert, Denis Villeneuve, 2001: Uma Odisseia no Espaço e Blade Runner 2049.",
        "recepcao": "Apontado pela imprensa especializada como o ápice visual e dramático do cinema de grande porte do final de 2026.",
        "capa": "capas/95a774ab9821004a58e311cc92eae99e.jpg",
        "imagem": "capas/95a774ab9821004a58e311cc92eae99e.jpg"
    },
    "2026-11--rosebush-pruning": {
        "id": "2026-11--rosebush-pruning",
        "edicao": "2026-11",
        "ordem": 31,
        "secao": "breve",
        "titulo": "Rosebush Pruning",
        "titulo_original": "Rosebush Pruning",
        "autor": "Karim Aïnouz",
        "ano": 2026,
        "pais": "Brasil, Itália, Alemanha",
        "tempo": "1h 55min (Estreia: Dezembro 2026)",
        "genero": "sátira política / drama psicológico / humor ácido",
        "tipo": "filme",
        "onde": "Circuito de cinema de arte e streaming MUBI",
        "imdb": "tt31735166",
        "trailer_url": "https://www.youtube.com/results?search_query=Rosebush+Pruning+Karim+Ainouz+trailer",
        "olho": "O cineasta brasileiro Karim Aïnouz comanda Elle Fanning, Callum Turner e Pamela Anderson em uma sátira mordaz sobre a decadência familiar das elites.",
        "texto": "Com roteiro assinado pelo grego Efthimis Filippou (parceiro habitual de Yorgos Lanthimos), o longa adapta livremente Os Punhos nos Bolsos de Bellocchio com humor corrosivo.",
        "resenha": [
            "Após brilhar na competição oficial dos maiores festivais internacionais, Karim Aïnouz consolida seu prestígio global com Rosebush Pruning. Ambientada no isolamento claustrofóbico de uma propriedade rural na Catalunha, a trama acompanha uma família abastada corroída por neuroses, privilégios parasitários e ressentimentos ocultos.",
            "A direção de arte suntuosa e a câmera precisa de Aïnouz transformam os jantares familiares em verdadeiros duelos dialéticos e teatrais, potencializados pelo texto desconcertante de Filippou.",
            "Elle Fanning e Callum Turner entregam performances magnéticas, enquanto Pamela Anderson surpreende em uma virada dramática cortante e madura."
        ],
        "ponte": "Karim Aïnouz, Yorgos Lanthimos, Marco Bellocchio e O Anjo Exterminador (Luis Buñuel).",
        "recepcao": "Destaque nos festivais de Berlim e Rio; elogiado pelo humor ferino e pela precisão cirúrgica na dissecação de privilégios de classe.",
        "capa": "capas/d7d714c27170944a01313b4f6740cba6.jpg",
        "imagem": "capas/d7d714c27170944a01313b4f6740cba6.jpg"
    },
    "2026-11--fatherland": {
        "id": "2026-11--fatherland",
        "edicao": "2026-11",
        "ordem": 32,
        "secao": "breve",
        "titulo": "Fatherland",
        "titulo_original": "Fatherland",
        "autor": "Paweł Pawlikowski",
        "ano": 2026,
        "pais": "Polônia, Reino Unido, França",
        "tempo": "1h 48min (Previsão: Dezembro 2026)",
        "genero": "drama histórico / cinema autoral / memória e política",
        "tipo": "filme",
        "onde": "Circuito Estação Net e Salas de Cinema de Arte",
        "imdb": "tt31735199",
        "trailer_url": "https://www.youtube.com/results?search_query=Fatherland+Pawel+Pawlikowski+trailer",
        "olho": "O vencedor do Oscar Paweł Pawlikowski (Ida, Guerra Fria) retorna com Sandra Hüller e August Diehl em uma investigação visceral sobre culpa histórica e nacionalismo.",
        "texto": "Filmado na habitual fotografia monocromática de enquadramentos milimétricos do diretor polonês, o filme investiga os fantasmas da Europa Central no pós-Segunda Guerra.",
        "resenha": [
            "Nenhum diretor contemporâneo domina a geometria moral e estética do plano em preto e branco como Paweł Pawlikowski. Em Fatherland, o cineasta volta seu olhar rigoroso para os dilemas éticos da reconstrução europeia.",
            "Sandra Hüller, uma das atrizes mais potentes do cinema mundial recente, contracena com August Diehl em uma espiral de cumplicidade e traição política, cercada pela trilha folk polonesa e jazz melancólico.",
            "Uma obra de imensa densidade estética e rigor formal que exige a experiência silenciosa e atenta das salas de cinema."
        ],
        "ponte": "Ida, Guerra Fria (Zimna Wojna), Andrzej Wajda e Michael Haneke.",
        "recepcao": "Fortemente cotado para os festivais de fim de ano e precursor da temporada internacional de premiações de 2027.",
        "capa": "capas/619064ec693b5d584a0bebbe7a84a57d.jpg",
        "imagem": "capas/619064ec693b5d584a0bebbe7a84a57d.jpg"
    },
    "2026-11--feito-pipa": {
        "id": "2026-11--feito-pipa",
        "edicao": "2026-11",
        "ordem": 33,
        "secao": "breve",
        "titulo": "Feito Pipa",
        "titulo_original": "Feito Pipa",
        "autor": "Allan Deberton",
        "ano": 2026,
        "pais": "Brasil",
        "tempo": "1h 42min (Estreia: Novembro/Dezembro 2026)",
        "genero": "drama brasileiro / cinema independente / laços de afeto",
        "tipo": "filme",
        "onde": "Cinemas e Mostras Nacionais",
        "imdb": "tt31735288",
        'trailer_url': "https://www.youtube.com/results?search_query=Feito+Pipa+Lazaro+Ramos+Allan+Deberton+trailer",
        "olho": "Lázaro Ramos protagoniza este drama sensível e luminoso gravado no interior do Nordeste sobre reconstrução pessoal, infância e pertencimento comunitário.",
        "texto": "Dirigido por Allan Deberton (Pacarrete), o filme foge dos estereótipos regionais para construir uma crônica humana intimista de profunda delicadeza.",
        "resenha": [
            "Feito Pipa reafirma a vitalidade do cinema brasileiro contemporâneo em retratar as geografias afetivas do país longe dos clichês dos grandes centros urbanos.",
            "Com uma atuação contida e tocante de Lázaro Ramos, o filme equilibra a aspereza do cotidiano com a poesia visual do voo das pipas, transformadas em metáfora de liberdade e libertação de traumas geracionais.",
            "Uma obra comovente que resgata a pureza da narrativa popular sem abrir mão do rigor estético e da autenticidade sonora."
        ],
        "ponte": "Pacarrete, Marte Um, Cinema, Aspirinas e Urubus e Central do Brasil.",
        "recepcao": "Aclamado pelo público e pela crítica nas primeiras mostras nacionais, com destaque para a trilha sonora e o elenco de apoio.",
        "capa": "capas/e1717f689b8a4a9b634bb2a177b326a2.jpg",
        "imagem": "capas/e1717f689b8a4a9b634bb2a177b326a2.jpg"
    }
}


CINE_GUIAS = {
    "guia-kleber-cinema-nordeste-2026": {
        "id": "guia-kleber-cinema-nordeste-2026",
        "edicao": "2026-11",
        "tipo": "roteiro de cinema",
        "titulo": "O cinema de Kleber Mendonça Filho e o novo cinema pernambucano",
        "subtitulo": "Cinco filmes essenciais para entender a renovação estética, política e arquitetônica do Recife nas telas do mundo.",
        "texto": (
            "Desde que 'O Som ao Redor' despertou a atenção internacional em 2012, o cinema pernambucano consolidou-se como "
            "o polo de invenção narrativa mais vigoroso do audiovisual brasileiro. Com o lançamento do consagrado 'O Agente Secreto', "
            "este roteiro percorre as tensões entre especulação imobiliária, violência de classe e memória histórica que redefiniram nossa cinematografia."
        ),
        "filmes": [
            {
                "titulo": "O Som ao Redor",
                "ano": 2012,
                "autor": "Kleber Mendonça Filho",
                "nota": "O microcosmo de uma rua de classe média em Boa Viagem revela as raízes escravocratas sob o verniz moderno da segurança privada.",
                "imdb": "tt2190367",
                "onde": "Netflix e Globoplay"
            },
            {
                "titulo": "Aquarius",
                "ano": 2016,
                "autor": "Kleber Mendonça Filho",
                "nota": "Sônia Braga monumental como Clara, a jornalista que recusa vender seu apartamento diante da chantagem da especulação imobiliária.",
                "imdb": "tt4990978",
                "onde": "Netflix e Apple TV"
            },
            {
                "titulo": "Bacurau",
                "ano": 2019,
                "autor": "Kleber Mendonça Filho e Juliano Dornelles",
                "nota": "Um faroeste distópico no sertão que virou manifesto internacional de resistência comunitária e soberania popular.",
                "imdb": "tt2762506",
                "onde": "Globoplay e Telecine"
            },
            {
                "titulo": "Retratos Fantasmas",
                "ano": 2023,
                "autor": "Kleber Mendonça Filho",
                "nota": "Documentário memorialístico deslumbrante sobre os antigos cinemas de rua do centro do Recife e a transformação da cidade.",
                "imdb": "tt26451634",
                "onde": "Netflix"
            },
            {
                "titulo": "Tatuagem",
                "ano": 2013,
                "autor": "Hilton Lacerda",
                "nota": "Irandhir Santos e Jesuíta Barbosa no calor do grupo teatral Chão de Estrelas durante a ditadura militar no Recife de 1978.",
                "imdb": "tt3089408",
                "onde": "Globoplay e MUBI"
            }
        ]
    },
    "guia-suspense-politico-resistencia-2026": {
        "id": "guia-suspense-politico-resistencia-2026",
        "edicao": "2026-11",
        "tipo": "roteiro de cinema",
        "titulo": "Vigilância, repressão e o thriller de resistência",
        "subtitulo": "Cinco filmes magistrais sobre indivíduos e famílias que desafiam sistemas autoritários e Estados policiais.",
        "texto": (
            "O suspense político ganha sua máxima voltagem dramática quando a câmera sai das salas de governo para registrar "
            "o impacto do medo nos lares comuns. Este guia reúne cinco obras-primas que investigam os mecanismos da vigilância civil e a coragem da dissidência."
        ),
        "filmes": [
            {
                "titulo": "A Conversação",
                "ano": 1974,
                "autor": "Francis Ford Coppola",
                "nota": "Gene Hackman é Harry Caul, o especialista em escutas que é tragado pela paranoia em uma das obras máximas do cinema americano.",
                "imdb": "tt0071360",
                "onde": "Plataformas digitais (Apple TV, MUBI)"
            },
            {
                "titulo": "A Vida dos Outros",
                "ano": 2006,
                "autor": "Florian Henckel von Donnersmarck",
                "nota": "Na Berlim Oriental de 1984, um capitão da Stasi é transformado pela escuta secreta da vida íntima de um dramaturgo e uma atriz.",
                "imdb": "tt0405094",
                "onde": "Max e Apple TV"
            },
            {
                "titulo": "Z",
                "ano": 1969,
                "autor": "Costa-Gavras",
                "nota": "O assassinato de um político de oposição desencadeia uma investigação eletrizante contra a junta militar grega.",
                "imdb": "tt0065234",
                "onde": "MUBI e Telecine Cult"
            },
            {
                "titulo": "Não Há Mal Algum",
                "ano": 2020,
                "autor": "Mohammad Rasoulof",
                "nota": "Urso de Ouro em Berlim, quatro contos devastadores sobre a pena de morte e a desobediência moral no Irã contemporâneo.",
                "imdb": "tt11756604",
                "onde": "MUBI"
            },
            {
                "titulo": "Cabra Marcado para Morrer",
                "ano": 1984,
                "autor": "Eduardo Coutinho",
                "nota": "Interrompido pelo golpe de 1964 e retomado vinte anos depois, o maior documentário político da história do cinema brasileiro.",
                "imdb": "tt0087023",
                "onde": "Globoplay e YouTube IMS"
            }
        ]
    },
    "guia-cinema-autoral-europeu-2026": {
        "id": "guia-cinema-autoral-europeu-2026",
        "edicao": "2026-11",
        "tipo": "roteiro de cinema",
        "titulo": "O novo cinema de autor europeu: silêncio e fricção social",
        "subtitulo": "Cinco títulos indispensáveis que rejeitam fórmulas fáceis para investigar as fraturas do continente contemporâneo.",
        "texto": (
            "Das margens da burocracia romena às florestas da Toscana e à Polônia em preto e branco, os grandes festivais europeus "
            "têm consagrado realizadores que desafiam a montagem convencional e a pressa contemporânea com rigor sensorial impecável."
        ),
        "filmes": [
            {
                "titulo": "Feliz como Lázaro",
                "ano": 2018,
                "autor": "Alice Rohrwacher",
                "nota": "Uma parábola poética e atemporal sobre a pureza de um camponês que desafia a passagem do tempo na Itália rural.",
                "imdb": "tt6752992",
                "onde": "Netflix"
            },
            {
                "titulo": "Toni Erdmann",
                "ano": 2016,
                "autor": "Maren Ade",
                "nota": "Um pai excêntrico tenta reconectar-se com sua filha corporativa em Bucareste numa das comédias mais geniais do século XXI.",
                "imdb": "tt4048272",
                "onde": "MUBI e Apple TV"
            },
            {
                "titulo": "Anatomia de uma Queda",
                "ano": 2023,
                "autor": "Justine Triet",
                "nota": "Palma de Ouro em Cannes, a autópsia de um casamento e dos limites da verdade em um tribunal nos Alpes franceses.",
                "imdb": "tt17009710",
                "onde": "Prime Video"
            },
            {
                "titulo": "Guerra Fria",
                "ano": 2018,
                "autor": "Paweł Pawlikowski",
                "nota": "Uma paixão impossível entre um músico e uma cantora através de duas décadas na Europa dividida pela Cortina de Ferro.",
                "imdb": "tt6543652",
                "onde": "MUBI e Prime Video"
            },
            {
                "titulo": "O Acontecimento",
                "ano": 2021,
                "autor": "Audrey Diwan",
                "nota": "Leão de Ouro em Veneza, a adaptação implacável do relato autobiográfico de Annie Ernaux na França dos anos 1960.",
                "imdb": "tt13880104",
                "onde": "Max e Apple TV"
            }
        ]
    }
}
