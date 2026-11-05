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
* **Agenda Cultural do Rio:**
  * Foco prioritário em **rock, música independente e cena underground/alternativa**.
  * Circuitos: Botafogo (Audio Rebel, etc.), Estúdio Hanoi, Circo Voador, Centro e Tijuca.
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

A curadoria da Faixa Oculta foi desenhada para seu leitor-alvo, professor e pesquisador de biofísica na UFRJ. Todos os pilares editoriais devem refletir esse horizonte:

1. **Ciência, Saúde Pública & Amazônia:** Pesquisas de ponta em biofísica, imunometabolismo, arboviroses e vetores; mobilização acadêmica (SBPC, ABC, UFRJ, Fiocruz, FAPESP); clima, sustentabilidade e a Amazônia (Davi Kopenawa, Sumaúma).
2. **Política & Diplomacia:** Geopolítica internacional e política externa brasileira (Itamaraty, CEBRI, multilateralismo, BRICS, transição global); política nacional plural, reformas institucionais, STF e memória histórica democrática.
3. **Ficção Científica (Sci-Fi) & Fantasia:** Hard sci-fi, especulação sobre inteligência artificial, colapso tecnológico e ecologia (Editora Aleph, Morro Branco, Todavia); alta fantasia mitológica, cosmologias indígenas e realismo mágico de autor.
4. **Música:** Indie rock/folk e canção confessional (Lucy Dacus, Phoebe Bridgers, Julia Jacklin, Soccer Mommy, Sharon Van Etten); art-rock e pós-punk (Geese, bar italia); shoegaze-pop (Wishy, beabadoobee); folk literário (The Decemberists, Okkervil River, Greg Freeman); rock e vanguarda brasileira (Papangu, Letrux, El Efecto, Clau Aniz, Marcelo Cabral); cânone moderno (Radiohead, Blur, Queens of the Stone Age).
5. **Cinema:** Cinema autoral e de festivais internacionais (Cannes, Veneza, Festival do Rio, Mostra SP); cinema brasileiro independente (Gabriel Martins, Kleber Mendonça Filho, Filmes de Plástico, Pedro Freire); documentários reflexivos e cosmologias visuais.

---

## 12. Prioridade Editorial do Boletim Diário (Economia, Política e Diplomacia Primeiro)

> [!IMPORTANT]
> **Volume Editorial Mandatório:** O boletim diário (manhã e noite) DEVE conter obrigatoriamente **AO MENOS 10 NOTÍCIAS DENSAS E ANALÍTICAS** (10 a 12 matérias). Edições com 5 ou 6 notas são consideradas incompletas.
> As pautas de nicho acadêmico e pessoal NÃO devem canibalizar o noticiário duro nacional e internacional. Economia e Política estruturais têm prioridade máxima de abertura.

1. **Hierarquia Editorial Obrigatória do Boletim (Mínimo de 10 Notas):**
   - **1º e 2º:** **Economia & Contas Públicas** (corte de gastos, juros Selic, câmbio, inflação, meta fiscal, reforma tributária, dívida pública, estatais).
   - **3º e 4º:** **Política Nacional & Instituições** (STF, Congresso, governabilidade, regras de emendas, equilíbrio entre Poderes, segurança pública).
   - **5º e 6º:** **Diplomacia & Geopolítica Internacional** (eleições globais, BRICS, G20, Itamaraty, multilateralismo e conflitos).
   - **7º:** **Economia Setorial, Energia & Regulação** (impactos sociais de apostas/bets, malha elétrica, data centers, regulação de IA).
   - **8º e 9º:** **Ciência, Saúde Pública & Universidades** (FNDCT, UFRJ, Fiocruz, SBPC, CNPq, arboviroses, soberania vacinal no SUS).
   - **10º e 11º:** **Clima & Amazônia** (bacias hidrográficas, estiagem, terras indígenas, queimadas, COP30, transição ecológica).
2. **Estrutura Mandatória de Cada Nota (`dias[dia].notas`):**
   - `texto_completo`: 3 a 4 parágrafos densos e analíticos para leitura integral direta.
   - `resumo_visoes`: Síntese contrastando as diferentes linhas editoriais e posições políticas da imprensa (*mercado vs independente vs governamental*).
   - `por_que_importa`: Impacto institucional e cotidiano direto.
   - `aprofundamento`: Contexto histórico, desdobramentos legislativos e o que observar adiante.
   - `fontes`: Múltiplas fontes com links reais diretos para consulta externa.

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

## 17. Equivalência da Mídia Internacional com Tradução Integral

> [!IMPORTANT]
> **Paridade Editorial Mandatória:** O boletim diário da Faixa Oculta não se limita à imprensa brasileira. Toda edição deve obrigatoriamente trazer um **material equivalente dos principais veículos da mídia internacional** (*The New York Times, The Guardian, Financial Times, Le Monde, El País, Scientific American, MIT Technology Review, BBC World, Al Jazeera*).

1. **Tradução Fiel e Rigorosa nas Caixas e no Modo Leitor:**
   * **Cartão da Notícia (`.d-nota`):** Título, texto resumo, editoria e "Por que importa" traduzidos para o português com redação jornalística de alto nível.
   * **Modo Leitor (`abrirNota` e `#texto`):** Reportagem completa de 3 a 4 parágrafos densos (`texto_completo`), síntese de visões e pontos-chave traduzidos na íntegra para o português.
2. **Preservação dos Links Originais na Língua Materna:**
   * O link externo de conferência (`f.url`) deve apontar **obrigatoriamente para a URL original no site da publicação estrangeira**, na língua original em que foi escrita (*inglês, francês, espanhol, etc.*).
   * No rodapé do leitor, o botão deve explicitar o idioma: `Acessar no site original de The Guardian (EN) ↗`.
3. **Filtro de Navegação e Alternância de Eixos:**
   * O topo do boletim deve fornecer a alternância de eixos: `[ Todas ]`, `[ 🇧🇷 Mídia Nacional ]` e `[ 🌍 Mídia Internacional Traduzida ]`, permitindo ao leitor focar no cenário nacional, no panorama global ou em ambos integrados.

---

## 18. Ferramentas e Scripts de Suporte

Ao manipular a base ou realizar manutenções, utilize os utilitários já homologados em `tools/`:

| Script | Função Principal |
| :--- | :--- |
| `tools/varredura_cultural_online.py` | Apuração em tempo real de novos filmes, álbuns e livros via APIs externas (anti-cutoff). |
| `tools/popular_resenhas_completas.py` | Geração de resenhas críticas densas de 4 parágrafos e erradicação de placeholders. |
| `tools/gerar_analises_criticas_2026_11.py` | Geração de 2 a 3 análises críticas de veículos especializados por obra (música, cinema e livros). |
| `tools/atualizar_boletim_prioridades.py` | Reestruturação de edições com a hierarquia estrita de Economia e Política Nacional/Internacional. |
| `tools/aprimorar_leitor_e_analises.py` | Atualização do modo leitor com controle de tamanho, contraste correto no tema escuro e abertura prioritária. |
| `tools/gerar_audio_boletim.py` | Síntese de áudio da notícia completa via `edge-tts` (pt-BR-AntonioNeural) e fallback local. |
| `tools/orquestrador_nuvem.py` / `sentinela_boletim.py` | Orquestração periódica matinal e noturna das edições. |
