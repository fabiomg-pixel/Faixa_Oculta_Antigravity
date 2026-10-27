# Leituras limpas da Faixa Oculta: regras

A Faixa Oculta é a revista pessoal do Fabio (professor de biofísica na UFRJ, Rio). Ela mostra notícias e críticas em "formato limpo": em vez de mandar o leitor para o site, abre um RESUMO NOSSO do texto, com o link para o original. A página é pública, por isso NUNCA reproduzimos o texto: só paráfrase.

## Formato de cada leitura (um objeto JSON)
{
  "url": "URL exata da página que você abriu (sem parâmetros utm)",
  "fonte": "nome do veículo, ex.: Pitchfork, Folha de S.Paulo, The Guardian",
  "titulo": "título original da matéria ou crítica",
  "autor": "nome de quem assina, se houver",
  "data": "AAAA-MM-DD da publicação, se aparecer",
  "tipo": "noticia" ou "review",
  "ref": "(só em reviews) o campo ref da obra, exatamente como na lista",
  "ordem": "(só em reviews) 1, 2, 3 na ordem em que devem aparecer",
  "nota": "(só em reviews) a nota dada pelo veículo, como aparece: \"8.3\", \"4/5\", \"★★★★\"; omita se não houver",
  "resumo": ["2 a 4 parágrafos em português do Brasil, 140 a 260 palavras no total"],
  "pontos": ["opcional: 2 a 4 tópicos curtos com os fatos, números ou argumentos centrais"],
  "citacao": "opcional: UMA frase curta do original, com menos de 15 palavras, entre as melhores do texto, no idioma original"
}

## Regras
- Abra cada página de verdade (WebFetch ou `curl -sL --max-time 30 URL` simples, sem User-Agent falso nem contorno de bloqueio). Só escreva sobre o que leu. Se a página estiver fechada por paywall, fora do ar ou não abrir, NÃO escreva a leitura: registre em "pulados" com o motivo. Nunca invente conteúdo, autor, data ou nota.
- Paráfrase sempre, com palavras próprias. Nada de copiar frases ou parágrafos, nem traduzir trechos literalmente. No máximo a "citacao" curta.
- Notícia: o resumo diz o que aconteceu, com fatos, números, atores e o enquadramento daquele veículo (quem ele ouviu, o que destacou). Neutro.
- Review: o resumo diz o que o crítico pensa da obra, com os argumentos dele, as faixas/cenas/capítulos que cita, o que elogia e o que critica, e o veredito. Deixe claro que é a opinião do crítico ("para a Pitchfork...", "o crítico acha...").
- Voz: clara e direta; frases curtas. Evite travessão para apartes, "não é X, é Y", dois-pontos seguidos de revelação, "vale notar", "sem dúvida".
- Saída: um arquivo JSON { "leituras": [...], "pulados": [ { "url" ou "ref", "motivo" } ] } no caminho indicado. Valide o JSON com python3 antes de terminar.

## Gravar no banco
1. Junte as leituras num arquivo `{ "leituras": [...], "pulados": [...] }`.
2. Rode `python3 -I tools/leituras.py --saida <pasta> <arquivo.json>` (do repositório clonado). Ele grava um JSON por leitura com o nome `<doc_id>.json` (o id sai da URL) e avisa o que quebra as regras: corrija antes de gravar.
3. Grave na coleção `leituras` do artefato https://claude.ai/artifact/955jruTrT56VTc12DpqiPS com ArtifactData action "batch" (até 50 por chamada), op "set", collection "leituras", doc_id = nome do arquivo sem .json, file_path = o arquivo. Para um id que já existe, faça get antes e passe if_version (ou pule: a leitura já está lá).
4. A página liga sozinha: notícias pelo `url` (o mesmo url da fonte no boletim ou na revista da semana) e críticas pelo `ref` (o id do documento do disco, filme ou livro; nos guias, `<id do guia>~<índice>`).
