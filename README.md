# Faixa Oculta (Antigravity)

Revista pessoal de música, notícias, filmes e livros. Site: https://fabiomg-pixel.github.io/Faixa_Oculta_Antigravity/

O conteúdo nasce no artefato do claude.ai (https://claude.ai/artifact/955jruTrT56VTc12DpqiPS), que é a fonte de verdade. Este repositório é a cópia estática publicada no GitHub Pages, com player embutido do Spotify (ou do Apple Music quando o disco não está no Spotify).

- `pagina.html`: a página como publicada no claude.ai. A mesma página lê o banco do artefato no claude.ai e `data/revista.json` aqui.
- `index.html`: gerado a partir de `pagina.html`.
- `data/revista.json`: exportação das coleções `edicoes`, `itens`, `guias`, `semanas` e `cultura`.
- `capas/`: capas, nomeadas pelo id do asset no artefato.
- `tools/montar_site.py`: gera `index.html`, `data/` e `capas/` a partir de uma exportação do banco.

As tarefas agendadas do Claude atualizam o artefato e depois rodam `tools/montar_site.py` e fazem push aqui.
