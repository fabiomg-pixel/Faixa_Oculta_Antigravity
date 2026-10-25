"""Two-way bridge between the Radar cultural artifact and Faixa Oculta.

Usage:
  python3 -I tools/sync_radar.py --radar DIR [--estado FILE] --saida DIR

--radar   ArtifactData export (list with out_dir) of the radar, https://claude.ai/artifact/TyWptAvjgeNdjpqoKie5hb:
          DIR/eventos, DIR/retorno, DIR/idas, DIR/rodadas, DIR/playlists (optional).
--estado  Fabio's private Faixa Oculta marks, exported from data/users/me/estado (optional).
--saida   Writes:
            agenda_atual.json   Body for Faixa Oculta's single doc `agenda/atual`: events, feedback, the
                                "Fomos" diary, last radar round and playlists. Kept under 230 KB by dropping
                                metrics and reviews if needed.
            radar_retorno.json  {retorno_id: body} for marks made in Faixa Oculta (keys "radar:<retorno id>")
                                that are newer than the radar's own decision. Before writing each one, read the
                                radar doc with ArtifactData get to learn its version and pass it as if_version
                                (omit if_version only when the doc does not exist yet).
Never writes the radar's `idas`, `notas` or `perfil`: they are Fabio's.
"""
import argparse, glob, json, os

DECISOES = {"quero", "talvez", "fui", "nao"}
LIMITE = 230_000


def ler(d):
    out = {}
    for f in sorted(glob.glob(os.path.join(d, "*.json"))):
        doc = json.load(open(f, encoding="utf-8"))
        if isinstance(doc, dict) and "data" in doc and "version" in doc:
            doc = doc["data"]
        out[os.path.basename(f)[:-5]] = doc
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--radar", required=True)
    ap.add_argument("--estado")
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()
    os.makedirs(a.saida, exist_ok=True)

    eventos = ler(os.path.join(a.radar, "eventos"))
    retorno = ler(os.path.join(a.radar, "retorno"))
    idas = ler(os.path.join(a.radar, "idas"))
    rodadas = sorted(ler(os.path.join(a.radar, "rodadas")).values(), key=lambda r: r.get("em", ""))
    playlists = ler(os.path.join(a.radar, "playlists")).get("atual")

    agenda = {
        "eventos": [{**d, "id": k} for k, d in eventos.items()],
        "retorno": {k: {kk: vv for kk, vv in d.items() if kk in ("decisao", "em", "nota")} for k, d in retorno.items()},
        "idas": [{**d, "id": k} for k, d in idas.items()],
        "rodada": rodadas[-1] if rodadas else None,
        "playlists": playlists,
        "radar_url": "https://claude.ai/artifact/TyWptAvjgeNdjpqoKie5hb",
    }
    for campo in ("reviews", "metricas", "fonte"):
        if len(json.dumps(agenda, ensure_ascii=False).encode()) <= LIMITE:
            break
        for e in agenda["eventos"]:
            e.pop(campo, None)
            for p in e.get("destaques", []) or []:
                p.pop(campo, None)
    tamanho = len(json.dumps(agenda, ensure_ascii=False).encode())
    json.dump(agenda, open(os.path.join(a.saida, "agenda_atual.json"), "w", encoding="utf-8"), ensure_ascii=False)

    vindos = {}
    if a.estado and os.path.exists(a.estado):
        est = json.load(open(a.estado, encoding="utf-8"))
        if isinstance(est, dict) and "data" in est and "version" in est:
            est = est["data"]
        marcas, quando = est.get("marcas", {}) or {}, est.get("marcas_em", {}) or {}
        for chave, valor in marcas.items():
            if not chave.startswith("radar:") or valor not in DECISOES:
                continue
            rid = chave[len("radar:"):]
            em = quando.get(chave, "")
            atual = retorno.get(rid, {})
            if atual.get("decisao") == valor or (atual.get("em") and em and atual["em"] >= em):
                continue
            vindos[rid] = {**atual, "decisao": valor, "em": em or atual.get("em", ""), "origem": "faixa-oculta"}
    json.dump(vindos, open(os.path.join(a.saida, "radar_retorno.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(f"agenda/atual: {len(agenda['eventos'])} eventos, {len(agenda['idas'])} idas, {tamanho / 1000:.0f} KB; "
          f"retornos vindos da revista: {len(vindos)}")
    if tamanho > 250_000:
        raise SystemExit("agenda/atual passou de 250 KB: reduza os campos antes de gravar")


if __name__ == "__main__":
    main()
