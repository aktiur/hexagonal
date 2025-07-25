import zipfile
from io import BytesIO
from pathlib import Path

import click
import geopandas as gpd
import pandas as pd
import pyzstd
from shapely.geometry.point import Point

INT = pd.Int64Dtype()
STR = pd.StringDtype()
FLOAT = pd.Float64Dtype()

NAMES = {
    "geoname_id": INT,
    "nom": STR,
    "asciiname": None,
    "noms_alt": STR,
    "latitude": FLOAT,
    "longitude": FLOAT,
    "fclass": STR,
    "fcode": STR,
    "code_pays_a2": STR,
    "cc2": None,
    "a1_code": STR,
    "a2_code": STR,
    "a3_code": STR,
    "a4_code": STR,
    "population": INT,
    "elevation": INT,
    "digital_elevation_model": INT,
    "timezone": STR,
    "mod_date": STR,
}


@click.command()
@click.argument("source", type=click.Path(exists=True, dir_okay=False, readable=True))
@click.argument("dest", type=click.Path(dir_okay=False, writable=True, path_type=Path))
def extract_geonames(source, dest):
    with zipfile.ZipFile(source) as archive:
        with archive.open("cities1000.txt") as fd:
            villes = pd.read_csv(
                fd,
                sep="\t",
                names=list(NAMES),
                usecols=[c for c, t in NAMES.items() if t],
                dtype={c: t for c, t in NAMES.items() if t},
                header=None,
                index_col="geoname_id",
            )

    villes["coordinates"] = [
        Point(x, y)
        for x, y in zip(villes["longitude"], villes["latitude"], strict=False)
    ]
    del villes["longitude"]
    del villes["latitude"]

    villes["noms_alt"] = villes["noms_alt"].str.split(",")

    villes = gpd.GeoDataFrame(villes, geometry="coordinates", crs="EPSG:4326")

    dest.parent.mkdir(parents=True, exist_ok=True)

    # pour une raison inconnue, geopandas accepte d'écrire vers un buffer mais pas vers
    # un fichier ouvert…
    buffer = BytesIO()
    villes.to_file(buffer, driver="GeoJSON")

    with pyzstd.open(dest, "wb") as fd:
        fd.write(buffer.getvalue())


if __name__ == "__main__":
    extract_geonames()
