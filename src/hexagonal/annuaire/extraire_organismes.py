import json
import re
import sys
import tarfile
from contextlib import contextmanager
from pathlib import Path

import json_stream
from json_stream.dump import JSONStreamEncoder

PATH_RE = re.compile(r"\./\d{4}-\d{2}-\d{2}_\d{6}-data.gouv_local.json")

ORGANISMES = {
    "mairies": [
        "mairie",
        "paris_mairie",
        "paris_mairie_arrondissement",
        "mairie_com",
    ],
    "epcis": ["epci"],
    "conseils_regionaux": ["cr"],
    "conseils_departementaux": ["cg"],
    "prefectures": [
        "prefecture",
        "paris_ppp",
        "pp_marseille",
        "prefecture_region",
        "sous_pref",
    ],
}


@contextmanager
def ouvrir_pour_ecrire(out_dir: Path):
    fds = {}
    mapping = {}
    try:
        for extraction, pivots in ORGANISMES.items():
            fds[extraction] = (out_dir / f"{extraction}.json").open("w")
            for pivot in pivots:
                mapping.setdefault(pivot, []).append(fds[extraction])

        yield mapping
    finally:
        for fd in fds.values():
            fd.close()


def extraire(archive: tarfile.TarFile, out_path):
    while info := archive.next():
        if PATH_RE.match(info.path):
            break
    else:
        raise FileNotFoundError("Pas possible de trouver le fichier.")

    with (
        archive.extractfile(info) as organismes_fd,
        ouvrir_pour_ecrire(out_path) as out_fds,
    ):
        service = json_stream.load(organismes_fd)["service"]

        for organisme in service.persistent():
            pivots = [p["type_service_local"] for p in organisme["pivot"]]
            fds = {fd for p in pivots for fd in out_fds.get(p, ())}
            for fd in fds:
                json_out = json.dumps(
                    organisme, cls=JSONStreamEncoder, separators=(",", ":")
                )
                fd.write(f"{json_out}\n")


def run():
    archive_path, out_dir = sys.argv[1:]
    out_dir = Path(out_dir)

    with tarfile.open(archive_path) as archive:
        extraire(archive, out_dir)


if __name__ == "__main__":
    run()
