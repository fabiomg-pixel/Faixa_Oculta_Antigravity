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
> A experiência de áudio foi concebida para audição contínua e imersiva de fim de semana. Prévias truncadas de 30 segundos inviabilizam o produto.

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
  * Deve constituir uma **leitura rica e profunda de fim de semana**.
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
  * Modo Leitor limpo na íntegra para todas as notas, sem anúncios, sem popups e sem redirecionamentos externos indesejados.

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

## 9. Boletim em Áudio · Transcrição Narrada das Notícias do Dia

* **Geração Automática de Áudio:** Sempre que uma nova edição do boletim diário for gerada (manhã ou noite), o script `tools/gerar_audio_boletim.py` deve ser acionado.
* **Motor de Voz Neural:** Utiliza `edge-tts` com a voz `pt-BR-AntonioNeural` (taxa de locução natural de rádio/podcast), gerando um arquivo de áudio de alta fidelidade em `audios/boletim_<dia>.mp3` (~5 minutos).
* **Interface do Usuário:** O topo da aba "Hoje" exibe o card `.d-audio-card` com:
  * Player de áudio embutido para reprodução imediata do briefing do dia.
  * Botão de narração ao vivo integrada via **Web Speech API** (`window.speechSynthesis`), permitindo ouvir qualquer boletim diretamente pelo navegador com a voz do sistema.

---

## 10. Varredura Online Obrigatória e Dados Contemporâneos (Anti-Cutoff)

> [!IMPORTANT]
> A Faixa Oculta NUNCA deve utilizar a memória interna estática (cutoff 2024) do modelo de IA para inventar ou reciclar safras culturais contemporâneas. Toda e qualquer edição cultural DEVE ser apurada por varredura eficiente online.

* **Cinema em Cartaz:** Os filmes na seção "Em cartaz ou estreando nos próximos dias" DEVEM ser lançamentos reais contemporâneos ao calendário da edição (novembro de 2026), apurados via festivais (Festival do Rio, Mostra SP), distribuidoras brasileiras e programações das salas de cinema (CineSesc, Estação Net, Salas de Arte, IMAX). Filmes de safras passadas (ex: 2024) devem figurar em seções de acervo/streaming/achados e NUNCA como "em cartaz".
* **Livros Novos:** Lançamentos editoriais devem ser apurados online junto às editoras brasileiras (Companhia das Letras, Todavia, Record, Zahar, Bazar do Tempo) e portais literários (*PublishNews*, *Quatro Cinco Um*).
* **Música e Álbuns:** Discos novos contemporâneos devem ser apurados via portais e APIs de música (Pitchfork, Billboard Brasil, Rolling Stone, Deezer, iTunes).
* **Varredor Automático:** O script `tools/varredura_cultural_online.py` integra a orquestração do sistema (`tools/orquestrador_nuvem.py` e `tools/sentinela_boletim.py`), garantindo que 100% dos dados e das capas oficiais sejam sincronizados ao vivo das APIs externas.

---

## 11. Perfil Editorial Personalizado do Leitor (Fabio Gomes / UFRJ)

A curadoria da Faixa Oculta foi desenhada especificamente para seu leitor-alvo, professor e pesquisador de biofísica na UFRJ. Todos os pilares editoriais devem refletir esse horizonte:

1. **Ciência, Saúde Pública & Amazônia:** Pesquisas de ponta em biofísica, imunometabolismo, arboviroses e vetores; mobilização acadêmica (SBPC, ABC, UFRJ, Fiocruz, FAPESP); clima, sustentabilidade e a Amazônia (Davi Kopenawa, Sumaúma).
2. **Política & Diplomacia:** Geopolítica internacional e política externa brasileira (Itamaraty, CEBRI, multilateralismo, BRICS, transição global); política nacional plural, reformas institucionais, STF e memória histórica democrática.
3. **Ficção Científica (Sci-Fi) & Fantasia:** Hard sci-fi, especulação sobre inteligência artificial, colapso tecnológico e ecologia (Editora Aleph, Morro Branco, Todavia); alta fantasia mitológica, cosmologias indígenas e realismo mágico de autor.
4. **Música:** Indie rock/folk e canção confessional (Lucy Dacus, Phoebe Bridgers, Julia Jacklin, Soccer Mommy, Sharon Van Etten); art-rock e pós-punk (Geese, bar italia); shoegaze-pop (Wishy, beabadoobee); folk literário (The Decemberists, Okkervil River, Greg Freeman); rock e vanguarda brasileira (Papangu, Letrux, El Efecto, Clau Aniz, Marcelo Cabral); cânone moderno (Radiohead, Blur, Queens of the Stone Age).
5. **Cinema:** Cinema autoral e de festivais internacionais (Cannes, Veneza, Festival do Rio, Mostra SP); cinema brasileiro independente (Gabriel Martins, Kleber Mendonça Filho, Filmes de Plástico, Pedro Freire); documentários reflexivos e cosmologias visuais.

---

## 12. Prioridade Editorial do Boletim Diário & Modo Leitor

1. **Hierarquia Estrita do Boletim:**
   - **1º e 2º:** Economia & Contas Públicas (corte de gastos, juros Selic, câmbio, inflação, reforma tributária).
   - **3º e 4º:** Política Nacional & Instituições (STF, Congresso, governabilidade).
   - **5º:** Diplomacia & Geopolítica Internacional (eleições EUA, BRICS, G20, Itamaraty, conflitos globais).
   - **6º:** Ciência, Saúde Pública & Universidades (UFRJ, Fiocruz, SBPC, FAPESP).
   - **7º:** Clima & Amazônia (secas, queimadas, COP30).
2. **Estrutura Completa de Cada Nota:**
   - `texto_completo`: 3 a 4 parágrafos densos disponíveis diretamente no Modo Leitor.
   - `resumo_visoes`: Síntese contrastando as diferentes linhas editoriais e posições políticas da imprensa.
   - `aprofundamento`: Contexto histórico e próximos passos a acompanhar.
   - `fontes`: Múltiplas fontes com links diretos para o site original.
3. **Modo Leitor Imersivo:**
   - Controles de tipografia (Serif, Sans, Mono), tamanho (A- / A+) e tema (Papel, Escuro, Branco) com persistência em `localStorage`.
   - 100% dos lançamentos com `resenha` crítica completa de 3-4 parágrafos. É proibido exibir placeholders como 'O texto completo entra na próxima atualização.'.
