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

10. **Perfil de Interesses e Separação Editorial (Interesse Pessoal vs. Rotina de Trabalho):**
   - O leitor busca a Faixa Oculta pelo seu **interesse pessoal, cívico e cultural**, e **NÃO como extensão de trabalho ou de laboratório**.
   - **No 'Hoje' (Boletim Diário):** Noticiário estritamente **CLÁSSICO DE PRIMEIRA LINHA** (Economia, Política Nacional, Internacional/Geopolítica e Sociedade). É TERMINANTEMENTE PROIBIDO incluir rotinas de trabalho/laboratório (editais de biotérios/compras, feiras universitárias de recrutamento de estudantes, notas departamentais).
   - **Na 'Semana' (Revista da Semana):** Espaço para grandes ensaios reflexivos, ideias, debates de fronteiras do conhecimento e filosofia da ciência como leitura e deleite intelectual de fim de semana.
   - **Música & Cinema (Mensal / Agenda):** Indie rock, pós-punk, vanguarda brasileira, cinema autoral e independente.

11. **Prioridade Editorial e Volume do Boletim Diário ('Hoje' - Notícias Clássicas):**
   - O boletim diário (manhã e noite) DEVE conter obrigatoriamente **AO MENOS 10 NOTÍCIAS DENSAS NACIONAIS + 10 INTERNACIONAIS TRADUZIDAS** (20 a 22 matérias por dia).
   - As notícias duras e estruturais de Economia (corte de gastos, juros Selic, câmbio/dólar, dívida pública, reforma tributária, emprego, indústria), Política Nacional (STF, Congresso, governabilidade) e Diplomacia / Política Internacional (geopolítica global, eleições EUA, BRICS, G20, Itamaraty, conflitos) são a espinha dorsal e DEVEM compor a totalidade do boletim diário.
   - Cada nota do boletim DEVE contar com: múltiplas fontes plurais, síntese das diferentes visões da imprensa (`resumo_visoes`), reportagem completa de 3 a 4 parágrafos para o Modo Leitor (`texto_completo`), contexto de aprofundamento (`aprofundamento`) e link direto para o site original.

12. **Zero Placeholders de Resenha ("O texto completo entra na próxima atualização"):**
   - É estritamente proibido exibir a frase 'O texto completo entra na próxima atualização.' no leitor. 100% dos lançamentos, álbuns, filmes e livros devem ter o array `resenha` com 3 a 4 parágrafos densos de crítica aprofundada, além de ficha técnica, faixas/capítulos e recepção crítica.

13. **Modo Leitor Imersivo com Controles Tipográficos e Temas Contrastantes:**
   - O Modo Leitor (`#texto` e `#leitura`) deve obrigatoriamente fornecer controles interativos de família de fonte (Serifada / Sans-serif / Monospaçada), tamanho de fonte (A- / A+) e tema de contraste (Papel / Escuro / Branco), com preferências salvas em `localStorage`.
   - No tema Escuro, o fundo escuro (`#161513`) DEVE obrigatoriamente vir acompanhado de texto claro e legível (`#EAE5DB`), sendo proibido texto preto invisível. O controle de tamanho deve atuar diretamente sobre os parágrafos (`p`) para surtir efeito imediato.

14. **Navegação Temporal Limpa e Notícias Salvas:**
   - No topo do boletim ("Hoje"), substituir o acúmulo de pílulas/botões de datas por um menu dropdown (`<select>`) elegante com as edições agrupadas por mês via `<optgroup>`, acompanhado do botão `🔖 Notícias salvas` para resgate imediato de artigos marcados para ler depois.

15. **Áudio Completo das Notícias (Narração Integral):**
   - O áudio narrado do boletim (`tools/gerar_audio_boletim.py`) e a síntese de voz integrada DEVEM narrar o texto completo das reportagens (`texto_completo`), proporcionando um jornal falado / podcast aprofundado e completo (~5-8 minutos), sem resumos telegráficos rasos.

16. **Prioridade do Modo Leitor e 2 a 3 Análises Críticas Especializadas:**
   - Ao clicar em notícias ou obras culturais, a plataforma DEVE abrir prioritariamente o Modo Leitor interno antes de qualquer redirecionamento para o site original (o link externo fica acessível dentro do leitor).
   - Todo material de mídia cultural (álbuns, filmes e livros) DEVE carregar 2 a 3 análises críticas aprofundadas extraídas de publicações especializadas (*Pitchfork, The Guardian, RogerEbert.com, The New York Times, Quatro Cinco Um, etc.*), com notas, citações e parágrafos de ensaio crítico.

17. **Equivalência da Mídia Internacional com Tradução Integral e Paridade Mandatória:**
   - O boletim diário (manhã e noite) DEVE incorporar obrigatoriamente um material equivalente de cobertura dos principais veículos da mídia internacional (*The New York Times, The Guardian, Financial Times, Le Monde, El País, Scientific American, MIT Technology Review, BBC World, Al Jazeera*).
   - O piso mínimo obrigatório é de **ao menos 10 notícias de Mídia Nacional + 10 notícias de Mídia Internacional traduzidas na íntegra** (20 a 22 matérias por dia), com o atributo `"escopo": "nacional"` ou `"escopo": "internacional"` em 100% dos itens.
   - Nas caixas/cartões (`.d-nota`) e no Modo Leitor (`#texto`), todo o material internacional DEVE ser traduzido com rigor analítico para o português (título, resumo, texto completo de 3 a 4 parágrafos, pontos centrais e citações).
   - Os links para consulta externa (`f.url`) DEVEM direcionar obrigatoriamente para a matéria original no idioma de origem (*inglês, francês, espanhol, etc.*).
   - A interface deve oferecer alternância fluida entre os eixos de apuração (`Todas`, `🇧🇷 Mídia Nacional` e `🌍 Mídia Internacional Traduzida`).

18. **Especificação Detalhada de Bandas nas Pequenas Casas (Agenda Cultural do Rio):**
   - É estritamente proibido cadastrar eventos guarda-chuva ou genéricos sem atrações específicas, bem como omitir turnês e lançamentos relevantes agendados para o dia ou fim de semana.
   - Cada casa de shows da cena alternativa (Audio Rebel, Saloon 79, Estúdio Hanoi, Garage Grindhouse, Circo Voador, Bar Bukowski) DEVE trazer os shows desmembrados em `destaques` com as bandas identificadas em `artistas: ["Banda A", "Banda B"]` (ex.: *Flerte Flamingo com VALLADA na Audio Rebel*, *Ploho no Garage Grindhouse*).
   - 100% das bandas devem estar cadastradas em `agenda.artistas.mapa` (Spotify ID) e `agenda.artistas.youtube` (YouTube ID/Playlist) para permitir execução imediata no player sem cortes de 30 segundos (`Ouvir aqui`) e links diretos para os aplicativos.
   - Cada show deve detalhar data futura real no mês, horários, ingressos, resenha crítica (`porque`) e citações de veículos musicais especializados.


19. **Botão e Diálogo de Convite Compartilhável para Cada Evento:**
   - Todo card de evento (`cardEvento`) e todo show individual (`agDestaques`) DEVE fornecer o botão `✉️ Convidar`.
   - Ao clicar, abre o modal `#dlg-convite` contendo: cabeçalho com selo e chamada de convite, grade prática (Onde com Google Maps, Quando com datas/horas, Ingressos com valores e link de compra), sinopse curatorial, line-up de bandas com player de áudio e links externos, resenha crítica, trailer/vídeo e botões de compartilhamento (Copiar Link com deep link `#convite=<id>`, envio formatado para WhatsApp e compartilhamento nativo).
   - A plataforma DEVE abrir o convite automaticamente caso a página seja acessada com `#convite=<id>` ou `?convite=<id>`.

