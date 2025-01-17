from pathlib import Path, PurePath

import click
import py7zr

EXTRAIRE = {
    "COMMUNE": "communes",
    "COMMUNE_ASSOCIEE_OU_DELEGUEE": "communes_deleguees",
    "ARRONDISSEMENT_MUNICIPAL": "arrondissements_municipaux",
}


@click.command()
@click.argument(
    "chemin_archive", type=click.Path(exists=True, file_okay=True, dir_okay=False)
)
@click.argument(
    "dest_dir", type=click.Path(file_okay=False, dir_okay=True, path_type=Path)
)
def nettoyer(chemin_archive, dest_dir):
    with py7zr.SevenZipFile(chemin_archive, "r") as archive:
        paths = [PurePath(name) for name in archive.namelist()]

        for prefix, dest_name in EXTRAIRE.items():
            geometry_files = [p for p in paths if p.stem == prefix]
            bufs = archive.read([str(p) for p in geometry_files])
            for p in geometry_files:
                with open(dest_dir / f"{dest_name}{p.suffix}", "wb") as dest:
                    dest.write(bufs[str(p)].getvalue())
                archive.reset()


if __name__ == "__main__":
    nettoyer()
