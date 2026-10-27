# Rotinas de conteúdo da Faixa Oculta

Roteiro das rotinas na nuvem que alimentam o site além do boletim diário (`tools/BOLETIM.md`). A fonte de verdade é o
banco do artefato https://claude.ai/artifact/955jruTrT56VTc12DpqiPS (ferramenta ArtifactData); o site no GitHub Pages
é atualizado no fim por `tools/PUBLICAR.md`. O leitor é o Fabio, professor de biofísica na UFRJ, no Rio. Português do Brasil.

| Rotina | Quando | O que grava |
|---|---|---|
| Revista da semana | domingo, 8h23 | `semanas/<domingo de hoje>` |
| Música do mês | dia 1, 14h12 | `edicoes/AAAA-MM`, `itens/*`, `guias/*` |
| Cinema do mês | dia 3, 14h12 | `cine_edicoes/AAAA-MM`, `cine_itens/*`, `cine_guias/*` |
| Livros do mês | dia 5, 14h12 | `livro_edicoes/AAAA-MM`, `livro_itens/*`, `livro_guias/*` |
| Complemento quinzenal | dia 15, 14h12 | itens novos nas edições do mês de música e cinema |

## 0. Regras comuns
- `git -C /home/user/faixa-oculta pull origin main` antes de tudo. Data de hoje com `TZ=America/Sao_Paulo date +%F`.
- **Modelo é a edição anterior.** Antes de escrever, exporte com ArtifactData (action "list", out_dir) a coleção da
  rotina e leia o documento mais recente do mesmo tipo: os campos, as seções e o tamanho dos textos seguem o que está
  lá. Não invente campo novo; a página só desenha os que conhece.
- **Se o documento desta rodada já existir, não reescreva.** Só complete o que faltar e publique se o site estiver atrás.
- **Nada repetido.** Obra (disco, filme, série, livro) que já saiu em qualquer edição anterior não volta, a não ser num
  guia em que ela seja indispensável, e então com texto novo.
- Fatos: os briefs `tools/BRIEF_MUSICA.md`, `BRIEF_CINEMA.md` e `BRIEF_LIVROS.md` mandam. Pesquise tudo que for de
  2025–2026 ou incerto (WebSearch; páginas com WebFetch ou, se ele der erro de DNS, `curl -sL --compressed --max-time 30`
  simples). Não contorne bloqueio de site: 403, captcha ou paywall, use outra fonte. Nada inventado; o que não se
  confirmou fica de fora e vai para o relatório.
- Voz: a dos briefs. Sem travessão para apartes, sem "não é X, é Y", sem dois-pontos de revelação.
- Direitos autorais: paráfrase sempre; no máximo uma citação curta (menos de 15 palavras) por lote, com a fonte.
- Lote grande: divida por seção entre subagentes (ferramenta Agent), cada um com o brief inteiro, o caminho de saída e a
  lista de obras já publicadas; confira os JSON que voltarem antes de gravar.
- Gravação: ArtifactData "batch" em lotes de até 50, `if_version` em documento que já existe. Valide cada JSON com
  `python3 -I -m json.tool` antes.
- Nunca escreva em `data/users/`, e nunca crie, altere ou apague idas, notas ou o perfil do Radar por conta própria.
- Commits terminam com `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## 1. Capas e players
- Filmes, séries e livros: `python3 -I tools/capas_obras.py <pasta> <lote.json>` (pôster pela Wikipedia ou iTunes, capa
  de livro pelo iTunes). Disco: iTunes Search (`https://itunes.apple.com/search?term=<artista álbum>&entity=album&country=br`),
  aceite só o resultado com mesmo artista e álbum, e troque `100x100bb` por `600x600bb` no `artworkUrl100`.
- Suba as imagens para o artefato: ferramenta Artifact, `url` do artefato, `asset: true`, `file_paths` (até 25 por
  chamada). Cada resultado traz a url do asset; grave no item `"capa": "/_blob/<id>"` e copie o arquivo para
  `$T/assets/<id>.jpg` no passo 5 do PUBLICAR. Sem capa confirmada, deixe o campo de fora (a página desenha um selo).
- Discos: `spotify_id` pelo conector Spotify (search, só álbum do mesmo artista) e `youtube_list` (playlist `OLAK5uy_`
  do álbum, conferida com o oEmbed do YouTube como no passo 3d2 do PUBLICAR). YouTube Music é o player principal, Spotify (barra compacta)
  o de reserva; Apple só como link (`apple_url`) quando não houver os outros.
- Filmes e séries: `imdb` (id `tt…`, conferido na página do IMDb ou da Wikipedia) para o botão do Stremio.

## 2. Revista da semana (domingo)
- doc_id = a data de hoje (domingo); `inicio` = domingo anterior, `fim` = ontem (sábado).
- Base: os boletins da semana (`dias`, query por `data` entre `inicio` e `fim`, manhã e noite) e as leituras ligadas a
  eles. Apure de novo os temas centrais: o que mudou até sábado, como cada lado cobriu.
- Forma (a de `semanas/2026-10-25`): `titulo`; `panorama` (3 parágrafos sobre o padrão da semana);
  `temas` (8 a 10, cada um com `id`, `editoria`, `titulo`, `linha_fina`, `resumo` [3 a 4 parágrafos], `cobertura`
  [4 a 6 veículos de perfis diferentes com `fonte`, `perfil`, `enfoque`, `url`], `vieses`, `o_que_falta`, `perguntas`
  [3 a 4], `por_que_importa`, `aprofundar` [3 a 5 livros, artigos, podcasts ou documentários reais, com `tipo`,
  `titulo`, `autor`, `ano`, `nota`, `url` quando houver]); `fora_do_radar` (4 a 6 assuntos que a cobertura ignorou,
  com `id`, `editoria`, `titulo`, `texto`, `ler` [{`fonte`, `titulo`, `url`}]).
- Cubra Brasil, Mundo, Ciência e universidades, Clima e Tecnologia; Rio quando houver.
- Faça as leituras limpas das URLs de `cobertura` que ainda não estão em `leituras` (`tools/LEITURAS.md`, tipo "noticia").
- Commit "Revista da semana de DD a DD/MM".

## 3. Música do mês (dia 1)
- doc_id `AAAA-MM`; `numero` = anterior + 1; `mes` "Novembro de 2026"; `data` = hoje.
- Perfil do Fabio: pelo conector Spotify (mais ouvidos recentes, playlists do mês) atualize `perfil` e `habitos` só com
  o que a ferramenta mostrar; se o conector falhar, repita o perfil anterior e diga isso no `fontes_perfil`.
- Seções (as da edição anterior): `radar` (lançamentos do mês anterior e do começo deste, 8 a 10), `descobertas` (discos
  de 2024–2026 que ele talvez não conheça, 8 a 10), `brasil` (4 a 6), `breve` (anunciados, 3 a 5). Dois ou três `guias`
  novos (7 discos cada, `tipo` "Seleção temática", "Gênero", "Cena" ou "Artista"), em temas que conversam com o perfil e
  ainda não foram feitos.
- `itens/<artista-album>` (slug minúsculo com hífens) com `edicao`, `secao`, `ordem` e os campos do item anterior.
- `layout` alterna seções e guias, como na edição anterior. `manchete` e `editorial` escritos por último, a partir do
  que entrou.
- Playlist do mês: conector Spotify, generate_playlist "Faixa Oculta nº N · <Mês> AAAA" com as faixas recomendadas dos
  itens, na ordem da revista; grave `playlist` {nome, url}. Se falhar, deixe de fora e registre.
- Commit "Música: edição de <mês>".

## 4. Cinema do mês (dia 3) e Livros do mês (dia 5)
- doc_id da edição `AAAA-MM`, itens `AAAA-MM--<slug do título>`, guias `guia-cine-<slug>` / `guia-livro-<slug>`.
- Cinema, seções da edição anterior: `cartaz` (em cartaz ou estreando no Brasil), `series` (minisséries fechadas),
  `achados`, `brasil`, `pop`, `breve`; 20 a 25 itens e 2 guias. `onde` conferido no JustWatch Brasil ou equivalente na
  semana da rodada.
- Livros, seções: `lancamentos`, `brasil`, `ideias` (não ficção), `achados`; 15 a 18 itens e 2 guias. Edição brasileira,
  editora e páginas conferidas. Campo `downloads` só com cópias gratuitas autorizadas (regra no brief); nunca acervo pirata.
- Commit "Cinema: edição de <mês>" ou "Livros: edição de <mês>".

## 5. Complemento quinzenal (dia 15)
- Não cria edição. Acrescenta à edição de música do mês 5 a 8 discos lançados desde o dia 1 (seção `radar`) e à de
  cinema 3 a 5 estreias da quinzena no Brasil (seções `cartaz` ou `series`), com `ordem` seguindo a última do mês.
- Se as edições do mês ainda não existirem (rotina do dia 1 ou 3 falhou), faça primeiro a que faltar, pelos passos 3 e 4.
- Commit "Complemento da quinzena de <mês>".

## 6. Publicar e relatar
Siga `tools/PUBLICAR.md` inteiro (inclui a ponte com o Radar e as capas novas em `$T/assets`). Depois do push, confira
o `data/revista.json` do site. Relatório curto: o que entrou (quantos itens e guias, títulos dos guias), o que ficou sem
confirmação e por quê, e o hash do commit.
