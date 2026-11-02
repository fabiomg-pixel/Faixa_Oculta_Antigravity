# Regras do Projeto · Faixa Oculta

Este repositório contém a revista cultural e boletim diário **Faixa Oculta**.
Ao executar tarefas neste repositório, obedeça rigorosamente às diretrizes consolidadas na skill `.agents/skills/faixa-oculta-curadoria/SKILL.md`:

## Regras Críticas Invioláveis:

1. **Zero Capas Sintéticas / Zero Fallbacks Pretos:**
   - Nunca use `fallback_capa_elegante()` nem gere imagens sólidas pretas com texto desenhado via PIL.
   - 100% dos lançamentos, livros, filmes, álbuns, matérias de capa e itens dos "Retratos de Autor" (essenciais e influenciados) DEVEM ter capas oficiais de alta resolução obtidas via Deezer API (música), Wikimedia / Wikipedia API (cinema) ou Open Library / iTunes API (livros).
   - Use User-Agent `FaixaOcultaBot/1.0 (contact@faixaoculta.com)` ao consultar APIs.

2. **Player de Áudio sem Cortes de 30 Segundos:**
   - O player embed padrão é YouTube Music (`youtube-nocookie.com/embed/...`).
   - A playlist do mês deve ser encadeada em URL real contínua (`watch_videos?video_ids=...`) e a lista na interface deve ficar dentro de um bloco retrátil `<details>`.
   - Inclua sempre botões para abrir nos apps externos (`Spotify ↗` e `YT Music ↗`).

3. **Integrações de Consumo Cultural:**
   - Cinema: Botão direto para Stremio (`stremio:///detail/movie/...` e web) e JustWatch.
   - Livros: Links para Google Play Livros e Estante Virtual, com editoras e tradutores brasileiros.

4. **Feedback de Gosto Cultural (Sim / Não / Já Aproveitado):**
   - Todos os cartões de Música, Cinema, Livros e Agenda devem exibir os botões de afinidade (`👍 Sim`, `👎 Não`, `✓ Já aproveitado`).

5. **Densidade Editorial e Síntese Plural:**
   - Revista Semanal (rodada na quinta à noite): Síntese de fim de semana densa e plural cruzando 6-8 veículos de diferentes linhas políticas (*Folha, O Globo, g1, BBC Brasil, Poder360, Metrópoles, Valor, EBC*).
   - Cultura Mensal (todo dia 01): Safra completa de Música (35+ álbuns), Cinema (25+ filmes) e Livros (20+ obras).
   - Agenda do Rio: Foco em rock, música independente e cena underground (Botafogo, Estúdio Hanoi, Circo Voador, Tijuca, Centro).
   - Retrato de Autor (Grande Destaque do Mês): Análise aprofundada da trajetória, card da obra em foco com player, catálogo essencial e árvore de influências com explicação conceitual detalhada.

6. **Identidade Visual "Elenco Refinado":**
   - Papel creme impresso, tipografia sóbria e grafite nobre. Sem botões plásticos neon.
   - O banner de capas do topo permanece fixo e visível em todos os filtros.

7. **Prioridade Local:**
   - O sentinela local no Mac tem prioridade para rodar as edições. O GitHub Actions atua como salvaguarda na nuvem.

8. **Boletim em Áudio das Notícias do Dia:**
   - Todo boletim diário deve contar com transcrição em áudio narrado (`tools/gerar_audio_boletim.py`), disponibilizado via player embutido no card `.d-audio-card` e narração integrada via Web Speech API.

9. **Varredura Online Obrigatória e Dados 100% Contemporâneos (Anti-Cutoff):**
   - É estritamente proibido utilizar a memória interna estática (cutoff 2024) do modelo de IA para inventar ou reciclar safras culturais contemporâneas.
   - Todo e qualquer filme em cartaz nos cinemas, álbum recém-lançado e livro novo no Brasil DEVE ser apurado através de varredura eficiente online (`tools/varredura_cultural_online.py`, APIs do iTunes, Deezer, Wikipedia e portais de estreias/festivais).
   - Filmes e obras de safras passadas (ex: 2024) devem figurar em seções de acervo/streaming/achados e NUNCA como 'em cartaz ou estreando nos cinemas' em edições de anos posteriores.

10. **Perfil de Interesses e Pilares de Rastreamento (Fabio Gomes / UFRJ):**
   - **Ciência, Saúde & Universidades:** Biofísica, imunometabolismo, arboviroses, UFRJ, Fiocruz, FAPESP, SBPC, Amazônia, clima e saúde pública.
   - **Política & Diplomacia:** Política externa brasileira, Itamaraty, geopolítica global, multilateralismo, BRICS, STF, Congresso e teoria política.
   - **Ficção Científica (Sci-Fi) & Fantasia:** Hard sci-fi, IA, distopias sociais e especulativas (Editoras Aleph, Morro Branco, Todavia), alta fantasia mitológica e realismo mágico de autor.
   - **Música:** Indie rock/folk, canção confessional (Lucy Dacus, Phoebe Bridgers, Soccer Mommy), art-rock/pós-punk (Geese, bar italia), shoegaze (Wishy), vanguarda e rock brasileiro (Papangu, Letrux, El Efecto), cânone (Radiohead, QOTSA).
   - **Cinema:** Cinema de autor contemporâneo (festivais de Cannes, Mostra SP, Festival do Rio) e cinema brasileiro independente (Gabriel Martins, Kleber Mendonça Filho, Filmes de Plástico).
