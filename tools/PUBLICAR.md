# Publicar a Faixa Oculta no GitHub Pages

Passo final das tarefas agendadas, depois de gravar no banco do artefato.

1. Crie uma pasta temporária nova, por exemplo `T=$(mktemp -d)`.
2. Exporte o banco com a ferramenta ArtifactData, action "list", url https://claude.ai/artifact/955jruTrT56VTc12DpqiPS, query {"limit": 1000}, out_dir "$T/dump", uma chamada para cada coleção: `edicoes`, `itens`, `guias`, `semanas`, `cultura`, `dias`, `cine_edicoes`, `cine_itens`, `cine_guias`, `livro_edicoes`, `livro_itens`, `livro_guias`. Para `dias`, que cresce todo dia, use query {"limit": 60, "order_by": {"field": "data", "direction": "desc"}} com action "query" (os últimos 60 boletins bastam no site). Nunca exporte nada de `data/users`.
3. Clone o site: `gh repo clone fabiomg-pixel/faixa-oculta "$T/site"`.
4. Monte a pasta de capas: `mkdir -p "$T/assets" && cp "$T/site/capas/"* "$T/assets/"`. Copie também as capas novas desta execução com o nome `<id do asset>.jpg` (o id é o que vem depois de `/_blob/`).
5. Rode, de dentro de `"$T/site"`: `python3 -I tools/montar_site.py --dump "$T/dump" --assets "$T/assets"`. Não passe `--pagina`: a página do site não muda.
6. Se o script listar ids em `FALTANDO`, baixe cada um com a ferramenta Artifact, action "read", url do artefato, path = o id, out_dir = "$T/assets". Rode o passo 5 de novo.
7. `git add -A`, commit com uma mensagem curta (ex.: "Edição de novembro", "Revista da semana de 25 a 31 out" ou "Boletim de 26/10") terminando com a linha `Co-Authored-By: Claude <noreply@anthropic.com>`, e `git push`.
8. Confira depois de um ou dois minutos: `curl -s https://fabiomg-pixel.github.io/faixa-oculta/data/revista.json` deve conter o id do documento novo.
