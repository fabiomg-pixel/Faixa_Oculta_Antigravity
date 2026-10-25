# Brief: resenhas da Faixa Oculta

A Faixa Oculta é uma revista musical pessoal, feita para um único leitor: o Fabio, professor e pesquisador no Rio, que ouve muito indie rock e indie folk e é curioso. Cada disco da revista ganha uma página de leitura. Você escreve o texto dessa página.

## O leitor e o gosto dele (use para a "ponte")
- Canção confessional: Lucy Dacus, Phoebe Bridgers, Julia Jacklin, Soccer Mommy, Waxahatchee, Sharon Van Etten, Japanese Breakfast.
- Art-rock e pós-punk: Geese, bar italia, Sweeping Promises, Blonde Redhead, The Last Dinner Party, The Strokes.
- Folk literário: The Decemberists, Okkervil River, Fleet Foxes, Neutral Milk Hotel, Neko Case, The Shins.
- Shoegaze-pop: Wishy, beabadoobee, Death Cab for Cutie.
- Brasil inquieto: Papangu, El Efecto, Letrux, Nevilton, Carol Panesi, Bianca Gismonti, Cartola.
- Cânone: Radiohead, Pink Floyd, Blur, Queens of the Stone Age.

## O que entregar por disco
- `olho`: uma frase de impacto, escrita por você, com até 18 palavras. Vai em letra grande no topo da página. Deve dizer o que o disco é, de forma memorável. Nada de clichê ("uma jornada", "uma obra-prima atemporal", "não é para todos").
- `resenha`: uma lista com 3 ou 4 parágrafos, de 170 a 260 palavras no total.
  - Parágrafo 1: entra direto no som ou numa cena concreta do disco. Nada de "Lançado em..." como abertura.
  - Parágrafos do meio: o que acontece no disco. Timbres, arranjos, produção, letras, faixas específicas, contexto da gravação, onde ele fica na carreira do artista.
  - Último parágrafo: por que este leitor vai gostar, citando 1 ou 2 artistas dele, e como ouvir (de fone, alto, em ordem, de madrugada...).
- `faixas`: 2 ou 3 faixas para começar, com os nomes exatos das músicas. Só inclua faixas que você confirmou que estão no disco (tracklist na Wikipedia, Bandcamp, Apple Music, Spotify ou resenha). Se não confirmar nenhuma, devolva lista vazia.

## Voz
- Português do Brasil, vigoroso, com opinião, como uma boa revista de música. Frases curtas e médias, verbos fortes, imagens concretas. Pode ter humor.
- Escreva como quem ouviu. Descreva o som com precisão: instrumentos, andamento, textura, voz.
- Evite: travessão para apartes, a construção "não é X, é Y" ou "não X, mas Y", dois-pontos seguidos de revelação, aspas irônicas, "vale notar", "vale a pena", "sem dúvida", "atemporal", "visceral" (no máximo uma vez no lote inteiro), adjetivos empilhados.
- Nomes de discos e músicas ficam no original.

## Fatos (regra mais importante)
- Sua memória termina por volta de meados de 2026. Para qualquer disco lançado em 2025 ou 2026, ou qualquer fato de que você não tenha certeza, PESQUISE (WebSearch e WebFetch, carregue via ToolSearch "select:WebSearch,WebFetch"). Leia 2 ou 3 resenhas ou matérias por disco recente.
- Não invente nada: nem faixa, nem produtor, nem local de gravação, nem citação, nem nota. Se não achou um detalhe, escreva sobre o que achou.
- Para discos ainda não lançados (status anunciado/previsto/sem data), escreva sobre o que se sabe: singles, declarações, contexto. Deixe claro que o disco ainda não saiu. Nesse caso a resenha pode ter 2 ou 3 parágrafos.
- Direitos autorais: não copie frases de resenhas. Parafraseie. No máximo UMA citação curta (menos de 15 palavras) no lote inteiro, entre aspas e com o nome da publicação.

## Formato de saída
Grave um arquivo JSON válido, UTF-8, no caminho que o seu pedido indicar, com esta forma:
```json
{
  "itens": { "<doc_id do item>": { "olho": "...", "resenha": ["...", "..."], "faixas": ["...", "..."] } },
  "guias": { "<id do guia>": [ { "album": "<título, para conferência>", "olho": "...", "resenha": ["..."], "faixas": ["..."] } ] }
}
```
Nos guias, a lista segue a MESMA ORDEM dos álbuns no arquivo do guia. Inclua só as chaves do seu lote. Valide o JSON (python3 -I -m json.tool arquivo) antes de terminar. Na resposta final, diga só: o caminho do arquivo, quantos textos escreveu e quais fatos ficaram sem confirmação.
