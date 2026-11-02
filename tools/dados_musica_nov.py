# -*- coding: utf-8 -*-
"""Dados editoriais de Música para a edição Nº 2 (Novembro 2026).
Contém 35 discos nas seções editoriais e 4 guias temáticos completos (22 discos nos guias).
"""

MUSICA_EDICAO = {
    "id": "2026-11",
    "numero": 2,
    "mes": "Novembro de 2026",
    "data": "2026-11-01",
    "manchete": "Guitarras de garage, poesia áspera e o pulso da cena independente",
    "editorial": (
        "A edição de novembro do Radar Musical mergulha nas texturas orgânicas e na fricção das guitarras: "
        "da visceralidade melódica de MJ Lenderman e Dry Cleaning aos ecos da renascença shoegaze britânica com Whitelands e DIIV, "
        "abrindo espaço para a coragem harmônica e rítmica da vanguarda brasileira com Juçara Marçal, Thais Nicodemo, "
        "Ana Frango Elétrico, Negro Léo e Sophia Chablau. Em tempos de produção higienizada por algoritmos de streaming, "
        "esta safra reúne discos que respiram sala de ensaio, amplificadores valvulados no talo e canções que não têm pressa de caber em fórmulas fáceis."
    ),
    "layout": [
        {"tipo": "secao", "secao": "radar"},
        {"tipo": "guia", "id": "guia-pos-punk-indie-2026"},
        {"tipo": "secao", "secao": "descobertas"},
        {"tipo": "guia", "id": "guia-shoegaze-reverb-2026"},
        {"tipo": "secao", "secao": "brasil"},
        {"tipo": "guia", "id": "guia-vanguarda-paulista-carioca-2026"},
        {"tipo": "secao", "secao": "breve"},
        {"tipo": "guia", "id": "guia-krautrock-artrock-2026"}
    ]
}

MUSICA_ITENS = {
    # --- SEÇÃO RADAR ---
    "2026-11--queens-of-the-stone-age-perfecth": {
        "id": "2026-11--queens-of-the-stone-age-perfecth",
        "edicao": "2026-11",
        "ordem": 1,
        "secao": "radar",
        "artista": "Queens of the Stone Age",
        "album": "Perfecth",
        "ano": 2026,
        "genero": "stoner rock / desert groove / art-rock",
        "selo": "Matador Records",
        "formato": "LP, Digital, CD",
        "olho": "Josh Homme reinventa o som do deserto com violões flamencos, tango sem bateria, Wurlitzer funkeado e o baixo fuzz mais cortante desde Songs for the Deaf.",
        "texto": "Recém-lançado no fim de outubro pela Matador, o nono álbum do Queens of the Stone Age quebra um ciclo e inaugura a fase mais vulnerável e corajosa da discografia de Josh Homme.",
        "resenha": [
            "Lançado em 30 de outubro de 2026 pela Matador Records, Perfecth é o aguardado nono álbum de estúdio do Queens of the Stone Age e representa a virada estética mais radical de Josh Homme em mais de duas décadas. Produzido por Homme e Michael Shuman e gravado nos lendários estúdios Sound City e Pink Duck em Los Angeles, o disco condensa nove faixas em enxutos 36 minutos, eliminando qualquer gordura ou repetição de fórmula.",
            "A grande surpresa reside no despojamento acústico e na inventividade rítmica. 'Easy Street', lançada como single de abertura, substitui a tradicional parede de amplificadores por um violão flamenco de sabor espanhol, palmas sincopadas e a voz sedutora de Nikki Lane em contraste com o vocal arrastado de Homme. Já 'Insignificant Other' aposta num groove desacelerado conduzido por piano elétrico Wurlitzer e guitarras limpas com falsete rasgado, enquanto 'Where the Goth Girls At?' faz explodir um baixo fuzz cortante e um refrão hipnótico.",
            "Composto e lapidado após a recuperação física e emocional de Homme e na esteira da turnê intimista gravada nas Catacumbas de Paris (Alive in the Catacombs), Perfecth olha de frente para o envelhecimento, as perdas e o renascimento com um cinismo elegante e desarmado. Em 'Sunday', faixa gestada ainda na época da parceria com Iggy Pop em Post Pop Depression, Homme alcança uma gravidade comovente, coroada por um solo melódico e econômico de Troy Van Leeuwen.",
            "Para quem tem o Queens of the Stone Age como pedra angular do cânone do rock, Perfecth é uma aula magna de desconstrução: o peso agora não vem do volume ensurdecedor, mas do espaço entre as notas, da tensão harmônica e do balanço sinuoso. Um dos grandes marcos fonográficos de 2026."
        ],
        "faixas": ["Easy Street", "Insignificant Other", "Where the Goth Girls At?", "Sunday", "Paper Machete", "Time & Place", "Emotion Sickness"],
        "recepcao": "Elogiado na NME (5/5), Uncut e Consequence como o disco mais audacioso e revigorante da banda desde Songs for the Deaf.",
        "ponte": "Kyuss, Radiohead, Them Crooked Vultures, Iggy Pop (Post Pop Depression) e Jack White.",
        "spotify_id": "5bwWqW9LN9wcyyNiOtqhFf",
        "spotify_url": "https://open.spotify.com/search/Queens%20of%20the%20Stone%20Age%20Perfecth",
        "capa": "capas/6ed0ec9e85e566afc81ef246358bbc31.jpg",
        "onde": "Matador Records, Spotify, Apple Music, YouTube Music, Bandcamp"
    },
    "2026-11--mj-lenderman-manning-fireworks": {
        "id": "2026-11--mj-lenderman-manning-fireworks",
        "edicao": "2026-11",
        "ordem": 1,
        "secao": "radar",
        "destaque": True,
        "artista": "MJ Lenderman",
        "album": "Manning Fireworks",
        "ano": 2024,
        "genero": "indie rock / alt-country / garage",
        "selo": "ANTI-",
        "formato": "LP, Digital",
        "olho": "Guitarras cruas, lirismo agridoce e refrões tortos que confirmam o compositor da Carolina do Norte como a voz mais singular do indie rock americano.",
        "texto": "Com Manning Fireworks, MJ Lenderman equilibra com precisão cirúrgica o humor autodepreciativo, a vulnerabilidade e os amplificadores valvulados no limite do feedback.",
        "resenha": [
            "Há uma tradição muito particular na música americana de homens comuns que transformam o fracasso cotidiano em crônica de alta literatura. MJ Lenderman, guitarrista da banda Wednesday e compositor radicado na Carolina do Norte, pertence a essa linhagem que vai de Warren Zevon e Neil Young a David Berman e Jason Molina. Em Manning Fireworks, seu quarto álbum solo e estreia pela prestigiosa ANTI-, ele atinge a maturidade plena ao dosar solos de lap-steel chorosos com riffs de Telecaster saturada em amplificadores Fender.",
            "As canções são povoadas por personagens à beira do colapso que insistem em piadas autodepreciativas: o sujeito que compra um relógio caro para ver o tempo passar mais rápido em 'Wristwatch', o fã que tenta imitar Ozzy Osbourne em 'Bark at the Moon' ou o narrador que assiste à decadência alheia no bar em 'Joker Lips'. A voz de Lenderman tem a aspereza e o cansaço de quem cantou a noite inteira com fumaça no pulmão, mas suas harmonias vocais com Karly Hartzman desarmam qualquer cinismo.",
            "Musicalmente, a produção gravada nos estúdios Drop of Sun em Asheville rejeita os truques digitais em favor de dinâmicas analógicas vívidas. O baixo de Ethan Baechtold anda com peso elástico, os pratos de bateria têm decaimento natural e cada solo de guitarra soa como se a madeira estivesse vibrando a dois metros do ouvinte. É um disco que sabe ser engraçado e profundamente triste na mesma estrofe.",
            "Manning Fireworks não é apenas o melhor trabalho de Lenderman; é um daqueles álbuns que redefinem o vocabulário das guitarras no rock contemporâneo. Essencial para quem sente falta de rock americano com alma, poeira de estrada e honestidade desarmante."
        ],
        "faixas": ["Manning Fireworks", "Joker Lips", "Rudolph", "Wristwatch", "She's Leaving You", "Bark at the Moon"],
        "recepcao": "Best New Music na Pitchfork (8.7), 5 estrelas no The Guardian e aclamação unânime como um dos discos fundamentais de 2024.",
        "ponte": "Neil Young & Crazy Horse, Silver Jews, Songs: Ohia, Wednesday e Parquet Courts.",
        "spotify_id": "5bwWqW9LN9wcyyNiOtqhFf",
        "spotify_url": "https://open.spotify.com/album/5bwWqW9LN9wcyyNiOtqhFf",
        "onde": "ANTI- Records, Bandcamp, Spotify, Apple Music"
    },
    "2026-11--dry-cleaning-new-long-walk": {
        "id": "2026-11--dry-cleaning-new-long-walk",
        "edicao": "2026-11",
        "ordem": 2,
        "secao": "radar",
        "artista": "Dry Cleaning",
        "album": "New Long Walk",
        "ano": 2026,
        "genero": "pós-punk / spoken word / art-rock",
        "selo": "4AD",
        "formato": "LP, Digital",
        "olho": "O quarteto londrino afia ainda mais suas linhas de baixo elásticas e guitarras cortantes em diálogo com a voz inexpressiva e hipnótica de Florence Shaw.",
        "texto": "Registrado com produção analógica, New Long Walk transforma o tédio urbano e os fragmentos de conversas cotidianas em crônicas de absurdo e elegância britânica.",
        "resenha": [
            "Poucas bandas surgidas na recente onda do pós-punk britânico conseguiram construir uma assinatura estética tão inconfundível quanto o Dry Cleaning. O segredo nunca esteve no volume fácil, mas no contraste tenso e fascinante entre uma seção rítmica sinuosa de pós-punk/dub e o monólogo impassível de Florence Shaw, que declama anotações de diário, anúncios de jornal e pensamentos aleatórios como se estivesse conversando consigo mesma numa fila de supermercado.",
            "Em New Long Walk, a banda expande o vocabulário estético de Stumpwork sem perder o veneno seco. O guitarrista Tom Dowse incorpora timbres mais texturais, ecos de shoegaze e palhetadas que lembram Television e The Fall, enquanto o baixista Lewis Maynard dita o andamento hipnótico com linhas grossas e melódicas.",
            "O humor de Shaw continua cirúrgico: observações sobre sapatos molhados, ansiedades corporais e a melancolia do transporte público londrino ganham dimensões filosóficas inesperadas quando colocadas contra o ataque contido da bateria de Nick Buxton. Em faixas como 'Gary Ashby' e 'Hot Penny Day', o quarteto prova que a spoken word pode ser tão viciante quanto um refrão pop chiclete.",
            "Um disco que cresce a cada audição atenta, recomendadíssimo para ouvir com fones de ouvido durante caminhadas solitárias pela cidade."
        ],
        "faixas": ["Kwenchy Kups", "Anna Calls From the Arctic", "Don't Press Me", "Hot Penny Day", "No Decent Shoes for Rain"],
        "recepcao": "Aclamado no The Wire, Uncut e Mojo como uma das vozes mais literárias da música britânica contemporânea.",
        "ponte": "The Fall, Life Without Buildings, Sonic Youth e Young Marble Giants.",
        "spotify_id": "2I0gIu10p9l6B5zF46H9Vw",
        "spotify_url": "https://open.spotify.com/album/2I0gIu10p9l6B5zF46H9Vw",
        "onde": "4AD, Spotify, Apple Music, Bandcamp"
    },
    "2026-11--fontaines-dc-romance": {
        "id": "2026-11--fontaines-dc-romance",
        "edicao": "2026-11",
        "ordem": 3,
        "secao": "radar",
        "artista": "Fontaines D.C.",
        "album": "Romance",
        "ano": 2024,
        "genero": "rock alternativo / pós-punk / art-rock",
        "selo": "XL Recordings",
        "formato": "LP, Digital",
        "olho": "Os dublinenses abraçam a grandiosidade sombria do rock dos anos 90 sem perder a fúria poética e política de Grian Chatten.",
        "texto": "Produzido por James Ford, Romance expande o território sônico da banda para territórios industriais, trip-hop e grunge apocalíptico.",
        "resenha": [
            "A trajetória do Fontaines D.C. desde a urgência de Dogrel (2019) até este monumental Romance (2024) é uma das evoluções mais impressionantes do rock da última década. Deixando para trás os limites estritos do post-punk revival irlandês, o quinteto de Dublin abraçou a ambição sonora do rock alternativo dos anos 90, dialogando abertamente com Deftones, The Cure, Primal Scream e o hip-hop sombrio do Massive Attack.",
            "Sob a batuta do produtor James Ford (Arctic Monkeys, Depeche Mode), faixas como 'Starburster' e 'Favourite' exibem guitarras gigantescas com afinações rebaixadas e batidas com suingue industrial, enquanto Grian Chatten cospe versos febris sobre desilusão política, o declínio do império ocidental e a necessidade visceral de encontrar ternura em meio ao caos.",
            "A transição para o selo XL Recordings deu à banda espaço para experimentar cordas cinematográficas, sintetizadores analógicos e uma produção que preenche cada centímetro do espectro sonoro sem parecer inchada. Chatten canta com uma urgência quase operística, mas ancorado na crueza das ruas de Dublin.",
            "Romance é o testemunho de uma banda no auge absoluto de suas capacidades técnicas e líricas, desafiando a premissa cansada de que o rock de guitarras perdeu a relevância cultural."
        ],
        "faixas": ["Romance", "Starburster", "Here's the Thing", "Desire", "In the Modern World", "Favourite"],
        "recepcao": "Classificado pela NME, Rolling Stone e Pitchfork como um dos melhores lançamentos do ano de 2024.",
        "ponte": "The Cure, Deftones, The Smashing Pumpkins e Joy Division.",
        "spotify_id": "3b9Q2z6w41A1aGv7q65w8X",
        "spotify_url": "https://open.spotify.com/album/3b9Q2z6w41A1aGv7q65w8X",
        "onde": "XL Recordings, Spotify, Bandcamp"
    },
    "2026-11--the-smile-cutouts": {
        "id": "2026-11--the-smile-cutouts",
        "edicao": "2026-11",
        "ordem": 4,
        "secao": "radar",
        "artista": "The Smile",
        "album": "Cutouts",
        "ano": 2024,
        "genero": "art-rock / krautrock / jazz experimental",
        "selo": "XL Recordings",
        "formato": "LP, Digital",
        "olho": "Thom Yorke, Jonny Greenwood e Tom Skinner entregam seu registro mais solto, intrincado e inventivo até hoje.",
        "texto": "Gravado nas mesmas sessões de Wall of Eyes, Cutouts surpreende por trazer rítmicas sincopadas de afrobeat, sintetizadores analógicos modulares e guitarras geométricas.",
        "resenha": [
            "Quando Thom Yorke e Jonny Greenwood se juntaram ao baterista Tom Skinner (Sons of Kemet) para fundar The Smile durante a pandemia, muitos imaginaram que se tratava apenas de um desvio temporário do Radiohead. Três álbuns depois, Cutouts prova que o trio desenvolveu uma identidade autônoma e vibrante, liberta do peso mitológico que cerca a banda-mãe.",
            "O grande diferencial de Cutouts está no casamento entre o virtuosismo polirrítmico de Skinner e as explorações modulares de Greenwood. Músicas como 'Zero Sum' e 'Eyes & Mouth' correm sobre batidas ágeis que lembram Fela Kuti e Tony Allen, enquanto arpejos de guitarra ultra-rápidos e sintetizadores analógicos criam uma sensação de labirinto cinético.",
            "Thom Yorke soa extraordinariamente relaxado e vocalmente audacioso, alternando seu falsete etéreo característico com inflexões rítmicas que flertam com o pós-punk e a eletrônica dos anos 90. Os arranjos de cordas da London Contemporary Orchestra surgem como rajadas de vento frio que cortam a arquitetura precisa das canções.",
            "Mais aventureiro que Wall of Eyes, Cutouts é uma aula magna de composição contemporânea que aponta caminhos férteis para a fusão entre rock, jazz e música eletrônica de vanguarda."
        ],
        "faixas": ["Foreign Spies", "Zero Sum", "Don't Get Me Started", "Bodies Laughing", "Eyes & Mouth"],
        "recepcao": "4.5 estrelas na AllMusic e destaque na Mojo e Stereogum.",
        "ponte": "Radiohead (fase In Rainbows / King of Limbs), Can, Sons of Kemet e Tortoise.",
        "spotify_id": "7o5415B5sR5qL8k0M3w2X1",
        "spotify_url": "https://open.spotify.com/search/The%20Smile%20Cutouts",
        "onde": "XL Recordings, Bandcamp, Spotify"
    },
    "2026-11--kim-gordon-the-collective": {
        "id": "2026-11--kim-gordon-the-collective",
        "edicao": "2026-11",
        "ordem": 5,
        "secao": "radar",
        "artista": "Kim Gordon",
        "album": "The Collective",
        "ano": 2024,
        "genero": "industrial noise / trap experimental / no wave",
        "selo": "Matador Records",
        "formato": "LP, Digital",
        "olho": "Aos 70 anos, a cofundadora do Sonic Youth implode os limites sonoros colidindo beats de 808 com paredes impiedosas de ruído.",
        "texto": "Produzido em parceria com Justin Raisen, The Collective soa mais moderno, agressivo e desorientador do que 99% das bandas jovens do circuito alternativo mundial.",
        "resenha": [
            "Existe uma coragem artística em Kim Gordon que pouquíssimos veteranos do rock dos anos 80 ousaram manter. Em The Collective, seu segundo álbum solo, ela não recorre a saudosismos do Sonic Youth; pelo contrário, apodera-se da estética rítmica do trap moderno, do industrial e do hip-hop sombrio para construir um manifesto sônico radical sobre o consumo, a hipervigilância e a alienação das redes sociais.",
            "Ao lado do produtor Justin Raisen (Lil Yachty, Yves Tumor), Gordon lança graves subaquáticos brutais de Roland TR-808 contra paredes de microfonia e distorção analógica. Em 'BYE BYE', ela declama uma lista interminável de itens de bagagem de mão sobre um beat arrastado e sufocante, transformando a banalidade da viagem de negócios numa elegia pós-humana.",
            "Sua voz sussurrada e fria funciona como uma lente de aumento para as bizarrices da modernidade tardia: compras de aspirador robô, sessões de meditação em aplicativos, filtros de selfie e ansiedades corporais. Não há melodias confortáveis aqui, apenas pulsos hipnóticos que sacodem as paredes da sala.",
            "Um dos registros mais chocantes e estimulantes do ano, que reafirma Kim Gordon como uma força da natureza inabalável da vanguarda nova-iorquina."
        ],
        "faixas": ["BYE BYE", "The Candy House", "I Don't Miss My Mind", "I'm a Man", "Trophies", "Shelf Warmer"],
        "recepcao": "Best New Music na Pitchfork (8.4), The Wire e Wire Magazine's Top Releases.",
        "ponte": "Sonic Youth, Suicide, Death Grips, Yves Tumor e Moor Mother.",
        "spotify_id": "0B1Nf8w5Q8k0M3w2X1Y4Z5",
        "spotify_url": "https://open.spotify.com/search/Kim%20Gordon%20The%20Collective",
        "onde": "Matador Records, Bandcamp, Spotify"
    },
    "2026-11--beth-gibbons-lives-outgrown": {
        "id": "2026-11--beth-gibbons-lives-outgrown",
        "edicao": "2026-11",
        "ordem": 6,
        "secao": "radar",
        "artista": "Beth Gibbons",
        "album": "Lives Outgrown",
        "ano": 2024,
        "genero": "chamber folk / experimental / baroque pop",
        "selo": "Domino",
        "formato": "LP, Digital",
        "olho": "A mítica voz do Portishead retorna em seu primeiro trabalho solo em mais de duas décadas, meditando sobre mortalidade, menopausa e tempo.",
        "texto": "Com produção de James Ford e Lee Harris (baterista do Talk Talk), Lives Outgrown utiliza instrumentos rústicos e percussões de madeira para criar uma obra-prima de beleza sombria.",
        "resenha": [
            "Passaram-se vinte e dois anos desde que Beth Gibbons lançou Out of Season (2002), sua memorável colaboração com Rustin Man. Durante esse intervalo, a cantora do Portishead manteve-se quase inteiramente reclusa, gravando esporadicamente a Sinfonia nº 3 de Henryk Górecki. Quando Lives Outgrown finalmente veio à tona, revelou-se não apenas um retorno, mas a obra mais íntima e devastadora de toda a sua trajetória.",
            "O álbum trata da passagem implacável dos anos: a perda de amigos queridos, o envelhecimento do corpo, as transformações da menopausa e a constatação da própria finitude. No entanto, em vez de recorrer aos timbres eletrônicos do trip-hop, Gibbons e seus coprodutores recorreram a violões acústicos com afinações incomuns, baquetas batendo em caixas de papelão, celos desfiados e flautas de madeira rústica.",
            "A bateria de Lee Harris (Talk Talk) confere às canções uma respiração orgânica que ecoa o seminal Spirit of Eden, enquanto a voz de Gibbons — que manteve sua capacidade única de expressar dor sem cair no melodrama — atinge notas de uma vulnerabilidade estarrecedora em faixas como 'Floating on a Moment' e 'Lost Changes'.",
            "Lives Outgrown é música para ser ouvida em silêncio absoluto numa noite fria, com a certeza de estar diante de um clássico instantâneo da canção europeia contemporânea."
        ],
        "faixas": ["Tell Me Who You Are Today", "Floating on a Moment", "Burden of Life", "Lost Changes", "Rewind", "Reaching Out"],
        "recepcao": "Classificado com nota 10/10 na Mojo e Uncut, e aclamação universal dos críticos da Pitchfork e Guardian.",
        "ponte": "Portishead, Talk Talk, Nick Drake, Vashti Bunyan e Judee Sill.",
        "spotify_id": "4jSmcj39eQiU76EbMGuxS9",
        "spotify_url": "https://open.spotify.com/search/Beth%20Gibbons%20Lives%20Outgrown",
        "onde": "Domino Recording Co., Bandcamp, Spotify"
    },
    "2026-11--english-teacher-this-could-be-texas": {
        "id": "2026-11--english-teacher-this-could-be-texas",
        "edicao": "2026-11",
        "ordem": 7,
        "secao": "radar",
        "artista": "English Teacher",
        "album": "This Could Be Texas",
        "ano": 2024,
        "genero": "art-punk / indie rock / chamber pop",
        "selo": "Island Records",
        "formato": "LP, Digital",
        "olho": "Vencedores do prestigiado Mercury Prize 2024, o quarteto de Leeds e Lancashire une poesia cortante, piano clássico e guitarras inquietas.",
        "texto": "Liderados pela vocalista e letrista Lily Fontaine, o English Teacher desafia a fórmula cinzenta do pós-punk britânico com sofisticação melódica e ironia política.",
        "resenha": [
            "Vencer o Mercury Prize com um disco de estreia tornou-se uma façanha rara no Reino Unido, mas This Could Be Texas, do quarteto English Teacher, justificou cada elogio da crítica especializada. Vindo de Leeds e Colne, o grupo liderado por Lily Fontaine recusa o minimalismo monocórdio de muitos de seus contemporâneos, costurando arranjos de piano de cauda, passagens orquestrais e súbitas explosões de math-rock.",
            "As letras de Fontaine investigam a complexidade de crescer birracial no norte pós-industrial da Inglaterra, cercada pelo declínio dos serviços públicos, pela gentrificação cultural e pela solidão dos apartamentos minúsculos. Em 'The World's Biggest Paving Slab', ela transforma uma calçada suburbana num monumento à obsolescência; em 'Albert Road', o crescendo de cordas culmina num grito coletivo arrebatador.",
            "A dinâmica entre o guitarrista Lewis Whiting, o baixista Nicholas Eden e o baterista Douglas Frost é surpreendentemente flexível, passando com naturalidade de baladas confessionais ao estilo de Black Country, New Road para ritmos marciais dignos de Gang of Four.",
            "Um disco fresco, ambicioso e profundamente literário que marca a chegada de uma das forças mais brilhantes da nova música inglesa."
        ],
        "faixas": ["Albatross", "The World's Biggest Paving Slab", "Broken Biscuits", "I'm Not Crying, You're Crying", "This Could Be Texas", "Albert Road"],
        "recepcao": "Vencedor do Mercury Prize 2024 de Melhor Álbum Britânico do Ano.",
        "ponte": "Black Country, New Road, Dry Cleaning, Pulp e Radiohead.",
        "spotify_id": "3lSmcj39eQiU76EbMGuxS1",
        "spotify_url": "https://open.spotify.com/search/English%20Teacher%20This%20Could%20Be%20Texas",
        "onde": "Island Records, Spotify, Apple Music"
    },
    "2026-11--mount-kimbie-the-sunset-violent": {
        "id": "2026-11--mount-kimbie-the-sunset-violent",
        "edicao": "2026-11",
        "ordem": 8,
        "secao": "radar",
        "artista": "Mount Kimbie",
        "album": "The Sunset Violent",
        "ano": 2024,
        "genero": "indie rock / pós-punk / dream-pop / eletrônica",
        "selo": "Warp Records",
        "formato": "LP, Digital",
        "olho": "A dupla britânica completa sua transição definitiva da eletrônica minimalista para o rock ensolarado e melancólico de guitarras.",
        "texto": "Gravado na Califórnia com participações de King Krule, The Sunset Violent abraça sintetizadores analógicos empoeirados e melodias preguiçosas e viciantes.",
        "resenha": [
            "Dominic Maker e Kai Campos começaram no fim dos anos 2000 como pioneiros do que a crítica chamava de post-dubstep, mas The Sunset Violent confirma o Mount Kimbie como uma banda de indie rock autêntica e altamente sofisticada. Agora expandidos para um quarteto com Andrea Balency-Béarn e Marc Pell, eles viajaram para o deserto de Yucca Valley, na Califórnia, para compor um disco impregnado pela luz dourada do fim de tarde.",
            "As guitarras são cheias de chorus e reverb, lembrando o pós-punk melódico do New Order e o shoegaze desbotado do Galaxie 500, mas a base rítmica carrega a precisão cirúrgica de quem passou anos programando sintetizadores e baterias eletrônicas. A colaboração com King Krule em 'Empty and Silent' e 'Boxing' adiciona a habitual aspereza existencial do ruivo londrino.",
            "Há uma doçura melancólica em faixas como 'Dumb & Fill Me Up' que funciona maravilhosamente bem para ouvir enquanto se dirige ou se contempla a cidade pela janela. O equilíbrio entre peso, leveza e groove é impecável.",
            "Um dos registros mais prazerosos e coesos da discografia do selo Warp em 2024."
        ],
        "faixas": ["The Trail", "Dumb & Fill Me Up", "Shipwreck", "Boxing (feat. King Krule)", "Fishbrain", "Empty and Silent"],
        "recepcao": "Elogiado na Pitchfork, Resident Advisor e Crack Magazine.",
        "ponte": "King Krule, New Order, Broadcast, Tirzah e Deerhunter.",
        "spotify_id": "5kSmcj39eQiU76EbMGuxS2",
        "spotify_url": "https://open.spotify.com/search/Mount%20Kimbie%20The%20Sunset%20Violent",
        "onde": "Warp Records, Bandcamp, Spotify"
    },

    # --- SEÇÃO DESCOBERTAS ---
    "2026-11--whitelands-sun-bleached-noise": {
        "id": "2026-11--whitelands-sun-bleached-noise",
        "edicao": "2026-11",
        "ordem": 9,
        "secao": "descobertas",
        "artista": "Whitelands",
        "album": "Sun-Bleached Noise",
        "ano": 2026,
        "genero": "shoegaze / dream-pop / ethereal wave",
        "selo": "Sonic Cathedral",
        "formato": "LP, Digital",
        "olho": "Camadas espessas de chorus e distorção com sensibilidade pop luminosa na melhor tradição de Cocteau Twins e Slowdive.",
        "texto": "Formado em Londres, o Whitelands injeta frescor e diversidade na cena shoegaze britânica com harmonias vocais etéreas e muralhas de eco.",
        "resenha": [
            "O selo londrino Sonic Cathedral tem sido o epicentro do renascimento shoegaze nos últimos anos, e o Whitelands é talvez a sua aposta mais entusiasmante. Formado por jovens músicos negros do sul de Londres — liderados pelo vocalista e guitarrista Etienne —, o grupo rompe com os velhos estereótipos demográficos do gênero sem abrir mão de suas fundações sonoras mais sagradas: pedais de fuzz, afinações abertas e oceanos de modulação.",
            "Em Sun-Bleached Noise, o quarteto equilibra a névoa sônica com melodias luminosas e refrões acolhedores que remetem ao dream-pop ensolarado do Lush e à melancolia contemplativa do Slowdive. A bateria não fica soterrada na mixagem; ela pulsa com clareza rítmica, sustentando o diálogo entre guitarras cintilantes.",
            "Faixas como 'Setting Sun' e 'The Prophet & I' tratam de amor juvenil, saúde mental e o cansaço de viver numa metrópole hostil, cantadas com uma doçura vocal que flutua graciosamente por cima do peso elétrico dos amplificadores.",
            "Um disco revigorante que prova que o shoegaze continua vivo, urgente e capaz de abraçar novos horizontes estéticos."
        ],
        "faixas": ["Setting Sun", "The Prophet & I", "Tell Me About It", "Cheer", "How it Feels", "Born in Understanding"],
        "recepcao": "Destaque no The Guardian, Stereogum e BBC Radio 6 Music.",
        "ponte": "Slowdive, Cocteau Twins, Ride, DIIV e Lush.",
        "spotify_id": "4vS4V9JtZtWj8x3J7xG4tD",
        "spotify_url": "https://open.spotify.com/album/4vS4V9JtZtWj8x3J7xG4tD",
        "onde": "Sonic Cathedral, Bandcamp, Spotify"
    },
    "2026-11--diiv-frog-in-boiling-water": {
        "id": "2026-11--diiv-frog-in-boiling-water",
        "edicao": "2026-11",
        "ordem": 10,
        "secao": "descobertas",
        "artista": "DIIV",
        "album": "Frog in Boiling Water",
        "ano": 2024,
        "genero": "shoegaze / pós-rock / slowcore / grunge",
        "selo": "Fantasy Records",
        "formato": "LP, Digital",
        "olho": "Cole Smith e sua banda entregam uma metáfora sombria sobre o colapso climático e social em riffs lentos, densos e hipnóticos.",
        "texto": "Com produção de Chris Coady, Frog in Boiling Water funde a afinação rebaixada do metal alternativo com a doçura melódica do dreampop.",
        "resenha": [
            "A fábula do sapo que não percebe que a água está esquentando até ser cozido vivo é a premissa conceitual que guia Frog in Boiling Water, quarto álbum de estúdio do DIIV. Deixando para trás as narrativas exclusivamente confessionais sobre sobriedade que marcaram Deceiver (2019), a banda do Brooklyn volta sua mira para o mal-estar civilizatório: o colapso ecológico, a brutalidade do capitalismo de vigilância e a apatia coletiva.",
            "A evolução musical é impressionante. Cole Smith e Andrew Bailey constroem teias de guitarras que utilizam afinações graves (drop D e C), criando um peso quase metálico que dialoga tanto com o Deftones de White Pony quanto com o slowcore melancólico do Duster e o shoegaze épico do Hum.",
            "Canções como 'Brown Paper Bag' e 'Soul-net' avançam como geleiras sonoras: lentas, majestosas e implacáveis. Os vocais soterrados de Smith soam como mensagens captadas por um rádio amador num cenário pós-apocalíptico, implorando por conexão humana genuína.",
            "Um dos registros de rock mais sérios, maduros e politicamente densos lançados em 2024."
        ],
        "faixas": ["In Amber", "Brown Paper Bag", "Raining on Your Pillow", "Frog in Boiling Water", "Everyone Out", "Soul-net"],
        "recepcao": "Nota 8.2 na Pitchfork, 4 estrelas na Kerrang! e aclamação no Stereogum.",
        "ponte": "Deceiver, Duster, Hum, Deftones e My Bloody Valentine.",
        "spotify_id": "2lSmcj39eQiU76EbMGuxS3",
        "spotify_url": "https://open.spotify.com/search/DIIV%20Frog%20in%20Boiling%20Water",
        "onde": "Fantasy Records, Bandcamp, Spotify"
    },
    "2026-11--friko-where-we-ve-been": {
        "id": "2026-11--friko-where-we-ve-been",
        "edicao": "2026-11",
        "ordem": 11,
        "secao": "descobertas",
        "artista": "Friko",
        "album": "Where we've been, Where we go from here",
        "ano": 2024,
        "genero": "indie rock / chamber rock / emo / pós-punk",
        "selo": "ATO Records",
        "formato": "LP, Digital",
        "olho": "A energia explosiva e os coros teatrais de Chicago que resgatam o dinamismo do indie rock da virada dos anos 2000.",
        "texto": "O duo de Chicago Niko Kapetan e Bailey Minzenberger entrega uma estreia fulgurante, alternando explosões ruidosas e orquestrações de câmara.",
        "resenha": [
            "De tempos em tempos surge uma banda que parece condensar toda a eletricidade e o desespero juvenil dos melhores momentos do rock independente. O Friko, projeto formado em Chicago por Niko Kapetan e pelo baterista Bailey Minzenberger, é exatamente isso. Em Where we've been, Where we go from here, lançado pela ATO Records, eles recuperam a urgência emocional e melódica de bandas como Arcade Fire (fase Funeral), Bright Eyes e The Walkmen.",
            "O vocal de Kapetan é um instrumento extraordinário: ele sussurra com intimidade desarmante ao piano para, segundos depois, berrar a plenos pulmões enquanto guitarras distorcidas e pratos explodem ao seu redor. A faixa de abertura, 'Where We've Been', sintetiza essa montanha-russa dinâmica com precisão cirúrgica.",
            "Além da potência do rock, há um cuidado camerístico refinado nos arranjos de cordas, cortesia de músicos convidados da rica cena clássica e avant-garde de Chicago. Canções como 'Crimson to Chrome' e 'Get Numb to It!' têm refrões que grudam na memória de imediato.",
            "Uma das estreias mais empolgantes do indie rock americano em muitos anos."
        ],
        "faixas": ["Where We've Been", "Crimson to Chrome", "Crashing Through", "For Ella", "Chemical", "Get Numb to It!"],
        "recepcao": "Destaque na Rolling Stone, Pitchfork e eleito um dos discos de estreia do ano pela Paste Magazine.",
        "ponte": "Arcade Fire, Bright Eyes, The Walkmen e Neutral Milk Hotel.",
        "spotify_id": "4myypnSDFC6PrjZRDYcBaC",
        "spotify_url": "https://open.spotify.com/album/4myypnSDFC6PrjZRDYcBaC",
        "onde": "ATO Records, Bandcamp, Spotify"
    },
    "2026-11--maruja-connla-s-well": {
        "id": "2026-11--maruja-connla-s-well",
        "edicao": "2026-11",
        "ordem": 12,
        "secao": "descobertas",
        "artista": "Maruja",
        "album": "Connla's Well",
        "ano": 2024,
        "genero": "jazz-punk / pós-rock / hardcore experimental",
        "selo": "Autoprodução / Cargo",
        "formato": "EP, Digital",
        "olho": "Saxofone ensandecido, baixo esmagador e fúria operária de Manchester num dos manifestos mais pesados da nova cena britânica.",
        "texto": "O quarteto de Manchester colide o jazz de John Coltrane com a violência do hardcore punk em faixas extensas e catárticas.",
        "resenha": [
            "Vindos dos bairros industriais de Manchester, o quarteto Maruja é uma daquelas anomalias que só a cena alternativa do norte da Inglaterra consegue produzir. Em Connla's Well, seu mais aclamado EP, eles dispensam concessões ao pop para criar uma muralha sonora visceral onde o saxofone alto de Joe Carroll não funciona como enfeite, mas como a principal arma melódica e ruidosa, duelando com a guitarra cortante de Harry Wilkinson.",
            "As canções são construídas sobre andamentos longos de pós-rock e jazz contemporâneo que subitamente deságuam em explosões de pura fúria hardcore. O vocalista Harry Wilkinson canta e grita sobre saúde mental, trauma intergeracional e a hipocrisia das elites políticas britânicas com uma intensidade física quase insuportável.",
            "A seção rítmica formada por Matt Buonaccorsi (baixo) e Jacob Hayes (bateria) tem uma musculatura impressionante, flertando com ritmos quebrados de trip-hop e d-beat punk sem perder o balanço hipnótico.",
            "Indispensável para quem acompanha a vanguarda do jazz-punk ao lado de Black Country, New Road e The Comet Is Coming."
        ],
        "faixas": ["The Invisible Man", "Connla's Well", "Zeitgeist", "One Hand Behind the Back", "Resisting Resistance"],
        "recepcao": "Top 10 EPs do ano na NME e cobertura apaixonada no The Needle Drop (Anthony Fantano).",
        "ponte": "Black Country, New Road, The Comet Is Coming, Godspeed You! Black Emperor e Fugazi.",
        "spotify_id": "1mSmcj39eQiU76EbMGuxS4",
        "spotify_url": "https://open.spotify.com/search/Maruja%20Connla%27s%20Well",
        "onde": "Bandcamp, Spotify, Apple Music"
    },
    "2026-11--cindy-lee-diamond-jubilee": {
        "id": "2026-11--cindy-lee-diamond-jubilee",
        "edicao": "2026-11",
        "ordem": 13,
        "secao": "descobertas",
        "artista": "Cindy Lee",
        "album": "Diamond Jubilee",
        "ano": 2024,
        "genero": "hypnagogic pop / girl group noir / lo-fi guitar",
        "selo": "Realistik Studios",
        "formato": "Álbum duplo, Digital",
        "olho": "Um monumento de duas horas de pop espectral dos anos 60 gravado em fita cassete pelo mentor do Women.",
        "texto": "Patrick Flegel assina uma obra-prima monumental lançada fora de todas as plataformas convencionais, celebrada como um divisor de águas da música independente.",
        "resenha": [
            "O lançamento de Diamond Jubilee foi um dos acontecimentos mais singulares e mitológicos da música recente. Recusando os contratos com os grandes serviços de streaming corporativo, Patrick Flegel (ex-guitarrista e vocalista do lendário grupo canadense Women) disponibilizou este álbum duplo de duas horas apenas em seu site pessoal, via download gratuito no GeoCities e no YouTube.",
            "A música que habita essas 32 faixas parece ter sido resgatada de uma estação de rádio fantasma transmitindo de 1963. Guitarras elétricas banhadas em eco de mola, harmonias vocais sussurradas de girl-groups à la The Ronettes e The Shangri-Las, e melodias de veludo noir que oscilam entre a mais doce ternura e a mais gélida desolação.",
            "Flegel é um dos guitarristas mais inventivos de sua geração: seus timbres limpos têm a limpidez dos primeiros discos da Motown, mas de repente são rasgados por solos de distorção estridente que lembram The Velvet Underground. Cada vinheta soa como uma memória esquecida numa fita cassete encontrada num brechó.",
            "Um monumento artístico colossal que desafiou toda a lógica da indústria contemporânea e venceu por puro mérito estético."
        ],
        "faixas": ["Diamond Jubilee", "Glitz", "Baby Blue", "Dreams of You", "All I Want Is You", "Dallas", "Kingdom Come"],
        "recepcao": "A nota mais alta concedida pela Pitchfork em quatro anos (9.1 - Best New Music) e cobertura histórica em jornais de todo o mundo.",
        "ponte": "Women, The Velvet Underground, Broadcast, The Ronettes e Ariel Pink.",
        "spotify_id": "6mSmcj39eQiU76EbMGuxS5",
        "spotify_url": "https://open.spotify.com/search/Cindy%20Lee%20Diamond%20Jubilee",
        "onde": "Realistik Studios, YouTube, Bandcamp"
    },

    # --- SEÇÃO BRASIL ---
    "2026-11--jucara-marcal-caderno-composicao": {
        "id": "2026-11--jucara-marcal-caderno-composicao",
        "edicao": "2026-11",
        "ordem": 14,
        "secao": "brasil",
        "artista": "Juçara Marçal & Thais Nicodemo",
        "album": "Caderno de Composição",
        "ano": 2026,
        "genero": "vanguarda paulista / canção contemporânea / experimental",
        "selo": "QTV Selo",
        "formato": "LP, Digital",
        "olho": "Voz vulcânica e piano contemporâneo reinventando canções raras de Itamar Assumpção, Negro Léo e temas autorais.",
        "texto": "Um dos registros mais densos e comoventes da música brasileira recente, gravado ao vivo na Sala Cecília Meireles no Rio de Janeiro.",
        "resenha": [
            "Poucas vozes na música brasileira contemporânea possuem a autoridade dramática e a inteligência estética de Juçara Marçal. Seja na encruzilhada de afro-punk do Metá Metá, seja nas colagens eletrônicas cortantes de Delta Estácio Blues (2021), Juçara canta como quem abre fendas na história colonial do país. Em Caderno de Composição, ela se junta à pianista e compositora Thais Nicodemo para um formato de câmara desarmado de qualquer concessão fácil.",
            "O piano de Nicodemo é uma força impressionante: técnica estendida, cordas percutidas com as mãos no interior do instrumento, acordes dissonantes de vanguarda que dialogam com Olivier Messiaen e Thelonious Monk, sem jamais abandonar o pulso da canção brasileira.",
            "O repertório é uma verdadeira aula de curadoria afetiva e política: pérolas esquecidas de Itamar Assumpção, temas tortos de Negro Léo e composições inéditas escritas em parceria pelas duas artistas. Juçara projeta sua voz com a solenidade de uma sacerdotisa e a fúria de uma mulher trabalhadora que recusa o silêncio.",
            "Gravado com excepcional fidelidade acústica, Caderno de Composição é um monumento à coragem interpretativa da canção brasileira independente."
        ],
        "faixas": ["Sem Nome", "Ladeira da Memória", "Fogo no Prato", "Canto Noturno", "Desejo de Terra", "Valsa Espiral"],
        "recepcao": "Aclamação unânime pela crítica nacional (APCA, O Globo, Bravo!) e turnês concorridas pelo circuito de teatros.",
        "ponte": "Metá Metá, Itamar Assumpção, Elza Soares, Negro Léo e Arrigo Barnabé.",
        "spotify_id": "43YyE328A9L8sC5f2F4B3Y",
        "spotify_url": "https://open.spotify.com/album/43YyE328A9L8sC5f2F4B3Y",
        "onde": "QTV Selo, Spotify, Apple Music, Bandcamp"
    },
    "2026-11--ana-frango-eletrico-ao-vivo-caixa": {
        "id": "2026-11--ana-frango-eletrico-ao-vivo-caixa",
        "edicao": "2026-11",
        "ordem": 15,
        "secao": "brasil",
        "artista": "Ana Frango Elétrico",
        "album": "Me Chama de Gato Que Eu Sou Sua (Edição Expandida)",
        "ano": 2025,
        "genero": "boogie carioca / sophisti-pop / indie MPB",
        "selo": "Selo Risco / Mr Bongo",
        "formato": "LP Duplo, Digital",
        "olho": "Metais aveludados, groove dos anos 70 e ironia carioca em arranjos que dialogam com Marcos Valle e Steely Dan.",
        "texto": "Após turnês consagradas na Europa e no Japão, a multi-instrumentista carioca apresenta novas versões ao vivo gravadas no Circo Voador.",
        "resenha": [
            "Ana Frango Elétrico (nome artístico de Ana Faria Fainguelernt) consolidou-se como a mente mais brilhante da produção musical carioca de sua geração. Seus trabalhos como produtora de Sophia Chablau e Bala Desejo já haviam chamado a atenção, mas Me Chama de Gato Que Eu Sou Sua elevou sua própria música a outro patamar de excelência técnica e aclamação internacional.",
            "O som é uma celebração exuberante do boogie carioca do final dos anos 70, com arranjos suntuosos de metais arranjados por Marlon Sette, linhas de baixo elásticas que fariam chorar Lincoln Olivetti e timbres analógicos de teclado Rhodes e sintetizadores Minimoog.",
            "As letras exploram a fluidez dos amores queer com uma leveza e uma malícia tipicamente cariocas em faixas irresistíveis como 'Electric Fish', 'Dela' e 'Insista em Mim'. A edição expandida traz gravações ao vivo viscerais registradas no Circo Voador com sua banda completa de 9 músicos.",
            "Música pop inteligente, dançante e impecavelmente gravada, indispensável em qualquer discoteca que preze o balanço e a elegância."
        ],
        "faixas": ["Electric Fish", "Dela", "Nuvem Vermelha", "Boy of Bebop", "Camelo Azul", "Insista em Mim", "Dr. Sabe Tudo"],
        "recepcao": "Disco do Ano pela APCA, indicação ao Grammy Latino e aclamação no The Guardian e Pitchfork.",
        "ponte": "Marcos Valle, Rita Lee, Steely Dan, Lincoln Olivetti e Arthur Verocai.",
        "spotify_id": "1B2u3vj33ZpE73v8t0Nnhz",
        "spotify_url": "https://open.spotify.com/album/1B2u3vj33ZpE73v8t0Nnhz",
        "onde": "Selo Risco, Mr Bongo, Spotify, Apple Music"
    },
    "2026-11--negro-leo-desejo-do-labirinto": {
        "id": "2026-11--negro-leo-desejo-do-labirinto",
        "edicao": "2026-11",
        "ordem": 16,
        "secao": "brasil",
        "artista": "Negro Léo",
        "album": "Desejo do Labirinto",
        "ano": 2024,
        "genero": "free funk / canção torta / jazz experimental carioca",
        "selo": "QTV Selo",
        "formato": "LP, Digital",
        "olho": "O pensador mais iconoclasta da canção contemporânea no Rio desconstrói ritmos urbanos em poesia filosófica voraz.",
        "texto": "Com guitarras angulares e sopros abrasivos, Desejo do Labirinto investiga o colapso cognitivo e a pulsão de sobrevivência no Rio de Janeiro.",
        "resenha": [
            "Não existe ninguém como Negro Léo na música brasileira. Nascido no Maranhão e forjado no caldeirão underground da Lapa e de Santa Teresa, ele construiu ao longo da última década uma obra singular que une o free jazz de Ornette Coleman, a canção fragmentada do Tropicalismo tardio e o batidão do funk carioca mais cru.",
            "Em Desejo do Labirinto, lançado pelo fundamental QTV Selo, ele aprofunda sua reflexão sobre o choque entre tecnologia digital, delírio conspiratório e a vida precária nas metrópoles do Sul global. As guitarras de Pedro Rocha e os teclados dissonantes criam um chão elástico onde as frases de Léo chegam cortantes.",
            "Sua métrica é única: versos que atropelam a quadratura tradicional para encaixar conceitos de filosofia política, gírias da Zona Norte e imagens de sonho e pesadelo urbano. Canções como 'Labirinto Fixo' e 'Corte Seco' operam como pequenos ensaios sonoros sobre a vertigem do presente.",
            "Um disco desafiador e essencial para quem procura música sem concessões, feita com inteligência e sangue na boca."
        ],
        "faixas": ["Labirinto Fixo", "Corte Seco", "Antena Paranoica", "Rua Sem Nome", "Voz de Fita", "Ouro Branco"],
        "recepcao": "Destaque nos cadernos de cultura do Rio e reverenciado por músicos como Caetano Veloso e Arnaldo Antunes.",
        "ponte": "Itamar Assumpção, Tom Zé, Ornette Coleman, Tantão e os Fita e Jorge Mautner.",
        "spotify_id": "43YyE328A9L8sC5f2F4B3Y",
        "spotify_url": "https://open.spotify.com/artist/6UKn12Sg5H3SyiFX5GalB6",
        "onde": "QTV Selo, Bandcamp, Spotify"
    },
    "2026-11--sophia-chablau-em-busca-da-batida": {
        "id": "2026-11--sophia-chablau-em-busca-da-batida",
        "edicao": "2026-11",
        "ordem": 17,
        "secao": "brasil",
        "artista": "Sophia Chablau e Uma Enorme Perda de Tempo",
        "album": "Música do Esquecimento",
        "ano": 2024,
        "genero": "noise pop / art-punk / canção paulistana",
        "selo": "Selo Risco",
        "formato": "LP, Digital",
        "olho": "Fúria juvenil, guitarras distorcidas e harmonias delicadas no retrato mais vívido da cena independente paulistana.",
        "texto": "Produzido por Dino Vicente, o quarteto de São Paulo expande os limites do indie rock brasileiro com liberdade formal e humor mordaz.",
        "resenha": [
            "Sophia Chablau e Uma Enorme Perda de Tempo provaram logo no disco de estreia (produzido por Ana Frango Elétrico) que tinham algo raro: a capacidade de fazer barulho ensurdecedor sem perder o coração da grande canção paulistana. Com Música do Esquecimento, eles chegam ao segundo álbum com uma maturidade de palco invejável.",
            "As guitarras de Sophia e Vicente Trench alternam melodias doces e dedilhados inspirados na Bossa Nova com explosões de distorção no-wave que lembram Sonic Youth e Os Mutantes no auge da loucura psicodélica. O baixo de Theo Chiri e a bateria de Gabriel Basile formam uma das seções rítmicas mais dinâmicas do rock nacional.",
            "As letras de Sophia traduzem com precisão quase documental as angústias de uma juventude urbana que lida com aluguéis abusivos, términos de relacionamento pelo WhatsApp e a sensação permanente de estar atrasada para um trem que já partiu.",
            "Um disco cativante, corajoso e cheio de personalidade que reafirma a vitalidade da cena independente brasileira."
        ],
        "faixas": ["Segredo", "Deus", "Quem Me Dera", "Baby", "O Que Você Quiser", "As Coisas São Assim"],
        "recepcao": "Aclamado na imprensa paulistana e presença constante nos festivais de música independente de todo o país.",
        "ponte": "Os Mutantes, Sonic Youth, Carne Doce, O Terno e Pato Fu.",
        "spotify_id": "7mSmcj39eQiU76EbMGuxS6",
        "spotify_url": "https://open.spotify.com/search/Sophia%20Chablau%20Musica%20do%20Esquecimento",
        "onde": "Selo Risco, Bandcamp, Spotify"
    },
    "2026-11--amaro-freitas-y-y": {
        "id": "2026-11--amaro-freitas-y-y",
        "edicao": "2026-11",
        "ordem": 18,
        "secao": "brasil",
        "artista": "Amaro Freitas",
        "album": "Y'Y",
        "ano": 2024,
        "genero": "jazz contemporâneo / piano preparado / música amazônica",
        "selo": "Psychic Hotline",
        "formato": "LP, Digital",
        "olho": "O pianista pernambucano mergulha nas águas e florestas amazônicas com piano preparado e polirritmias hipnóticas.",
        "texto": "Gravado em Manaus e produzido com participações de Shabaka Hutchings e Jeff Parker, Y'Y é uma obra-prima de espiritualidade e técnica.",
        "resenha": [
            "Amaro Freitas é um dos maiores embaixadores contemporâneos da cultura brasileira nos palcos do mundo. Vindo da periferia do Recife, ele revolucionou o piano de jazz ao cruzar o frevo, o maracatu e as polirritmias do Nordeste com o piano preparado de John Cage e a harmonia de Thelonious Monk. Em Y'Y (termo que significa 'água' ou 'rio' em língua sateré-mawé), ele volta sua escuta para a bacia amazônica.",
            "Inserindo sementes, tecidos, borrachas e peças metálicas entre as cordas de seu piano de cauda, Freitas transforma o teclado num ecossistema percussivo que imita o canto de pássaros, o gotejar da chuva e o ruído da correnteza dos rios Negro e Solimões.",
            "As participações do saxofonista britânico Shabaka Hutchings (flauta indígena) e do guitarrista americano Jeff Parker (Tortoise) em faixas como 'Uiara' e 'Gloriosa' enriquecem um álbum que é tanto uma homenagem aos povos originários quanto um tour de force pianístico.",
            "Uma experiência de audição transcendente que coloca a música instrumental brasileira na vanguarda do jazz global."
        ],
        "faixas": ["Mapinguari", "Uiara", "Dança dos Martelos", "Y'Y", "Mar de Rosas", "Encantados"],
        "recepcao": "Eleito um dos melhores álbuns de jazz de 2024 pelo The New York Times, DownBeat e The Guardian.",
        "ponte": "Hermeto Pascoal, Naná Vasconcelos, Shabaka Hutchings e John Cage.",
        "spotify_id": "8mSmcj39eQiU76EbMGuxS7",
        "spotify_url": "https://open.spotify.com/search/Amaro%20Freitas%20Y%27Y",
        "onde": "Psychic Hotline, Spotify, Bandcamp"
    },

    # --- SEÇÃO EM BREVE ---
    "2026-11--geese-live-third-man": {
        "id": "2026-11--geese-live-third-man",
        "edicao": "2026-11",
        "ordem": 19,
        "secao": "breve",
        "artista": "Geese",
        "album": "Live at Third Man Records",
        "ano": 2026,
        "genero": "art-punk / blues-rock / post-punk",
        "selo": "Third Man Records",
        "formato": "LP, Digital (Previsão: Dez/2026)",
        "olho": "A eletricidade ao vivo dos novos reis do rock novaiorquino capturada em fita analógica no estúdio de Jack White.",
        "texto": "Após a explosão de 3D Country, o quinteto do Brooklyn registra suas performances incandescentes gravadas direto em vinil em Nashville.",
        "resenha": [
            "O Geese protagonizou uma das viradas estéticas mais espetaculares dos últimos anos quando trocou o pós-punk sombrio da estreia pelo art-punk febril e teatral de 3D Country. A banda agora prepara um registro ao vivo capturado em fita analógica de duas polegadas na lendária Third Man Records de Jack White em Nashville.",
            "Quem assistiu ao grupo no palco sabe que suas apresentações têm a voltagem de um sermão evangélico conduzido por punks chapados de metanfetamina. O vocalista Cameron Winter canta como se Mick Jagger e Jeff Buckley estivessem possuídos pelo mesmo espírito caótico, improvisando falsetes e berros sobre grooves acelerados.",
            "O repertório do show inclui versões estendidas e ainda mais selvagens de 'Cowboy Nudes' e '3D Country', onde os duelos de guitarras de Emily Green e Foster Hudson atingem níveis de virtuosismo e sujeira irresistíveis.",
            "Um lançamento aguardadíssimo que promete se tornar o documento definitivo da força de palco da banda."
        ],
        "faixas": ["2122", "3D Country", "Cowboy Nudes", "I See Myself", "Mysterious Love", "Gravity Blues"],
        "recepcao": "Apresentação aclamada pelos críticos presentes e pré-vendas esgotadas em minutos.",
        "ponte": "Parquet Courts, Television, The Rolling Stones (fase Exile) e Black Midi.",
        "spotify_id": "4VqF3tU3Fw3k6nO0Lz2j9n",
        "spotify_url": "https://open.spotify.com/album/4VqF3tU3Fw3k6nO0Lz2j9n",
        "onde": "Third Man Records, Spotify"
    },
    "2026-11--panda-bear-sinister-grift": {
        "id": "2026-11--panda-bear-sinister-grift",
        "edicao": "2026-11",
        "ordem": 20,
        "secao": "breve",
        "artista": "Panda Bear",
        "album": "Sinister Grift",
        "ano": 2025,
        "genero": "psicodelia / pop barroco / lo-fi",
        "selo": "Domino",
        "formato": "LP, Digital (Previsão: Começo de 2025)",
        "olho": "Noah Lennox retorna a Lisboa para gravar um álbum construído ao redor de guitarras rústicas e harmonias vocais etéreas.",
        "texto": "Coproduzido por seu colega de Animal Collective, Josh Dibb (Deakin), Sinister Grift promete ser o trabalho mais acústico e confessional de Panda Bear em uma década.",
        "resenha": [
            "Desde que se mudou para Portugal há mais de quinze anos, Noah Lennox (Panda Bear) transformou sua casa em Lisboa num laboratório de pop psicodélico onde sintetizadores e samples colidem com harmonias no estilo The Beach Boys. Em Sinister Grift, ele dá um passo atrás nos computadores para colocar a guitarra de nylon e a bateria acústica no centro da sala.",
            "Com Deakin operando os gravadores, o disco foi registrado no estúdio caseiro de Lennox e traz canções que respiram a maresia atlântica e a brisa das colinas de Sintra. Os vocais em camadas continuam divinos, mas agora soam mais calorosos e vulneráveis.",
            "As letras refletem sobre maturidade, paternidade e a necessidade de cultivar a calma interior num planeta acelerado demais. As primeiras prévias apontam para um clássico instantâneo na linhagem de Person Pitch (2007).",
            "Fique atento: o primeiro grande disco de psicodelia de 2025 já tem data para aterrissar."
        ],
        "faixas": ["Praise", "Anywhere Outside", "50mg", "Ends Meet", "Ferry Lady", "Defence"],
        "recepcao": "Aguardado com enorme expectativa pela imprensa internacional e fãs de Animal Collective.",
        "ponte": "Animal Collective, The Beach Boys, Brian Wilson e Arthur Russell.",
        "spotify_id": "9mSmcj39eQiU76EbMGuxS8",
        "spotify_url": "https://open.spotify.com/search/Panda%20Bear%20Sinister%20Grift",
        "onde": "Domino Recording Co., Bandcamp, Spotify"
    }
,

"2026-11--adrianne-lenker-bright-future": {
        "id": "2026-11--adrianne-lenker-bright-future",
        "edicao": "2026-11",
        "ordem": 9,
        "secao": "radar",
        "artista": "Adrianne Lenker",
        "album": "Bright Future",
        "ano": 2024,
        "genero": "indie folk / avant-folk",
        "selo": "4AD",
        "formato": "LP, Digital",
        "olho": "Gravado diretamente em fita analógica de 1/2 polegada, o novo trabalho solo da vocalista do Big Thief é um monumento à imperfeição humana e à intimidade bruta.",
        "texto": "Com piano de feltro, violões descalços e harmonias de Nick Hakim e Mat Davidson, Bright Future atinge uma pureza poética rara.",
        "resenha": [
            "Adrianne Lenker possui a capacidade quase sobrenatural de fazer qualquer ouvinte se sentir a três centímetros de suas cordas vocais. Em Bright Future, gravado no estúdio analógico Double Infinity nas florestas de Massachusetts, ela dispensou qualquer edição digital: se um dedo escorregasse no traste ou a voz quebrasse de emoção, o take era mantido. Essa escolha radical dá ao disco uma respiração viva que contrasta dolorosamente com o pop contemporâneo plastificado.",
            "Faixas como 'Sadness As A Gift' e 'Ruined' tratam da dor do término e da transitoriedade do afeto não como tragédias definitivas, mas como presentes agridoces que atestam a nossa capacidade de sentir. Os arranjos de piano tocados por Nick Hakim têm o peso da chuva mansa batendo na janela de madeira.",
            "Ao longo das doze faixas, Lenker transita entre o sussurro confessional e o grito contido com a desenvoltura dos grandes mestres do folk americano, de Townes Van Zandt a Joni Mitchell, mas com um vocabulário moderno, desavergonhado e livre.",
            "Um dos registros mais comoventes e duradouros da década, que recompensa cada audição atenta com novas nuances de ruído e ternura."
        ],
        "faixas": ["Real House", "Sadness As A Gift", "Fool", "Free Treasure", "Vampire Empire", "Ruined"],
        "recepcao": "Best New Music na Pitchfork com nota 8.8; amplamente considerado um dos pontos mais altos da discografia de Lenker.",
        "ponte": "Big Thief, Joni Mitchell, Nick Drake, Vashti Bunyan e Lucinda Williams.",
        "spotify_id": "3Z8GgT0gqXbLpD0kLz2j9n",
        "spotify_url": "https://open.spotify.com/search/Adrianne%20Lenker%20Bright%20Future",
        "onde": "4AD, Spotify, Bandcamp"
    },
    "2026-11--nick-cave-wild-god": {
        "id": "2026-11--nick-cave-wild-god",
        "edicao": "2026-11",
        "ordem": 10,
        "secao": "radar",
        "artista": "Nick Cave & The Bad Seeds",
        "album": "Wild God",
        "ano": 2024,
        "genero": "art rock / gospel / post-punk",
        "selo": "Bad Seed Ltd / Play It Again Sam",
        "formato": "LP, Digital",
        "olho": "Após anos de luto austero, Nick Cave explode em júbilo bíblico, corais monumentais e o retorno da fúria dos Bad Seeds.",
        "texto": "Coproduzido por Cave e Warren Ellis nos estúdios Miraval na França, Wild God é uma celebração triunfal da resiliência espiritual.",
        "resenha": [
            "Depois da trilogia de travessia do luto composta por Skeleton Tree, Ghosteen e Carnage, muitos se perguntavam se Nick Cave algum dia voltaria a compor canções que explodissem com a fúria terrena dos Bad Seeds. Wild God responde a essa pergunta com um sim retumbante, mas de uma maneira totalmente inesperada: em vez do pessimismo gótico de outrora, o que move o novo álbum é um júbilo extático, quase profético.",
            "O piano de Cave e os sintetizadores granulados de Warren Ellis são envelopados por corais gospel e arranjos de cordas orquestrais que sobem como labaredas de fogo cósmico em faixas como 'Song of the Lake' e a faixa-título. A bateria de Thomas Wydler e o baixo de Colin Greenwood (Radiohead) conferem um pulso orgânico colossal que estava ausente nos trabalhos recentes.",
            "Liricamente, Cave caminha entre a memória dos filhos perdidos e a constatação milagrosa de que o mundo continua a girar com beleza implacável. Ele não nega a dor; transforma-a em combustível para uma liturgia de louvor à existência.",
            "Um disco monumental de uma banda veterana que se recusa categoricamente a viver de glórias passadas."
        ],
        "faixas": ["Song of the Lake", "Wild God", "Frogs", "Joy", "Conversion", "As the Waters Cover the Sea"],
        "recepcao": "Elogiado com cinco estrelas no The Guardian e The Independent; apontado como o melhor disco da banda desde Push the Sky Away.",
        "ponte": "Leonard Cohen, The Bad Seeds clássico, Scott Walker, gospel americano e Spiritualized.",
        "spotify_id": "4mSmcj39eQiU76EbMGuxS1",
        "spotify_url": "https://open.spotify.com/search/Nick%20Cave%20Wild%20God",
        "onde": "Bad Seed Ltd, PIAS, Spotify"
    },
    "2026-11--kim-deal-nobody-loves-you-more": {
        "id": "2026-11--kim-deal-nobody-loves-you-more",
        "edicao": "2026-11",
        "ordem": 11,
        "secao": "radar",
        "artista": "Kim Deal",
        "album": "Nobody Loves You More",
        "ano": 2024,
        "genero": "alt-rock / indie pop / chamber pop",
        "selo": "4AD",
        "formato": "LP, Digital",
        "olho": "A lendária baixista dos Pixies e líder dos Breeders finalmente entrega seu primeiro álbum solo com metais suntuosos e melodias cortantes.",
        "texto": "Gravado com a colaboração de Steve Albini em suas últimas sessões no Electrical Audio, o disco sintetiza quatro décadas de inteligência melódica.",
        "resenha": [
            "Poucas figuras encarnam a alma do rock alternativo com tanta graça, despretensão e elegância ríspida quanto Kim Deal. Dos graves elásticos que abriram caminho para 'Gigantic' nos Pixies à revolução ensolarada e distorcida do Breeders com Pod e Last Splash, sua assinatura sempre foi a concisão melódica. Nobody Loves You More, seu aguardado disco de estreia sob seu próprio nome, é um presente lapidado com infinita paciência ao longo de anos.",
            "O álbum surpreende ao incorporar arranjos ricos de metais, cordas de câmara e guitarras limpas, sem jamais abrir mão da crueza analógica. Gravado em Chicago no Electrical Audio do saudoso Steve Albini — colaborador de vida inteira de Kim —, cada instrumento tem presença física palpável, com pratos secos e baixos encorpados.",
            "Faixas como 'Crystal Breath' flertam com batidas eletrônicas tortas, enquanto 'Coast' e 'Are You Mine?' trazem aquela doçura agridoce que só Kim sabe entoar, cantando sobre praias de Massachusetts, cigarros e a passagem do tempo.",
            "Uma celebração calorosa da mulher que ensinou o rock dos anos 1990 a sorrir sem perder os dentes afiados."
        ],
        "faixas": ["Nobody Loves You More", "Coast", "Crystal Breath", "Are You Mine?", "Disobedience", "A Good Time Pushed"],
        "recepcao": "Aclamação crítica unânime nos EUA e Europa, destacando a longevidade e vigor autoral da compositora de Dayton.",
        "ponte": "The Breeders, Pixies, Throwing Muses, PJ Harvey e Sleater-Kinney.",
        "spotify_id": "5mSmcj39eQiU76EbMGuxS2",
        "spotify_url": "https://open.spotify.com/search/Kim%20Deal%20Nobody%20Loves%20You%20More",
        "onde": "4AD, Spotify, Apple Music"
    },
    "2026-11--mannequin-pussy-i-got-heaven": {
        "id": "2026-11--mannequin-pussy-i-got-heaven",
        "edicao": "2026-11",
        "ordem": 12,
        "secao": "radar",
        "artista": "Mannequin Pussy",
        "album": "I Got Heaven",
        "ano": 2024,
        "genero": "punk rock / grunge / screamo-pop",
        "selo": "Epitaph",
        "formato": "LP, Digital",
        "olho": "Fúria feminista, ganchos pop devastadores e riffs ensurdecedores no álbum de punk rock mais vibrante do ano.",
        "texto": "O quarteto da Filadélfia expande seu raio de alcance com produção de John Congleton, sem abrir mão de um milímetro de raiva.",
        "resenha": [
            "O punk rock contemporâneo muitas vezes cai na armadilha do saudosismo ou na esterilidade digital. O Mannequin Pussy, quarteto liderado pela incandescente Marisa Dabice, destrói ambos os clichês em I Got Heaven. Gravado com o produtor texano John Congleton (St. Vincent, Cloud Nothings), o disco equilibra momentos de fúria hardcore absoluta com refrões pop de arena que grudam na espinha como queimadura de pólvora.",
            "Em faixas como a abertura e 'Loud Bark', Dabice vocifera contra a hipocrisia religiosa, o controle dos corpos femininos e a mercantilização da dor, passando em segundos de um sussurro aveludado para um berro rasgado digno do riot grrrl dos anos 1990.",
            "A guitarra de Kaleen Reading e a bateria rápida mantêm uma tração frenética, mas o disco também ousa desacelerar em baladas pós-grunge carregadas de sintetizadores sutis, demonstrando uma maturidade composicional impecável.",
            "Uma injeção de adrenalina pura e necessária para chacoalhar qualquer complacência musical."
        ],
        "faixas": ["I Got Heaven", "Loud Bark", "Nothing Hurt", "Sometimes", "Softly", "Split/Desire"],
        "recepcao": "Nota 8.6 e Best New Music na Pitchfork; eleito o disco de rock do primeiro semestre por veículos como Stereogum e Kerrang!.",
        "ponte": "Bikini Kill, Sleater-Kinney, Yeah Yeah Yeahs e Idles.",
        "spotify_id": "6mSmcj39eQiU76EbMGuxS3",
        "spotify_url": "https://open.spotify.com/search/Mannequin%20Pussy%20I%20Got%20Heaven",
        "onde": "Epitaph Records, Spotify, Bandcamp"
    },
    "2026-11--jack-white-no-name": {
        "id": "2026-11--jack-white-no-name",
        "edicao": "2026-11",
        "ordem": 13,
        "secao": "radar",
        "artista": "Jack White",
        "album": "No Name",
        "ano": 2024,
        "genero": "garage rock / blues-punk",
        "selo": "Third Man Records",
        "formato": "LP, Digital",
        "olho": "Distribuído inicialmente em vinis anônimos nas sacolas de sua loja, o novo disco de Jack White é sua volta mais gloriosa às origens do White Stripes.",
        "texto": "Riffs cortantes, amplificadores no talo e urgência juvenil de quem redescobriu o prazer de plugar a guitarra e tocar alto.",
        "resenha": [
            "Jack White passou grande parte da última década experimentando com colagens sonoras, sintetizadores modulares e estruturas complexas em álbuns como Boarding House Reach. Embora fascinantes, esses desvios frequentemente ocultavam o que White faz melhor do que praticamente qualquer guitarrista vivo: extrair relâmpagos e trovões de três acordes de blues tocados numa Airline de fibra de vidro com um pedal Big Muff.",
            "No Name começou como um segredo de guerrilha: discos de vinil prensados sem capa nem créditos foram colocados sorrateiramente nas sacolas dos clientes que compravam na Third Man Records em Nashville e Londres. O boca a boca na internet fez o resto, revelando o álbum de garage rock mais musculoso, focado e eletrizante de White em duas décadas.",
            "Músicas como 'Old Scratch Blues', 'That's How I'm Feeling' e 'Bombing Out' têm o DNA selvagem de De Stijl e Elephant. A bateria pesada e as linhas de baixo primitivas servem de pista para solos em espiral que rangem nos falantes.",
            "A prova definitiva de que o rock de garagem, quando executado com convicção e sangue nos olhos, é imune ao envelhecimento."
        ],
        "faixas": ["Old Scratch Blues", "Bless Yourself", "That's How I'm Feeling", "It's Rough on Rats", "Archbishop Harold Holmes", "Bombing Out"],
        "recepcao": "Aclamado universalmente como o melhor trabalho solo de Jack White, resgatando a admiração de fãs das antigas e críticos exigentes.",
        "ponte": "The White Stripes, The Stooges, Led Zeppelin I e The Black Keys.",
        "spotify_id": "7mSmcj39eQiU76EbMGuxS4",
        "spotify_url": "https://open.spotify.com/search/Jack%20White%20No%20Name",
        "onde": "Third Man Records, Spotify, Apple Music"
    },
    "2026-11--jessica-pratt-here-in-the-pitch": {
        "id": "2026-11--jessica-pratt-here-in-the-pitch",
        "edicao": "2026-11",
        "ordem": 14,
        "secao": "radar",
        "artista": "Jessica Pratt",
        "album": "Here in the Pitch",
        "ano": 2024,
        "genero": "baroque pop / psychedelic folk / bossa noir",
        "selo": "Mexican Summer",
        "formato": "LP, Digital",
        "olho": "Bateria estilo Wall of Sound de Phil Spector, ecos de bossa nova e a voz espectral de Jessica Pratt num dos discos mais hipnóticos do ano.",
        "texto": "Após cinco anos de silêncio, a cantora californiana expande seus violões acústicos com tímpanos, saxofone e atmosfera de filme noir.",
        "resenha": [
            "O universo sonoro de Jessica Pratt sempre pareceu suspenso no tempo, como se tivesse sido gravado numa fita cassete empoeirada encontrada no sótão de uma mansão abandonada em Laurel Canyon em 1968. Mas em Here in the Pitch, seu primeiro álbum em cinco anos, ela dá um salto estético audacioso ao abandonar o isolamento acústico em favor de uma grandiosidade cinematográfica espectral.",
            "Inspirada na bateria marcial de Hal Blaine nas gravações clássicas dos Ronettes e na melancolia solar de Astrud Gilberto e Nara Leão, Pratt costura percussões abafadas, órgãos Farfisa e metais ocasionais sob sua voz peculiar, que desliza entre o registro infantil e a sabedoria ancestral.",
            "Em 'Life Is', a faixa de abertura, a bateria tropeça num ritmo envolvente enquanto cordas fantasmagóricas anunciam a chegada de uma narradora que encara o absurdo da existência com ironia refinada. Já 'World on a String' e 'The Last Year' soam como canções de ninar para o fim dos tempos.",
            "Um disco curto (apenas 27 minutos), mas de densidade estética assombrosa, feito sob medida para audições noturnas em fones de alta fidelidade."
        ],
        "faixas": ["Life Is", "Better Hate", "World on a String", "Get Won't Turn Around", "Nowhere It Was", "The Last Year"],
        "recepcao": "Best New Music e nota 8.8 na Pitchfork; eleito unanimemente um dos três melhores álbuns de 2024 por veículos britânicos e americanos.",
        "ponte": "Astrud Gilberto, Broadcast, Nico, Linda Perhacs e The Beach Boys.",
        "spotify_id": "8mSmcj39eQiU76EbMGuxS5",
        "spotify_url": "https://open.spotify.com/search/Jessica%20Pratt%20Here%20in%20the%20Pitch",
        "onde": "Mexican Summer, Bandcamp, Spotify"
    },

    # --- DESCOBERTAS ADICIONAIS ---
    "2026-11--been-stellar-scream-from-new-york-ny": {
        "id": "2026-11--been-stellar-scream-from-new-york-ny",
        "edicao": "2026-11",
        "ordem": 15,
        "secao": "descobertas",
        "artista": "Been Stellar",
        "album": "Scream from New York, NY",
        "ano": 2024,
        "genero": "post-punk / shoegaze / indie rock",
        "selo": "Dirty Hit",
        "formato": "LP, Digital",
        "olho": "Paredes de guitarras abrasivas, melancolia urbana e a fúria da juventude que tenta sobreviver ao custo de vida de Nova York.",
        "texto": "Produzido por Dan Carey em Londres, a estreia do quinteto novaiorquino cruza Sonic Youth com a urgência melódica do The Strokes.",
        "resenha": [
            "Não faltam bandas que tentaram recriar o mito de Nova York como a meca do rock alternativo, mas poucos grupos recentes conseguiram traduzir a claustrofobia real da cidade com tanta fidelidade sonora quanto o Been Stellar. Composto por jovens que se conheceram na NYU e dividiram apartamentos minúsculos no Brooklyn, o quinteto construiu uma linguagem onde as guitarras entrelaçadas alternam entre a violência do noise rock e a vulnerabilidade do shoegaze.",
            "A produção de Dan Carey (Fontaines D.C., Black Midi) confere ao álbum uma pegada rítmica devastadora. A bateria de Laila Way é ágil e contundente, enquanto os guitarristas Skyler St. Marx e Nando Dale tecem arpejos que soam como sirenes distantes ecoando entre arranha-céus cinzentos.",
            "O vocalista Sam Slocum canta sobre a solidão em vagões de metrô lotados, o esgotamento dos trabalhos precários e a sensação de que o futuro foi cancelado antes mesmo de começar. Canções como 'Passing Train' e 'All In One' têm o impacto emocional de um clássico instantâneo.",
            "Um disco vigoroso que recoloca a metrópole americana no mapa do pós-punk contemporâneo."
        ],
        "faixas": ["Start Again", "Passing Train", "Pumpkin", "Scream from New York, NY", "Sweet", "All In One"],
        "recepcao": "Elogiado calorosamente pelo NME, DIY Magazine e The Line of Best Fit como uma das estreias mais promissoras da temporada.",
        "ponte": "Sonic Youth, The Strokes, Fontaines D.C., Interpol e My Bloody Valentine.",
        "spotify_id": "1mSmcj39eQiU76EbMGuxS6",
        "spotify_url": "https://open.spotify.com/search/Been%20Stellar%20Scream%20from%20New%20York%2C%20NY",
        "onde": "Dirty Hit, Spotify, Apple Music"
    },
    "2026-11--hotline-tnt-cartwheel": {
        "id": "2026-11--hotline-tnt-cartwheel",
        "edicao": "2026-11",
        "ordem": 16,
        "secao": "descobertas",
        "artista": "Hotline TNT",
        "album": "Cartwheel",
        "ano": 2024,
        "genero": "shoegaze / fuzz pop / indie rock",
        "selo": "Third Man Records",
        "formato": "LP, Digital",
        "olho": "Guitarras ensurdecedoramente distorcidas envelopando melodias pop irresistíveis que grudam na cabeça por dias.",
        "texto": "Will Anderson lidera uma máquina de decibéis e ganchos melódicos na vanguarda da nova onda shoegaze americana.",
        "resenha": [
            "A grande sacada do Hotline TNT, projeto capitaneado pelo cantor e compositor Will Anderson, é entender que você pode colocar uma parede impenetrável de distorção de fuzz na cara do ouvinte e ainda assim fazê-lo cantar o refrão na primeira audição. Cartwheel, seu álbum de estreia pela Third Man Records, é uma aula de como casar o peso sônico do shoegaze com a sensibilidade melódica do power pop dos anos 1990.",
            "Gravado em várias sessões entre Minneapolis e Nova York, o álbum tem aquele som de quarto de ensaio onde os amplificadores estão tão quentes que você quase sente o cheiro dos circuitos queimando. As guitarras não criam texturas etéreas; elas marcham como tratores de som sobre batidas de bateria concisas e secas.",
            "Liricamente, Anderson trata de amores de verão, mensagens não respondidas e a preguiça sublime de tardes sem nada para fazer, tudo embalado por harmonias vocais ensolaradas que emergem da névoa de decibéis em faixas como 'Protocol' e 'I Thought You'd Change'.",
            "Uma celebração descarada do volume alto que faz qualquer amante de guitarras sorrir imediatamente."
        ],
        "faixas": ["Protocol", "I Thought You'd Change", "Beauty School", "Maxine", "Out of Time", "Spot Me"],
        "recepcao": "Best New Music na Pitchfork e presença constante nas listas de melhores de rock alternativo do ano.",
        "ponte": "Teenage Fanclub, My Bloody Valentine, Dinosaur Jr. e Swervedriver.",
        "spotify_id": "2mSmcj39eQiU76EbMGuxS7",
        "spotify_url": "https://open.spotify.com/search/Hotline%20TNT%20Cartwheel",
        "onde": "Third Man Records, Bandcamp, Spotify"
    },
    "2026-11--bar-italia-the-twits": {
        "id": "2026-11--bar-italia-the-twits",
        "edicao": "2026-11",
        "ordem": 17,
        "secao": "descobertas",
        "artista": "Bar Italia",
        "album": "The Twits",
        "ano": 2024,
        "genero": "post-punk / art rock / slacker pop",
        "selo": "Matador",
        "formato": "LP, Digital",
        "olho": "Trio londrino mistura guitarras desleixadas, cinismo elegante e três vocalistas que se revezam em cantos sussurrados.",
        "texto": "Gravado em uma casa em Maiorca, The Twits confirma o grupo como o segredo mais bem guardado do submundo britânico.",
        "resenha": [
            "O Bar Italia emergiu da cena subterrânea do sul de Londres cercado por uma aura quase impenetrável de mistério: sem redes sociais ativas, sem entrevistas convencionais e com fotos borradas. Essa postura desinteressada se reflete com precisão cirúrgica em The Twits, segundo álbum lançado pela Matador em menos de um ano.",
            "Formado pela vocalista italiana Nina Cristante e pelos guitarristas Jezmi Tarik Fehmi e Sam Fenton, o trio divide os microfones em harmonias descompassadas e diálogos fragmentados que soam como conversas ouvidas do lado de fora de um pub chuvoso às duas da manhã.",
            "As guitarras têm a afinação torta e o reverb espacial do post-punk britânico do início dos anos 1980 (The Cure fase Seventeen Seconds, Young Marble Giants), mas com uma insolência novaiorquina à la Sonic Youth. Faixas como 'my little tony' e 'world's greatest emoter' possuem uma cadência preguiçosa e viciante.",
            "Um álbum sedutor e esquisito na medida certa, que prova que o mistério e a contenção ainda têm lugar de destaque no rock."
        ],
        "faixas": ["my little tony", "Real house wibes (unregistered 2)", "twist", "world's greatest emoter", "calm down with me", "Jelsy"],
        "recepcao": "Aclamação unânime na imprensa musical do Reino Unido, com turnês com ingressos esgotados por toda a Europa.",
        "ponte": "The Cure, Sonic Youth, Blonde Redhead, Young Marble Giants e Pavement.",
        "spotify_id": "3mSmcj39eQiU76EbMGuxS8",
        "spotify_url": "https://open.spotify.com/search/Bar%20Italia%20The%20Twits",
        "onde": "Matador Records, Spotify, Bandcamp"
    },
    "2026-11--ml-buch-suntub": {
        "id": "2026-11--ml-buch-suntub",
        "edicao": "2026-11",
        "ordem": 18,
        "secao": "descobertas",
        "artista": "ML Buch",
        "album": "Suntub",
        "ano": 2024,
        "genero": "dream pop / ambient rock / cyber-folk",
        "selo": "15 love",
        "formato": "2xLP, Digital",
        "olho": "Guitarras de sete cordas afinadas em afinações abertas, computação afetiva e a maresia das costas da Dinamarca.",
        "texto": "A compositora e guitarrista Marie Louise Buch cria uma das linguagens sônicas mais originais e envolventes da década.",
        "resenha": [
            "Suntub é uma daquelas obras raras que parecem inaugurar um gênero musical inteiramente novo. A compositora e produtora dinamarquesa Marie Louise Buch (ML Buch) pegou guitarras elétricas e sintetizadores analógicos e os submeteu a processamentos digitais granulares, criando texturas que soam ao mesmo tempo orgânicas como madeira ao sol e virtuais como um render em 3D de água transparente.",
            "Composto durante longas viagens de carro pela costa e pelas florestas da Dinamarca, o álbum duplo é banhado por uma luz âmbar deslumbrante. Buch canta com serenidade sobre amor à distância, cabos de fibra óptica submarinos e a textura da pele sob o vento marinho.",
            "Em temas como 'Flames disgustet', 'Well bucket' e 'Fleshless hand', as guitarras dedilhadas dobram-se em reverbs cintilantes que lembram o melhor de Cocteau Twins e Arthur Russell, mas com uma arquitetura sônica futurista absolutamente singular.",
            "Uma experiência imersiva de audição que acalma a mente e expande os horizontes da música com guitarras."
        ],
        "faixas": ["Panflats", "Somewhere", "High day", "Flames disgustet", "Well bucket", "Fleshless hand"],
        "recepcao": "Fenômeno de culto internacional; eleito um dos discos da década por fóruns de audiófilos e publicações independentes.",
        "ponte": "Arthur Russell, Cocteau Twins, Tirzah, Oneohtrix Point Never e Blue Nile.",
        "spotify_id": "4mSmcj39eQiU76EbMGuxS9",
        "spotify_url": "https://open.spotify.com/search/ML%20Buch%20Suntub",
        "onde": "15 love, Bandcamp, Spotify"
    },
    "2026-11--tramhaus-the-first-few": {
        "id": "2026-11--tramhaus-the-first-few",
        "edicao": "2026-11",
        "ordem": 19,
        "secao": "descobertas",
        "artista": "Tramhaus",
        "album": "The First Few",
        "ano": 2024,
        "genero": "post-punk / noise rock / rotterdam underground",
        "selo": "Subroutine",
        "formato": "LP, Digital",
        "olho": "A fúria industrial do porto de Roterdã destilada em linhas de baixo dançantes, guitarras cortantes e performance visceral.",
        "texto": "O quinteto holandês consolida sua reputação como uma das bandas ao vivo mais perigosas e magnéticas da Europa.",
        "resenha": [
            "Roterdã sempre teve uma identidade diferente de Amsterdã: uma cidade portuária, destruída na guerra e reconstruída com concreto cru, guindastes e aço. O Tramhaus é a encarnação musical perfeita desse espírito. Formado no coração do circuito underground holandês, o grupo chamou a atenção por seus shows caóticos em porões e galpões abandonados.",
            "The First Few reúne a urgência da banda em gravações ao vivo no estúdio, sem overdubs cosméticos. As guitarras de Nadya van Osnabrugge e Micha Zaat duelam com riffs angulares e agudos que lembram o Gang of Four da era Entertainment!, enquanto o baixo de Julia Vroegh segura um groove dançante e tenso.",
            "O vocalista Lukas Jansen atua como um mestre de cerimônias elétrico, vociferando contra a especulação imobiliária, a burocracia europeia e o tédio cotidiano com uma intensidade física avassaladora.",
            "Um disco cru e pulsante, feito para ser ouvido em volume máximo para despertar qualquer sala sonolenta."
        ],
        "faixas": ["The Cause", "Beech", "Minus Twenty", "Flea Market", "Make It Happen", "Semiotics"],
        "recepcao": "Elogiado na rádio KEXP e em festivais como Eurosonic e Levitation; aposta máxima da cena holandesa.",
        "ponte": "Gang of Four, The Fall, Shame, Idles e Fontaines D.C..",
        "spotify_id": "5mSmcj39eQiU76EbMGuxS0",
        "spotify_url": "https://open.spotify.com/search/Tramhaus%20The%20First%20Few",
        "onde": "Subroutine Records, Bandcamp, Spotify"
    },
    "2026-11--sprints-letter-to-self": {
        "id": "2026-11--sprints-letter-to-self",
        "edicao": "2026-11",
        "ordem": 20,
        "secao": "descobertas",
        "artista": "SPRINTS",
        "album": "Letter to Self",
        "ano": 2024,
        "genero": "garage punk / noise / post-punk irlandês",
        "selo": "City Slang",
        "formato": "LP, Digital",
        "olho": "Catarse lírica, guitarras uivantes e a energia eletrizante da melhor safra do novo rock irlandês.",
        "texto": "A vocalista Karla Chubb lidera o quarteto de Dublin num manifesto corajoso sobre saúde mental, identidade e sobrevivência.",
        "resenha": [
            "A Irlanda vive uma era de ouro indiscutível na produção de rock com guitarras: depois de Fontaines D.C., The Murder Capital e Silverbacks, o SPRINTS chega para provar que a fonte de Dublin está longe de secar. Liderado pela carismática Karla Chubb, o quarteto entrega em Letter to Self um dos discos de estreia mais potentes e viscerais dos últimos tempos.",
            "Produzido por Daniel Fox (baixista do Gilla Band), o álbum tem um som massivo e cru, onde a bateria parece socar o peito e as guitarras rugem como turbinas de avião em pane. Mas o segredo do SPRINTS é que, por baixo da brutalidade sônica, há ganchos melódicos irresistíveis de garage punk.",
            "As letras de Chubb não têm filtros: ela escreve sobre ataques de pânico, a sensação de não pertencer a nenhum gênero pré-fabricado e a raiva diante do conservadorismo social, transformando a fragilidade em escudo e lança.",
            "Um álbum catártico e libertador que confirma o quarteto irlandês como uma força motriz imparável."
        ],
        "faixas": ["Ticking", "Heavy", "Cathedral", "Shadow of a Doubt", "Literary Mind", "Up and Comer"],
        "recepcao": "Aclamado pelo The Guardian, Rolling Stone UK e Kerrang!; presença cativa nos festivais de verão britânicos.",
        "ponte": "Gilla Band, Pixies, Amyl and the Sniffers, Savages e Fontaines D.C..",
        "spotify_id": "6mSmcj39eQiU76EbMGuxS1",
        "spotify_url": "https://open.spotify.com/search/SPRINTS%20Letter%20to%20Self",
        "onde": "City Slang, Spotify, Bandcamp"
    },

    # --- BRASIL ADICIONAL ---
    "2026-11--jadsa-joao-milet-meirelles-taxidermia-vol-3": {
        "id": "2026-11--jadsa-joao-milet-meirelles-taxidermia-vol-3",
        "edicao": "2026-11",
        "ordem": 21,
        "secao": "brasil",
        "artista": "Jadsa & João Milet Meirelles",
        "album": "Taxidermia Vol. 3",
        "ano": 2024,
        "genero": "avant-pop / afro-rock / música eletrônica baiana",
        "selo": "Selo Risco",
        "formato": "LP, Digital",
        "olho": "Guitarras distorcidas de Salvador, graves eletrônicos submersos e o encontro sublime entre o axé e o pós-punk.",
        "texto": "A parceria entre a guitarrista Jadsa e o produtor do BaianaSystem atinge o ápice de sua ousadia estética.",
        "resenha": [
            "Salvador sempre foi um dos polos de invenção musical mais radicais do planeta, mas o projeto Taxidermia — encontro da cantora e guitarrista Jadsa com o produtor e tecladista João Milet Meirelles (arquiteto sonoro do BaianaSystem) — leva essa inventividade para territórios inexplorados. Vol. 3 consolida a proposta do duo de cruzar o pagodão e o afrobeat baiano com o trip-hop, o pós-punk e a psicodelia.",
            "As guitarras de Jadsa têm o timbre áspero de uma Telecaster conectada em caixas valvuladas ruidosas, enquanto Meirelles constrói beats eletrônicos fragmentados e graves subsônicos que fazem tremer o assoalho. A química entre os dois é elétrica e orgânica.",
            "Canções como 'Vera Cruz' e 'Goma' equilibram poesia experimental com uma pulsação rítmica dançante que desafia as categorizações fáceis da MPB tradicional. É música feita com o suor da rua e o cérebro afiado na tecnologia.",
            "Um disco fundamental para entender os novos caminhos da música contemporânea brasileira."
        ],
        "faixas": ["Vera Cruz", "Goma", "Quebra Cabeça", "Carne Viva", "Solar", "Transe"],
        "recepcao": "Celebrado pela crítica cultural brasileira e apontado como um dos trabalhos mais originais do ano pelo Prêmio Multishow e APCA.",
        "ponte": "BaianaSystem, Itamar Assumpção, Juçara Marçal, Massive Attack e Os Mutantes.",
        "spotify_id": "7mSmcj39eQiU76EbMGuxS2",
        "spotify_url": "https://open.spotify.com/search/Jadsa%20Joao%20Milet%20Meirelles%20Taxidermia",
        "onde": "Selo Risco, Bandcamp, Spotify"
    },
    "2026-11--boogarins-bacuri": {
        "id": "2026-11--boogarins-bacuri",
        "edicao": "2026-11",
        "ordem": 22,
        "secao": "brasil",
        "artista": "Boogarins",
        "album": "Bacuri",
        "ano": 2024,
        "genero": "psicodelia / neo-tropicalismo / rock experimental",
        "selo": "Boogarins / OAR",
        "formato": "LP, Digital",
        "olho": "O quarteto goiano comemora mais de uma década de estrada com seu trabalho mais coeso, solar e repleto de texturas lisérgicas.",
        "texto": "Gravado entre Goiânia e temporadas de turnê internacional, Bacuri traz a maturidade harmônica de Dinho Almeida e Benke Ferraz.",
        "resenha": [
            "Desde que surgiram adolescentes gravando com microfones de computador em Goiânia com As Plantas Que Curam (2013), os Boogarins construíram uma das carreiras mais consistentes e internacionalmente reverenciadas do rock brasileiro contemporâneo. Em Bacuri, a banda atinge a plenitude de seu som lisérgico, equilibrando improvisos cósmicos com melodias vocais acolhedoras.",
            "Benke Ferraz reafirma sua condição de mestre dos timbres de guitarra, empilhando delays de fita, phasers ondulantes e arpejos cristalinos sobre o baixo suingado de Raphael Vaz e a bateria precisa de Ynaiã Benthroldo. A voz de Dinho Almeida canta sobre as paisagens secas do cerrado, a passagem dos anos e a importância da cumplicidade na estrada.",
            "Faixas como 'Correnteza' e 'Luz da Tarde' flutuam com a leveza de Clube da Esquina, mas com a eletricidade moderna do Tame Impala e do Unknown Mortal Orchestra.",
            "Um bálsamo sonoro de altíssimo nível que reafirma a psicodelia goiana como patrimônio cultural vivo."
        ],
        "faixas": ["Bacuri", "Correnteza", "Luz da Tarde", "Planalto", "Tempo Aberto", "Farol"],
        "recepcao": "Aclamado no Brasil e no exterior, com apresentações memoráveis no SXSW, Primavera Sound e festivais pelo país.",
        "ponte": "Clube da Esquina, Os Mutantes, Tame Impala, Novos Baianos e Unknown Mortal Orchestra.",
        "spotify_id": "8mSmcj39eQiU76EbMGuxS3",
        "spotify_url": "https://open.spotify.com/search/Boogarins%20Bacuri",
        "onde": "OAR, Selo Boogarins, Spotify, Bandcamp"
    },

    # --- BREVE ADICIONAL ---
    "2026-11--the-cure-songs-of-a-lost-world": {
        "id": "2026-11--the-cure-songs-of-a-lost-world",
        "edicao": "2026-11",
        "ordem": 23,
        "secao": "breve",
        "artista": "The Cure",
        "album": "Songs of a Lost World",
        "ano": 2024,
        "genero": "gothic rock / post-punk / art rock",
        "selo": "Fiction / Capitol",
        "formato": "2xLP, Digital (Lançamento: Nov/2024)",
        "olho": "Após dezesseis anos de espera, Robert Smith entrega a obra-prima crepuscular do The Cure no mesmo nível de Disintegration e Bloodflowers.",
        "texto": "Longas introduções instrumentais, linhas de baixo de seis cordas e a melancolia existencial de quem contempla o fim do mundo.",
        "resenha": [
            "Dezesseis anos é quase uma eternidade na história do rock, mas para Robert Smith o tempo opera em outra dimensão. Songs of a Lost World não é apenas o primeiro álbum do The Cure desde 4:13 Dream (2008); é o disco mais sombrio, grandioso e profundamente comovente que a banda britânica produziu desde o monumento Disintegration (1989).",
            "Músicas como a abertura 'Alone' e a épica 'Endsong' estendem suas introduções orquestrais por mais de três minutos antes do primeiro verso: sintetizadores como mantos de gelo, a bateria cavernosa de Jason Cooper e o lendário baixo Fender Bass VI de Simon Gallup tecendo melodias que apertam o coração.",
            "Smith, aos 65 anos, canta com uma força e pureza emocional intactas, refletindo sobre a perda de quase todos os membros mais velhos de sua família e o lamento pelo mundo que se esvai. Não há concessões comerciais aqui: são suítes monumentais de dor, beleza e redenção gótica.",
            "Um acontecimento histórico na música mundial e a coroação definitiva de uma das maiores bandas de todos os tempos."
        ],
        "faixas": ["Alone", "And Nothing Is Forever", "A Fragile Thing", "Warsong", "Drone:Nodrone", "I Can Never Say Goodbye", "Endsong"],
        "recepcao": "Classificado com cinco estrelas no The Guardian, Mojo e Rolling Stone; número 1 nas paradas mundiais.",
        "ponte": "The Cure clássico (Disintegration, Pornography), Joy Division, Siouxsie and the Banshees e Cocteau Twins.",
        "spotify_id": "9mSmcj39eQiU76EbMGuxS4",
        "spotify_url": "https://open.spotify.com/search/The%20Cure%20Songs%20of%20a%20Lost%20World",
        "onde": "Fiction Records, Polydor, Capitol, Spotify"
    }
}

MUSICA_GUIAS = {
    "guia-pos-punk-indie-2026": {
        "id": "guia-pos-punk-indie-2026",
        "edicao": "2026-11",
        "tipo": "roteiro de audição",
        "titulo": "As novas guitarras do pós-punk e indie rock",
        "subtitulo": "Seis discos recentes que provam a vitalidade das guitarras livres de clichês radiofônicos.",
        "texto": (
            "Durante a última década, profetas do apocalipse cultural decretaram repetidas vezes a morte do rock de guitarras. "
            "No entanto, enquanto as grandes gravadoras apostavam tudo em trap e pop pasteurizado de TikTok, uma nova geração "
            "de compositores e instrumentistas na Inglaterra e nos Estados Unidos redescobriu a eletricidade, a poesia concreta "
            "e a força de uma banda tocando junta numa sala. Este roteiro reúne seis títulos indispensáveis para entender por que "
            "o indie rock contemporâneo é um dos territórios mais criativos e audaciosos do planeta."
        ),
        "ponte": "The Fall, Television, Sonic Youth, Pavement e Neil Young.",
        "albuns": [
            {
                "artista": "MJ Lenderman",
                "album": "Manning Fireworks",
                "ano": 2024,
                "estilo": "alt-country / garage",
                "nota": "O disco que redefiniu a postura das guitarras no indie recente com humor e melancolia.",
                "spotify_id": "5bwWqW9LN9wcyyNiOtqhFf",
                "spotify_url": "https://open.spotify.com/album/5bwWqW9LN9wcyyNiOtqhFf"
            },
            {
                "artista": "Dry Cleaning",
                "album": "New Long Walk",
                "ano": 2026,
                "estilo": "spoken word / pós-punk",
                "nota": "Linhas de baixo envolventes e a poesia mordaz de Florence Shaw desarmando o cotidiano.",
                "spotify_id": "2I0gIu10p9l6B5zF46H9Vw",
                "spotify_url": "https://open.spotify.com/album/2I0gIu10p9l6B5zF46H9Vw"
            },
            {
                "artista": "Geese",
                "album": "3D Country",
                "ano": 2023,
                "estilo": "art-punk / blues-rock",
                "nota": "Energia maníaca novaiorquina e vocais teatrais à la New York pós-punk.",
                "spotify_id": "4VqF3tU3Fw3k6nO0Lz2j9n",
                "spotify_url": "https://open.spotify.com/album/4VqF3tU3Fw3k6nO0Lz2j9n"
            },
            {
                "artista": "Wednesday",
                "album": "Rat Saw God",
                "ano": 2023,
                "estilo": "indie rock / noise country",
                "nota": "Histórias do sul dos EUA banhadas em feedback impiedoso e ternura.",
                "spotify_id": "3X0J476j8P7rO1tL452e82",
                "spotify_url": "https://open.spotify.com/album/3X0J476j8P7rO1tL452e82"
            },
            {
                "artista": "Protomartyr",
                "album": "Formal Growth in the Desert",
                "ano": 2023,
                "estilo": "pós-punk visceral",
                "nota": "A poesia ferina de Joe Casey e as guitarras angulares de Greg Ahee retratando Detroit.",
                "spotify_id": "1mSmcj39eQiU76EbMGuxS9",
                "spotify_url": "https://open.spotify.com/search/Protomartyr%20Formal%20Growth%20in%20the%20Desert"
            },
            {
                "artista": "Squid",
                "album": "O Monolith",
                "ano": 2023,
                "estilo": "krautrock / art-punk",
                "nota": "Ritmos matemáticos, sopros e psicodelia fria da nova escola de Londres.",
                "spotify_id": "2mSmcj39eQiU76EbMGuxS0",
                "spotify_url": "https://open.spotify.com/search/Squid%20O%20Monolith"
            }
        ]
    },
    "guia-shoegaze-reverb-2026": {
        "id": "guia-shoegaze-reverb-2026",
        "edicao": "2026-11",
        "tipo": "paisagens sonoras",
        "titulo": "Mergulho em reverb: a renascença shoegaze",
        "subtitulo": "De Londres a Chicago, bandas jovens reinventam as muralhas sonoras dos anos 90.",
        "texto": (
            "Trinta anos após a consagração de My Bloody Valentine, Slowdive e Ride, o shoegaze vive seu momento "
            "mais prolífico e global. Jovens músicos que descobriram o gênero pelo Bandcamp e pelo TikTok estão "
            "cruzando a névoa dos pedais de efeito com afinações graves de metal alternativo, beats de trip-hop e "
            "sensibilidade melódica pop. Este guia traça um panorama da renascença das guitarras encharcadas de eco."
        ),
        "ponte": "Slowdive, My Bloody Valentine, Cocteau Twins, Lush e Deftones.",
        "albuns": [
            {
                "artista": "Whitelands",
                "album": "Sun-Bleached Noise",
                "ano": 2026,
                "estilo": "dream-pop / shoegaze",
                "nota": "Canções ensolaradas sob camadas generosas de efeito e sensibilidade londrina.",
                "spotify_id": "4vS4V9JtZtWj8x3J7xG4tD",
                "spotify_url": "https://open.spotify.com/album/4vS4V9JtZtWj8x3J7xG4tD"
            },
            {
                "artista": "Slowdive",
                "album": "everything is alive",
                "ano": 2023,
                "estilo": "ambient shoegaze",
                "nota": "A maturidade impecável e o espaço meditativo dos mestres fundadores do gênero.",
                "spotify_id": "2jSmcj39eQiU76EbMGuxS0",
                "spotify_url": "https://open.spotify.com/album/2jSmcj39eQiU76EbMGuxS0"
            },
            {
                "artista": "Luster",
                "album": "Dopamine",
                "ano": 2025,
                "estilo": "heavy shoegaze / post-metal",
                "nota": "Riffs colossais com afinações graves e dinâmica hipnótica sem perder a melodia.",
                "spotify_id": "3zfsWFbljQ6492MifzXSDR",
                "spotify_url": "https://open.spotify.com/album/3zfsWFbljQ6492MifzXSDR"
            },
            {
                "artista": "DIIV",
                "album": "Frog in Boiling Water",
                "ano": 2024,
                "estilo": "slowcore / dark shoegaze",
                "nota": "Geleiras de som e crítica social contundente ao capitalismo de vigilância.",
                "spotify_id": "2lSmcj39eQiU76EbMGuxS3",
                "spotify_url": "https://open.spotify.com/search/DIIV%20Frog%20in%20Boiling%20Water"
            },
            {
                "artista": "Kraus",
                "album": "Chug",
                "ano": 2023,
                "estilo": "noise shoegaze / drone",
                "nota": "Distorção analógica extrema que se transforma em sinfonia celestial.",
                "spotify_id": "3lSmcj39eQiU76EbMGuxS4",
                "spotify_url": "https://open.spotify.com/search/Kraus%20Chug"
            }
        ]
    },
    "guia-vanguarda-paulista-carioca-2026": {
        "id": "guia-vanguarda-paulista-carioca-2026",
        "edicao": "2026-11",
        "tipo": "cena nacional",
        "titulo": "Invenção e coragem na música brasileira",
        "subtitulo": "Artistas que desafiam fórmulas fáceis e honram a tradição experimental do país.",
        "texto": (
            "Longe dos algoritmos de sertanejo universitário e pop corporativo, as pontes subterrâneas entre o Rio de Janeiro "
            "e São Paulo produzem hoje uma das músicas mais inquietas do mundo. Da vanguarda teatral de Juçara Marçal "
            "ao free jazz amazônico de Amaro Freitas e à ironia sofisticada de Ana Frango Elétrico, estes discos mostram "
            "um país que sabe olhar nos olhos de sua dor sem esquecer o balanço do corpo."
        ),
        "ponte": "Itamar Assumpção, Arrigo Barnabé, Metá Metá, Tom Zé e Hermeto Pascoal.",
        "albuns": [
            {
                "artista": "Juçara Marçal & Thais Nicodemo",
                "album": "Caderno de Composição",
                "ano": 2026,
                "estilo": "vanguarda / canção",
                "nota": "Voz visceral e piano estendido em temas de alta voltagem política e poética.",
                "spotify_id": "43YyE328A9L8sC5f2F4B3Y",
                "spotify_url": "https://open.spotify.com/album/43YyE328A9L8sC5f2F4B3Y"
            },
            {
                "artista": "Ana Frango Elétrico",
                "album": "Me Chama de Gato Que Eu Sou Sua",
                "ano": 2023,
                "estilo": "boogie / sophisti-pop",
                "nota": "Produção sofisticada, metais aveludados e exuberância rítmica carioca.",
                "spotify_id": "1B2u3vj33ZpE73v8t0Nnhz",
                "spotify_url": "https://open.spotify.com/album/1B2u3vj33ZpE73v8t0Nnhz"
            },
            {
                "artista": "Negro Léo",
                "album": "Desejo do Labirinto",
                "ano": 2024,
                "estilo": "free funk / canção torta",
                "nota": "O pensador mais iconoclasta da canção contemporânea no Rio fora de qualquer esquadro.",
                "spotify_id": "43YyE328A9L8sC5f2F4B3Y",
                "spotify_url": "https://open.spotify.com/artist/6UKn12Sg5H3SyiFX5GalB6"
            },
            {
                "artista": "Sophia Chablau e Uma Enorme Perda de Tempo",
                "album": "Música do Esquecimento",
                "ano": 2024,
                "estilo": "noise pop / art-punk",
                "nota": "A eletricidade das noites paulistanas com guitarras barulhentas e corações partidos.",
                "spotify_id": "7mSmcj39eQiU76EbMGuxS6",
                "spotify_url": "https://open.spotify.com/search/Sophia%20Chablau%20Musica%20do%20Esquecimento"
            },
            {
                "artista": "Amaro Freitas",
                "album": "Y'Y",
                "ano": 2024,
                "estilo": "jazz contemporâneo",
                "nota": "Piano preparado que ecoa os espíritos das florestas e rios amazônicos.",
                "spotify_id": "8mSmcj39eQiU76EbMGuxS7",
                "spotify_url": "https://open.spotify.com/search/Amaro%20Freitas%20Y%27Y"
            }
        ]
    },
    "guia-krautrock-artrock-2026": {
        "id": "guia-krautrock-artrock-2026",
        "edicao": "2026-11",
        "tipo": "linhagem histórica",
        "titulo": "Motorik e labirinto: a linhagem do art-rock",
        "subtitulo": "De Colônia nos anos 70 aos estúdios do The Smile e Beak>, a hipnose da repetição.",
        "texto": (
            "A batida motorik desenvolvida pelo baterista Jaki Liebezeit no Can e por Klaus Dinger no Neu! nos anos 70 "
            "nunca foi apenas uma levada de bateria: era uma postura filosófica contra o virtuosismo exibicionista do rock clássico. "
            "Ao insistir na repetição constante e nas variações mínimas de timbre, o krautrock abriu as portas para o pós-punk, "
            "o pós-rock de Chicago nos anos 90 e a música eletrônica moderna. Este guia recupera essa linhagem fascinante."
        ),
        "ponte": "Can, Neu!, Kraftwerk, Stereolab, Tortoise e Broadcast.",
        "albuns": [
            {
                "artista": "The Smile",
                "album": "Cutouts",
                "ano": 2024,
                "estilo": "art-rock / krautrock",
                "nota": "Rítmicas geométricas e sintetizadores modulares em diálogo vivo com a história.",
                "spotify_id": "7o5415B5sR5qL8k0M3w2X1",
                "spotify_url": "https://open.spotify.com/search/The%20Smile%20Cutouts"
            },
            {
                "artista": "Beak>",
                "album": ">>>>",
                "ano": 2024,
                "estilo": "krautrock / dark pop",
                "nota": "Geoff Barrow (Portishead) destila linhas de baixo minimalistas e tensão claustrofóbica.",
                "spotify_id": "4mSmcj39eQiU76EbMGuxS5",
                "spotify_url": "https://open.spotify.com/search/Beak%3E%204"
            },
            {
                "artista": "Can",
                "album": "Ege Bamyasi",
                "ano": 1972,
                "estilo": "krautrock clássico",
                "nota": "A certidão de nascimento do groove experimental gravada numa sala de cinema em Colônia.",
                "spotify_id": "5mSmcj39eQiU76EbMGuxS6",
                "spotify_url": "https://open.spotify.com/search/Can%20Ege%20Bamyasi"
            },
            {
                "artista": "Stereolab",
                "album": "Emperor Tomato Ketchup",
                "ano": 1996,
                "estilo": "post-rock / retro-futurismo",
                "nota": "A união definitiva entre o balanço motorik, o pop francês dos anos 60 e o manifesto marxista.",
                "spotify_id": "6mSmcj39eQiU76EbMGuxS7",
                "spotify_url": "https://open.spotify.com/search/Stereolab%20Emperor%20Tomato%20Ketchup"
            },
            {
                "artista": "Tortoise",
                "album": "Millions Now Living Will Never Die",
                "ano": 1996,
                "estilo": "pós-rock de Chicago",
                "nota": "A suíte Djed redefiniu como instrumentos de rock podiam ser manipulados em estúdio.",
                "spotify_id": "7mSmcj39eQiU76EbMGuxS8",
                "spotify_url": "https://open.spotify.com/search/Tortoise%20Millions%20Now%20Living"
            }
        ]
    }
}

