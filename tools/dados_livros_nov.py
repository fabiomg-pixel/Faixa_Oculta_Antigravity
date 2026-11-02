# -*- coding: utf-8 -*-
"""Dados editoriais de Livros e Ideias para a edição Nº 2 (Novembro 2026).
Contém 22 livros/ensaios nas seções editoriais e 2 guias temáticos completos (10 livros nos guias).
"""

LIVRO_EDICAO = {
    "id": "2026-11",
    "numero": 2,
    "mes": "Novembro de 2026",
    "data": "2026-11-01",
    "manchete": "Ciência como ensaio vivo, memórias da biologia e o melhor da literatura contemporânea",
    "editorial": (
        "Na edição de novembro da Revista de Livros, a curadoria foge das listas comerciais de marketing para selecionar "
        "obras onde o rigor do conhecimento e a força poética da linguagem caminham juntos. "
        "Na matéria de capa, 'A Trama da Vida' de Merlin Sheldrake desvela a rede invisível dos fungos que sustenta a biosfera, "
        "dialogando de perto com as perturbações mentais e matemáticas de 'Maniac' (Benjamín Labatut), "
        "o humanismo clínico e generoso de Oliver Sacks, a consagração de Han Kang com o Prêmio Nobel de Literatura "
        "e o vigor telúrico de 'Salvar o Fogo' de Itamar Vieira Junior. Uma travessia densa e fértil para o fim de semana."
    ),
    "layout": [
        {"tipo": "secao", "secao": "lancamentos"},
        {"tipo": "guia", "id": "guia-biologia-ensaio-narrativa-2026"},
        {"tipo": "secao", "secao": "ideias"},
        {"tipo": "secao", "secao": "brasil"},
        {"tipo": "guia", "id": "guia-vozes-terra-brasil-2026"},
        {"tipo": "secao", "secao": "achados"}
    ]
}

LIVRO_ITENS = {
    # --- SEÇÃO LANÇAMENTOS & DESTAQUES ---
    "2026-11--a-trama-da-vida": {
        "id": "2026-11--a-trama-da-vida",
        "edicao": "2026-11",
        "ordem": 1,
        "secao": "lancamentos",
        "destaque": True,
        "titulo": "A Trama da Vida",
        "titulo_original": "Entangled Life: How Fungi Make Our Worlds, Change Our Minds & Shape Our Futures",
        "autor": "Merlin Sheldrake",
        "ano": 2024,
        "ano_original": 2020,
        "pais": "Reino Unido",
        "tempo": "424 páginas",
        "genero": "ensaio científico / biologia / ecologia",
        "tipo": "livro",
        "onde": "Ubu Editora (Tradução de Clara Allain); impresso e e-book",
        "olho": "O micologista britânico revela a inteligência descentralizada dos fungos e desconstrói a ilusão de individualidade biológica.",
        "texto": "Um dos ensaios biológicos mais fascinantes do século, celebrando a simbiose como motor fundamental da evolução na Terra.",
        "resenha": [
            "Durante séculos, a botânica e a zoologia ocidentais trataram os fungos como meros parasitas ou curiosidades no rodapé dos reinos da natureza. Merlin Sheldrake, biólogo tropical formado em Cambridge e pesquisador no Instituto Smithsonian no Panamá, vira essa perspectiva colonial de cabeça para baixo: sem as redes de hifas subterrâneas que há 500 milhões de anos ajudaram as plantas aquáticas a colonizar a terra seca, a própria vida terrestre tal como a conhecemos simplesmente não existiria.",
            "Com uma prosa vívida, elegante e sensorial que lembra o melhor de Oliver Sacks e Michael Pollan, Sheldrake desce literalmente às raízes do solo para explicar o funcionamento das micorrizas — a chamada 'Wood Wide Web' —, a inteligência química com que os fungos distribuem fósforo e carbono entre árvores de espécies diferentes e a capacidade de decompor plásticos, rochas e até radiação nuclear.",
            "O livro atinge picos de brilhantismo filosófico ao analisar a psilocibina e os líquens (a clássica associação entre algas e fungos que desafiou a taxonomia tradicional de Lineu), forçando o leitor a questionar onde termina um organismo e começa o outro. Para Sheldrake, a biologia não é uma competição de indivíduos isolados, mas uma dança interminável de cooperação e contaminação mútua.",
            "Uma leitura essencial, transformadora e indispensável para qualquer pesquisador, estudante de biociências ou amante da literatura de ideias."
        ],
        "ponte": "Oliver Sacks, Lynn Margulis, Michael Pollan e Stefano Mancuso.",
        "recepcao": "Vencedor do Royal Society Science Book Prize; best-seller internacional traduzido em mais de 20 línguas."
    },
    "2026-11--maniac": {
        "id": "2026-11--maniac",
        "edicao": "2026-11",
        "ordem": 2,
        "secao": "lancamentos",
        "titulo": "Maniac",
        "titulo_original": "The MANIAC",
        "autor": "Benjamín Labatut",
        "ano": 2023,
        "ano_original": 2023,
        "pais": "Chile, Holanda",
        "tempo": "368 páginas",
        "genero": "ficção científica histórica / biografia / ensaio filosófico",
        "tipo": "livro",
        "onde": "Todavia (Tradução de Mariana Sanchez); impresso e e-book",
        "olho": "Benjamín Labatut investiga os delírios da razão pura através da vida assombrosa do matemático John von Neumann.",
        "texto": "Da bomba atômica e teoria dos jogos aos algoritmos que derrotaram os mestres humanos de Go, um mergulho vertiginoso no abismo da IA.",
        "resenha": [
            "Após o impacto planetário de Quando Deixamos de Entender o Mundo (2020), o escritor chileno Benjamín Labatut retorna aos limites sombrios do conhecimento científico moderno em Maniac. Aqui, o epicentro da tempestade é John von Neumann (1903-1957), a mente mais rápida e temida do século XX, pioneiro da mecânica quântica, da teoria dos jogos, da arquitetura dos computadores digitais e da bomba de hidrogênio.",
            "Construído como um romance polifônico em que dezenas de colaboradores, amigos e familiares de Von Neumann — incluindo figuras monumentais como Eugene Wigner, Hans Bethe e sua esposa Klára Dán — prestam depoimentos fragmentados, o livro pinta o retrato de um gênio cuja inteligência computacional parecia desprovida de qualquer freio moral humano.",
            "O livro abre com a tragédia real do físico austríaco Paul Ehrenfest, que assassinou o próprio filho com síndrome de Down antes de se suicidar em 1933 apavorado pelo irracionalismo nazista e pela abstração quântica, e encerra no duelo histórico de 2016 em Seul entre o programa AlphaGo da DeepMind e o campeão mundial Lee Sedol.",
            "Uma obra-prima literária perturbadora sobre o instante em que a inteligência humana criou as ferramentas de sua própria obsolescência."
        ],
        "ponte": "Quando Deixamos de Entender o Mundo, Robert Oppenheimer, Jorge Luis Borges e W.G. Sebald.",
        "recepcao": "Aclamação unânime pela crítica global; eleito um dos dez melhores livros do ano pelo The New York Times e The Guardian."
    },
    "2026-11--nexus": {
        "id": "2026-11--nexus",
        "edicao": "2026-11",
        "ordem": 3,
        "secao": "lancamentos",
        "titulo": "Nexus: Uma Breve História das Redes de Informação",
        "titulo_original": "Nexus: A Brief History of Information Networks from the Stone Age to AI",
        "autor": "Yuval Noah Harari",
        "ano": 2024,
        "ano_original": 2024,
        "pais": "Israel",
        "tempo": "544 páginas",
        "genero": "ensaio histórico / tecnologia / filosofia política",
        "tipo": "livro",
        "onde": "Companhia das Letras (Tradução de Odorico Leal); impresso e e-book",
        "olho": "Harari desmonta o mito ingênuo de que mais informação gera mais sabedoria e alerta para os perigos existenciais dos agentes inorgânicos.",
        "texto": "Da caça às bruxas na Idade Média e burocracias soviéticas aos algoritmos de engajamento que sabotam democracias contemporâneas.",
        "resenha": [
            "Dez anos após o fenômeno editorial de Sapiens, Yuval Noah Harari entrega sua reflexão mais urgente e politicamente afiada em Nexus. O ponto de partida é uma desilusão histórica necessária: a premissa do Vale do Silício de que a livre circulação de informação leva automaticamente à verdade e à paz é uma falácia perigosa que a história desmente a cada capítulo.",
            "A informação, lembra Harari, não é a matéria-prima da verdade; ela é a matéria-prima da ordem. Grandes impérios, da Bíblia canônica à Inquisição europeia e à máquina burocrática stalinista, sempre usaram a informação para criar coesão social ao custo do silenciamento da realidade empírica e da perseguição à dissidência.",
            "O livro ganha contornos alarmantes ao analisar o advento da Inteligência Artificial. Diferente da imprensa de Gutenberg ou da televisão — ferramentas que dependiam de cérebros humanos para produzir e interpretar conteúdo —, a IA é a primeira tecnologia da história capaz de tomar decisões autônomas e gerar novas ideias e códigos por conta própria, criando o que Harari chama de 'burocratas inorgânicos'.",
            "Um alerta lúcido e embasado sobre a urgência de construir mecanismos de autocorreção e prestação de contas antes que os sistemas algorítmicos engulam o tecido democrático."
        ],
        "ponte": "Sapiens, Homo Deus, Shoshana Zuboff (A Era do Capitalismo de Vigilância) e Cathy O'Neil.",
        "recepcao": "Lançamento global simultâneo; destaque em debates sobre regulação de tecnologia em todo o mundo."
    },
    "2026-11--intermezzo": {
        "id": "2026-11--intermezzo",
        "edicao": "2026-11",
        "ordem": 4,
        "secao": "lancamentos",
        "titulo": "Intermezzo",
        "titulo_original": "Intermezzo",
        "autor": "Sally Rooney",
        "ano": 2024,
        "ano_original": 2024,
        "pais": "Irlanda",
        "tempo": "448 páginas",
        "genero": "romance contemporâneo / drama psicológico",
        "tipo": "livro",
        "onde": "Companhia das Letras (Tradução de Débora Landsberg); impresso e e-book",
        "olho": "Sally Rooney amadurece sua prosa com virtuosismo modernista ao investigar o luto e o embate fraterno entre dois irmãos em Dublin.",
        "texto": "Peter, um advogado bem-sucedido de 32 anos, e Ivan, um mestre de xadrez introvertido de 22, tentam reconstruir a vida após a morte do pai.",
        "resenha": [
            "Sally Rooney foi catapultada ao estrelato pop com Conversas entre Amigos e Pessoas Normais, rotulada com frequência como a 'voz da geração millennial'. Em Intermezzo, seu quarto e mais ambicioso romance, ela silencia os céticos ao entregar uma obra de extraordinário fôlego formal que dialoga diretamente com o fluxo de consciência de James Joyce e a precisão filosófica de Ludwig Wittgenstein.",
            "O enredo acompanha os irmãos Peter e Ivan Koubek nos meses seguintes à morte do pai por câncer em Dublin. Peter é um advogado carismático e atormentado que se divide entre a dependência química de calmantes e o afeto dividido por duas mulheres (sua ex-namorada Sylvia e a jovem Naomi). Ivan, por sua vez, é um prodígio do xadrez socialmente desajeitado que se apaixona por Margaret, uma mulher catorze anos mais velha recém-saída de um divórcio.",
            "A grande proeza de Rooney está no estilo: a seção de Peter é escrita em frases curtas, sincopadas e telegráficas que mimetizam sua mente febril e ansiosa, enquanto as partes de Ivan fluem com a calma lógica e analítica de quem calcula lances numa abertura de peão.",
            "Um romance deslumbrante sobre a aspereza do luto, a dificuldade de perdoar os próprios erros e a beleza da vulnerabilidade mútua."
        ],
        "ponte": "James Joyce (Ulisses), Pessoas Normais, Virginia Woolf e Rachel Cusk.",
        "recepcao": "Aclamado pela crítica de língua inglesa como o trabalho mais maduro e impecável da autora até hoje."
    },
    "2026-11--a-vegetariana": {
        "id": "2026-11--a-vegetariana",
        "edicao": "2026-11",
        "ordem": 5,
        "secao": "lancamentos",
        "titulo": "A Vegetariana",
        "titulo_original": "Chaeshikjuuija",
        "autor": "Han Kang",
        "ano": 2024,
        "ano_original": 2007,
        "pais": "Coreia do Sul",
        "tempo": "176 páginas",
        "genero": "romance / ficção existencial / parábola moderna",
        "tipo": "livro",
        "onde": "Todavia (Tradução direta do coreano por Ji Yun Kim); impresso e e-book",
        "olho": "A consagração de Han Kang com o Nobel de Literatura 2024 ilumina sua obra-prima sobre uma mulher que se recusa a ser carne humana.",
        "texto": "A decisão de Yeonghye de parar de comer carne após um pesadelo sangrento desata uma cadeia de violência e loucura familiar em Seul.",
        "resenha": [
            "A concessão do Prêmio Nobel de Literatura de 2024 à escritora sul-coreana Han Kang — 'por sua intensa prosa poética que confronta traumas históricos e expõe a fragilidade da vida humana' — coroou uma trajetória de rigor estético exemplar. E nenhuma de suas obras resume essa força de forma tão visceral e inesquecível quanto A Vegetariana, originalmente publicado em Seul em 2007 e vencedor do International Booker Prize em 2016.",
            "Dividido em três partes contadas respectivamente pelo marido medíocre, pelo cunhado artista visual e pela irmã exausta, o livro acompanha a dissolução de Yeonghye, uma dona de casa considerada comum que, após um pesadelo brutal com animais esquartejados, decide jogar fora toda a carne da geladeira e jejuar radicalmente.",
            "Sua recusa a comer carne é interpretada pela sociedade patriarcal sul-coreana como um ato de insubordinação intolerável, desencadeando abusos físicos por parte de seu pai, estupro marital e, posteriormente, a internação em um hospital psiquiátrico onde Yeonghye acredita que está se transformando em uma árvore que bebe apenas luz solar e chuva.",
            "Um livro magnético, perturbador e de economia cirúrgica, que transforma o corpo da mulher no último campo de batalha contra a violência estrutural do mundo."
        ],
        "ponte": "Franz Kafka (A Metamorfose), Han Kang (Atos Humanos), Clarice Lispector e Virginia Woolf.",
        "recepcao": "Prêmio Nobel de Literatura 2024; International Booker Prize 2016; reconhecimento unânime como um clássico contemporâneo."
    },
    "2026-11--o-ceu-que-nos-protege": {
        "id": "2026-11--o-ceu-que-nos-protege",
        "edicao": "2026-11",
        "ordem": 6,
        "secao": "lancamentos",
        "titulo": "O Céu Que Nos Protege",
        "titulo_original": "The Sheltering Sky",
        "autor": "Paul Bowles",
        "ano": 2024,
        "ano_original": 1949,
        "pais": "EUA, Marrocos",
        "tempo": "288 páginas",
        "genero": "romance clássico / existencialismo / viagem",
        "tipo": "livro",
        "onde": "Nova Fronteira (Tradução de Sérgio Flaksman); impresso e e-book",
        "olho": "Em nova edição comemorativa, a obra-prima de Paul Bowles sobre a dissolução psicológica de dois viajantes no silêncio cósmico do Saara.",
        "texto": "Port e Kit Moresby embrenham-se pelo norte da África pós-Segunda Guerra buscando salvar um amor já corroído pelo desencanto ocidental.",
        "resenha": [
            "Poucas distinções literárias são tão famosas quanto a que abre O Céu Que Nos Protege: a diferença irreconciliável entre o turista, que tem pressa para voltar para casa após duas semanas, e o viajante, que não pertence a lugar algum e pode passar anos sem saber para onde o próximo navio o levará. O compositor e escritor Paul Bowles (1910-1999) encarnou essa segunda linhagem como ninguém ao trocar Nova York por Tânger nos anos 1940.",
            "No romance, o casal de intelectuais nova-iorquinos Port e Kit Moresby viaja pelo deserto da Argélia e do Saara acompanhados pelo fútil Tunner. O que parecia uma fuga estética da Europa destruída pela guerra revela-se uma lenta descida ao vazio existencial, onde o calor implacável, a solidão das caravanas e a indiferença cósmica do céu azul aniquilam todas as ilusões da civilização burguesa.",
            "A prosa de Bowles é de uma clareza cortante e gelada, quase matemática em seu despojamento lírico. A agonia de Port acometido por febre tifóide em um forte militar isolado no Saara é uma das passagens mais assombrosas sobre a finitude física já registradas em papel.",
            "Um monumento da literatura do século XX que continua a fascinar e apavorar com seu chamado intransigente ao desconhecido."
        ],
        "ponte": "Albert Camus (O Estrangeiro), William S. Burroughs, Joan Didion e Graham Greene.",
        "recepcao": "Classificado pela Modern Library entre os 100 melhores romances do século XX; adaptado ao cinema por Bernardo Bertolucci."
    },

    # --- SEÇÃO IDEIAS & ENSAIOS ---
    "2026-11--o-homem-que-confundiu-sua-mulher": {
        "id": "2026-11--o-homem-que-confundiu-sua-mulher",
        "edicao": "2026-11",
        "ordem": 7,
        "secao": "ideias",
        "titulo": "O Homem Que Confundiu Sua Mulher com um Chapéu",
        "titulo_original": "The Man Who Mistook His Wife for a Hat and Other Clinical Tales",
        "autor": "Oliver Sacks",
        "ano": 2023,
        "ano_original": 1985,
        "pais": "Reino Unido, EUA",
        "tempo": "320 páginas",
        "genero": "ensaio neurológico / biografia médica / neurociência humanista",
        "tipo": "livro",
        "onde": "Companhia das Letras (Tradução de Laura Teixeira Motta); impresso e e-book",
        "olho": "Oliver Sacks une a medicina de ponta à compaixão literária nos casos clínicos mais comoventes e enigmáticos da mente humana.",
        "texto": "Da agnosia visual de Dr. P. à síndrome de Tourette e às memórias musicais da infância, uma ode à resiliência do sujeito neural.",
        "resenha": [
            "Oliver Sacks (1933-2015) reinventou a tradição dos 'relatos clínicos' do século XIX — de mestres como Sigmund Freud e Alexander Luria —, transformando patologias neurológicas graves em explorações profundas sobre a identidade, a consciência e a dignidade humana. O Homem Que Confundiu Sua Mulher com um Chapéu permanece como seu livro mais emblemático e universalmente comovente.",
            "O caso que dá título à obra é o do Dr. P., um professor de música brilhante que perdeu a capacidade de reconhecer visualmente rostos e objetos cotidianos (prosopagnosia e agnosia visual grave), precisando de pistas auditivas e musicais contínuas para vestir suas roupas ou interagir com o mundo ao redor.",
            "Mas o que torna a leitura inesquecível é o olhar de Sacks: ele nunca enxerga seus pacientes como 'casos' defeituosos ou meros cérebros lesionados. Ele investiga como o organismo humano improvisa soluções poéticas, musicais e criativas para contornar perdas irreparáveis de memória, propriocepção ou equilíbrio.",
            "Uma obra-prima indispensável para quem atua em biofísica, neurociência, psicologia ou simplesmente busca compreender a fragilidade do que chamamos de 'eu'."
        ],
        "ponte": "Alexander Luria, Antonio Damasio, Merlin Sheldrake e Stephen Jay Gould.",
        "recepcao": "Clássico mundial da literatura de divulgação científica e médica, com mais de 30 edições internacionais."
    },
    "2026-11--a-ordem-do-tempo": {
        "id": "2026-11--a-ordem-do-tempo",
        "edicao": "2026-11",
        "ordem": 8,
        "secao": "ideias",
        "titulo": "A Ordem do Tempo",
        "titulo_original": "L'ordine del tempo",
        "autor": "Carlo Rovelli",
        "ano": 2023,
        "ano_original": 2017,
        "pais": "Itália",
        "tempo": "208 páginas",
        "genero": "ensaio científico / física quântica / filosofia",
        "tipo": "livro",
        "onde": "Objetiva (Tradução de Silvana Cobucci); impresso e e-book",
        "olho": "O físico italiano Carlo Rovelli desmonta a ilusão de um tempo universal e linear com elegância poética inspirada em Lucrécio e Einstein.",
        "texto": "Na gravidade quântica de laços, o tempo não passa: ele se desdobra em relações de probabilidade e entropia entre eventos singulares.",
        "resenha": [
            "Não existe um relógio único no centro do cosmos que marque a passagem dos segundos de forma idêntica na Terra e no espaço. Na física moderna, o tempo passa mais devagar na montanha do que na praia; no nível subatômico fundamental das partículas, as equações sequer possuem a variável 't'. O físico teórico italiano Carlo Rovelli guia o leitor por essa demolição da nossa intuição mais elementar com a clareza e a graça de um filósofo renascentista.",
            "Rovelli explica que a percepção comum de passado, presente e futuro decorre unicamente de uma visão míope e macroscópica de nós mesmos, governada pelo segundo princípio da termodinâmica: a entropia. É a perda gradual de informação e a dispersão do calor que geram a ilusão de uma seta do tempo orientada.",
            "A linguagem de Rovelli é de uma beleza ímpar, entremeada por versos do De Rerum Natura de Lucrécio e reflexões de Santo Agostinho, mostrando que a física contemporânea e a poesia clássica buscam responder aos mesmos mistérios ontológicos fundamentais.",
            "Um livro curto, luminoso e profundamente reconfortante sobre nossa efêmera condição de eventos passageiros na teia do universo."
        ],
        "ponte": "Sete Breves Lições de Física, Albert Einstein, Marcelo Gleiser e Jorge Luis Borges.",
        "recepcao": "Best-seller global elogiado por cientistas e literatos; leitura indispensável sobre as fronteiras da gravidade quântica."
    },
    "2026-11--a-queda-do-ceu": {
        "id": "2026-11--a-queda-do-ceu",
        "edicao": "2026-11",
        "ordem": 9,
        "secao": "ideias",
        "titulo": "A Queda do Céu: Palavras de um Xamã Yanomami",
        "titulo_original": "La chute du ciel",
        "autor": "Davi Kopenawa, Bruce Albert",
        "ano": 2023,
        "ano_original": 2010,
        "pais": "Brasil, França",
        "tempo": "768 páginas",
        "genero": "antropologia / cosmologia indígena / autobiografia xamânica",
        "tipo": "livro",
        "onde": "Companhia das Letras (Tradução de Beatriz Perrone-Moisés); impresso e e-book",
        "olho": "O testemunho xamânico monumental de Davi Kopenawa denuncia a cegueira do 'povo da mercadoria' e profetiza o colapso ecológico da Terra.",
        "texto": "Fruto de três décadas de amizade entre Kopenawa e o antropólogo Bruce Albert, a obra máxima do pensamento ameríndio contemporâneo.",
        "resenha": [
            "Se existisse um cânone definitivo dos textos ecológicos mais fundamentais de toda a história humana, A Queda do Céu ocuparia sem dúvida o topo da lista. Fruto de conversas gravadas ao longo de quase trinta anos entre o líder e xamã yanomami Davi Kopenawa e o etnólogo francês Bruce Albert, o livro é ao mesmo tempo uma autobiografia épica, uma introdução incomparável ao xamanismo amazônico e um manifesto geopolítico devastador contra a sanha predatória do garimpo ilegal e do agronegócio.",
            "Kopenawa narra seu aprendizado rigoroso com os espíritos xapiri, que descem dos espelhos cósmicos sob o efeito do pó sagrado de yãkoana para sustentar o céu e impedir que a fumaça de epidemias dos brancos (xawara) destrua a fertilidade da floresta (urihi a).",
            "Sua crítica ao que chama de 'povo da mercadoria' — nós, os brancos que comemos terra e ouro sem nunca nos saciarmos e que tratamos as árvores como coisas mortas — antecipou com precisão cirúrgica a atual emergência climática do Antropoceno.",
            "Uma leitura que abala certezas ocidentais e transforma para sempre a relação do leitor com o planeta vivo."
        ],
        "ponte": "Eduardo Viveiros de Castro, Ailton Krenak, Claude Lévi-Strauss e Emanuele Coccia.",
        "recepcao": "Clássico mundial da antropologia moderna; apontado por filósofos e ecologistas de todo o mundo como uma das obras mais decisivas do nosso tempo."
    },
    "2026-11--metamorfoses": {
        "id": "2026-11--metamorfoses",
        "edicao": "2026-11",
        "ordem": 10,
        "secao": "ideias",
        "titulo": "Metamorfoses",
        "titulo_original": "Métamorphoses",
        "autor": "Emanuele Coccia",
        "ano": 2023,
        "ano_original": 2020,
        "pais": "Itália, França",
        "tempo": "224 páginas",
        "genero": "filosofia da natureza / biologia especulativa / ensaio ecológico",
        "tipo": "livro",
        "onde": "Dantes Editora / Ubu (Tradução de Fernando Scheibe); impresso e e-book",
        "olho": "O filósofo italiano Emanuele Coccia argumenta que a vida na Terra é uma única matéria em perpétua transmigração de formas.",
        "texto": "Da lagarta que se dissolve em líquido imaginal dentro do casulo para virar borboleta à nossa herança bacteriana.",
        "resenha": [
            "Depois de fascinar o meio acadêmico e literário com A Vida das Plantas (2018), o filósofo italiano Emanuele Coccia dá um passo ainda mais ousado em Metamorfoses: defender que o nascimento, a alimentação e a evolução não são processos de criação ex nihilo, mas momentos de uma única vida que muda de pele e de corpo incessantemente há quatro bilhões de anos.",
            "Coccia parte do fenômeno biológico misterioso da metamorfose dos insetos holometábolos: a lagarta não 'cresce' para virar borboleta; ela digere seus próprios tecidos dentro do casulo até virar uma sopa celular de discos imaginais que reorganiza a anatomia num ser alado totalmente novo, mantendo, no entanto, traços de memória da lagarta.",
            "A partir desse exemplo biológico concreto, Coccia estende a metamorfose a todos os seres vivos: nossos corpos são feitos de minerais que outrora pertenceram a dinossauros, plantas antigas e bactérias primordiais. O eu humano deixa de ser uma fortaleza isolada para ser um veículo temporário pelo qual a matéria da Terra experimenta o cosmos.",
            "Uma obra de filosofia lírica, solar e profundamente generosa que cura o isolamento do homem contemporâneo."
        ],
        "ponte": "A Vida das Plantas (Coccia), Merlin Sheldrake, Donna Haraway e Bruno Latour.",
        "recepcao": "Aclamado na França e na Itália como uma das vozes mais originais da nova ecologia filosófica europeia."
    },
    "2026-11--vida-3-0": {
        "id": "2026-11--vida-3-0",
        "edicao": "2026-11",
        "ordem": 11,
        "secao": "ideias",
        "titulo": "Vida 3.0: O Ser Humano na Era da Inteligência Artificial",
        "titulo_original": "Life 3.0: Being Human in the Age of Artificial Intelligence",
        "autor": "Max Tegmark",
        "ano": 2023,
        "ano_original": 2017,
        "pais": "Suécia, EUA",
        "tempo": "448 páginas",
        "genero": "ensaio científico / inteligência artificial / física teórica / ética",
        "tipo": "livro",
        "onde": "Record (Tradução de Alexandre Martins); impresso e e-book",
        "olho": "O físico do MIT e cofundador do Future of Life Institute analisa os cenários futuros da inteligência artificial geral.",
        "texto": "Uma reflexão lúcida sobre metas de alinhamento, consciência sintética e como garantir que a tecnologia beneficie a humanidade.",
        "resenha": [
            "Em meio à histeria de manchetes alarmistas e promessas de marketing bilionário, o livro de Max Tegmark, professor de física no MIT e fundador do Future of Life Institute, permanece como o guia mais sóbrio, rigoroso e abrangente sobre os rumos da Inteligência Artificial.",
            "Tegmark divide a história da vida em três estágios conceituais: a Vida 1.0 (biológica, onde tanto o hardware biológico quanto o software de comportamento são moldados pela evolução lenta do DNA), a Vida 2.0 (cultural, onde o hardware continua biológico, mas o software pode ser reprogramado rapidamente pelo aprendizado e pela linguagem) e a Vida 3.0 (tecnológica, onde um agente pode redesenhar não apenas seu software, mas seu próprio hardware computacional).",
            "O coração do livro é o debate sobre o 'alinhamento de objetivos' (goal alignment): como programar sistemas de IA com capacidades sobre-humanas para que suas metas nunca divirjam dos valores de florescimento e sobrevivência da espécie humana.",
            "Leitura obrigatória para qualquer profissional de tecnologia, cientistas de dados e cidadãos que desejam participar conscientemente do debate regulatório atual."
        ],
        "ponte": "Nick Bostrom (Superinteligência), Stuart Russell (Compatibilidade Humana), Yuval Noah Harari e Carl Sagan.",
        "recepcao": "Recomendado por Elon Musk e Barack Obama; referência seminal nos estudos de segurança e alinhamento de IA."
    },
    "2026-11--a-danca-do-universo": {
        "id": "2026-11--a-danca-do-universo",
        "edicao": "2026-11",
        "ordem": 12,
        "secao": "ideias",
        "titulo": "A Dança do Universo: Dos Mitos de Criação ao Big Bang",
        "titulo_original": "A Dança do Universo",
        "autor": "Marcelo Gleiser",
        "ano": 2024,
        "ano_original": 1997,
        "pais": "Brasil, EUA",
        "tempo": "432 páginas",
        "genero": "história da ciência / cosmologia / ensaio filosófico",
        "tipo": "livro",
        "onde": "Companhia das Letras; edição revista e ampliada; impresso e e-book",
        "olho": "Em edição comemorativa, o clássico de Marcelo Gleiser que une o encanto dos mitos cosmogônicos às teorias da física moderna.",
        "texto": "Vencedor do Prêmio Jabuti e do Prêmio Templeton, uma jornada inesquecível pelo desejo humano de decifrar as origens do cosmos.",
        "resenha": [
            "Poucos livros de divulgação científica escritos em língua portuguesa alcançaram a longevidade e o impacto cultural de A Dança do Universo, do físico e cosmólogo brasileiro Marcelo Gleiser. Lançado no final dos anos 1990 e continuamente reeditado, o livro consolidou Gleiser como uma ponte viva entre a ciência de ponta nos EUA e a cultura brasileira.",
            "A grande originalidade do ensaio é não tratar a cosmologia moderna como uma ruptura absoluta com o passado mítico, mas como a continuação natural da mesma obsessão humana que levou nossos ancestrais a olharem para a abóbada celeste e inventarem mitos de criação a partir do barro, da luz ou do ovo primordial.",
            "Gleiser percorre com maestria a revolução de Copérnico, Galileu, Kepler e Newton, até desembocar na teoria da relatividade de Einstein, na física quântica e no modelo padrão do Big Bang, sempre ressaltando as dúvidas, os impasses e a beleza humana por trás de cada avanço teórico.",
            "Uma celebração da curiosidade intelectual que continua a inspirar novas gerações de cientistas e leitores."
        ],
        "ponte": "Carl Sagan (Cosmos), Stephen Hawking, Carlo Rovelli e Fritjof Capra.",
        "recepcao": "Vencedor do Prêmio Jabuti de Não Ficção em 1998; livro fundamental da divulgação científica no Brasil."
    },

    # --- SEÇÃO BRASIL ---
    "2026-11--salvar-o-fogo": {
        "id": "2026-11--salvar-o-fogo",
        "edicao": "2026-11",
        "ordem": 13,
        "secao": "brasil",
        "titulo": "Salvar o Fogo",
        "titulo_original": "Salvar o Fogo",
        "autor": "Itamar Vieira Junior",
        "ano": 2023,
        "ano_original": 2023,
        "pais": "Brasil",
        "tempo": "320 páginas",
        "genero": "romance contemporâneo / literatura brasileira / saga familiar",
        "tipo": "livro",
        "onde": "Todavia; impresso e e-book",
        "olho": "No vale do rio Paraguaçu na Bahia, Itamar Vieira Junior constrói uma saga monumental sobre laços de sangue, posse da terra e misticismo.",
        "texto": "Após o fenômeno Torto Arado, o autor mergulha na comunidade ribeirinha de Tapera do Paraguaçu pela voz da lavadeira Luzia.",
        "resenha": [
            "A grande pergunta que pairava sobre a literatura brasileira contemporânea era como Itamar Vieira Junior responderia ao estrondoso impacto de Torto Arado, um dos maiores fenômenos editoriais das últimas décadas. Salvar o Fogo respondeu com maturidade estilística e densidade polifônica ainda maiores, confirmando a força permanente de seu projeto literário.",
            "Ambientado na comunidade fictícia de Tapera do Paraguaçu, no Recôncavo Baiano, o livro acompanha a família de Mundinho e suas filhas e filhos, com destaque para Luzia, uma mulher dotada de intuições premonitórias e marcada por dores físicas crônicas que cuida dos afazeres de uma igreja dominada por padres de uma ordem religiosa que detém a posse cartorial das terras onde os caboclos e ribeirinhos vivem há gerações.",
            "A chegada do irmão Moisés, educado em Salvador no seminário para ser padre, reabre feridas de silenciamento, violência fundiária e preconceito racial. Vieira Junior domina com maestria a fala popular, a vegetação ribeirinha e os rituais de cura dos encantados.",
            "Uma obra-prima vigorosa que aprofunda a ferida aberta da propriedade de terra no Brasil com lírica inesquecível."
        ],
        "ponte": "Torto Arado, Graciliano Ramos, Jorge Amado e Guimarães Rosa.",
        "recepcao": "Best-seller imediato no Brasil e no exterior; aclamado pela crítica por sua complexidade psicológica e força poética."
    },
    "2026-11--a-visao-em-parafuso": {
        "id": "2026-11--a-visao-em-parafuso",
        "edicao": "2026-11",
        "ordem": 14,
        "secao": "brasil",
        "titulo": "A Visão em Parafuso",
        "titulo_original": "A Visão em Parafuso: Antologia Poética",
        "autor": "Manoel de Barros",
        "ano": 2024,
        "ano_original": 2003,
        "pais": "Brasil",
        "tempo": "256 páginas",
        "genero": "poesia / literatura brasileira / ecologia lírica",
        "tipo": "livro",
        "onde": "Alfaguara / Companhia das Letras; impresso e e-book",
        "olho": "A celebração do desimportante, dos caramujos e da matéria rasteira na antologia essencial do maior poeta pantaneiro do Brasil.",
        "texto": "Uma aula de desaprendizagem da linguagem utilitária para enxergar o mundo com os olhos puros das águas e dos pássaros.",
        "resenha": [
            "Manoel de Barros (1916-2014) gostava de dizer que sua profissão era 'desinventar a linguagem'. Em uma época viciada na velocidade, na eficácia produtiva e na ostentação de poder, os versos do poeta do Pantanal matogrossense funcionam como um poderoso antídoto ético e estético, convidando o leitor a se ajoelhar no chão para conversar com formigas, pedras e cacos de vidro.",
            "A Visão em Parafuso reúne os momentos mais sublimes de sua obra — de O Guardador de Águas e Ensaios Fotográficos a Memórias Inventadas —, onde a gramática é torcida para que as palavras voltem a ter peso de matéria viva, húmus e vento.",
            "Para Barros, a poesia não serve para explicar o mundo ou ditar lições morais; serve para desaprender o olhar viciado e devolver às coisas ordinárias o espanto sagrado de sua existência inútil e bela.",
            "Um livro para manter na cabeceira e abrir a qualquer hora do dia para desintoxicar a mente das urgências do mundo urbano."
        ],
        "ponte": "Guimarães Rosa, Francis Ponge, Carlos Drummond de Andrade e A Trama da Vida (Sheldrake).",
        "recepcao": "Dois prêmios Jabuti na carreira; reconhecido internacionalmente como uma das vozes poéticas mais singulares da língua portuguesa."
    },
    "2026-11--mata-doce": {
        "id": "2026-11--mata-doce",
        "edicao": "2026-11",
        "ordem": 15,
        "secao": "brasil",
        "titulo": "Mata Doce",
        "titulo_original": "Mata Doce",
        "autor": "Luciany Aparecida",
        "ano": 2023,
        "ano_original": 2023,
        "pais": "Brasil",
        "tempo": "304 páginas",
        "genero": "romance / literatura brasileira contemporânea",
        "tipo": "livro",
        "onde": "Alfaguara; impresso e e-book",
        "olho": "O vilarejo de Mata Doce e a saga mítica de Maria Filhana numa das estreias literárias mais arrebatadoras da ficção brasileira recente.",
        "texto": "A escritora baiana Luciany Aparecida cria uma prosa de alta voltagem poética sobre maternidade, violência, desejo e luto.",
        "resenha": [
            "Poucas estreias literárias recentes causaram um impacto tão fulminante quanto Mata Doce, da escritora, professora e pesquisadora baiana Luciany Aparecida. O romance constrói um vilarejo mítico no interior da Bahia onde o tempo parece circular em redemoinhos de poeira e segredos sussurrados sob as copas das jaqueiras.",
            "A protagonista é Maria Filhana, uma mulher que carrega a dor da perda e a honra de sua linhagem amorosa, criada por duas mães adotivas — Mariinha e Tuninha — que desafiaram a moral patriarcal da região. A chegada de uma tragédia que envolve abuso, assassinato e a disputa pelas terras de Mata Doce põe à prova a resiliência das mulheres da comunidade.",
            "A grande força do livro reside na dicção de Luciany Aparecida: sua prosa tem a cadência do canto de carpideira e a precisão afiada do corte da foice, misturando lendas populares, rituais do catolicismo sertanejo e uma sensualidade crua.",
            "Um romance extraordinário que coloca Luciany Aparecida na linha de frente da nova literatura brasileira."
        ],
        "ponte": "Itamar Vieira Junior, Raduan Nassar (Lavoura Arcaica), Conceição Evaristo e Toni Morrison.",
        "recepcao": "Aclamado pela crítica nos principais cadernos culturais do país; finalista dos principais prêmios literários nacionais."
    },
    "2026-11--doramar-ou-a-odisseia": {
        "id": "2026-11--doramar-ou-a-odisseia",
        "edicao": "2026-11",
        "ordem": 16,
        "secao": "brasil",
        "titulo": "Doramar ou a Odisseia: Histórias",
        "titulo_original": "Doramar ou a Odisseia: Histórias",
        "autor": "Itamar Assumpção",
        "ano": 2023,
        "ano_original": 2023,
        "pais": "Brasil",
        "tempo": "160 páginas",
        "genero": "contos / crônica poética / literatura da vanguarda paulista",
        "tipo": "livro",
        "onde": "Todavia (Organização de Frederico Coelho); impresso e e-book",
        "olho": "Os contos e textos em prosa do mestre da Vanguarda Paulista revelam o humor cortante e a genialidade literária de Itamar Assumpção.",
        "texto": "Uma joia redescoberta que une a mitologia grega à crônica urbana da noite paulistana, do racismo cotidiano e da paixão pela língua.",
        "resenha": [
            "O Brasil conhece e reverencia Itamar Assumpção (1949-2003) como o faraó negro da Vanguarda Paulista, baixista virtuoso e criador de álbuns fundamentais como Beleléu e Bicho de 7 Cabeças. O que poucos sabiam era que o compositor de Tietê também era um contista genial, dono de uma prosa afiada, inventiva e profundamente musical.",
            "Organizado pelo ensaísta Frederico Coelho a partir dos cadernos originais e datiloscritos guardados pelo acervo da família, Doramar ou a Odisseia reúne narrativas curtas onde Itamar reinterpreta o mito de Homero sob a ótica de um homem negro periférico navegando os perigos da noite de São Paulo nos anos 1980.",
            "As histórias são povoadas por músicos sem dinheiro para o ônibus, garçons noturnos, paixões fulminantes e reflexões cortantes sobre a violência policial e o racismo estrutural, sempre filtrados por um humor corrosivo e uma elegância lexical deslumbrante.",
            "Um livro indispensável para os fãs da música de Itamar e para qualquer leitor apaixonado pela grande prosa brasileira de vanguarda."
        ],
        "ponte": "Itamar Assumpção (música), Lima Barreto, Luiz Melodia, Oswald de Andrade e Machado de Assis.",
        "recepcao": "Celebrado no lançamento na FLIP e na imprensa cultural como uma das mais felizes ressurreições literárias recentes."
    },
    "2026-11--o-arroz-de-palma": {
        "id": "2026-11--o-arroz-de-palma",
        "edicao": "2026-11",
        "ordem": 17,
        "secao": "brasil",
        "titulo": "O Arroz de Palma",
        "titulo_original": "O Arroz de Palma",
        "autor": "Francisco Azevedo",
        "ano": 2023,
        "ano_original": 2008,
        "pais": "Brasil",
        "tempo": "368 páginas",
        "genero": "romance familiar / ficção histórica / memória",
        "tipo": "livro",
        "onde": "Record; impresso e e-book",
        "olho": "Cem anos de uma família de imigrantes portugueses no Rio de Janeiro unidos pela tradição mágica de um punhado de arroz de casamento.",
        "texto": "'Família é prato difícil de preparar': a saga enternecedora que conquistou leitores pelo afeto da culinária e da memória.",
        "resenha": [
            "Há livros que encontram o leitor como um almoço de domingo preparado com amor por várias gerações em torno de uma grande mesa de cozinha. O Arroz de Palma, do dramaturgo e escritor carioca Francisco Azevedo, é exatamente esse tipo de romance acolhedor, terno e generoso.",
            "A trama abre em 1908, numa aldeia em Portugal, no casamento de José Custódio e Maria Romana. Na saída da igreja, Palma, o irmão do noivo, atira sobre o casal um punhado de arroz benzido com votos de fertilidade e paz. Aquele arroz recolhido do chão transforma-se na relíquia que atravessará o oceano Atlântico até o Rio de Janeiro, acompanhando quatro gerações de descendentes ao longo de todo o século XX.",
            "Narrado pelo octogenário Antônio enquanto ele prepara o banquete que reunirá filhos e netos para finalmente cozinhar os últimos grãos daquele arroz centenário, o livro entrelaça a história política da capital carioca com os pequenos dramas de nascimentos, desavenças e reconciliações domésticas.",
            "Uma celebração inesquecível da família e da memória afetiva que aquece o coração com extrema delicadeza."
        ],
        "ponte": "Como Água para Chocolate (Laura Esquivel), Milton Hatoum, Eça de Queirós e Gabriel García Márquez.",
        "recepcao": "Fenômeno contínuo de boca a boca com dezenas de reimpressões no Brasil e traduções na Europa e América Latina."
    },

    # --- SEÇÃO ACHADOS & CLÁSSICOS ---
    "2026-11--a-sociedade-do-cansaco": {
        "id": "2026-11--a-sociedade-do-cansaco",
        "edicao": "2026-11",
        "ordem": 18,
        "secao": "achados",
        "titulo": "A Sociedade do Cansaço",
        "titulo_original": "Müdigkeitsgesellschaft",
        "autor": "Byung-Chul Han",
        "ano": 2023,
        "ano_original": 2010,
        "pais": "Coreia do Sul, Alemanha",
        "tempo": "128 páginas",
        "genero": "ensaio filosófico / crítica cultural / sociologia",
        "tipo": "livro",
        "onde": "Vozes (Tradução de Enio Paulo Giachini); impresso e e-book",
        "olho": "Byung-Chul Han diagnostica a patologia da autoexploração voluntária e o colapso psíquico sob o imperativo tirânico do 'você pode'.",
        "texto": "Um dos livros de filosofia mais influentes do século XXI sobre burnout, depressão e a perda da capacidade contemplativa.",
        "resenha": [
            "Em pouco mais de uma centena de páginas concisas e afiadas como bisturi, o filósofo sul-coreano radicado em Berlim Byung-Chul Han sintetizou a angústia fundamental do sujeito contemporâneo: nós deixamos para trás a sociedade disciplinar descrita por Michel Foucault — feita de prisões, fábricas e proibições externas — para entrar na sociedade do desempenho, onde cada indivíduo é o seu próprio algoz e explorador.",
            "Sob o lema motivacional onipresente do 'Yes, we can', o indivíduo contemporâneo não é mais coagido por um chefe autoritário; ele se explora voluntariamente acreditando que está se realizando, até desabar no esgotamento físico e na depressão crônica.",
            "Han argumenta que o excesso de positividade, a hiperatividade digital e a perda da negatividade da pausa destruíram a capacidade de contemplação que dá origem à verdadeira arte e ao pensamento filosófico.",
            "Uma leitura rápida, cortante e indispensável para repensar nossa relação com o trabalho, as telas e o tempo livre."
        ],
        "ponte": "Michel Foucault, Friedrich Nietzsche, Theodor Adorno e Mark Fisher (Realismo Capitalista).",
        "recepcao": "Impacto planetário indiscutível; obra de referência na sociologia e na saúde mental contemporânea."
    },
    "2026-11--stoner": {
        "id": "2026-11--stoner",
        "edicao": "2026-11",
        "ordem": 19,
        "secao": "achados",
        "titulo": "Stoner",
        "titulo_original": "Stoner",
        "autor": "John Williams",
        "ano": 2023,
        "ano_original": 1965,
        "pais": "EUA",
        "tempo": "296 páginas",
        "genero": "romance clássico / literatura acadêmica / drama existencial",
        "tipo": "livro",
        "onde": "Rádio Londres (Tradução de Marcos Maffei); impresso e e-book",
        "olho": "O romance esquecido de 1965 que virou sensação mundial: a extraordinária e comovente vida ordinária de um professor de literatura em Missouri.",
        "texto": "Uma obra-prima silenciosa sobre vocação, casamento infeliz, paixão tardia e a dignidade inabalável diante da derrota.",
        "resenha": [
            "Publicado discretamente em 1965 e praticamente ignorado na época, Stoner foi resgatado meio século depois para ser celebrado por escritores como Ian McEwan, Bret Easton Ellis e Julian Barnes como um dos romances mais perfeitos e comoventes de toda a literatura americana.",
            "A trama acompanha William Stoner, filho de camponeses pobres do interior do Missouri enviado à universidade agrícola no início do século XX. Lá, ao assistir a uma aula sobre os sonetos de Shakespeare, Stoner tem uma epifania silenciosa e decide abandonar a agricultura para dedicar a vida aos estudos de literatura inglesa.",
            "Sua trajetória não tem grandes heroísmos públicos: um casamento gélido e destrutivo com uma mulher amargurada, as intrigas mesquinhas do departamento universitário chefiado por um rival rancoroso e um caso de amor secreto e luminoso que precisa ser sacrificado. No entanto, a integridade moral com que Stoner encara cada revés confere à sua existência uma grandeza trágica sublime.",
            "Uma lição de prosa límpida, comedida e devastadora sobre o amor aos livros e a coragem de viver sem autoengano."
        ],
        "ponte": "F. Scott Fitzgerald, Richard Yates (Foi Apenas um Sonho), Philip Roth e Chekhov.",
        "recepcao": "Ressurreição crítica sem precedentes no século XXI, com milhões de exemplares vendidos no mundo inteiro."
    },
    "2026-11--o-leopardo": {
        "id": "2026-11--o-leopardo",
        "edicao": "2026-11",
        "ordem": 20,
        "secao": "achados",
        "titulo": "O Leopardo",
        "titulo_original": "Il Gattopardo",
        "autor": "Giuseppe Tomasi di Lampedusa",
        "ano": 2023,
        "ano_original": 1958,
        "pais": "Itália",
        "tempo": "312 páginas",
        "genero": "romance histórico / clássico / literatura italiana",
        "tipo": "livro",
        "onde": "Companhia das Letras (Tradução de Maurício Santana Dias); impresso e e-book",
        "olho": "'Se queremos que tudo fique como está, é preciso que tudo mude': a melancolia da nobreza siciliana diante do avanço da história.",
        "texto": "A obra-prima póstuma de Lampedusa sobre a unificação italiana, adaptada magistralmente ao cinema por Luchino Visconti.",
        "resenha": [
            "Recusado em vida pelas grandes editoras italianas e publicado apenas após a morte prematura de seu autor, O Leopardo de Giuseppe Tomasi di Lampedusa tornou-se um dos maiores marcos da ficção histórica de todos os tempos. Ambientado na Sicília durante o desembarque de Garibaldi em 1860, o romance capta como nenhum outro o instante crepuscular em que uma classe dominante percebe que seu tempo histórico se esgotou.",
            "Dom Fabrizio Corbera, Príncipe de Salina — homem de porte imponente e paixão solitária pela astronomia —, assiste à decadência da aristocracia feudal siciliana e à ascensão de uma nova burguesia vulgar e endinheirada simbolizada pelo prefeito Don Calogero. Seu sobrinho Tancredi percebe a virada antes de todos e se alia aos revolucionários, proferindo a máxima célebre que virou sinônimo de cinismo político: 'Se queremos que tudo fique como está, é preciso que tudo mude'.",
            "A prosa de Lampedusa é suntuosa, saturada de sol, poeira siciliana e o cheiro doce de flores murchas nos palácios de Donnafugata. O baile no terceiro ato é uma das maiores cenas de reflexão sobre a morte e a passagem do tempo da história da literatura ocidental.",
            "Uma leitura majestosa, cínica e melancólica que ilumina os paradoxos permanentes de qualquer transição política."
        ],
        "ponte": "Marcel Proust, Guerra e Paz (Tolstói), Memórias de Adriano (Yourcenar) e Visconti.",
        "recepcao": "Prêmio Strega em 1959; considerado por consenso internacional um dos pontos mais altos da literatura europeia."
    },
    "2026-11--a-hora-da-estrela": {
        "id": "2026-11--a-hora-da-estrela",
        "edicao": "2026-11",
        "ordem": 21,
        "secao": "achados",
        "titulo": "A Hora da Estrela",
        "titulo_original": "A Hora da Estrela",
        "autor": "Clarice Lispector",
        "ano": 2024,
        "ano_original": 1977,
        "pais": "Brasil",
        "tempo": "96 páginas",
        "genero": "romance curto / clássico / literatura brasileira",
        "tipo": "livro",
        "onde": "Rocco; edição especial; impresso e e-book",
        "olho": "O canto de cisne de Clarice Lispector: a miséria invisível de Macabéa no Rio de Janeiro e a angústia do escritor diante dos despossuídos.",
        "texto": "Publicado semanas antes da morte de Clarice em 1977, uma obra-prima breve sobre culpa de classe, solidão e o direito ao grito.",
        "resenha": [
            "Concluído quando Clarice Lispector já enfrentava o câncer terminal que a vitimaria em dezembro de 1977, A Hora da Estrela é um dos ápices da literatura brasileira. Aqui, a autora de Perto do Coração Selvagem e A Paixão Segundo G.H. sai das angústias da classe média para encarar a miséria nua e crua da migração nordestina na metrópole carioca.",
            "Para contar a história de Macabéa — a jovem alagoana órfã, datilógrafa subnutrida que adora café frio com cachorro-quente e coleciona anúncios da rádio Relógio Federal —, Clarice cria o narrador fictício Rodrigo S.M., um escritor burguês atormentado pela própria culpa de ter teto e palavras enquanto Macabéa mal tem consciência de sua própria existência desvalida.",
            "O contraste entre a arrogância de Olímpico de Jesus, o namorado metalúrgico que sonha ser deputado, e a doçura ingênua de Macabéa atinge momentos de dor e poesia sem paralelos, culminando na famosa consulta à cartomante Madame Carlota.",
            "Um livro curto que se lê em um único fôlego, mas cujas perguntas sobre justiça, linguagem e empatia ecoam para sempre na consciência."
        ],
        "ponte": "Clarice Lispector, Vidas Secas (Graciliano Ramos), Carolina Maria de Jesus e Machado de Assis.",
        "recepcao": "Patrimônio incontestável da cultura brasileira; leitura obrigatória e reverenciada internacionalmente."
    },
    "2026-11--a-cidade-e-as-serras": {
        "id": "2026-11--a-cidade-e-as-serras",
        "edicao": "2026-11",
        "ordem": 22,
        "secao": "achados",
        "titulo": "A Cidade e as Serras",
        "titulo_original": "A Cidade e as Serras",
        "autor": "Eça de Queirós",
        "ano": 2023,
        "ano_original": 1901,
        "pais": "Portugal",
        "tempo": "288 páginas",
        "genero": "romance clássico / literatura portuguesa / sátira social",
        "tipo": "livro",
        "onde": "L&PM / Ateliê Editorial; impresso e e-book",
        "olho": "A sátira hilária e deliciosa de Eça de Queirós sobre o delírio da tecnologia parisiense em contraste com a fartura campestre de Tormes.",
        "texto": "Jacinto de Tormes descobre que o progresso das máquinas só gerou tédio e reencontra a alegria no pão caseiro, na horta e nas montanhas do Douro.",
        "resenha": [
            "Escrito no final da vida de Eça de Queirós (1845-1900) e publicado postumamente, A Cidade e as Serras é uma das obras mais luminosas, bem-humoradas e proféticas de toda a literatura em língua portuguesa. O que Eça satirizou na Paris fin-de-siècle de 1890 antecipou com precisão cirúrgica o nosso atual cansaço das notificações, gadgets e dependência tecnológica excessiva.",
            "O protagonista é Jacinto de Tormes, herdeiro riquíssimo que vive no palacete número 202 dos Champs-Élysées cercado por 30 mil livros, telégrafos particulares, elevadores hidráulicos, telefones primitivos e fonógrafos. Quanto mais aparelhos Jacinto compra para economizar tempo e aumentar o conforto, mais infeliz, entediado e estressado ele se torna.",
            "A grande virada ocorre quando um desabamento na capela dos antepassados força Jacinto a viajar para suas propriedades rurais em Tormes, nas serras do Douro. Desprovido de suas malas e quinquilharias perdidas no trem, ele reencontra a alegria de viver ao saborear um prato de arroz com favas, beber vinho fresco da adega e caminhar descalço sob a sombra das castanheiras.",
            "Um banquete literário inigualável que celebra a simplicidade orgânica contra a neurose mecânica."
        ],
        "ponte": "Os Maias, O Primo Basílio, Henry David Thoreau (Walden) e Byung-Chul Han.",
        "recepcao": "Clássico supremo do realismo e da literatura portuguesa; lido com encantamento inalterado há mais de 120 anos."
    }
}

LIVRO_GUIAS = {
    "guia-biologia-ensaio-narrativa-2026": {
        "id": "guia-biologia-ensaio-narrativa-2026",
        "edicao": "2026-11",
        "tipo": "roteiro de leitura",
        "titulo": "Biologia como narrativa: a ciência que se lê como grande literatura",
        "subtitulo": "Cinco ensaios fundamentais onde cientistas e pesquisadores transformam o mundo vivo em alta prosa reflexiva.",
        "texto": (
            "A ciência não precisa ser fria, burocrática ou confinada a jargões impenetráveis. Quando grandes biólogos e naturalistas "
            "empunham a pena com sensibilidade literária, a descrição de uma célula, de um fungo ou de uma floresta torna-se "
            "uma meditação comovente sobre nossa própria existência. Este guia reúne cinco clássicos contemporâneos do ensaio biológico."
        ),
        "livros": [
            {
                "titulo": "A Trama da Vida",
                "autor": "Merlin Sheldrake",
                "ano": 2020,
                "nota": "Como os fungos tecem a rede subterrânea que sustenta as florestas e reinventam a ideia de cooperação biológica.",
                "onde": "Ubu Editora"
            },
            {
                "titulo": "O Homem Que Confundiu Sua Mulher com um Chapéu",
                "autor": "Oliver Sacks",
                "ano": 1985,
                "nota": "O mestre da neurologia humanista investiga a mente e a identidade através de casos clínicos inesquecíveis.",
                "onde": "Companhia das Letras"
            },
            {
                "titulo": "Metamorfoses",
                "autor": "Emanuele Coccia",
                "ano": 2020,
                "nota": "A continuidade física e espiritual entre animais, vegetais e humanos além das fronteiras artificiais das espécies.",
                "onde": "Dantes / Ubu"
            },
            {
                "titulo": "A Montanha Viva",
                "autor": "Nan Shepherd",
                "ano": 1977,
                "nota": "O clássico do naturalismo poético escocês que une caminhada de altitude e filosofia dos sentidos.",
                "onde": "Zahar"
            },
            {
                "titulo": "O Polegar do Panda",
                "autor": "Stephen Jay Gould",
                "ano": 1980,
                "nota": "As imperfeições e improvisos da evolução natural narrados por um dos maiores divulgadores científicos do século.",
                "onde": "Companhia das Letras"
            }
        ]
    },
    "guia-vozes-terra-brasil-2026": {
        "id": "guia-vozes-terra-brasil-2026",
        "edicao": "2026-11",
        "tipo": "roteiro de leitura",
        "titulo": "Vozes da terra e resistência: literatura brasileira além do asfalto",
        "subtitulo": "Cinco obras contemporâneas que mergulham no sertão, nas águas e nas florestas para reinventar a nossa ficção.",
        "texto": (
            "A ficção brasileira mais potente das últimas décadas não está nos gabinetes urbanos ou no cinismo das metrópoles, "
            "mas nas margens dos rios, nos quilombos, nos sertões e nas aldeias indígenas. Este roteiro celebra autores que recolocam "
            "a terra, os corpos e a ancestralidade no centro da nossa imaginação."
        ),
        "livros": [
            {
                "titulo": "Torto Arado",
                "autor": "Itamar Vieira Junior",
                "ano": 2019,
                "nota": "A saga de Bibiana e Belonísia na Chapada Diamantina que recolocou a questão agrária e quilombola no topo da literatura.",
                "onde": "Todavia"
            },
            {
                "titulo": "Salvar o Fogo",
                "autor": "Itamar Vieira Junior",
                "ano": 2023,
                "nota": "A luta ribeirinha pelo direito à terra e à memória no vale do Paraguaçu.",
                "onde": "Todavia"
            },
            {
                "titulo": "A Queda do Céu",
                "autor": "Davi Kopenawa e Bruce Albert",
                "ano": 2010,
                "nota": "O manifesto xamânico yanomami mais contundente já publicado sobre a preservação da floresta e da vida.",
                "onde": "Companhia das Letras"
            },
            {
                "titulo": "Ideias para Adiar o Fim do Mundo",
                "autor": "Ailton Krenak",
                "ano": 2019,
                "nota": "Reflexões filosóficas fulgurantes sobre a desumanização ocidental e a comunhão com rios e montanhas.",
                "onde": "Companhia das Letras"
            },
            {
                "titulo": "Mata Doce",
                "autor": "Luciany Aparecida",
                "ano": 2023,
                "nota": "A prosa arrebatadora da autora baiana sobre amor de mães, violência e segredos no interior do país.",
                "onde": "Alfaguara"
            }
        ]
    }
}
