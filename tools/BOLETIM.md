# Boletim diário da Faixa Oculta

Roteiro da rotina na nuvem que roda todo dia de manhã. O boletim é o documento `dias/<AAAA-MM-DD>` do artefato
https://claude.ai/artifact/955jruTrT56VTc12DpqiPS (a fonte de verdade); depois o site no GitHub Pages é atualizado.

O leitor é o Fabio, professor de biofísica na UFRJ, no Rio. Português do Brasil.

## 1. Ver o que já existe
- `date` com TZ=America/Sao_Paulo dá a data de hoje (o doc_id).
- ArtifactData action "query", collection `dias`, query {"limit": 2, "order_by": {"field": "data", "direction": "desc"}},
  com out_dir. Se o boletim de hoje já existir, não reescreva: pule para o passo 4 só se o site estiver atrás.
- Leia o boletim anterior para continuar as histórias (o que mudou desde ontem) e não repetir notas sem novidade.

## 2. Apurar
- Use WebSearch (mode "extended" para os temas centrais, "standard" para checagens) para achar as matérias e
  WebFetch para abrir as principais e conferir números e falas. Se o WebFetch der erro de DNS (já aconteceu nesta
  nuvem), abra com `curl -sL --max-time 30 URL` simples, uma URL por vez, e confira o link canônico da página baixada.
  Não contorne bloqueios de site (nada de User-Agent falso nem truques): se um veículo responder 403, captcha ou
  paywall, use outro.
- Cubra, nesta ordem de peso: Brasil (política, economia), Mundo, Ciência e universidades, Clima, Tecnologia.
  Rio de Janeiro quando houver algo relevante para quem mora lá.
- Cada fato precisa de fonte. Números, nomes e datas só entram se aparecerem numa fonte; quando as fontes divergem,
  diga isso ou use o número mais conservador. Se um número é de antes de um evento (pré-mercado, apuração parcial),
  diga isso no texto.
- Para cada nota, 2 a 4 fontes de perfis diferentes (agência, jornal de centro, veículo à direita, veículo à esquerda,
  imprensa internacional, especializado). O `enfoque` diz o que aquele veículo destacou.

## 3. Escrever o documento
Confira nas páginas abertas os números e as falas de cada nota antes de gravar; o que só aparece em resumo de busca
vai atribuído ao veículo ("segundo a Reuters...").

```json
{
 "data": "AAAA-MM-DD",
 "titulo": "manchete do dia, até ~70 caracteres",
 "resumo_dia": "4 a 7 frases curtas com o essencial",
 "notas": [
  {
   "id": "slug-curto",
   "editoria": "Política | Economia | Mundo | Ciência | Clima | Tecnologia | Rio | Cultura",
   "titulo": "título da nota",
   "texto": "90 a 160 palavras, só fatos com fonte",
   "por_que_importa": "1 ou 2 frases",
   "fontes": [ { "fonte": "Veículo", "perfil": "ex.: jornal de referência, centro", "enfoque": "o que destacou", "url": "https://..." } ]
  }
 ],
 "agenda": [ { "quando": "hoje, 10h", "o_que": "o que acontece" } ]
}
```
- 7 a 10 notas. Agenda com 4 a 6 itens dos próximos dias e semanas.
- Voz: clara e direta, frases curtas. Evite travessão para apartes, "não é X, é Y", dois-pontos seguidos de revelação,
  "vale notar", "sem dúvida". Paráfrase sempre; nada copiado das fontes.
- Valide o JSON com python3 e grave com ArtifactData action "set", collection `dias`, doc_id = data, file_path.

## 4. Publicar
Siga `tools/PUBLICAR.md` inteiro (ponte com o Radar, exportação, `montar_site.py`, commit "Boletim de DD/MM", push).
Antes de publicar, faça as leituras limpas das fontes do boletim (`tools/LEITURAS.md`, tipo "noticia", campo `url`
igual ao do boletim): abra cada página com WebFetch ou curl simples; as que recusarem acesso vão para "pulados". Grave na coleção
`leituras` e só então exporte e publique. Se nenhum dos dois funcionar nesta execução, pule as leituras e registre.

## 5. Relatório final
Uma resposta curta: manchete, número de notas, o que foi pulado e por quê, e o hash do commit.
