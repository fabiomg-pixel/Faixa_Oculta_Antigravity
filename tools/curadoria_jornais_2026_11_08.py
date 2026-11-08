#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curadoria integral extraída das edições impressas de 08 de novembro de 2026 (Beeper):
- Folha de S.Paulo (52 págs)
- O Estado de S. Paulo (56 págs)
- O Globo (45 págs)
- Valor Econômico (Edição de Fim de Semana, 58 págs)
- Financial Times Weekend (56 págs)
- The Washington Post (Sunday, 78 págs)
- The Guardian (212 págs)
- The Sunday Times UK (352 págs)

Todo o material internacional está traduzido para o português culto, preservando os títulos originais.
"""

def obter_jornais_2026_11_08(imagens_por_jornal=None):
    imagens_por_jornal = imagens_por_jornal or {}
    return {
        "data_edicao": "2026-11-08",
        "resumo": "Nas edições deste domingo (8 de novembro de 2026), os grandes diários brasileiros concentram-se no dilema fiscal do novo mandato de Lula sob juros elevados, no isolamento político de Flávio Bolsonaro após sua viagem aos Estados Unidos, nos custos bilionários da PEC da Segurança Pública e na crise institucional do Paraguai após a renúncia e prisão de Santiago Peña. Na imprensa internacional, o Financial Times, o Washington Post e o Guardian dissecam o terremoto político da 'onda azul' democrata nas midterms americanas, o freio regulatório sobre os megacentros de dados de inteligência artificial e o alarme europeu diante das negociações diretas entre a Casa Branca e Moscou.",
        "contraste": "Enquanto Folha de S.Paulo e Valor Econômico priorizam o alerta de economistas sobre o risco de estagnação ou recessão em 2027 caso o Planalto adie o corte estrutural de gastos, O Globo destaca a rejeição de 60% dos brasileiros à postura de Flávio Bolsonaro nos EUA, e o Estadão põe em foco a disputa energética na Margem Equatorial e a governabilidade no Congresso. No exterior, o Financial Times enfatiza o choque financeiro sobre as Big Techs e o IPO da Anthropic, ao passo que o Washington Post destaca a mobilização histórica do eleitorado negro no Sul dos EUA e a expurgação ética no Capitólio.",
        "manchetes": [
            {
                "jornal": "Folha de S.Paulo",
                "pais": "Brasil",
                "escopo": "nacional",
                "total_paginas": 52,
                "imagem": imagens_por_jornal.get("Folha de S.Paulo", "capas/5a6ca87148f8249123a81e1bf969e801.jpg"),
                "site": "https://www.folha.uol.com.br",
                "manchete": "Alta dos juros e ausência de plano fiscal elevam risco de recessão no Brasil em 2027",
                "nota": "Projeções da FGV, bancos e consultorias apontam PIB ao redor de 1% em 2027 com risco de contração; edição destaca ainda custo de R$ 14 bi da PEC da Segurança, prisão de Santiago Peña no Paraguai e escolha de Gadi Eisenkot para formar governo em Israel.",
                "resumo_edicao": [
                    "A edição dominical da Folha de S.Paulo abre com um diagnóstico severo sobre a travessia econômica pós-eleitoral: levantamentos do Ibre/FGV, instituições financeiras e consultorias independentes projetam uma desaceleração brusca do Produto Interno Bruto (PIB) para cerca de 1% em 2027, sem descartar recessão técnica caso a taxa Selic permaneça em patamar contracionista e o governo Luiz Inácio Lula da Silva postergue um plano crível de contenção de despesas obrigatórias.",
                    "Na esfera institucional e de segurança pública, o jornal revela estudo do Fórum Brasileiro de Segurança Pública segundo o qual o país precisará investir R$ 14 bilhões para abrir e custear 123,7 mil novas vagas em regime fechado exigidas pela PEC da Segurança Pública. No noticiário internacional, ganham capa a prisão preventiva do ex-presidente paraguaio Santiago Peña após o colapso do Ueno Bank e a decisão do presidente de Israel, Isaac Herzog, de confiar ao oposicionista Gadi Eisenkot a formação de um novo gabinete após a perda de maioria de Binyamin Netanyahu."
                ],
                "editorial": {
                    "titulo": "Supremo deve chancelar a extinção da jogatina online e Planalto precisa encarar âncora fiscal",
                    "texto": [
                        "No espaço editorial (Pág. A2), a Folha sustenta que o Supremo Tribunal Federal tem elementos empíricos de sobra para restringir drasticamente a exploração predatória das apostas esportivas online ('bets'), ressaltando que a jogatina sempre ao alcance do celular corroeu a renda popular, agravou o endividamento das famílias de baixa renda e converteu-se em emergência de saúde pública.",
                        "Nas colunas políticas, Dora Kramer (Pág. A3) avalia que a direita brasileira precisará executar um recuo tático pragmático e afastar-se do radicalismo bolsonarista para preservar competitividade, enquanto Lara Mesquita e Bruno Bolognesi (Pág. A10) advertem contra o 'puxadinho do sistema eleitoral misto' em gestação na Câmara dos Deputados."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Economia",
                        "pagina": "A17",
                        "autor": "Redação Economia",
                        "titulo": "Alta dos juros e ausência de plano fiscal elevam risco de recessão no Brasil em 2027",
                        "texto_integral": [
                            "Projeções atualizadas da Fundação Getulio Vargas (FGV), de grandes bancos e de consultorias macroeconômicas indicam que a economia brasileira deverá crescer apenas ao redor de 1% em 2027, com probabilidade crescente de estagnação ou recessão técnica nos primeiros trimestres do próximo ano. O esfriamento decorre da combinação entre o ciclo de aperto monetário conduzido pelo Banco Central, a volatilidade cambial e a demora do Palácio do Planalto em apresentar medidas estruturais de revisão de gastos.",
                            "Segundo os economistas ouvidos pela reportagem, a menor contribuição esperada da agropecuária e a perda de fôlego da indústria extrativa tornarão o PIB de 2027 muito mais dependente dos setores cíclicos, como comércio, serviços e indústria de transformação. Contudo, o encarecimento do crédito corporativo e ao consumidor já começa a travar decisões de investimento e consumo de bens duráveis.",
                            "A hesitação do presidente Luiz Inácio Lula da Silva em arbitrar o pacote de contenção de despesas desenhado pela equipe econômica — raiz dos prêmios elevados na curva de juros futuros — deteriorou o humor dos mercados logo após o segundo turno eleitoral, exigindo uma sinalização rápida antes da votação do Orçamento."
                        ],
                        "pontos": [
                            "Projeções do Ibre/FGV e de bancos apontam expansão do PIB próxima de 1% em 2027, com risco real de trimestre negativo.",
                            "Menor impulso do agronegócio e da indústria extrativa deixará a atividade mais exposta aos juros altos no comércio e serviços.",
                            "Indefinição sobre corte de gastos obrigatórios após o segundo turno pressiona dólar e curva futura da Selic."
                        ]
                    },
                    {
                        "caderno": "Segurança Pública",
                        "pagina": "A30",
                        "autor": "Fórum Brasileiro de Segurança Pública / Cotidiano",
                        "titulo": "País precisa de R$ 14 bilhões para adequar presídios à PEC da Segurança Pública",
                        "texto_integral": [
                            "O Brasil precisará desembolsar cerca de R$ 14 bilhões para criar e manter 123,7 mil novas vagas em regime fechado, segundo cálculos inéditos do Fórum Brasileiro de Segurança Pública obtidos pela Folha. O montante reflete o impacto direto das diretrizes previstas na Proposta de Emenda à Constituição (PEC) da Segurança Pública e do endurecimento das regras de progressão de regime para crimes ligados a facções.",
                            "Como a gestão dos sistemas penitenciários cabe constitucionalmente aos governos estaduais, a proposta amplia a pressão para que a União destine recursos bilionários extras dos fundos federais aos estados, sob pena de agravar a superlotação carcerária e fortalecer o recrutamento de detentos por organizações criminosas dentro das unidades prisionais.",
                            "Especialistas alertam que a simples ampliação de vagas sem reforma na gestão prisional e integração de inteligência financeira entre Polícia Federal e forças estaduais tende a consumir recursos orçamentários escassos sem reduzir os indicadores de letalidade e domínio territorial."
                        ],
                        "pontos": [
                            "Déficit projetado exige a abertura e manutenção de 123,7 mil vagas em regime fechado no sistema prisional.",
                            "Custo estimado de R$ 14 bilhões pressiona repasses do governo federal aos estados, gestores das penitenciárias.",
                            "Debate sobre a PEC no Congresso opõe governadores que temem perda de autonomia e ala governista que busca padronização."
                        ]
                    },
                    {
                        "caderno": "Mundo · Oriente Médio",
                        "pagina": "A27",
                        "autor": "Redação Mundo",
                        "titulo": "Presidente de Israel escolhe oposicionista Gadi Eisenkot para tentar formar novo governo",
                        "texto_integral": [
                            "O presidente de Israel, Isaac Herzog, designou oficialmente Gadi Eisenkot — ex-chefe do Estado-Maior das Forças de Defesa de Israel e principal rival de centro contra Binyamin Netanyahu — para tentar construir uma coalizão governamental no Knesset. A decisão ocorre após as eleições parlamentares de 27 de outubro terminarem em impasse, retirando a maioria da aliança direitista e ultraortodoxa de Netanyahu.",
                            "Eisenkot terá agora semanas de negociações intensas para costurar um gabinete de unidade ampla capaz de encerrar a paralisia institucional, estabilizar as frentes de segurança regional e restaurar a confiança com aliados ocidentais após anos de polarização em torno da reforma judicial e da condução da guerra.",
                            "Netanyahu, porém, articula nos bastidores para bloquear a adesão de partidos menores ao bloco de Eisenkot, apostando na fragmentação parlamentar para forçar uma nova rodada de negociações ou manter-se no comando interino."
                        ],
                        "pontos": [
                            "Isaac Herzog entrega mandato de formação de governo ao ex-chefe militar Gadi Eisenkot após eleições de 27 de outubro.",
                            "Coalizão de Binyamin Netanyahu perdeu a maioria parlamentar, abrindo caminho para semanas decisivas de negociação no Knesset."
                        ]
                    },
                    {
                        "caderno": "Mundo · América Latina",
                        "pagina": "A28",
                        "autor": "Redação Mundo",
                        "titulo": "Justiça do Paraguai decreta prisão preventiva do ex-presidente Santiago Peña após impeachment",
                        "texto_integral": [
                            "A Justiça paraguaia decretou a prisão preventiva do ex-presidente Santiago Peña, um dia após sua renúncia e a conclusão do processo de impeachment pelo Congresso em Assunção. Peña é alvo de inquérito criminal que apura desvios financeiros, tráfico de influência e irregularidades na liquidação do Ueno Bank, principal banco digital do país, do qual o ex-mandatário foi acionista até 2025.",
                            "A queda vertiginosa de Peña — que tentou renunciar na sexta-feira para escapar da inabilitação política, mas viu a Câmara dos Deputados prosseguir com o julgamento por 78 votos a 0 — mergulhou o Partido Colorado na maior crise institucional da última década e levou o governo brasileiro a monitorar de perto a estabilidade política no país vizinho e sócio de Itaipu."
                        ],
                        "pontos": [
                            "Prisão preventiva de Santiago Peña ocorre horas após renúncia e votação unânime de impeachment na Câmara paraguaia.",
                            "Investigação concentra-se nas relações societárias e comerciais de Peña com o recém-liquidado Ueno Bank."
                        ]
                    },
                    {
                        "caderno": "Ambiente · COP31",
                        "pagina": "A35",
                        "autor": "Enviados Especiais",
                        "titulo": "COP31 na Turquia começa com aposta em meta global de 35% de eletrificação até 2035",
                        "texto_integral": [
                            "A 31ª Conferência das Nações Unidas sobre Mudança Climática (COP31), que abre suas portas em Antália, na Turquia, com expectativa de reunir 60 mil participantes e a presença do presidente Lula, tem como principal aposta diplomática a fixação de uma meta global de 35% de eletrificação da economia mundial até 2035.",
                            "O objetivo é acelerar a substituição de combustíveis fósseis no transporte, no aquecimento urbano e nos processos industriais por energia elétrica gerada a partir de fontes renováveis, criando um indicador mensurável que complemente os compromissos de triplicar a capacidade solar e eólica firmados nas cúpulas anteriores."
                        ],
                        "pontos": [
                            "COP31 em Antália (Turquia) propõe elevar a participação da eletricidade na matriz final global para 35% até 2035.",
                            "Cúpula espera 60 mil delegados e testará o novo equilíbrio geopolítico climático após as eleições americanas."
                        ]
                    },
                    {
                        "caderno": "C-Level & Negócios",
                        "pagina": "A20 / A23",
                        "autor": "Caderno Economia",
                        "titulo": "Indústria de motos bate recorde histórico de 2,35 milhões de unidades impulsionada por delivery",
                        "texto_integral": [
                            "O setor de motocicletas no Brasil caminha para registrar em 2026 o melhor ano de toda a sua história, com vendas projetadas em 2,35 milhões de unidades. O salto é impulsionado pela expansão contínua dos aplicativos de entrega e mobilidade, pelo avanço dos consórcios e pelo encarecimento do chamado 'carro popular' diante do crédito restrito.",
                            "No varejo esportivo (Pág. A23), o CEO da Decathlon no Brasil, Cedric Burel, detalha a estratégia de modernização e abertura cadenciada de lojas compactas no país: 'Não queremos arrancar demais', afirma o executivo diante do cenário de juros elevados."
                        ],
                        "pontos": [
                            "Produção e venda de motocicletas devem atingir marca histórica de 2,35 milhões de unidades em 2026.",
                            "Fim do carro de entrada barato, consórcios e economia de aplicativos sustentam a demanda."
                        ]
                    }
                ]
            },
            {
                "jornal": "O Estado de S. Paulo",
                "pais": "Brasil",
                "escopo": "nacional",
                "total_paginas": 56,
                "imagem": imagens_por_jornal.get("O Estado de S. Paulo", "capas/41d2e3357148204714a56b9d8c9e47f0.jpg"),
                "site": "https://www.estadao.com.br",
                "manchete": "Corrida pelo petróleo na Margem Equatorial atrai investimentos bilionários e expõe gargalos no extremo norte",
                "nota": "Estadão destaca a disputa energética e ambiental na Foz do Amazonas, o apoio de 70% da Câmara à reeleição de Hugo Motta, negócios de parceiro de Paulo Gonet com verba pública e os desafios diplomáticos de Lula diante de Milei no Mercosul.",
                "resumo_edicao": [
                    "A edição dominical de O Estado de S. Paulo traz como grande reportagem de capa a corrida bilionária pelo petróleo na Margem Equatorial, no extremo norte do país, mostrando como a nova fronteira exploratória da Petrobras e de petroleiras globais atrai investimentos de grande porte, mas esbarra em severos gargalos de infraestrutura local e disputas de licenciamento ambiental.",
                    "No caderno de Política, o jornal revela que os partidos que já declararam apoio à reeleição de Hugo Motta (Republicanos-PB) para a presidência da Câmara somam 70% dos deputados eleitos para a próxima legislatura, consolidando a hegemonia do Centrão. A edição traz ainda investigação sobre sociedade empresarial envolvendo o procurador-geral da República, Paulo Gonet, e um balanço das 7 mil denúncias de assédio eleitoral registradas pelo Ministério do Trabalho."
                ],
                "editorial": {
                    "titulo": "A eleição encerra a disputa nas urnas, mas não encerrará a crise institucional e fiscal",
                    "texto": [
                        "Em análise de fundo (Págs. A5 e A6), o Estadão observa que a impaciência dos eleitores com quem governa tem atravessado fronteiras e rótulos ideológicos — derrubando conservadores no Reino Unido, democratas em 2024 e agora republicanos nas midterms de 2026 nos EUA. No Brasil, adverte o jornal, 'as urnas distribuem poder e conferem legitimidade aos eleitos, mas não corrigem instituições que perderam capacidade de funcionar em harmonia nem resolvem o desequilíbrio estrutural das contas públicas'."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Economia & Negócios",
                        "pagina": "Capa / E&N",
                        "autor": "Enviados Especiais",
                        "titulo": "Corrida em torno do petróleo no extremo norte do País atrai investimento e expõe desafios",
                        "texto_integral": [
                            "Vista pelo setor de óleo e gás como a sucessora natural do pré-sal para evitar o declínio das reservas brasileiras na década de 2030, a Margem Equatorial — faixa costeira que se estende do Amapá ao Rio Grande do Norte — vive uma corrida silenciosa por infraestrutura portuária, logística aérea e licenciamento ambiental.",
                            "A reportagem mostra que municípios da costa amapaense e paraense enfrentam precariedade de saneamento, energia e mão de obra qualificada justamente no momento em que a Petrobras pressiona pela liberação de perfurações na Bacia da Foz do Amazonas.",
                            "O impasse coloca em rota de colisão a ala desenvolvimentista do governo e o Ministério de Minas e Energia contra o Ibama e organizações socioambientais, às vésperas da participação brasileira na COP31 na Turquia."
                        ],
                        "pontos": [
                            "Margem Equatorial concentra a maior aposta exploratória da Petrobras para repor reservas após o pico do pré-sal.",
                            "Municípios do extremo norte sofrem com déficit severo de infraestrutura básica para absorver o choque de investimentos."
                        ]
                    },
                    {
                        "caderno": "Política · Congresso",
                        "pagina": "A13",
                        "autor": "Redação Brasília",
                        "titulo": "Partidos que já declararam apoio à reeleição de Hugo Motta somam 70% dos deputados eleitos",
                        "texto_integral": [
                            "A articulação pela recondução de Hugo Motta (Republicanos-PB) ao comando da Câmara dos Deputados a partir de fevereiro de 2027 atingiu massa crítica: as legendas que já oficializaram ou encaminharam adesão ao bloco do parlamentar paraibano representam 70% das cadeiras eleitas para a próxima legislatura.",
                            "O amplo arco de alianças — que vai do PT e siglas da base governista ao PP, União Brasil, PSD e ala pragmática do PL — esvazia tentativas de candidatura avulsa da oposição bolsonarista e reforça o poder de barganha do Centrão sobre o ritmo da reforma tributária, das emendas parlamentares e do ajuste fiscal no quarto mandato de Lula."
                        ],
                        "pontos": [
                            "Bloco de apoio a Hugo Motta já reúne cerca de 70% dos deputados federais eleitos para a nova legislatura.",
                            "Consenso suprapartidário garante estabilidade na Mesa Diretora, mas eleva o custo político das votações econômicas do Executivo."
                        ]
                    },
                    {
                        "caderno": "Política · Justiça",
                        "pagina": "A9",
                        "autor": "Investigação Política",
                        "titulo": "PGR Paulo Gonet é sócio de empresário do setor de educação que recebe recursos públicos para congressos",
                        "texto_integral": [
                            "O procurador-geral da República, Paulo Gonet, mantém sociedade empresarial com um empresário do ramo educacional cuja instituição recebe recursos públicos de órgãos estatais e tribunais para a organização de congressos jurídicos, seminários e palestras com a presença de autoridades do Judiciário e do Ministério Público.",
                            "A revelação reacende o debate no Congresso e em entidades de transparência sobre os limites éticos para a participação societária de integrantes da cúpula do sistema de Justiça em empresas que contratam com o poder público ou promovem eventos patrocinados por entes fiscalizados."
                        ],
                        "pontos": [
                            "Sociedade envolve empresa que capta verbas públicas de órgãos estatais para realização de eventos e seminários jurídicos.",
                            "Caso amplia pressões no Parlamento por regras mais rígidas sobre conflitos de interesse na magistratura e no MP."
                        ]
                    },
                    {
                        "caderno": "Política · Trabalho",
                        "pagina": "A11",
                        "autor": "Redação Política",
                        "titulo": "Ministério do Trabalho registra mais de 7 mil denúncias de assédio eleitoral na campanha de 2026",
                        "texto_integral": [
                            "O Ministério do Trabalho e Emprego (MTE) contabilizou mais de 7 mil denúncias formais de assédio eleitoral em ambientes corporativos e rurais ao longo da campanha presidencial de 2026, segundo balanço divulgado pelo ministro Luiz Marinho.",
                            "Os processos encaminhados ao Ministério Público do Trabalho envolvem coação de empregados, ameaças de demissão condicionadas ao resultado das urnas e promessas de bonificação vinculadas ao voto, exigindo forças-tarefa de fiscalização nos estados com maior concentração de queixas."
                        ],
                        "pontos": [
                            "Mais de 7 mil queixas de coação política no ambiente de trabalho foram apuradas pelo MTE e MPT no ciclo eleitoral de 2026."
                        ]
                    },
                    {
                        "caderno": "Internacional",
                        "pagina": "A10 / A14",
                        "autor": "Correspondentes",
                        "titulo": "Derrota republicana nas midterms dos EUA e agenda de Milei no Mercosul desafiam diplomacia brasileira",
                        "texto_integral": [
                            "No caderno Internacional, o Estadão analisa em duas frentes o tabuleiro externo para o Brasil: nos Estados Unidos (Pág. A14), as eleições de meio de mandato serviram como teste de fogo para o Partido Republicano, onde a baixa popularidade de Donald Trump penalizou candidatos aliados em todos os grupos demográficos.",
                            "Já na América do Sul (Pág. A10), os desdobramentos políticos e econômicos do governo de Javier Milei na Argentina funcionam como alerta para a região às vésperas da Cúpula do Mercosul, marcada para os dias 4 e 5 de dezembro, na qual Lula buscará destravar impasses comerciais do bloco."
                        ],
                        "pontos": [
                            "Cúpula do Mercosul em 4 e 5 de dezembro testará convivência entre Lula e Javier Milei.",
                            "Desgaste de Donald Trump nas midterms abre espaço para revisão de tarifas e diálogo mais institucional com Brasília."
                        ]
                    }
                ]
            },
            {
                "jornal": "O Globo",
                "pais": "Brasil",
                "escopo": "nacional",
                "total_paginas": 45,
                "imagem": imagens_por_jornal.get("O Globo", "capas/703be265f213493543a153a54424d58f.jpg"),
                "site": "https://oglobo.globo.com",
                "manchete": "Fuga e postura golpista de Flávio Bolsonaro dividem a direita e são rejeitadas por seis em cada dez brasileiros",
                "nota": "Pesquisa Quaest exclusiva mostra que 60% desaprovam a ida do candidato derrotado aos EUA; edição destaca resistência de Lula a corte drástico de gastos, futuro de Alckmin na Esplanada e isolamento de Nunes Marques e Mendonça no STF.",
                "resumo_edicao": [
                    "O Globo abre sua edição de domingo com os dados da pesquisa Genial/Quaest pós-eleitoral ('O Brasil depois das urnas'): seis em cada dez brasileiros rejeitam a decisão do senador Flávio Bolsonaro (PL-RJ) de viajar para os Estados Unidos logo após a derrota no segundo turno e de colocar em dúvida a lisura do processo eleitoral. Nos bastidores da própria direita (Pág. 6), governadores e líderes do Centrão já tratam a manobra como erro estratégico e priorizam a disputa pela presidência do Senado.",
                    "Na área econômica e governamental (Págs. 8 e 15), o jornal relata que o presidente Lula e seus principais auxiliares no Planalto têm resistido à pressão da Faria Lima por um choque fiscal imediato, argumentando que o governo já realizou contenções relevantes. Enquanto isso, Lula discute um novo papel de peso para o vice-presidente Geraldo Alckmin, cotado para assumir Defesa, Segurança Pública ou permanecer no Desenvolvimento e Indústria."
                ],
                "editorial": {
                    "titulo": "Responsabilidade fiscal e pacificação institucional são inadiáveis após o veredito das urnas",
                    "texto": [
                        "Na página de Opinião e nas colunas de Merval Pereira e Bernardo Mello Franco (Págs. 2 e 3), O Globo aponta que o encerramento do ciclo eleitoral de 2026 impõe duas tarefas imediatas: ao campo conservador, abandonar aventuras antidemocráticas e construir uma oposição parlamentar responsável; ao presidente reeleito, compreender que a estabilidade da moeda e dos juros depende de um compromisso transparente com a solvência do arcabouço fiscal."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Política · Pós-Eleição",
                        "pagina": "1, 4 e 6",
                        "autor": "Redação Política",
                        "titulo": "Fuga e postura golpista de Flávio Bolsonaro dividem direita e são rejeitadas por 6 em cada 10 brasileiros",
                        "texto_integral": [
                            "Levantamento nacional da Quaest publicado neste domingo revela que a decisão do senador Flávio Bolsonaro (PL-RJ) de embarcar para os Estados Unidos após ser derrotado por Luiz Inácio Lula da Silva no segundo turno — somada ao discurso de contestação ao sistema eleitoral — é desaprovada por cerca de 60% do eleitorado brasileiro, incluindo parcela expressiva de eleitores moderados que votaram contra o PT.",
                            "Na reportagem de bastidores (Pág. 6), O Globo reconstitui a reunião de emergência realizada pelo comando de campanha do PL ainda durante a apuração dos votos: enquanto aliados mais radicais defendiam dobrar a aposta na retórica de confronto, o senador Rogério Marinho (PL-RN) mudou o foco da conversa para a urgência de negociar espaços na eleição para a presidência do Senado em 2027.",
                            "Governadores de direita e dirigentes do PP, Republicanos e União Brasil avaliam reservadamente que a autoexílio temporário de Flávio nos EUA enfraquece a liderança do clã Bolsonaro, Ainda mais após a derrota republicana nas eleições legislativas americanas esvaziar o apoio que o grupo esperava receber em Washington."
                        ],
                        "pontos": [
                            "Pesquisa Quaest mostra que 6 em cada 10 brasileiros consideram errada a ida de Flávio Bolsonaro para os EUA pós-derrota.",
                            "Na noite da apuração, Rogério Marinho já redirecionava o foco do PL para a disputa pela presidência do Senado.",
                            "Derrota de Trump no Congresso americano reduz margem de manobra internacional da ala bolsonarista."
                        ]
                    },
                    {
                        "caderno": "Economia & Planalto",
                        "pagina": "8 e 15",
                        "autor": "Redação Brasília",
                        "titulo": "Lula resiste a aperto fiscal mais duro e avalia novo ministério estratégico para Geraldo Alckmin",
                        "texto_integral": [
                            "Diante da cobrança do mercado financeiro e da equipe econômica por um pacote robusto de revisão de gastos obrigatórios, o presidente Luiz Inácio Lula da Silva e seus assessores mais próximos no Palácio do Planalto têm sustentado que o governo já promoveu um ajuste relevante e que eventuais correções no arcabouço fiscal não podem sacrificar investimentos estratégicos nem programas sociais.",
                            "Paralelamente ao debate econômico (Pág. 8), Lula iniciou as conversas para a reforma ministerial do novo mandato e pretende ampliar o protagonismo do vice-presidente Geraldo Alckmin (PSB). Três pastas estão na mesa para Alckmin: a permanência no Ministério do Desenvolvimento, Indústria e Comércio (MDIC), a transferência para o Ministério da Defesa ou a chefia de um eventual Ministério da Segurança Pública.",
                            "A escolha do posto de Alckmin servirá como peça-chave para abrir espaço aos partidos de centro na Esplanada e sinalizar moderação institucional ao empresariado e às Forças Armadas."
                        ],
                        "pontos": [
                            "Ala política do Planalto resiste a corte profundo em despesas indexadas e defende ajuste gradual.",
                            "Geraldo Alckmin é cotado para assumir Defesa, eventual pasta da Segurança Pública ou seguir na Indústria e Comércio."
                        ]
                    },
                    {
                        "caderno": "Supremo Tribunal Federal",
                        "pagina": "11",
                        "autor": "Bastidores da Corte",
                        "titulo": "Reeleição de Lula acirra isolamento de Nunes Marques e André Mendonça no STF",
                        "texto_integral": [
                            "O resultado das urnas deve aprofundar o isolamento dos ministros Kassio Nunes Marques e André Mendonça no plenário do Supremo Tribunal Federal. Indicados por Jair Bolsonaro e vistos nos bastidores da Corte como alinhados a pautas conservadoras que saíram derrotadas na eleição presidencial, ambos terão de calibrar sua atuação diante de uma maioria consolidada.",
                            "Com a vitória de Lula, o presidente da República ainda poderá fazer novas indicações ao tribunal nos próximos quatro anos em caso de aposentadorias, frustrando o plano da oposição de alterar o equilíbrio de forças na Suprema Corte a partir de 2027."
                        ],
                        "pontos": [
                            "Ministros indicados por Bolsonaro ficam em posição minoritária ainda mais nítida após a confirmação do quarto mandato de Lula."
                        ]
                    },
                    {
                        "caderno": "Segurança Pública",
                        "pagina": "10",
                        "autor": "Entrevista / Segurança",
                        "titulo": "Ex-diretor da PF analisa alcances e limites da PEC da Segurança no combate às facções",
                        "texto_integral": [
                            "Em análise detalhada na página 10, o delegado da Polícia Federal no Rio e ex-diretor da área de repressão ao crime organizado avalia que a Proposta de Emenda à Constituição (PEC) da Segurança Pública avança ao constitucionalizar o Sistema Único de Segurança Pública (Susp), mas não será suficiente sem asfixia patrimonial das facções.",
                            "Segundo ele, a integração de bancos de dados criminais e o fortalecimento da Polícia Federal no combate a milícias e lavagem de dinheiro interestadual precisam caminhar juntos com o controle efetivo dos presídios estaduais."
                        ],
                        "pontos": [
                            "Especialistas defendem foco na asfixia financeira e patrimonial das facções criminosas além da mudança constitucional."
                        ]
                    },
                    {
                        "caderno": "Cultura & Livros",
                        "pagina": "12 e 13",
                        "autor": "Segundo Caderno",
                        "titulo": "Memórias do carcereiro de Lula em Curitiba chegam às livrarias; 'raves literárias' ganham adeptos",
                        "texto_integral": [
                            "Na seção cultural (Pág. 12), chega às livrarias a obra 'Banho de sol: Os 580 dias de Lula na prisão', escrita por Jorge Chastalo Filho, o agente da Polícia Federal encarregado da custódia do então ex-presidente na Superintendência da PF em Curitiba entre 2018 e 2019, narrando os bastidores humanos e políticos daquele período.",
                            "Na página 13, reportagem de comportamento mostra como as chamadas 'raves' e retiros literários — encontros silenciosos onde dezenas de leitores desligam celulares para ler juntos e debater livros — multiplicaram-se no Rio e em São Paulo como antídoto à exaustão digital."
                        ],
                        "pontos": [
                            "Agente da PF Jorge Chastalo Filho lança livro documental sobre os 580 dias de custódia de Lula em Curitiba.",
                            "Retiros e clubes de leitura presenciais desconectados crescem nas capitais brasileiras."
                        ]
                    }
                ]
            },
            {
                "jornal": "Valor Econômico",
                "pais": "Brasil",
                "escopo": "nacional",
                "total_paginas": 58,
                "imagem": imagens_por_jornal.get("Valor Econômico", "capas/0bd27b377050a2bc2b4628d5285499a0.jpg"),
                "site": "https://valor.globo.com",
                "manchete": "Produção industrial recua 0,8% e acumula perda de 4,1% desde maio; crise bancária derruba presidente do Paraguai",
                "nota": "Edição analisa desaceleração da indústria sob juros altos, recado de Dario Durigan sobre pacote fiscal, disputa em torno de R$ 41,9 bi do Imposto Seletivo e expectativa do Planalto por diálogo pragmático com os EUA após derrota de Trump.",
                "resumo_edicao": [
                    "O Valor Econômico destaca em sua edição de fim de semana a perda de tração do setor produtivo brasileiro: a produção industrial recuou 0,8% em setembro — queda mais intensa que a projetada pelo mercado — e já acumula retração de 4,1% desde maio, confirmando que o aperto monetário e o endividamento das famílias começaram a frear a atividade fabril.",
                    "Na política econômica (Págs. 6, 8 e 10), o secretário-executivo da Fazenda, Dario Durigan, busca conter especulações após reunião com economistas próximos ao PT afirmando que 'ainda não é o momento de tratar de medidas específicas', enquanto tributaristas alertam para o viés arrecadatório do Imposto Seletivo (estimado em R$ 41,9 bilhões para 2027). No plano externo, o jornal detalha a queda de Santiago Peña no Paraguai após a liquidação do Ueno Bank e a avaliação do Itamaraty de que a derrota de Trump nas midterms facilitará uma relação comercial mais pragmática com Washington."
                ],
                "editorial": {
                    "titulo": "Desaceleração industrial e transição fiscal exigem clareza imediata da equipe econômica",
                    "texto": [
                        "Nas análises de conjuntura, o Valor aponta que a sequência de quedas na produção industrial desde maio encerra a fase de surpresas positivas da atividade econômica e torna ainda mais urgente a definição do comando da Fazenda para 2027 e do desenho do pacote de contenção de gastos obrigatórios."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Conjuntura · Indústria",
                        "pagina": "A2",
                        "autor": "Redação Valor",
                        "titulo": "Indústria recua 0,8% além do esperado e já acumula perda de 4,1% desde maio, apontam economistas",
                        "texto_integral": [
                            "A produção industrial brasileira encolheu 0,8% na passagem mensal de setembro, resultado pior que a mediana das projeções do mercado financeiro, e já acumula uma perda de 4,1% desde o pico registrado em maio. Os dados divulgados pelo IBGE reforçam o diagnóstico de economistas de que a economia entrou em rota de desaceleração no segundo semestre de 2026.",
                            "A retração foi disseminada entre bens de capital e bens de consumo duráveis, segmentos diretamente sensíveis ao custo do crédito e à elevação da taxa Selic. Para analistas ouvidos pelo Valor, o carrego estatístico para 2027 será reduzido, exigindo reequilíbrio entre política fiscal e monetária para destravar investimentos."
                        ],
                        "pontos": [
                            "Queda de 0,8% no mês leva indústria a acumular perda de 4,1% desde maio.",
                            "Recuo de bens de capital e duráveis reflete impacto direto dos juros elevados sobre crédito e investimento."
                        ]
                    },
                    {
                        "caderno": "Política Fiscal · Fazenda",
                        "pagina": "A6 e A10",
                        "autor": "Giordanna Neves e Lu Aiko Otta",
                        "titulo": "Dario Durigan diz que 'não é momento de tratar de medida específica' após encontro com economistas; Rafael Fonteles segue no radar",
                        "texto_integral": [
                            "Após encontro reservado com ex-ministros e economistas ligados ao PT, o número dois do Ministério da Fazenda, Dario Durigan, afirmou que a reunião tratou do cenário macroeconômico geral e que 'não teve discussão sobre medidas específicas e não é ainda o momento de tratar de nenhuma medida específica' de corte de gastos.",
                            "Nos bastidores da transição para o novo mandato (Pág. A10), o governador reeleito do Piauí, Rafael Fonteles (PT), continua cotado como um dos nomes fortes para o Ministério da Fazenda caso Fernando Haddad seja deslocado para outra função estratégica, embora tenha optado por submergir publicamente para evitar ruídos com a atual equipe econômica."
                        ],
                        "pontos": [
                            "Dario Durigan evita antecipar detalhes do pacote de revisão de gastos antes do aval final de Lula.",
                            "Governador Rafael Fonteles (PT-PI) mantém interlocução econômica discreta enquanto segue cotado para a Esplanada."
                        ]
                    },
                    {
                        "caderno": "Tributação · Reforma",
                        "pagina": "A8",
                        "autor": "Redação Brasília",
                        "titulo": "Governo prevê R$ 41,9 bilhões com Imposto Seletivo em 2027, mas economistas criticam viés arrecadatório",
                        "texto_integral": [
                            "As projeções técnicas que embasam o orçamento de 2027 estimam uma arrecadação de R$ 41,9 bilhões com a entrada em vigor do Imposto Seletivo — o chamado 'imposto do pecado' criado pela Reforma Tributária sobre produtos prejudiciais à saúde e ao meio ambiente.",
                            "Tributaristas e economistas ouvidos pelo Valor advertem, contudo, que o tributo regulatório não deveria ter função primariamente arrecadatória para fechar metas fiscais, apontando que a calibragem das alíquotas sobre bebidas, cigarros, veículos e extração mineral corre o risco de gerar contencioso e distorções setoriais."
                        ],
                        "pontos": [
                            "Previsão de receita com o Imposto Seletivo chega a R$ 41,9 bilhões para o exercício de 2027.",
                            "Especialistas apontam tensão entre o caráter extrafiscal (inibir consumo nocivo) e a busca do Tesouro por receitas."
                        ]
                    },
                    {
                        "caderno": "Relações Externas",
                        "pagina": "A9",
                        "autor": "Redação Diplomacia",
                        "titulo": "Planalto vê chance de normalizar diálogo com os EUA após derrota eleitoral de Trump nas midterms",
                        "texto_integral": [
                            "O governo do presidente Luiz Inácio Lula da Silva avalia que a pesada derrota sofrida pelo Partido Republicano e por Donald Trump nas eleições de meio de mandato nos Estados Unidos tende a tornar a relação bilateral entre Washington e Brasília mais pragmática e previsível nos próximos dois anos.",
                            "Com os democratas no controle da Câmara dos Representantes e do Senado a partir de janeiro de 2027, diplomatas brasileiros acreditam que ímpetos protecionistas unilaterais ou sanções politicamente motivadas enfrentarão freios institucionais no Capitólio, facilitando negociações comerciais e climáticas."
                        ],
                        "pontos": [
                            "Vitória democrata no Congresso dos EUA é vista pelo Itamaraty como contrapeso a medidas comerciais unilaterais.",
                            "Na página A12, Flávio Bolsonaro diz que levará 'para o túmulo' detalhes de como viajou aos EUA após o segundo turno."
                        ]
                    },
                    {
                        "caderno": "América Latina & Poderes",
                        "pagina": "A1, A14 e A15",
                        "autor": "Luiza Palermo, Álvaro Campos e Eulina Oliveira",
                        "titulo": "Crise no Ueno Bank derruba presidente do Paraguai; no Rio, Eduardo Paes recorre ao STF por 2º turno",
                        "texto_integral": [
                            "Em destaque de capa e na página A15, o Valor detalha como a liquidação do Ueno Bank — instituição financeira da qual Santiago Peña foi acionista até 2025 — levou o presidente paraguaio a renunciar sob iminência de impeachment aprovado por 78 votos a 0 na Câmara em Assunção.",
                            "No caderno Poderes (Pág. A14), o prefeito e candidato derrotado ao governo do Rio de Janeiro, Eduardo Paes (PSD), intensifica mobilização jurídica no Supremo Tribunal Federal para tentar reverter a decisão do Tribunal Superior Eleitoral (TSE) que validou os votos e proclamou a vitória de Douglas Ruas (PL) ainda no primeiro turno fluminense."
                        ],
                        "pontos": [
                            "Colapso do Ueno Bank provoca renúncia e impeachment de Santiago Peña no Paraguai.",
                            "Eduardo Paes tenta no STF reverter decisão do TSE que confirmou vitória de Douglas Ruas no RJ."
                        ]
                    }
                ]
            },
            {
                "jornal": "Financial Times",
                "pais": "Reino Unido / EUA",
                "escopo": "internacional",
                "total_paginas": 56,
                "imagem": imagens_por_jornal.get("Financial Times", "capas/a076253430e0415c994a914473230f25.jpg"),
                "site": "https://www.ft.com",
                "manchete": "Anthropic mantém IPO bilionário antes do Thanksgiving apesar de derrocada tecnológica e corte de avaliação",
                "manchete_original": "Anthropic presses on with listing as AI giant defies tech rout; US warns China to honour trade truce 'immediately'",
                "nota": "Edição de fim de semana do FT destaca o choque de US$ 3,2 trilhões em Wall Street após vitórias democratas contra data centers de IA, o ultimato de Scott Bessent a Pequim sobre terras raras e o alarme europeu com plano de segurança de Trump e Kushner para a Rússia.",
                "resumo_edicao": [
                    "A edição de fim de semana do Financial Times (FT Weekend, 7–8 de novembro de 2026) traz na primeira página os dois grandes abalos econômicos e geopolíticos da semana: em São Francisco e Wall Street, a gigante de inteligência artificial Anthropic decidiu manter sua oferta pública inicial de ações (IPO) ainda para novembro, antes do feriado de Ação de Graças, mesmo após um tombo de US$ 3,2 trilhões nas bolsas americanas forçar o corte de sua avaliação pretendida de US$ 2 trilhões para a faixa de US$ 1,3 trilhão a US$ 1,5 trilhão.",
                    "Em Washington e Bruxelas, o jornal revela que o secretário do Tesouro dos EUA, Scott Bessent, advertiu o vice-premiê chinês He Lifeng a cumprir 'imediatamente' o acordo de exportação de terras raras firmado na trégua de Busan antes da cúpula da Apec em Shenzhen, enquanto líderes da União Europeia manifestam alarme com a tentativa de Donald Trump e Jared Kushner de negociar uma nova arquitetura de segurança europeia diretamente com Moscou."
                ],
                "editorial": {
                    "titulo": "A grande correção de rumo americana e o choque de realidade sobre a euforia da IA",
                    "texto": [
                        "No caderno de análise (FT View e Big Read, Págs. 8–10, com ensaio do historiador Simon Schama sobre 'a mãe de todas as correções de curso'), o Financial Times analisa como a vitória democrata nas midterms — com a maior virada no voto popular da Câmara desde 1948 (+12 pontos) — representa um repúdio simultâneo ao custo de vida inflacionado pelas tarifas e pela guerra com o Irã e à aliança irrestrita entre a Casa Branca e os bilionários do Vale do Silício."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Mercados & Inteligência Artificial",
                        "pagina": "1",
                        "autor": "São Francisco / Nova York",
                        "titulo": "Anthropic avança com IPO de até US$ 100 bilhões antes do Thanksgiving mesmo sob derrocada das ações de tecnologia",
                        "titulo_original": "Anthropic presses on with listing: AI giant defies tech rout, valuation hopes scaled back",
                        "texto_integral": [
                            "A criadora do modelo Claude, Anthropic, decidiu prosseguir com sua aguardada abertura de capital (IPO) ainda neste mês de novembro, antes do feriado de Ação de Graças nos Estados Unidos, desafiando a violenta liquidação que varreu o setor de tecnologia em Wall Street. Segundo múltiplos investidores ouvidos pelo Financial Times, a empresa espera captar entre US$ 80 bilhões e US$ 100 bilhões, mas aceitou reduzir sua avaliação de mercado para a faixa de US$ 1,3 trilhão a US$ 1,5 trilhão — bem abaixo dos US$ 2 trilhões projetados há apenas um mês.",
                            "O recuo nas expectativas reflete um acerto de contas mais amplo no setor de inteligência artificial: na quinta-feira, as ações americanas perderam US$ 3,2 trilhões em valor de mercado em um único pregão, com o índice Nasdaq 100 despencando 6,4%, enquanto a rival OpenAI também teve de cortar sua rodada privada de avaliação de US$ 1,4 trilhão para US$ 1,25 trilhão.",
                            "Segundo investidores próximos ao CEO Dario Amodei, a companhia não pretende adiar a listagem nem disputar tamanho com o IPO da SpaceX de Elon Musk realizado em junho: a aposta é que fundos de índice e grandes gestores institucionais ('compradores forçados') sustentarão a demanda assim que os papéis estrearem na bolsa."
                        ],
                        "pontos": [
                            "Anthropic planeja captar entre US$ 80 bi e US$ 100 bi antes do Thanksgiving, ajustando valuation para US$ 1,3–1,5 trilhão.",
                            "Bolsas dos EUA perderam US$ 3,2 trilhões na quinta-feira após vitória democrata ameaçar expansão de data centers.",
                            "OpenAI também reduziu valuation pretendido em rodada privada de US$ 1,4 trilhão para US$ 1,25 trilhão."
                        ],
                        "citacao": "É apenas um marco no caminho. Minha visão é que eles vão precificar de forma conservadora, em torno de US$ 1,5 trilhão, e subir a partir daí."
                    },
                    {
                        "caderno": "Comércio Global · EUA-China",
                        "pagina": "1",
                        "autor": "Demetri Sevastopulo (Washington)",
                        "titulo": "EUA advertem China a cumprir 'imediatamente' trégua comercial sobre terras raras antes de cúpula em Shenzhen",
                        "titulo_original": "US warns China to honour trade truce 'immediately' as summit talks loom",
                        "texto_integral": [
                            "O governo dos Estados Unidos advertiu formalmente Pequim de que a China deve cumprir de imediato os termos da trégua comercial firmada entre Donald Trump e Xi Jinping em Busan no ano passado, em meio à crescente frustração em Washington com a restrição chinesa às exportações de terras raras e produtos agrícolas.",
                            "A mensagem foi transmitida em telefonema pelo secretário do Tesouro, Scott Bessent, e pelo representante de Comércio dos EUA, Jamieson Greer, ao vice-premiê chinês He Lifeng. Segundo autoridades americanas, Pequim está cumprindo apenas dois terços da cota prometida de minerais críticos essenciais para a indústria de defesa e semicondutores.",
                            "O aviso ocorre a duas semanas da cúpula da Cooperação Econômica Ásia-Pacífico (Apec) na cidade chinesa de Shenzhen — onde Xi Jinping pode sediar um encontro trilateral com Trump e Vladimir Putin — e antes da reunião do G20 em Miami, em dezembro, já que a trégua de Busan expira em 10 de janeiro de 2027."
                        ],
                        "pontos": [
                            "Secretário do Tesouro Scott Bessent cobrou do vice-premiê He Lifeng a entrega integral de terras raras.",
                            "Trégua tarifária de Busan expira em 10 de janeiro; líderes se encontrarão na Apec (Shenzhen) e no G20 (Miami)."
                        ]
                    },
                    {
                        "caderno": "Midterms & Tecnologia",
                        "pagina": "2",
                        "autor": "Stephanie Findlay (Houston)",
                        "titulo": "Eleitores se voltam contra bilionários de IA aliados de Trump; novos governadores democratas ameaçam 41% dos data centers planejados",
                        "titulo_original": "Voters turn on Trump's tech titan cheerleaders / Landslide result sends convulsions through AI sector",
                        "texto_integral": [
                            "A aliança explícita dos magnatas do Vale do Silício com Donald Trump — que doaram mais de US$ 600 milhões a comitês republicanos na tentativa de bloquear regulações estaduais sobre inteligência artificial — saiu pela culatra nas urnas. Candidatos democratas venceram governos estaduais estratégicos como Texas, Ohio, Geórgia, Michigan, Pensilvânia, Arizona e Nevada prometendo moratórias na construção de megacentros de dados que encarecem a conta de luz e consomem água das comunidades locais.",
                            "No Texas, onde Elon Musk gastou mais de US$ 200 milhões apoiando republicanos, os democratas venceram tanto o Senado (com James Talarico batendo Ken Paxton por 12 pontos) quanto o governo estadual, onde a governadora eleita Gina Hinojosa anunciou que suspenderá aprovações de novos data centers — colocando em risco o terceiro supercomputador 'Colossus' da xAI de Musk e a megafábrica de chips da Tesla.",
                            "Segundo a consultoria Cleanview e o Goldman Sachs, entre 41% e 45% de toda a capacidade planejada de data centers dos EUA está localizada em estados onde os novos governadores democratas defendem pausas regulatórias, levando analistas como Dan Ives a preverem o corte de 20% na capacidade planejada de IA para 2027."
                        ],
                        "pontos": [
                            "Entre 41% e 45% da capacidade planejada de data centers nos EUA fica em estados conquistados por governadores democratas.",
                            "No Texas, vitória da democrata Gina Hinojosa e de James Talarico impõe freio direto aos projetos de Elon Musk.",
                            "Ações de fabricantes de chips (Nvidia, AMD) e 'neoclouds' sofreram forte correção diante do risco de moratórias."
                        ]
                    },
                    {
                        "caderno": "Guerra na Ucrânia & Europa",
                        "pagina": "2",
                        "autor": "Henry Foy (Bruxelas)",
                        "titulo": "Capitais europeias em alarme com planos dos EUA de negociar acordo de segurança europeia diretamente com Moscou",
                        "titulo_original": "Europe alarmed by US plans for security deal with Moscow",
                        "texto_integral": [
                            "As capitais da União Europeia reagiram com alarme após Donald Trump e seu genro e negociador, Jared Kushner, indicarem que Washington pretende discutir uma 'arquitetura duradoura para a segurança e estabilidade europeia' diretamente com a Rússia como parte de um acordo de paz na Ucrânia.",
                            "O alerta disparou após Trump receber na Casa Branca Kirill Dmitriev, enviado de Vladimir Putin, antes da nova rodada de negociações entre delegações dos EUA, Rússia e Ucrânia marcada para a próxima semana em Abu Dhabi. 'Haverá um acordo e ele envolverá mais do que a Ucrânia; pode envolver toda a Europa', declarou Trump.",
                            "Em resposta imediata, a Comissão Europeia e diplomatas da Otan afirmaram que 'cabe exclusivamente à União Europeia decidir sobre assuntos que afetam sua segurança' e rechaçaram qualquer recuo na presença militar da aliança atlântica no leste europeu."
                        ],
                        "pontos": [
                            "Encontro de Trump e Jared Kushner com enviado russo Kirill Dmitriev antecede negociações em Abu Dhabi.",
                            "União Europeia convoca cúpula para impedir que Washington negocie a arquitetura de segurança do continente sem Bruxelas."
                        ]
                    },
                    {
                        "caderno": "Política dos EUA · Congresso & Cidades",
                        "pagina": "3 e 4",
                        "autor": "James Politi, Joe Miller e Eric Platt",
                        "titulo": "Onda azul dá Câmara e Senado aos democratas com maior virada desde 1948; progressista Nithya Raman vence em Los Angeles",
                        "titulo_original": "Democrats vow 'dramatic change' to reshape America / Blue wave shifts voters to the left",
                        "texto_integral": [
                            "Os democratas conquistaram o controle da Câmara dos Representantes em apenas duas horas após o fechamento das urnas e garantiram maioria no Senado na maior virada do voto popular nacional (+12 pontos sobre os republicanos) desde 1948. O novo presidente da Câmara, Hakeem Jeffries, e o líder no Senado, Chuck Schumer, terão agora de equilibrar a ala centrista e a bancada progressista em torno da agenda de redução do custo de vida.",
                            "A análise de dados eleitorais do FT (Pág. 4) mostra que os eleitores de menor renda (abaixo de US$ 30 mil anuais) e os condados de maioria hispânica na fronteira do Texas — que haviam migrado para Trump em 2024 — voltaram em massa para o Partido Democrata em reação à inflação gerada pelas tarifas, à alta dos combustíveis provocada pela guerra no Irã e às batidas do ICE.",
                            "No Mississippi (Pág. 3), o promotor democrata negro Scott Colom lidera por cerca de 2 mil votos contra a senadora republicana Cindy Hyde-Smith com 96% das urnas apuradas, enquanto em Los Angeles (Pág. 4) a urbanista Nithya Raman, apoiada pelos Socialistas Democráticos da América (DSA), derrotou a prefeita Karen Bass com 52% dos votos."
                        ],
                        "pontos": [
                            "Democratas lideram voto popular nacional na Câmara por mais de 12 pontos — maior oscilação desde 1948.",
                            "No Mississippi, democrata Scott Colom lidera disputa histórica ao Senado por 49% a 48,85% na reta final da apuração.",
                            "Em Los Angeles, Nithya Raman derrota a prefeita Karen Bass com plataforma focada em moradia e crise social."
                        ]
                    },
                    {
                        "caderno": "Ásia-Pacífico · Nova Zelândia",
                        "pagina": "6",
                        "autor": "Nic Fildes (Sydney)",
                        "titulo": "Neozelandeses vão às urnas em 'eleição dos supermercados' sob carestia de alimentos e risco de parlamento sem maioria",
                        "titulo_original": "New Zealanders vote in 'supermarket' poll as retail chains blamed for cost of living",
                        "texto_integral": [
                            "Os eleitores da Nova Zelândia foram às urnas neste sábado em uma eleição geral dominada pela revolta contra o custo dos alimentos e o duopólio das redes de supermercados Woolworths e Foodstuffs, que controlam 82% das compras das famílias no país.",
                            "O primeiro-ministro conservador Christopher Luxon luta para evitar tornar-se o primeiro chefe de governo de mandato único desde 1975, em meio a um desemprego de 5,7% (o maior em 11 anos) e projeções que apontam um parlamento dividido entre a coalizão do Partido Nacional e o bloco trabalhista."
                        ],
                        "pontos": [
                            "Duopólio varejista controla 82% do mercado de alimentos na Nova Zelândia e domina debate eleitoral.",
                            "Premiê Christopher Luxon enfrenta risco de parlamento sem maioria ('hung parliament') sob desemprego de 5,7%."
                        ]
                    }
                ]
            },
            {
                "jornal": "The Washington Post",
                "pais": "Estados Unidos",
                "escopo": "internacional",
                "total_paginas": 78,
                "imagem": imagens_por_jornal.get("The Washington Post", "capas/8dc0331e0239562f98f1323b47bf54ab.jpg"),
                "site": "https://www.washingtonpost.com",
                "manchete": "Acerto de contas ético derruba seis congressistas acusados de má conduta sexual; midterms dão alento cauteloso à Ucrânia",
                "manchete_original": "A reckoning pushes out six congressmen accused of sexual misconduct; Midterms give Ukrainians cautious hope",
                "nota": "Edição dominical do Post destaca a queda de parlamentares envolvidos em escândalos no Capitólio, a mobilização histórica no Delta do Mississippi, a reforma na Casa Branca pós-derrota, a visão de Kiev e o pós-eleição no Brasil.",
                "resumo_edicao": [
                    "A edição de domingo do The Washington Post (8 de novembro de 2026) destaca um inédito expurgo ético no Congresso americano: seis deputados federais — tanto democratas quanto republicanos, incluindo nomes conhecidos como Eric Swalwell (Califórnia) e Tony Gonzales (Texas) — foram varridos do Capitólio após denúncias de má conduta sexual e abuso doméstico mobilizarem o eleitorado.",
                    "Nas páginas internas, o jornal traz grande reportagem de campo no Delta do Mississippi mostrando como a mobilização comunitária de jovens e eleitores negros colocou o estado mais pobre dos EUA à beira de eleger seu primeiro senador negro desde a Reconstrução. No noticiário internacional (Págs. 14 e 15), os correspondentes em Kiev e no Brasil analisam a esperança cautelosa da Ucrânia com o novo Congresso democrata e o isolamento de Flávio Bolsonaro após a vitória de Lula."
                ],
                "editorial": {
                    "titulo": "O recado das urnas contra o abuso de poder e a turbulência na Casa Branca",
                    "texto": [
                        "O Washington Post enfatiza que o ciclo eleitoral de 2026 restaurou linhas vermelhas éticas e institucionais que pareciam adormecidas na política americana, forçando Donald Trump a iniciar uma reforma de gabinete na Casa Branca para os dois anos finais de mandato diante de um Congresso hostil."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Política · Capitólio",
                        "pagina": "1 e 4",
                        "autor": "Redação Política Washington",
                        "titulo": "Acerto de contas nas urnas expulsa seis congressistas acusados de má conduta sexual e abuso doméstico",
                        "titulo_original": "A reckoning pushes out six congressmen accused of sexual misconduct, domestic abuse",
                        "texto_integral": [
                            "Uma onda bipartidária de responsabilização ética retirou do Congresso dos Estados Unidos seis deputados federais atingidos por investigações e revelações de assédio sexual, relacionamentos impróprios com subordinados e violência doméstica. Os casos envolveram parlamentares de ambos os partidos, incluindo o democrata Eric Swalwell, da Califórnia, e o republicano Tony Gonzales, do Texas.",
                            "Segundo o Washington Post, a combinação de regras mais severas do Comitê de Ética da Câmara com a recusa de doadores e eleitores suburbanos em tolerar escândalos pessoais produziu a maior renovação forçada por conduta moral desde o auge do movimento #MeToo."
                        ],
                        "pontos": [
                            "Seis integrantes da Câmara dos Representantes perderam seus mandatos ou renunciaram sob acusações éticas e sexuais.",
                            "Casos atingiram figuras de destaque nos dois partidos, como Eric Swalwell (D-CA) e Tony Gonzales (R-TX)."
                        ]
                    },
                    {
                        "caderno": "Eleições · Sul Profundo",
                        "pagina": "5, 6 e 7",
                        "autor": "Enviados ao Mississippi",
                        "titulo": "Participação recorde de eleitores negros e jovens no Delta do Mississippi impulsiona virada histórica",
                        "titulo_original": "Record-high turnout and engagement among Black voters across the Mississippi Delta",
                        "texto_integral": [
                            "Ao longo de três páginas de reportagem no coração do Delta do Mississippi — região rural, negra e historicamente marcada pela supressão de votos —, o Washington Post documenta a operação de base que registrou dezenas de milhares de jovens em encontros comunitários, igrejas e festas locais antes do prazo eleitoral.",
                            "O comparecimento recorde nas urnas das comunidades afro-americanas, somado ao desgaste econômico do governo republicano entre trabalhadores brancos devido à inflação de alimentos, explica como o democrata Scott Colom conseguiu abrir vantagem sobre a senadora Cindy Hyde-Smith em um estado que Donald Trump havia vencido por 22 pontos em 2024."
                        ],
                        "pontos": [
                            "Mobilização porta a porta no Delta do Mississippi gerou comparecimento histórico do eleitorado negro e jovem.",
                            "Descontentamento com o preço dos alimentos e tarifas corroeu a margem republicana no estado."
                        ]
                    },
                    {
                        "caderno": "Casa Branca & Saúde",
                        "pagina": "8 e 13",
                        "autor": "Redação Casa Branca",
                        "titulo": "Ex-assessor de saúde Calley Means acusa cúpula de Trump de ceder a lobbies enquanto Casa Branca prepara reforma",
                        "titulo_original": "Former health aide accuses Trump advisers of catering to special interests",
                        "texto_integral": [
                            "Calley Means, ex-assessor da Casa Branca ligado à agenda de saúde que pediu demissão no mês passado, acusou publicamente os principais estrategistas e chefes de gabinete de Donald Trump de engavetarem reformas contra alimentos ultraprocessados e a indústria farmacêutica para atender a lobbies corporativos e doadores de campanha.",
                            "Na página 13, o jornal relata que Trump iniciou uma ampla reformulação em sua equipe na Casa Branca após a derrota republicana nas midterms, buscando preencher cargos vagos e preparar a defesa do governo contra a enxurrada de intimações e CPIs que os democratas prometem abrir em janeiro."
                        ],
                        "pontos": [
                            "Ex-assessor Calley Means denuncia captura da agenda de saúde da Casa Branca por lobbies industriais.",
                            "Trump promove troca de assessores para enfrentar maioria democrata na Câmara e no Senado a partir de janeiro."
                        ]
                    },
                    {
                        "caderno": "Mundo · Ucrânia",
                        "pagina": "14",
                        "autor": "Correspondente em Kiev",
                        "titulo": "Vitória democrata nas midterms dá esperança cautelosa aos ucranianos, mesmo enquanto Trump negocia com Putin",
                        "titulo_original": "Midterms give Ukrainians cautious hope, even as Trump deals with Putin",
                        "texto_integral": [
                            "Em despacho direto de Kiev, o Washington Post relata que a derrota histórica do Partido Republicano nas eleições legislativas americanas trouxe um alívio cauteloso à liderança ucraniana, que via seu esforço de defesa sufocado pelo bloqueio de pacotes militares no Congresso.",
                            "Embora Donald Trump continue conduzindo conversas diretas com enviados de Vladimir Putin para tentar impor um acordo rápido antes do fim do ano, autoridades em Kiev avaliam que um Congresso dominado pelos democratas terá poder orçamentário e político para travar concessões territoriais unilaterais a Moscou."
                        ],
                        "pontos": [
                            "Kiev vê maioria democrata no Capitólio como freio legislativo contra um acordo desfavorável imposto pela Casa Branca."
                        ]
                    },
                    {
                        "caderno": "Mundo · América Latina",
                        "pagina": "15",
                        "autor": "Correspondente na América do Sul",
                        "titulo": "A vitória de Lula no Brasil e o impasse da direita bolsonarista após o segundo turno",
                        "titulo_original": "Lula's victory and the aftermath for Bolsonaro's movement in Brazil",
                        "texto_integral": [
                            "Na página 15, o Washington Post examina o desfecho da eleição presidencial brasileira de 2026, destacando como Luiz Inácio Lula da Silva conseguiu atrair o eleitorado moderado no segundo turno diante da rejeição ao sobrenome Bolsonaro.",
                            "A reportagem observa que, embora candidatos de centro-direita tenham somado forte votação no primeiro turno e conquistado governos estaduais importantes, a insistência do ex-presidente Jair Bolsonaro em impor a candidatura do filho Flávio Bolsonaro limitou o teto eleitoral da oposição e culminou na contestada viagem do senador aos Estados Unidos."
                        ],
                        "pontos": [
                            "Análise destaca como a escolha de Flávio Bolsonaro impediu a unificação do eleitorado de centro-direita no 2º turno."
                        ]
                    }
                ]
            },
            {
                "jornal": "The Guardian",
                "pais": "Reino Unido",
                "escopo": "internacional",
                "total_paginas": 212,
                "imagem": imagens_por_jornal.get("The Guardian", "capas/41d2e3357148204714a56b9d8c9e47f0.jpg"),
                "site": "https://www.theguardian.com",
                "manchete": "Bolsas caem na Ásia e na Europa após vitória democrata nos EUA; reação em Londres ao revés de Trump e corte de forças policiais",
                "manchete_original": "Stock markets fall sharply in Asia and Europe after US midterms tech rout; UK officials react to Republicans' defeat",
                "nota": "Guardian analisa o impacto global da liquidação das Big Techs, o alívio diplomático no gabinete de Keir Starmer, a revolta contra a fusão de forças policiais na Inglaterra, o alerta climático sobre 'falsa primavera' e o caso Russell Brand.",
                "resumo_edicao": [
                    "A edição britânica do The Guardian destaca na editoria internacional e econômica as ondas de choque das eleições de meio de mandato dos EUA sobre a Europa e a Ásia: o tombo das ações de tecnologia em Wall Street contaminou as bolsas de Tóquio, Londres e Frankfurt, enquanto integrantes da comitiva do primeiro-ministro britânico no Caribe acompanhavam com incredulidade e alívio a dimensão da derrota republicana — que a presidente do Comitê de Relações Exteriores da Câmara dos Comuns, Emily Thornberry, atribuiu diretamente ao desgaste da guerra com o Irã e à carestia.",
                    "No noticiário doméstico do Reino Unido, ganham destaque a reação de prefeitos trabalhistas como Andy Burnham contra o plano do Ministério do Interior de fundir e cortar o número de forças policiais regionais na Inglaterra e no País de Gales, o alerta de botânicos sobre uma 'primavera precoce' em pleno outono britânico e os desdobramentos judiciais antes da sentença de Russell Brand."
                ],
                "editorial": {
                    "titulo": "O terremoto nas midterms americanas e os limites do populismo de direita",
                    "texto": [
                        "O Guardian avalia que o resultado das urnas nos Estados Unidos desmonta a tese da invencibilidade eleitoral do trumpismo e oferece uma lição direta aos governos europeus: quando aventuras militares externas e desregulamentação para bilionários elevam o custo de vida das famílias trabalhadoras, a reação nas urnas é implacável."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Economia & Mercados Globais",
                        "pagina": "4",
                        "autor": "Editoria Financeira (Londres)",
                        "titulo": "Bolsas recuam forte na Ásia e na Europa após vitória democrata nos EUA desencadear liquidação em tecnologia",
                        "titulo_original": "Stock markets fell sharply in Asia and Europe after Democrats' decisive victory triggered US tech rout",
                        "texto_integral": [
                            "Os mercados acionários da Ásia e da Europa fecharam em queda acentuada, contagiados pela liquidação em massa de ações de tecnologia e inteligência artificial em Wall Street após a vitória decisiva do Partido Democrata nas eleições de meio de mandato dos Estados Unidos.",
                            "Investidores globais correram para reduzir exposição a fornecedores de semicondutores asiáticos e empresas de infraestrutura energética diante da promessa dos novos governadores e congressistas democratas de impor moratórias a megacentros de dados e elevar a tributação e a regulação antitruste sobre as gigantes do Vale do Silício."
                        ],
                        "pontos": [
                            "Queda de Wall Street espalhou-se pelas bolsas asiáticas e europeias puxada por fornecedores da cadeia de IA.",
                            "Mercado precifica freio regulatório sobre expansão de data centers e maior escrutínio antitruste no Congresso dos EUA."
                        ]
                    },
                    {
                        "caderno": "Diplomacia · Reino Unido & EUA",
                        "pagina": "12 e 13",
                        "autor": "Correspondentes Diplomáticos",
                        "titulo": "Comitiva britânica acompanha com incredulidade escala da derrota republicana; guerra no Irã pesou nas urnas",
                        "titulo_original": "UK officials scrolled through results in incredulity as scale of Republicans' defeat became clear",
                        "texto_integral": [
                            "Autoridades britânicas que acompanhavam o primeiro-ministro em viagem oficial pelo Caribe acompanharam madrugada adentro, com misto de espanto e alívio silencioso, a dimensão da derrota republicana nas urnas americanas.",
                            "Na página 13, a presidente do Comitê de Relações Exteriores da Câmara dos Comuns, a trabalhista Emily Thornberry, ressaltou que — como o próprio vice-presidente americano JD Vance admitiu nos bastidores pós-eleição — o envolvimento militar no conflito com o Irã e seu impacto direto na inflação de combustíveis foram decisivos para alienar a base eleitoral de Trump."
                        ],
                        "pontos": [
                            "Emily Thornberry e analistas em Londres apontam a guerra no Irã e a alta da gasolina como fatores centrais do revés de Trump.",
                            "Diplomacia britânica vê oportunidade para estabilizar alianças na Otan e acordos climáticos com o novo Congresso americano."
                        ]
                    },
                    {
                        "caderno": "Política Britânica · Segurança",
                        "pagina": "10",
                        "autor": "Editoria de Polícia e Interior",
                        "titulo": "Plano para cortar número de forças policiais na Inglaterra e Gales ameaça policiamento comunitário e agenda de Burnham",
                        "titulo_original": "Plans to slash the number of police forces in England and Wales represent a 'real threat' to local policing",
                        "texto_integral": [
                            "Planos do governo em Whitehall para fundir e reduzir drasticamente as 43 forças policiais regionais da Inglaterra e do País de Gales sob o argumento de corte de custos provocaram forte reação de chefes de polícia e líderes regionais trabalhistas.",
                            "Críticos alertam que a centralização representa uma 'ameaça real' ao policiamento de bairro e mina diretamente a agenda de descentralização administrativa (devolution) liderada pelo prefeito da Grande Manchester, Andy Burnham."
                        ],
                        "pontos": [
                            "Proposta de fusão das 43 forças policiais regionais gera confronto com prefeitos metropolitanos como Andy Burnham."
                        ]
                    },
                    {
                        "caderno": "Clima & Biodiversidade",
                        "pagina": "9",
                        "autor": "Editoria de Meio Ambiente",
                        "titulo": "Árvores no Reino Unido vivem 'primavera precoce' em pleno outono após outubro mais quente, alertam cientistas",
                        "titulo_original": "Trees in the UK are experiencing an 'early spring' because of mild autumn temperatures",
                        "texto_integral": [
                            "Cientistas florestais e botânicos britânicos emitiram um alerta após registrarem árvores florescendo novamente em novembro — uma 'falsa primavera precoce' provocada pelas temperaturas excepcionalmente amenas deste outono, depois de outubro ter fechado bem acima da média histórica.",
                            "Os pesquisadores advertem que o fenômeno esgota as reservas energéticas das espécies arbóreas antes das geadas de inverno e desorganiza o ciclo de polinizadores e aves migratórias em todo o arquipélago britânico."
                        ],
                        "pontos": [
                            "Temperaturas atípicas de outubro e novembro provocam floração fora de época em diversas regiões do Reino Unido."
                        ]
                    },
                    {
                        "caderno": "Justiça & Imigração no Reino Unido",
                        "pagina": "1, 6, 7, 8 e 15",
                        "autor": "Redação Londres",
                        "titulo": "Justiça britânica prepara sentença de Russell Brand; imigrantes denunciam travas à residência permanente após 10 anos",
                        "titulo_original": "Brand due to be sentenced on Monday as barrister reports himself to regulator; Migrants face indefinite leave to remain hurdles",
                        "texto_integral": [
                            "Nas páginas 1, 6, 7 e 8, o Guardian informa que a polícia britânica se prepara para o surgimento de novas vítimas antes da audiência de segunda-feira que fixará a sentença de prisão do ex-apresentador Russell Brand, recém-condenado por estupro e agressão sexual, enquanto seu advogado de defesa, Ian Winter KC, autodenunciou-se ao órgão regulador da advocacia após discussão ríspida com uma jornalista.",
                            "Na página 15, reportagem social retrata o drama de trabalhadores essenciais que vivem legalmente há quase dez anos no Reino Unido — como Aneisha Williams, 39 anos — e se veem subitamente ameaçados de deportação pelo endurecimento das taxas e exigências para a obtenção de residência permanente (indefinite leave to remain)."
                        ],
                        "pontos": [
                            "Sentença de Russell Brand será proferida na segunda-feira em Londres após condenação criminal.",
                            "Trabalhadores com quase uma década de residência legal denunciam barreiras financeiras e burocráticas do Home Office."
                        ]
                    }
                ]
            },
            {
                "jornal": "The Times UK",
                "pais": "Reino Unido",
                "escopo": "internacional",
                "total_paginas": 352,
                "imagem": imagens_por_jornal.get("The Times UK", "capas/5657802960f1312796a4887021c18e93.jpg"),
                "site": "https://www.thetimes.com",
                "manchete": "Novo currículo nacional britânico proibirá ensino antecipado para exames GCSE nos três primeiros anos do ensino secundário",
                "manchete_original": "GCSEs should not be taught in the first three years of secondary school, new national curriculum will say",
                "nota": "Edição do Sunday Times destaca a reforma educacional no Reino Unido, o perfil de bastidores do chanceler Ed Miliband no Foreign Office, os detalhes da investigação do jornal no caso Russell Brand e estudo da Science sobre linguagem das aves.",
                "resumo_edicao": [
                    "A edição dominical do The Times / The Sunday Times (8 de novembro de 2026) revela que a revisão oficial do currículo nacional da Inglaterra determinará que as escolas secundárias deixem de preparar alunos para os exames GCSE durante os três primeiros anos (dos 11 aos 14 anos), após evidências de que o treinamento obsessivo para provas desde cedo está provocando desengajamento estudantil e empobrecendo o aprendizado.",
                    "Na política externa (Pág. 13), um amplo perfil de bastidores retrata a rotina de madrugada de Ed Miliband à frente do Foreign Office diante das crises geopolíticas globais. A edição traz ainda os detalhes agora liberados de embargo judicial sobre a investigação jornalística do Sunday Times que levou à condenação de Russell Brand e um estudo global publicado na revista Science sobre padrões universais entre o canto dos pássaros e as línguas humanas."
                ],
                "editorial": {
                    "titulo": "Educação ampla antes da obsessão pelos exames e os novos desafios do Foreign Office",
                    "texto": [
                        "O Sunday Times pondera que devolver os primeiros anos do ensino secundário à curiosidade intelectual, às artes e aos fundamentos científicos — em vez de reduzi-los a um cursinho precoce para o GCSE — é um passo bem-vindo, desde que acompanhado de rigor pedagógico."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Educação · Reino Unido",
                        "pagina": "4",
                        "autor": "Editoria de Educação",
                        "titulo": "Exames GCSE não deverão ser ensinados nos três primeiros anos do ensino secundário, determinará novo currículo nacional",
                        "titulo_original": "GCSEs should not be taught in the first three years of secondary school, the new national curriculum will say",
                        "texto_integral": [
                            "O novo currículo nacional britânico estabelecerá diretrizes claras para impedir que as escolas secundárias iniciem o treinamento específico para os exames GCSE já nos três primeiros anos do ciclo (Years 7, 8 e 9, equivalentes à faixa de 11 a 14 anos).",
                            "A mudança responde a conclusões da comissão de revisão curricular de que a preparação incessante para testes padronizados ao longo de cinco anos consecutivos tem provocado tédio, evasão escolar e abandono de disciplinas criativas, históricas e experimentais.",
                            "Com a diretriz, o Ministério da Educação busca garantir que os alunos tenham uma formação humanística e científica mais ampla antes de afunilarem os estudos para as avaliações nacionais aos 15 e 16 anos."
                        ],
                        "pontos": [
                            "Revisão curricular proíbe escolas de transformarem os três primeiros anos do ensino secundário em treino precoce para o GCSE.",
                            "Objetivo é combater o desengajamento escolar e preservar o ensino de artes, música, línguas e ciências."
                        ]
                    },
                    {
                        "caderno": "Política Externa · Perfil",
                        "pagina": "13",
                        "autor": "Tim Shipman / Política",
                        "titulo": "A obsessão da madrugada: os bastidores de Ed Miliband no comando da diplomacia britânica",
                        "titulo_original": "It is in the middle of the night that Ed Miliband's fascination with his new job as foreign secretary is most apparent",
                        "texto_integral": [
                            "É no meio da madrugada que o fascínio de Ed Miliband por seu novo cargo como secretário de Relações Exteriores (Foreign Secretary) fica mais evidente: segundo aliados próximos ouvidos pelo Sunday Times, quando acorda durante a noite, Miliband mergulha imediatamente nos despachos diplomáticos de Washington, Oriente Médio e Ásia em vez de voltar a dormir.",
                            "O perfil detalha como o ex-líder trabalhista e ex-ministro de Energia vem tentando reposicionar a diplomacia britânica diante da turbulência em Washington após as midterms, das negociações sobre a Ucrânia e da agenda climática global na COP31."
                        ],
                        "pontos": [
                            "Perfil revela o estilo intenso de trabalho de Ed Miliband à frente do Foreign Office em momento de transição geopolítica."
                        ]
                    },
                    {
                        "caderno": "Justiça & Investigação",
                        "pagina": "1, 6 e 7",
                        "autor": "Equipe de Investigação do Sunday Times",
                        "titulo": "Com fim do sigilo judicial, Sunday Times revela bastidores do julgamento que condenou Russell Brand",
                        "titulo_original": "Behind closed doors: how the trial and conviction of Russell Brand unfolded",
                        "texto_integral": [
                            "Com o levantamento das restrições de publicação após o veredito do júri na Crown Court, o Sunday Times publica uma reconstituição de três páginas dos bastidores do julgamento que levou à condenação de Russell Brand, originado pela reportagem investigativa conjunta do jornal em 2023.",
                            "Os relatos revelam as tentativas da defesa de anular o júri alegando prejuízo pela cobertura da imprensa e descrevem a mudança de postura do ex-comediante — que tentou apresentar-se durante o processo como influenciador cristão convertido — diante dos depoimentos contundentes das vítimas."
                        ],
                        "pontos": [
                            "Levantamento do embargo judicial permite revelar tentativas da defesa de barrar o julgamento na Crown Court."
                        ]
                    },
                    {
                        "caderno": "Negócios & Ciência",
                        "pagina": "5, 8 e 15",
                        "autor": "Redação Sunday Times",
                        "titulo": "Estudo da Science revela leis comuns entre canto das aves e linguagem humana; NHS revê protocolo para partos",
                        "titulo_original": "Science study of 5,900 bird songs from 367 species reveals universal laws shared with human languages",
                        "texto_integral": [
                            "Na editoria de Ciência (Pág. 8), o jornal destaca pesquisa internacional publicada na revista Science que analisou 5.900 cantos de 367 espécies de aves em todos os continentes e descobriu que as regras estatísticas de duração e frequência seguem leis matemáticas universais idênticas às das línguas humanas.",
                            "Na página 5, o caderno de negócios examina a transição da tradicional rede britânica de brinquedos The Entertainer, fundada por Gary e Catherine Grant, enquanto na página 15 o Serviço Nacional de Saúde (NHS) discute novas diretrizes sobre indução antecipada de parto quando exames de ultrassom apontam bebês grandes para a idade gestacional."
                        ],
                        "pontos": [
                            "Análise de 5.900 cantos de 367 espécies de aves comprova leis acústicas compartilhadas com a fala humana.",
                            "NHS avalia riscos e benefícios da indução precoce de parto em casos de suspeita de macrossomia fetal."
                        ]
                    }
                ]
            }
        ],
        "destaques": [
            {
                "editoria": "Economia & Fiscal",
                "titulo": "O dilema fiscal do novo mandato: risco de PIB a 1% em 2027 e queda de 4,1% na indústria pressionam Lula",
                "texto": "Folha de S.Paulo, Valor Econômico e O Globo convergem no diagnóstico de que a janela pós-eleitoral para anunciar um plano estrutural de contenção de gastos está se fechando rapidamente, com a indústria já acumulando retração de 4,1% desde maio sob juros altos.",
                "jornais": ["Folha de S.Paulo", "Valor Econômico", "O Globo", "O Estado de S. Paulo"],
                "texto_completo": [
                    "A leitura cruzada dos quatro grandes diários brasileiros deste domingo revela que a economia entrou no centro gravitacional do quarto mandato de Luiz Inácio Lula da Silva antes mesmo da posse de 2027. Na manchete da Folha de S.Paulo (Pág. A17), projeções do Ibre/FGV, de bancos e de consultorias apontam que o PIB brasileiro deverá desacelerar para cerca de 1% no próximo ano, sem descartar o risco de recessão caso a ausência de um plano fiscal mantenha o dólar pressionado e a taxa Selic em patamar contracionista.",
                    "O alerta encontra respaldo empírico nos dados de atividade destacados pelo Valor Econômico (Pág. A2): a produção industrial caiu 0,8% em setembro — recuo pior que o esperado — e já acumula perda de 4,1% desde maio. Ainda assim, como reportam O Globo (Pág. 15) e o Valor (Pág. A6), a ala política do Planalto resiste a um corte drástico em despesas indexadas, e o número dois da Fazenda, Dario Durigan, evitou cravar datas após reunião com economistas próximos ao PT.",
                    "Enquanto isso, o Estadão (Pág. A13) lembra que qualquer reforma dependerá de um Congresso onde 70% dos deputados eleitos já fecharam apoio à reeleição de Hugo Motta (Republicanos-PB), exigindo coordenação fina do governo — que cogita deslocar Geraldo Alckmin para a Defesa ou Segurança Pública e mantém o governador Rafael Fonteles no radar econômico."
                ],
                "por_que_importa": "A coordenação entre ajuste fiscal e política monetária nas próximas semanas definirá se o Brasil atravessará 2027 com crescimento moderado ou estagnação sob juros de dois dígitos."
            },
            {
                "editoria": "Política & América do Sul",
                "titulo": "Rejeição de 60% à viagem de Flávio Bolsonaro aos EUA e prisão de Santiago Peña no Paraguai",
                "texto": "Pesquisa Quaest em O Globo mostra que seis em cada dez brasileiros desaprovam a postura do candidato derrotado; no Paraguai, colapso do Ueno Bank leva à renúncia, impeachment e prisão preventiva de Santiago Peña.",
                "jornais": ["O Globo", "Folha de S.Paulo", "Valor Econômico", "The Washington Post"],
                "texto_completo": [
                    "No tabuleiro político pós-eleitoral, O Globo traz em manchete a pesquisa Genial/Quaest segundo a qual seis em cada dez brasileiros rejeitam a decisão do senador Flávio Bolsonaro (PL-RJ) de viajar para os Estados Unidos após a derrota no segundo turno e de alimentar retórica golpista. Nos bastidores da direita (O Globo, Pág. 6; Folha, Pág. A3), líderes partidários já defendem um recuo tático pragmático e concentram forças na disputa pela presidência do Senado em 2027.",
                    "A situação de Flávio tornou-se ainda mais isolada internacionalmente após a derrota republicana nas midterms americanas, analisada pelo Washington Post (Pág. 15) e pelo Valor Econômico (Pág. A9), que vê espaço para uma relação mais pragmática entre Lula e Washington.",
                    "Na vizinhança sul-americana, Folha (Pág. A28) e Valor (Pág. A1 e A15) destacam o terremoto institucional no Paraguai: após a liquidação do banco digital Ueno Bank — do qual foi acionista até 2025 —, o presidente Santiago Peña tentou renunciar na sexta-feira, mas sofreu impeachment por 78 votos a 0 na Câmara e teve sua prisão preventiva decretada pela Justiça paraguaia neste fim de semana."
                ],
                "por_que_importa": "A desaprovação majoritária a contestações eleitorais no Brasil e a crise aguda em Assunção redesenham o equilíbrio político do Cone Sul às vésperas da cúpula do Mercosul."
            },
            {
                "editoria": "EUA · Midterms & Tecnologia",
                "titulo": "A onda azul democrata (+12 pontos) e o freio sobre o império de IA e data centers nos EUA",
                "texto": "Financial Times, Washington Post e Guardian detalham como o custo de vida e a rejeição aos bilionários do Vale do Silício deram Câmara, Senado e governos-chave aos democratas, derrubando US$ 3,2 trilhões em Wall Street.",
                "jornais": ["Financial Times", "The Washington Post", "The Guardian"],
                "texto_completo": [
                    "Os grandes jornais anglo-saxões dedicam cobertura histórica ao rescaldo das eleições de meio de mandato nos Estados Unidos. Como demonstra o Financial Times (Págs. 1 a 4), a vitória democrata na Câmara e no Senado representou uma oscilação de 12 pontos percentuais no voto popular nacional — a maior desde 1948 —, puxada por eleitores de renda mais baixa (< US$ 30 mil/ano), condados hispânicos do Texas e participação recorde de eleitores negros no Delta do Mississippi (Washington Post, Págs. 5–7).",
                    "Um dos eixos mais surpreendentes da eleição foi a revolta popular contra os megacentros de dados de inteligência artificial e os bilionários de tecnologia que financiaram com US$ 600 milhões os comitês de Donald Trump. Com a vitória democrata para o governo de estados como Texas (Gina Hinojosa), Ohio e Geórgia, entre 41% e 45% da capacidade planejada de data centers nos EUA enfrenta agora risco de moratória devido ao consumo de energia e água.",
                    "O choque político provocou uma perda de US$ 3,2 trilhões nas bolsas americanas na quinta-feira — que se espalhou pela Ásia e Europa na sexta (The Guardian, Pág. 4) — e forçou a Anthropic a reduzir sua avaliação pretendida de US$ 2 trilhões para US$ 1,3–1,5 trilhão para manter seu IPO ainda antes do feriado de Ação de Graças (Financial Times, Pág. 1)."
                ],
                "por_que_importa": "O freio político e regulatório nos EUA sobre a construção de data centers e o aperto sobre as Big Techs alteram o ritmo global de investimentos em inteligência artificial e semicondutores."
            },
            {
                "editoria": "Geopolítica · Europa & China",
                "titulo": "Alarme europeu com negociação EUA-Rússia em Abu Dhabi e ultimato de Washington à China sobre terras raras",
                "texto": "Bruxelas reage à tentativa de Trump e Kushner de discutir a segurança de toda a Europa diretamente com Moscou, enquanto o Tesouro dos EUA cobra de Pequim o cumprimento imediato da trégua de Busan.",
                "jornais": ["Financial Times", "The Washington Post", "The Times UK"],
                "texto_completo": [
                    "Mesmo enfraquecido internamente pelas midterms, o governo Donald Trump acelerou duas frentes geopolíticas de alto risco reportadas pelo Financial Times (Págs. 1 e 2) e pelo Washington Post (Pág. 14). Na frente europeia, a reunião de Trump e Jared Kushner na Casa Branca com o enviado russo Kirill Dmitriev — preparando negociações em Abu Dhabi que 'podem envolver toda a Europa' — colocou as chancelarias da União Europeia e o secretário britânico Ed Miliband (The Times, Pág. 13) em estado de alerta máximo contra um acordo às custas da Otan.",
                    "Em Kiev, o Washington Post relata que a liderança ucraniana enxerga na nova maioria democrata no Capitólio uma salvaguarda crucial para impedir que a Casa Branca force uma capitulação territorial.",
                    "Paralelamente, na Ásia, o secretário do Tesouro americano, Scott Bessent, advertiu o vice-premiê chinês He Lifeng de que Pequim precisa cumprir imediatamente as cotas de exportação de terras raras acordadas na trégua de Busan (que expira em 10 de janeiro), elevando a tensão a duas semanas da cúpula da Apec em Shenzhen."
                ],
                "por_que_importa": "As próximas duas semanas — com as conversas em Abu Dhabi, a abertura da COP31 na Turquia e a cúpula da Apec em Shenzhen — serão decisivas para a segurança europeia e o comércio global."
            }
        ],
        "leitura": [
            {
                "jornal": "Financial Times",
                "pagina": "1 e 2",
                "autor": "Equipe FT em São Francisco, Houston e Washington",
                "titulo": "O terremoto das midterms sobre o Vale do Silício: o IPO da Anthropic e a revolta contra os data centers de IA",
                "nota": "Por que 41% da capacidade planejada de data centers nos EUA entrou na mira dos novos governadores democratas e como Wall Street perdeu US$ 3,2 trilhões.",
                "texto_integral": [
                    "A reportagem especial de capa e página 2 do Financial Times Weekend reconstitui a semana em que a aliança bilionária entre o Vale do Silício e o movimento MAGA colapsou nas urnas. Apesar de grupos ligados a titãs da tecnologia terem despejado mais de US$ 600 milhões em campanhas republicanas — incluindo mais de US$ 200 milhões de Elon Musk apenas no Texas —, o eleitorado americano puniu severamente a política do 'build, baby, build' para megacentros de dados de inteligência artificial.",
                    "Dezenas de candidatos democratas eleitos para o Congresso e para governos estaduais transformaram o impacto dos data centers nas tarifas residenciais de energia elétrica e no consumo de água local em bandeira central de campanha. Com as vitórias democratas nos governos do Texas (Gina Hinojosa), Geórgia (Keisha Lance Bottoms) e Ohio (Amy Acton), cerca de 41% a 45% de toda a capacidade planejada de data centers dos EUA encontra-se agora em estados cujos governadores prometem moratórias ou revisão rigorosa de licenças.",
                    "Em Wall Street, o terremoto político provocou uma perda de US$ 3,2 trilhões em um único pregão e levou analistas a projetarem o cancelamento de 20% da capacidade planejada de IA para 2027. Ainda assim, em São Francisco, Dario Amodei decidiu manter o IPO da Anthropic para antes do Thanksgiving, aceitando reduzir a avaliação pretendida de US$ 2 trilhões para cerca de US$ 1,3 trilhão a US$ 1,5 trilhão para captar até US$ 100 bilhões no mercado público."
                ],
                "pontos": [
                    "Doadores de tecnologia investiram mais de US$ 600 milhões em campanhas republicanas, mas enfrentaram rejeição popular.",
                    "Quase metade da expansão de data centers nos EUA está em estados conquistados por governadores favoráveis a moratórias.",
                    "Anthropic mantém IPO para novembro com valuation ajustado entre US$ 1,3 trilhão e US$ 1,5 trilhão."
                ],
                "citacao": "O partido deveria mandar os 'tech bros' de volta para o Vale do Silício. Apostamos nossas maiorias no dinheiro das grandes empresas de IA e ignoramos nossos próprios eleitores."
            },
            {
                "jornal": "Folha de S.Paulo",
                "pagina": "A17 e A30",
                "autor": "Editorias de Economia e Cotidiano",
                "titulo": "A encruzilhada orçamentária de 2027: risco de PIB a 1% sob juros altos e a fatura de R$ 14 bilhões dos presídios",
                "nota": "O choque entre a escassez fiscal que trava a economia e as novas demandas bilionárias de segurança pública nos estados.",
                "texto_integral": [
                    "Duas grandes reportagens da Folha de S.Paulo deste domingo iluminam os dois lados da mesma moeda orçamentária que aguarda o governo Lula em 2027. Na página A17, economistas da FGV, de bancos e consultorias alertam que a ausência de um plano estrutural de contenção de despesas obrigatórias mantém o dólar e os juros futuros pressionados, reduzindo a projeção de crescimento do PIB para apenas 1% no ano que vem — com risco concreto de recessão caso o comércio e os serviços sucumbam ao crédito caro.",
                    "Ao mesmo tempo, na página A30, um levantamento técnico do Fórum Brasileiro de Segurança Pública revela o tamanho da conta exigida para enfrentar a principal preocupação do eleitorado: adequar o sistema penitenciário às diretrizes da PEC da Segurança Pública exigirá R$ 14 bilhões para abrir e manter 123,7 mil vagas em regime fechado.",
                    "Como os estados já operam no limite fiscal, a pressão recairá sobre o Tesouro Nacional justamente no momento em que a equipe econômica precisa comprimir despesas discricionárias e rever indexadores para estabilizar a dívida pública."
                ],
                "pontos": [
                    "Economia mais dependente de comércio e serviços em 2027 sente o peso da Selic elevada.",
                    "Criação e custeio de 123,7 mil vagas prisionais em regime fechado exigem R$ 14 bilhões em novos recursos."
                ]
            },
            {
                "jornal": "O Globo",
                "pagina": "1, 4, 6 e 8",
                "autor": "Redação Política O Globo",
                "titulo": "O Brasil depois das urnas: a rejeição à viagem de Flávio Bolsonaro aos EUA e o redesenho da Esplanada de Lula",
                "nota": "Pesquisa Quaest e bastidores mostram como a direita tenta virar a página do bolsonarismo radical enquanto Lula calibra o papel de Alckmin.",
                "texto_integral": [
                    "O pacote especial de reportagens políticas de O Globo traça a radiografia completa da primeira semana após o segundo turno presidencial. A pesquisa Genial/Quaest (Pág. 4) mostra que 60% dos brasileiros reprovam a atitude de Flávio Bolsonaro (PL-RJ) de viajar para os Estados Unidos após a derrota e insistir em questionamentos ao processo eleitoral.",
                    "Nos bastidores (Pág. 6), o jornal revela que, ainda na noite da apuração, líderes pragmáticos do PL como Rogério Marinho já tentavam encerrar o discurso de contestação para focar na articulação pela presidência do Senado em 2027. Do lado do governo reeleito (Pág. 8), Lula prepara uma reforma ministerial que deve dar novo protagonismo a Geraldo Alckmin — cotado para assumir a Defesa, uma eventual pasta da Segurança Pública ou seguir na Indústria e Comércio."
                ],
                "pontos": [
                    "Seis em cada dez brasileiros rejeitam a viagem de Flávio Bolsonaro aos EUA após o 2º turno.",
                    "Geraldo Alckmin é peça central no desenho da nova Esplanada para dialogar com setor produtivo e Forças Armadas."
                ]
            },
            {
                "jornal": "The Washington Post",
                "pagina": "5, 6, 7 e 14",
                "autor": "Enviados ao Mississippi e Correspondente em Kiev",
                "titulo": "Do Delta do Mississippi a Kiev: como a mobilização comunitária nos EUA redesenhou o Congresso e deu fôlego à Ucrânia",
                "nota": "Reportagem de campo mostra como o voto negro e jovem produziu uma quase-virada histórica no Sul profundo e mudou o cálculo geopolítico na Europa.",
                "texto_integral": [
                    "A grande reportagem narrativa do Washington Post (Págs. 5 a 7) percorre as estradas rurais do Delta do Mississippi para explicar um dos fenômenos mais impressionantes das midterms de 2026: como um estado que votou em Donald Trump por 22 pontos de vantagem há dois anos chegou a este domingo com o democrata negro Scott Colom liderando a corrida pelo Senado.",
                    "A chave foi uma silenciosa operação de registro eleitoral que buscou jovens e trabalhadores em eventos de tratores, igrejas e festas comunitárias, combinada à frustração de eleitores brancos da classe trabalhadora com o preço da carne e dos combustíveis. Na página 14, o correspondente do Post em Kiev mostra a repercussão imediata dessa virada a milhares de quilômetros dali: para a Ucrânia, o novo Congresso democrata representa a principal garantia de que os EUA não abandonarão o país nas negociações com Moscou."
                ],
                "pontos": [
                    "Engajamento recorde no Delta do Mississippi colocou um democrata negro na liderança ao Senado pela primeira vez desde a Reconstrução.",
                    "Mudança de comando no Capitólio altera a correlação de forças para a política externa americana em 2027."
                ]
            },
            {
                "jornal": "The Times UK",
                "pagina": "4 e 13",
                "autor": "Editorias de Educação e Política do Sunday Times",
                "titulo": "O fim do treinamento precoce para o GCSE nas escolas britânicas e as madrugadas de Ed Miliband no Foreign Office",
                "nota": "Reforma curricular na Inglaterra busca resgatar o prazer de aprender entre 11 e 14 anos; perfil mostra como Ed Miliband comanda a diplomacia britânica.",
                "texto_integral": [
                    "Duas leituras de fôlego se destacam na edição dominical do Times britânico. Na página 4, o jornal antecipa que o novo currículo nacional determinará que as escolas secundárias deixem de ensinar conteúdo voltado exclusivamente aos exames GCSE nos três primeiros anos (11 a 14 anos), combatendo a cultura de 'fábrica de provas' que vinha esvaziando aulas de artes, música e ciências.",
                    "Na página 13, um longo perfil político revela os bastidores de Ed Miliband como secretário de Relações Exteriores (Foreign Secretary): acordando no meio da madrugada para ler telegramas diplomáticos e articular com aliados, Miliband tenta posicionar o Reino Unido como ponte entre uma União Europeia apreensiva e uma Washington dividida após as eleições de meio de mandato."
                ],
                "pontos": [
                    "Novo currículo britânico protege os três primeiros anos do ensino secundário contra a preparação antecipada para exames GCSE.",
                    "Ed Miliband assume protagonismo na política externa do gabinete trabalhista diante da nova ordem em Washington."
                ]
            }
        ]
    }
