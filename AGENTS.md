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
