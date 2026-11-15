---
name: faixa-oculta-curadoria
description: >-
  Diretrizes mandatórias, padrões de qualidade visual e procedimentos editoriais para a plataforma cultural Faixa Oculta.
  Use sempre que for atualizar boletins diários, revista semanal, edições mensais de cultura (Música, Cinema, Livros),
  agenda cultural do Rio, resolução de capas/banners, integrações de áudio/streaming e destaques com Retratos de Autor.
---

# Faixa Oculta · Guia Operacional e Regras de Curadoria

Este documento estabelece as diretrizes permanentes de qualidade, integridade visual, densidade editorial e automação da plataforma cultural **Faixa Oculta**. Nenhuma atualização ou geração futura deve infringir estes padrões.

---

## 1. Regra Fundamental: Proibição de Capas Sintéticas / Fallbacks Escuros

> [!CAUTION]
> **É TERMINANTEMENTE PROIBIDO gerar capas sintéticas ou cartões escuros com texto desenhado via Pillow/PIL (`fallback_capa_elegante` ou fundo `#0f172a`).**

* **100% dos itens da revista** (matéria de capa, guias temáticos, catálogo essencial e árvore de influências) DEVEM possuir capas ou pôsteres oficiais autênticos em alta resolução.
* **Fontes Oficiais por Vertente:**
  * **Música:** Deezer API (`https://api.deezer.com/search/album?q=...` campo `cover_xl` com `1000x1000px`) ou iTunes Search API (`entity=album`, `1000x1000bb`).
  * **Cinema e Séries:** Wikimedia / Wikipedia API (`action=query&prop=pageimages|imageinfo` usando obrigatoriamente User-Agent customizado `FaixaOcultaBot/1.0 (contact@faixaoculta.com)`) ou iTunes Movie API (`entity=movie`).
  * **Livros:** Open Library Covers API (`https://covers.openlibrary.org/b/id/{id}-L.jpg` ou por ISBN) ou iTunes Books API (`entity=ebook`).
* **Procedimento de Download e Padronização:**
  * Use sempre `curl -s -L -A "FaixaOcultaBot/1.0 (contact@faixaoculta.com)"` para evitar erros de SSL e bloqueios de hotlink da Wikipedia.
  * Todas as imagens baixadas devem ser convertidas para **JPEG RGB** padronizado com `Image.open().convert('RGB').save(dest, 'JPEG', quality=92)`.
  * Nomeação: `capas/<md5>.jpg` (ou hash de 32 caracteres hexadecimais), compatível com a validação `safeUrl` em `pagina.html`.
* **Validação Pré-Deploy Mandatória:**
  * Antes de qualquer commit, execute um scan visual em `capas/` garantindo que nenhuma imagem contenha mais de 70% de pixels pretos uniformes de fallback.

---

## 2. Áudio, Streaming e Playlists: Sem Cortes de 30 Segundos

> [!IMPORTANT]
> A experiência de áudio foi concebida para audição contínua e imersiva. Prévias truncadas de 30 segundos inviabilizam o produto.

* **Player Principal Embutido:** O player iframe oficial é o **YouTube Music** (`https://www.youtube-nocookie.com/embed/...`). Nunca volte para o player embutido do Spotify que limita a 30s.
* **Botões de Acesso Nativo:** Cada recomendação musical e a obra em foco devem conter links discretos em estilo editorial para abrir no aplicativo instalado: `Spotify ↗` e `YT Music ↗`.
* **Playlist do Mês Real e Sequencial:**
  * As recomendações do mês devem compor uma playlist contínua real, gerada na URL do YouTube (`https://www.youtube.com/watch_videos?video_ids=ID1,ID2,...`).
  * Os IDs de vídeo devem ser extraídos de canais oficiais ou tópicos do artista (`- Topic`).
* **Player Expansível:**
  * A lista completa de faixas da playlist mensal na interface deve permanecer envelopada em `<details class="pl-acc">` retrátil, para nunca empurrar o conteúdo dos demais pilares para baixo.
* **Grande Destaque do Mês:**
  * O card da "Obra em Foco" DEVE possuir o botão interativo `▶ Tocar álbum no player` com o `youtube_id` cadastrado.
* **Playlists dos Shows da Agenda (Semanal e Mensal):**
  * **Cadência Oficial Realista:** As playlists dos shows do Rio são atualizadas no **início da semana** (segunda-feira) para a playlist semanal (`semana`: shows dos próximos 7 dias) e no **início do mês** (todo dia 01) para a playlist mensal/30 dias (`trinta`: shows dos próximos 30 dias / mês).
  * **Proibição de Falsas Promessas:** É expressamente proibido alegar na interface ou notas que as playlists são atualizadas constantemente ou "a cada segunda e quinta", quando a cadência real estabelecida e suficiente é semanal e mensal.
  * **Composição Automática via Agenda:** O script `tools/atualizar_playlists_agenda.py` extrai automaticamente todos os artistas com sessões e shows marcados para o período a partir de `agenda.atual.eventos`.
  * **Acesso Nativo e Reprodutibilidade:** Os cartões das playlists na interface oferecem reprodução direta no site (`Ouvir aqui`) e link para a fila contínua no YouTube (`https://www.youtube.com/watch_videos?video_ids=...`, botão `YouTube ↗`), pois o domínio `music.youtube.com` não suporta `/watch_videos` e descarta para a página inicial. O detalhamento expansível de `Bandas` fornece chips individuais com links para os canais de cada banda no YouTube Music e Spotify.
  * **Preservação do Histórico:** Cada atualização arquiva a versão anterior em `agenda.atual.playlists.anteriores`, acessível pelo botão retrátil "Notas e versões anteriores".

---

## 3. Cinema, Streaming e Livros: Integrações de Consumo

* **Cinema & Séries:**
  * **Stremio:** Botão direto com deep link (`stremio:///detail/movie/...` ou web) para visualização imediata.
  * **JustWatch:** Link de busca (`https://www.justwatch.com/br/busca?q=...`) para consulta instantânea de onde o título está disponível em salas ou plataformas.
  * **Trailers:** Botão de trailer funcional apontando para o YouTube.
* **Livros:**
  * **Google Play Livros:** Link canônico para leitura de amostras e visualização.
  * **Estante Virtual:** Link de busca para aquisição de novos e sebos no Brasil.
  * **Ficha Editorial:** Sempre indicar ano de publicação, editora brasileira e tradutor(a).

---

## 4. Sistema de Feedback Cultural (Sim / Não / Aproveitado)

* **Abrangência Universal:** Todas as vertentes (Música, Cinema, Livros e Agenda de Eventos) DEVEM possuir os botões de afinidade:
  * `👍 Sim` — Gosto positivo / salvar na fila.
  * `👎 Não` — Descartar / ocultar da visualização imediata.
  * `✓ Já ouvi / Já vi / Já li / Fui` — Marcar como consumido/aproveitado sem descartar.
* **Persistência:** As marcações são guardadas no `localStorage` sob a chave `faixa_marcas` e alimentam os filtros e os perfis de gosto para futuras curadorias.

---

## 5. Densidade Editorial e Calendário de Rodadas

* **Quinta-feira à Noite — Revista Semanal (Semana):**
  * Leitura rica e aprofundada de fim de semana.
  * **Pluralidade Mandatória de Fontes:** A síntese DEVE cruzar pelo menos 6 a 8 veículos de diferentes inclinações e perfis editoriais (*Folha de S.Paulo, O Globo, g1, BBC News Brasil, Poder360, Metrópoles, Valor Econômico, EBC/Agência Brasil*).
  * Explicitar claramente nos eixos temáticos os pontos de divergência ou ênfase entre os veículos.
* **Dia 01 do Mês — Cultura Mensal (Música, Cinema, Livros):**
  * Curadoria robusta e aprofundada:
    * Música: 35 a 45 discos distribuídos em guias especializados (Rock/Alt, Jazz/Vanguardas, Eletrônica, Brasil).
    * Cinema: 25 a 35 títulos (estreias, festivais, clássicos e streaming).
    * Livros: 20 a 25 obras (ficção, não-ficção, ensaio científico e traduções no Brasil).
* **Agenda Cultural do Rio & Playlists dos Shows:**
  * Foco prioritário em **rock, música independente e cena underground/alternativa**.
  * Circuitos: Botafogo (Audio Rebel, Saloon 79, Estúdio Hanoi), Circo Voador, Centro e Tijuca (Garage Grindhouse).
  * **Cadência das Playlists dos Shows:** Atualização no **início da semana** (segunda-feira) para os shows dos próximos 7 dias e no **início do mês** (todo dia 01) para a safra completa dos próximos 30 dias.
* **Boletins Diários (Hoje):**
  * Duas edições: Manhã (05h BRT) e Noite (17h BRT).
  * Modo Leitor limpo na íntegra para todas as notas, sem anúncios e sem redirecionamentos externos indesejados.

---

## 6. Grande Destaque do Mês · Retrato de Autor

Em cada edição mensal (Música, Cinema e Livros), deve ser produzido um módulo de Retrato de Autor estruturado em:
1. **Ensaio Crítico Profundo:** Biografia artística, conceito estético, revoluções formais e trajetória.
2. **Obra em Foco (`ad-obra-foco-card`):** O lançamento do autor em destaque com resenha crítica e botões de player/streaming.
3. **Catálogo Essencial:** 3 a 5 obras seminais com capas oficiais, contextualização e links.
4. **Árvore de Influências & Diálogos:** Artistas e obras que beberam dessa fonte, com explicação conceitual e técnica minuciosa de **COMO** foram influenciados, acompanhados de suas respectivas capas/pôsteres oficiais.

---

## 7. Identidade Visual "Elenco Refinado"

* **Paleta & Atmosfera:** Inspirada em jornal/revista impressa em papel creme (`#F3EEE4`), tinta grafite nobre e escala tipográfica harmoniosa.
* **Proibição de Cores Neon:** Não utilizar botões com verde Spotify saturado, vermelho botão plástico ou degradês comerciais que quebrem a linguagem sóbria.
* **Banners Persistentes:** O painel superior de capas (folha de contato) deve permanecer visível em qualquer seleção de chip/filtro na visualização da revista.

---

## 8. Arquitetura de Execução: Prioridade Local com Salvaguarda na Nuvem

1. **Prioridade Local (Mac):** A execução prioritária é na máquina local quando você estiver operando (`tools/sentinela_boletim.py` / `tools/orquestrador_nuvem.py`).
2. **Salvaguarda Automática (GitHub Actions):** Se a máquina estiver desligada ou houver atraso, a nuvem assume via cron às 05h e 17h BRT com a API Gemini.
3. **Cache-Busting:** Toda requisição a `data/revista.json` deve incluir timestamp dinâmico (`?t=` + `Date.now()`) para garantir propagação instantânea.

---

## 9. Boletim em Áudio · Narração Integral da Notícia Completa (Não Resumo)

> [!IMPORTANT]
> O boletim em áudio é uma experiência de jornal falado / podcast diário imersivo. A locução DEVE cobrir o texto completo e aprofundado das reportagens, e nunca apenas resumos telegráficos rasos.

* **Geração Automática de Áudio:** Sempre que uma nova edição do boletim diário for gerada (manhã ou noite), o script `tools/gerar_audio_boletim.py` deve ser acionado.
* **Roteiro Longo e Substancial:** Cada notícia é narrada com seus parágrafos analíticos integrais (`texto_completo`), contexto político/econômico e desdobramentos práticos (~5 a 8 minutos de duração).
* **Motor de Voz Neural:** Utiliza `edge-tts` com a voz `pt-BR-AntonioNeural` (taxa de locução natural de rádio/podcast), gerando arquivo de alta fidelidade em `audios/boletim_<dia>.mp3`. Possui fallback transparente para voz local macOS `say` em caso de instabilidade na API externa.
* **Interface do Usuário:** O topo da aba "Hoje" exibe o card `.d-audio-card` com:
  * Player de áudio embutido para reprodução imediata do briefing do dia.
  * Botão de narração ao vivo integrada via **Web Speech API** (`window.speechSynthesis`), permitindo ouvir qualquer boletim diretamente pelo navegador com a voz do sistema.

---

## 10. Varredura Online Obrigatória e Dados Contemporâneos (Anti-Cutoff)

> [!IMPORTANT]
> A Faixa Oculta NUNCA deve utilizar a memória interna estática (cutoff 2024) do modelo de IA para inventar ou reciclar safras culturais contemporâneas. Toda e qualquer edição cultural DEVE ser apurada por varredura eficiente online.

* **Cinema em Cartaz:** Os filmes na seção "Em cartaz ou estreando nos próximos dias" DEVEM ser lançamentos reais contemporâneos ao calendário da edição (ex: novembro de 2026), apurados via festivais (Festival do Rio, Mostra SP), distribuidoras brasileiras e programações das salas de cinema (CineSesc, Estação Net, Salas de Arte, IMAX).
* **Separação Rígida entre Lançamentos e Acervo:** Filmes e obras de safras passadas (ex: 2024, 2023) devem figurar em seções de acervo/streaming/achados (`[achados]`) e NUNCA como "em cartaz" (`[cartaz]`).
* **Livros Novos:** Lançamentos editoriais devem ser apurados online junto às editoras brasileiras (Companhia das Letras, Todavia, Record, Zahar, Bazar do Tempo) e portais literários (*PublishNews*, *Quatro Cinco Um*).
* **Música e Álbuns:** Discos novos contemporâneos devem ser apurados via portais e APIs de música (Pitchfork, Billboard Brasil, Rolling Stone, Deezer, iTunes).
* **Varredor Automático:** O script `tools/varredura_cultural_online.py` integra a orquestração do sistema (`tools/orquestrador_nuvem.py` e `tools/sentinela_boletim.py`), garantindo que 100% dos dados e das capas oficiais sejam sincronizados ao vivo das APIs externas.

---

## 11. Perfil Editorial Personalizado do Leitor (Fabio Gomes / UFRJ)

A curadoria da Faixa Oculta foi desenhada para um leitor de alto capital cultural e intelectual, professor e pesquisador de biofísica na UFRJ.

> [!CAUTION]
> **Separação Rigorosa: Noticiário Diário vs. Leituras da Semana:**
> O leitor busca a Faixa Oculta pelo seu **interesse pessoal, cultural e cívico, e NÃO como extensão de rotina de trabalho ou de laboratório**.
> - **No 'Hoje' (Boletim Diário):** Estritamente **NOTÍCIAS CLÁSSICAS DE PRIMEIRA LINHA** (Economia dura, Política Nacional, Geopolítica/Internacional e Sociedade). É TERMINANTEMENTE PROIBIDO entupir o boletim diário com assuntos de trabalho/laboratório (editais burocráticos de fomento a biotérios, compras de insumos para bancada, feiras de recrutamento de estudantes, comunicados de pós-graduação ou notas departamentais).
> - **Na 'Semana' (Revista da Semana):** Espaço adequado para ensaios reflexivos, grandes debates de ideias, filosofia da ciência, fronteiras do conhecimento e reflexão humanística sobre tecnologia e cosmologia — como leitura prazerosa e descompromissada de fim de semana.

1. **Economia, Política & Diplomacia (Diário):** Macroeconomia, contas públicas, inflação, juros, câmbio, emprego, indústria, comércio exterior; reformas institucionais, Congresso, STF, governabilidade; geopolítica internacional, eleições globais, multilateralismo (BRICS, G20, ONU, Itamaraty).
2. **Sociedade, Cidades & Cidadania (Diário):** Segurança pública e pacto federativo, regulação e direitos do consumidor, infraestrutura urbana, eventos climáticos extremos e Defesa Civil.
3. **Ficção Científica (Sci-Fi), Fantasia & Ensaios (Semanal / Mensal):** Hard sci-fi, especulação sobre inteligência artificial, colapso tecnológico e ecologia (Editora Aleph, Morro Branco, Todavia); alta fantasia mitológica, cosmologias indígenas e realismo mágico de autor.
4. **Música (Mensal / Agenda):** Indie rock/folk e canção confessional (Lucy Dacus, Phoebe Bridgers, Julia Jacklin, Soccer Mommy, Sharon Van Etten); art-rock e pós-punk (Geese, bar italia); shoegaze-pop (Wishy, beabadoobee); folk literário (The Decemberists, Okkervil River, Greg Freeman); rock e vanguarda brasileira (Papangu, Letrux, El Efecto, Clau Aniz, Marcelo Cabral); cânone moderno (Radiohead, Blur, Queens of the Stone Age).
5. **Cinema (Mensal):** Cinema autoral e de festivais internacionais (Cannes, Veneza, Festival do Rio, Mostra SP); cinema brasileiro independente (Gabriel Martins, Kleber Mendonça Filho, Filmes de Plástico, Pedro Freire); documentários reflexivos e cosmologias visuais.

---

## 12. Prioridade Editorial do Boletim Diário ('Hoje': Noticiário Clássico de Alta Densidade)

> [!IMPORTANT]
> **Volume e Perfil Editorial Mandatório:** O boletim diário (manhã e noite) DEVE conter obrigatoriamente **AO MENOS 10 NOTÍCIAS DENSAS NACIONAIS + 10 INTERNACIONAIS TRADUZIDAS** (20 a 22 matérias por edição).
> O noticiário diário deve ser **CLÁSSICO, SÓBRIO E INDISPENSÁVEL**. ZERO matérias de rotina de trabalho/laboratório ou curiosidades menores (feiras universitárias de estudantes, cadeados de naufrágios, etc.).

1. **Hierarquia Editorial Obrigatória do 'Hoje':**
   - **1º:** **Economia & Contas Públicas** (corte de gastos, juros Selic, câmbio/dólar, inflação IPCA, meta fiscal, dívida pública, pacote fiscal, reforma tributária).
   - **2º:** **Política Nacional & Instituições** (Congresso Nacional, Câmara, Senado, STF, decisões judiciais estruturantes, governabilidade, eleições).
   - **3º:** **Geopolítica & Política Internacional** (eleições nos EUA, cúpulas G20/BRICS/ONU, diplomacia, relações internacionais, conflitos e comércio global).
   - **4º:** **Emprego, Indústria & Comércio Exterior** (mercado de trabalho, PNAD Contínua, produção fabril, balança comercial, logística e concessões de transporte).
   - **5º:** **Sociedade, Cidades & Cidadania** (segurança pública e inteligência federativa, defesa do consumidor, crédito, apostas/bets, Defesa Civil em eventos climáticos).
2. **Estrutura Mandatória de Cada Nota (`dias[dia].notas`):**
   - `texto_completo`: 3 a 4 parágrafos densos e analíticos para leitura integral direta sem nenhum placeholder.
   - `resumo_visoes`: Síntese contrastando as diferentes linhas editoriais e posições políticas da imprensa (*mercado vs independente vs governamental*).
   - `por_que_importa`: Impacto institucional e econômico direto.
   - `aprofundamento`: Contexto estrutural, desdobramentos legislativos e o que observar adiante.
   - `fontes`: Múltiplas fontes com links reais diretos para o site original.

---

## 13. Zero Placeholders de Resenha ("O texto completo entra na próxima atualização")

> [!CAUTION]
> **É TERMINANTEMENTE PROIBIDO exibir no modo leitor a mensagem: *"O texto completo entra na próxima atualização."* ou equivalentes de pendência.**

* **100% dos Itens Devem Conter Resenha Crítica:** Todo álbum, filme ou livro cadastrado em `itens`, `cine_itens` e `livro_itens` DEVE conter o array `resenha` populado com 3 a 4 parágrafos substanciais de ensaio crítico, contextualização estética, análise das faixas/cenas/capítulos e recepção pela crítica especializada.
* **Ficha Técnica e Informações do Artista:**
  * Música: Ficha com selo, gênero, data, formação da banda, faixas essenciais (`faixas`), álbum ponte (`ponte`) e recepção crítica (`recepcao`).
  * Cinema: Ficha com direção, elenco principal, fotografia, trilha, país, duração, onde assistir e prêmios.
  * Livros: Ficha com autor, tradutor brasileiro, editora nacional, número de páginas, temas e recepção.
* **Script Utilitário de Higienização:** Caso novos itens sejam importados sem resenhas completas, execute obrigatoriamente `python3 tools/popular_resenhas_completas.py` antes de qualquer commit ou publicação.

---

## 14. Modo Leitor Avançado com Controles Tipográficos e Temas

O diálogo de leitura (`#texto` para notícias e `#leitura` para obras culturais) deve obrigatoriamente incluir a toolbar de controles `.lt-controles`:

1. **Família de Fonte (`--lt-font`):**
   * **Serif:** `Newsreader`, Georgia, serif (leitura editorial e ensaística).
   * **Sans:** `-apple-system`, `Inter`, `Segoe UI`, sans-serif (leitura rápida e dinâmica).
   * **Mono:** `IBM Plex Mono`, monospace (leitura técnica e de pesquisa).
2. **Tamanho do Texto (`--lt-size` e `--lt-lh`):**
   * Botões interativos `A−` e `A+` com variação de 14px a 24px e indicador numérico central.
   * As regras CSS aplicam `!important` diretamente sobre os parágrafos (`dialog.texto .lt-corpo-completo p`, `dialog.leitura .l-texto p`, etc.) para assegurar que a alteração seja instantânea e visível em qualquer navegador.
3. **Temas de Contraste e Legibilidade (`--lt-bg`, `--lt-fg`, `--lt-card`, `--lt-rule`):**
   * **Papel (Creme):** Fundo clássico de papel de imprensa (`#F3EEE4`), tinta grafite (`#1C1A17`).
   * **Escuro:** Fundo noturno escuro elegante (`#161513`), tipografia creme suave de alto contraste (`#EAE5DB`). **Nunca manter fontes pretas sobre fundo preto.**
   * **Branco:** Fundo alvo puro (`#FFFFFF`), contraste editorial tradicional (`#111111`).
4. **Persistência das Escolhas:** Todas as preferências de fonte, tamanho e tema DEVEM ser salvas automaticamente em `localStorage` sob a chave `fo_leitor_prefs` para persistirem nas sessões subsequentes.

---

## 15. Prioridade do Modo Leitor e Análises Críticas Especializadas

> [!IMPORTANT]
> A Faixa Oculta prioriza a imersão de leitura dentro da própria plataforma. Nenhum clique em notícia ou obra deve redirecionar o usuário externamente sem antes apresentar a experiência completa no leitor.

1. **Abertura Imediata no Leitor:**
   * Clicar sobre qualquer cartão de notícia (`.d-nota`), matéria semanal ou obra cultural (`.card`, `.mcard`) aciona diretamente o diálogo de leitura (`#texto` ou `#leitura`).
   * O botão "Fonte" nos cards abre a análise/crítica no modo leitor; o acesso ao site original é mantido como ação secundária interna via botão `Acessar no site original ↗`.
2. **2 a 3 Análises Críticas por Obra Cultural:**
   * Todo álbum, filme ou livro cadastrado deve contar com 2 a 3 resenhas críticas detalhadas extraídas de publicações respeitadas (*Pitchfork, The Guardian, RogerEbert.com, The New York Times, Stereogum, Folha de S.Paulo, Quatro Cinco Um, etc.*).
   * As análises são exibidas no módulo "O que a crítica especializada disse" (`.l-criticas`), trazendo autor, data, veículo, cotação/nota, pontos essenciais e citações reflexivas.

---

## 16. Navegação Temporal Limpa (Dropdown por Mês) e Notícias Salvas

* **Dropdown de Edições com `<optgroup>`:** No topo da aba "Hoje", é proibido acumular dezenas de pílulas/botões soltos de datas. A navegação DEVE ser implementada através de um `<select class="d-edsel-select">`, agrupando as edições por mês (`optgroup label="Edições de ..."`) em ordem cronológica decrescente.
* **Sistema de Notícias Salvas:**
  * Cada nota do boletim possui o botão interativo `🔖 Salvar`.
  * As notícias salvas são guardadas em `localStorage` sob a chave `fo_noticias_salvas`.
  * O cabeçalho exibe o botão `🔖 Notícias salvas (${totalSalvas})`, permitindo ao leitor ativar um filtro instantâneo (`S.filtroSalvas`) para ler todas as matérias guardadas em uma lista dedicada.

---

## 17. Equivalência da Mídia Internacional com Tradução Integral e Paridade Mandatória

> [!IMPORTANT]
> **Paridade Editorial Mandatória (20 a 22 matérias por dia):** O boletim diário da Faixa Oculta não se limita à imprensa brasileira. Toda edição (manhã e noite) DEVE obrigatoriamente trazer **ao menos 10 notícias densas de Mídia Nacional + ao menos 10 notícias equivalentes dos principais veículos da mídia internacional generalista e diplomática** (*The New York Times, The Guardian, Financial Times, BBC World News, Le Monde, El País, Al Jazeera*).

1. **Atributo `escopo` Obrigatório em 100% das Notas:**
   * Toda nota nacional DEVE ter `"escopo": "nacional"` e `"pais": "Brasil"`.
   * Toda nota internacional DEVE ter `"escopo": "internacional"` e `"pais"` explicitado (ex: `"Estados Unidos"`, `"Reino Unido"`, `"Alemanha"`, `"Oriente Médio"`, `"América Latina"`).
   * A interface em `pagina.html` depende desse atributo para ativar a barra de filtros fluida (`Todas`, `🇧🇷 Mídia Nacional`, `🌍 Mídia Internacional Traduzida`).
2. **Tradução Fiel e Rigorosa nas Caixas e no Modo Leitor:**
   * **Cartão da Notícia (`.d-nota`):** Título, texto resumo, editoria e "Por que importa" traduzidos para o português culto com redação jornalística de alto nível.
   * **Modo Leitor (`abrirNota` e `#texto`):** Reportagem completa de 3 a 4 parágrafos densos (`texto_completo`), síntese de visões e pontos-chave traduzidos na íntegra para o português, preservando o título estrangeiro original em `titulo_original`.
3. **Preservação dos Links Originais na Língua Materna:**
   * O link externo de conferência (`f.url`) deve apontar **obrigatoriamente para a URL original no site da publicação estrangeira**, na língua original em que foi escrita (*inglês, francês, espanhol, etc.*) através do deep-link específico do artigo (ex.: `.../artigo.html`), sendo proibidas URLs genéricas de capa.
4. **Filtro de Navegação e Alternância de Eixos:**
   * O topo do boletim deve fornecer a alternância de eixos: `[ Todas ]`, `[ 🇧🇷 Mídia Nacional ]` e `[ 🌍 Mídia Internacional Traduzida ]`, permitindo ao leitor focar no cenário nacional, no panorama global ou em ambos integrados.
5. **Resiliência do Pipeline (100% Notícias Reais em Todos os Modos):**
   * Tanto a chamada da API do Gemini quanto o fallback algorítmico (`curadoria_algoritmica_resiliente` em `tools/boletim_nuvem.py`) DEVEM estruturar sempre os dois blocos equivalentes de 11 matérias nacionais e 11 internacionais baseadas exclusivamente em matérias reais contemporâneas das últimas 48 horas.

---

## 18. Veracidade Absoluta e Proibição Terminativa de Notícias Sintéticas (Anti-Fake / Anti-Placeholder)

> [!CAUTION]
> **Proibição Absoluta de Fabricação de Notícias ou Templates Simulados:**
> É estritamente proibido inventar notícias, simular manchetes de ficção ou utilizar templates/listas hardcoded de fatos fictícios com URLs genéricas de capa (`nytimes.com/world`, `theguardian.com/science`).
> - **100% de Fontes Reais Contemporâneas:** Toda e qualquer matéria (Nacional ou Internacional) DEVE ser extraída diretamente de reportagens reais apuradas nos feeds RSS e portais de jornalismo profissional nas últimas 48 horas (validado via `pubDate`).
> - **Deep-Link Real do Artigo:** Cada notícia deve manter a URL autêntica do artigo original específico na internet para verificação e conferência externa pelo leitor.
> - **Fidelidade Factual na Tradução:** O processo de tradução e síntese de matérias internacionais deve ser fiel ao fato apurado pelos correspondentes no exterior, proibindo extrapolações ficcionais ou datas defasadas.

---

## 19. Especificação Detalhada de Eventos e Bandas nas Pequenas Casas (Agenda Cultural do Rio)

> [!CAUTION]
> **Proibição de Eventos Genéricos ou Guarda-Chuva:** É expressamente proibido cadastrar eventos genéricos nas casas de shows com títulos vagos e `artistas: None`. Da mesma forma, é inaceitável omitir atrações relevantes da cena indie em turnê ou lançando álbum no dia de hoje ou no fim de semana nas casas prioritárias.

1. **Shows com Identificação Individual de Bandas e Artistas:**
   * Cada casa da cena independente (Audio Rebel, Saloon 79, Estúdio Hanoi, Garage Grindhouse, Circo Voador, Bar Bukowski) deve possuir atrações individuais no array `destaques`.
   * Cada destaque DEVE explicitar as bandas participantes no array `artistas: ["Banda A", "Banda B"]`.
2. **Varredura Fina da Programação do Dia e Fim de Semana (Sem Omissões de Turnês):**
   * Ao apurar ou atualizar a agenda, o curador DEVE rastrear ativamente os shows agendados para a data exata da edição e para o fim de semana imediato nos portais e bilheterias oficiais (*audiorebel.com.br/agenda*, Sympla, Shotgun, Instagram das casas).
   * Bandas em turnê de lançamento de discos nacionais elogiados (ex.: *Flerte Flamingo com a 'Dói Tour' na Audio Rebel*, *Ploho no Garage Grindhouse*, *The Baggios no Saloon 79*, *Ana Frango Elétrico no Circo Voador*) DEVEM ser cadastradas com destaque máximo no topo da programação da respectiva casa, acompanhadas de datas, horários e atrações de abertura (ex.: *VALLADA*).
3. **Suporte Completo a Áudio sem Cortes (YouTube Music e Spotify):**
   * 100% dos artistas listados na Agenda DEVEM ser cadastrados nos dicionários `agenda.artistas.mapa` (Spotify ID) e `agenda.artistas.youtube` (ID de playlist/canal no YouTube Music).
   * Com esse mapeamento, o card e o leitor geram nativamente o botão `▶ Ouvir agora` (player embed no topo sem cortes de 30 segundos) e links diretos para YouTube Music e Spotify.
4. **Ficha do Show e Sessões Futuras Reais:**
   * Cada destaque deve conter o array `sessoes` com datas reais de sexta, sábado ou domingo no mês (ex: `2026-11-06`, `2026-11-07`, `2026-11-08`), horários (`20h`, `21h`), preços dos ingressos (`obs`) e links de bilheteria (`link`).
   * Deve incluir a justificativa curatorial (`porque`), reviews de veículos especializados (*Popload, Tenho Mais Discos Que Amigos, Scream & Yell, Trabalho Sujo*) e links de vídeo/trailer ao vivo no YouTube (`trailer`).

---

## 19. Botão e Diálogo de Convite Compartilhável para Cada Evento Cultural

> [!IMPORTANT]
> **Convite Cultural Integrado:** Todo evento e toda atração individual da Agenda deve fornecer a opção de criar um convite compartilhável com um clique.

1. **Botão de Ação nos Cards:**
   * No card geral (`cardEvento`) e em cada atração individual (`agDestaques`), exibir o botão sóbrio `✉️ Convidar`.
2. **Modal Interativo de Convite (`#dlg-convite`):**
   * Ao clicar, abre o diálogo com:
     * Selo mono do evento e chamada de convite (*"Você foi convidado(a) para este evento pelo Radar Cultural Faixa Oculta"*).
     * Grade de informações práticas: 📍 Onde (com link para Google Maps), 📅 Quando (datas e horários formatados), 🎟️ Ingressos (preço e link de compra).
     * Sinopse curatorial "Por que ir / O que esperar".
     * Line-up completo com botões `▶ Ouvir agora` (player sem cortes), YouTube Music e Spotify para cada banda.
     * Recepção crítica e citação de reviews especializados.
     * Trailer / vídeo de apresentação.
3. **Compartilhamento e Deep Link:**
   * **Copiar Link de Convite:** Gera e copia para o clipboard o deep link exclusivo `...#convite=<id_do_evento>`.
   * **WhatsApp:** Gera mensagem pré-formatada pronta para envio: *"Bora nesse show? 🎵 [Título] no [Local], [Data] às [Hora]..."*.
   * **Compartilhar Nativo:** Aciona `navigator.share` em dispositivos móveis.
   * **Deep Link Automático:** Se a URL for acessada com `#convite=<id>` ou `?convite=<id>`, a página abre o modal do evento instantaneamente no carregamento.

---

## 21. Integração Direta com Jornais e Revistas via Beeper (PDFs no Modo Leitor)

> [!TIP]
> O Beeper Desktop no macOS funciona como a fonte primária definitiva de jornalismo impresso e revistas de primeira linha, com extração integral dos PDFs diretamente para leitura dentro do Modo Leitor (`#texto`).

1. **Acesso ao Acervo Local, Normalização NFC e Salas Monitoradas:**
   * O acervo local fica em `~/Library/Application Support/BeeperTexts/index.db` (tabela `mx_room_messages`, `type = 'FILE'`).
   * **Normalização Unicode obrigatória:** Nomes de arquivos no macOS chegam frequentemente em forma NFD (acentos decompostos em `Piauí`, `Fórum`, `Econômico`, `Estadão`). A busca DEVE aplicar `unicodedata.normalize("NFC", ...)` e consultar `limit >= 250` mensagens por sala (salas diárias recebem ~80 arquivos/dia; limites menores ocultam semanários como *The Economist* e *Pesquisa FAPESP*).
   * **Salas monitoradas (`PRESS_ROOMS`):**
     * `Jornais BR` (`!iq3RLvh1JnfH6vJzkvaL:beeper.local`): *Folha de S.Paulo*, *O Estado de S. Paulo*, *O Globo*, *Valor Econômico*, além de revistas brasileiras (*CartaCapital, Revista Fórum, Pesquisa FAPESP, Revista Oeste, Revista piauí, Veja/Veja Rio*) e ocasionais edições internacionais (*The Economist*).
     * `International Newspapers` (`!Q3EN2ZSkzkir8tYnRU7t:beeper.local`): *The New York Times*, *Financial Times*, *The Washington Post*, *The Guardian*, *The Times / The Sunday Times*, *The Observer*, *FT Weekend Magazine*, *NYT Magazine*, *NYT Book Review*.
     * Complementares / históricas: `Jornais e Revistas 4.0` (`!tFgakhGBTv3CNjiYMdkM:beeper.local`), `IELTS|Newspapers & Magazines｜English` (`!CKYQw8EzDcJJW9ZBUqB7:beeper.local`), `Jornais e Revistas 3.0` (`!I86rARDr2VolnIjl9pki:beeper.local`) e `Revista Jacobina` (`!0nZuyBr37onTMYp69CUi:beeper.local`).
     * Para *Le Monde*, caso não haja PDF recente no Beeper, usar o coletor RSS oficial integrado (`obter_edicao_lemonde_rss` em `tools/processar_jornais_beeper.py`).
2. **Download Automatizado sob Demanda (`tools/processar_jornais_beeper.py`):**
   * Autentica via OAuth PKCE na Beeper Client API local (`http://localhost:23373`) e baixa via `POST /v1/assets/download` (`timeout >= 150s`), ordenando candidatos SEMPRE por data (`data_msg[:10]`, `timestamp`) e NUNCA priorizando arquivos antigos só porque já estavam baixados em cache.
3. **Pipeline Layout-Aware de Extração e OCR:**
   * **PDFs Digitais Vetoriais (*Estadão, O Globo, Valor, WaPo, The Guardian, Pesquisa FAPESP, CartaCapital*):** Extração Layout-Aware (`tools/extrator_pdf_layout_v2.py`) usando `page.get_text("dict")` para ranquear manchetes por tamanho tipográfico e `page.get_text("blocks")` ordenado por coluna `(y0, x0)` para nunca misturar colunas/páginas ou fatiar frases no meio.
   * **PDFs Escaneados em Imagem (*Folha de S.Paulo, Financial Times, The Times UK, The Economist, Revista piauí, Revista Oeste, Veja Rio*):** OCR nativo do macOS via Apple Vision Framework (`VNRecognizeTextRequest` em Swift com `en-US` ou `pt-BR`, até `min(max_pages, 12)` páginas).
   * **Coesão Editorial & Integridade de Sentenças:** Nunca juntar blocos de páginas distintas sob a manchete de capa da página 1 e nunca fatiar `pontos` por índice fixo de caracteres (`[:160]` no meio de uma palavra); extrair sempre sentenças inteiras.
4. **Contrato Obrigatório de Schema e Hidratação no Modo Leitor (`#texto`):**
   * **Nunca disponibilizar ou linkar PDFs brutos (`jornais/*.pdf`, `url_pdf`, `jornal_pdf_nome`) na interface.**
   * **Chave Canônica Obrigatória:** Toda reportagem em `dias[id].jornais.manchetes[*].reportagens[*]` e em `semanas[id].revistas.publicacoes[*].reportagens[*]` DEVE preencher **`texto_integral`** (lista de parágrafos densos e traduzidos para português culto) **e `pontos`** (lista de 1–3 frases completas), além de `titulo`, `titulo_original` (quando estrangeiro) e `citacao` (quando disponível).
   * **Publicação Automática de Revistas Semanais:** `processar_perfil("semana")` deve invocar `publicar_revistas_semana(resultado)` para gravar/mesclar diretamente em `semanas[sabado_iso].revistas.publicacoes` (Preservando revistas curadas como *Foreign Affairs, The New Yorker, Time, Newsweek* ao lado das extrações Beeper *The Economist, Pesquisa FAPESP, Revista Oeste, piauí, CartaCapital, Veja, Fórum, Valor EU&, FT Weekend Magazine, Observer, NYT Magazine, NYTBR*).
   * **Proteção Anti-Stub no Boot (`pagina.html` -> `index.html`):** Como `data/boot.json` compacta `reportagens[*].texto_integral` para ~140 caracteres durante a carga inicial, `iniciarEstatico()` DEVE carregar imediatamente `data/dias/<hojeId>.json` logo após o primeiro render do boot, e `abrirJornalCompleto()` DEVE ler `r.texto_integral || r.texto || r.resumo` e hidratar `j.shard_completo` sob demanda caso receba qualquer stub truncado.

---

## 22. Arquitetura v2 e Ferramentas de Automação (`tools/`)

Ao manipular a base ou executar atualizações, utilize o pipeline modular v2 em `tools/`:

| Script | Função Principal |
| :--- | :--- |
| `~/.faixaoculta/sentinela_boletim.py` / `tools/orquestrador_nuvem.py` | Sentinela local no Mac (com recuperação automática de `git`/`rebase` antes e depois do `push`) e orquestração central em 8 estágios com salvaguarda em nuvem. |
| `tools/gemini_client.py` | Cliente unificado com prioridade para **`gemini-4-hydrogen`** / **`gemini-4-argon`** e fallback **`gemini-3.8-flash`**, com contexto SSL macOS e fallback determinístico resiliente. |
| `tools/boletim_nuvem.py` | Apuração diária (manhã `< 17h` e noite `>= 17h`) de 11 notícias nacionais + 11 internacionais traduzidas na íntegra, deduplicadas entre turnos. |
| `tools/extrator_pdf_layout_v2.py` & `tools/processar_jornais_beeper.py` | Extração Layout-Aware (`dict` + `blocks` por coluna + Apple Vision OCR bilingue) e publicação automática no `revista.json` tanto para `--perfil diario` (`publicar_banca_jornais`) quanto para `--perfil semana` (`publicar_revistas_semana`), incluindo *Le Monde*, *The Economist*, *Pesquisa FAPESP* e *Revista Oeste*. |
| `tools/coletor_cultural_v2.py` | Coleta ao vivo de safras de Música, Cinema, Livros e 12 fontes da Agenda do Rio. |
| `tools/revista_semanal.py` & `tools/cultura_mensal.py` | Compiladores semanais (quintas à noite) e mensais (dia 01) dinâmicos preservando o bloco `revistas`. |
| `tools/atualizar_playlists_agenda.py` | Atualização automatizada das playlists da agenda (segunda-feira e dia 01), com arquivamento de histórico. |
| `tools/gerar_audio_boletim.py` | Síntese de áudio integral da edição (`texto_completo`) via `edge-tts` (`pt-BR-AntonioNeural`) com `--dia <turno_id>`. |
| `tools/particionar_dados_v2.py` | Particionamento em `data/boot.json` + shards completos em `data/dias/`, `data/semanas/` e `data/cultura/`. |
| `tools/validar_edicao.py` | Quality Gate automatizado (Checks 1–9) que bloqueia publicação em caso de falhas. |

---

## 23. Protocolo Obrigatório Pré-Publicação e Quality Gate

Antes de qualquer `git commit` e `git push origin main`, execute **sempre** na raiz do repositório:

```bash
cp pagina.html index.html
python3 tools/particionar_dados_v2.py
python3 tools/validar_edicao.py
```

O `tools/validar_edicao.py` só aprova (`Exit Code 0`) quando **todos os 9 critérios** passam simultaneamente:
1. Edições diárias do dia mais recente com `>= 20` notas reais (`10+` nacionais + `10+` internacionais traduzidas).
2. Máximo de 2 notas do mesmo veículo internacional e zero textos não traduzidos (`_eh_texto_estrangeiro`).
3. Zero frases genéricas/boilerplate em títulos, visões ou aprofundamentos.
4. 100% das capas referenciadas existem em disco com tamanho `> 2 KB`.
5. Zero referências ou links `.pdf` expostos nos JSONs.
6. 100% dos itens culturais da edição atual têm `resenha` completa (`>= 3` parágrafos).
7. 100% das reportagens em `dias[id].jornais.manchetes` têm `texto_integral` completo e na íntegra (parágrafos coerentes da coluna/artigo, `>= 150` chars, sem resumos telegráficos de 3 frases), `pontos` factuais distintos (sem copiar `texto_integral[0]` literalmente) e tradução integral para PT-BR (sem ruído de UI).
8. 100% das reportagens em `semanas[id].revistas.publicacoes` têm `texto_integral` na íntegra (sem resumos ou cortes prematuros), `pontos` factuais distintos e tradução integral em PT-BR.
9. Paridade exata de arquivo entre `pagina.html` e `index.html`, orçamento de boot enxuto (`data/boot.json <= 150 KB` hidratando depois `data/dias/<id>.json` e `data/revista.json` integrais) e integridade dos shards em `data/dias/`.
