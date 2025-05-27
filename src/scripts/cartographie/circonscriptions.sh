#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

. "$(dirname -- "${BASH_SOURCE[0]}")/drom_idf.sh"

SRC_GEOMETRY="$1"
DST_TOPOLOGY="$2"
DST_DIR="$(dirname "DST_TOPOLOGY")"

mkdir -p "$DST_DIR"

args=()

args+=( -i "${SRC_GEOMETRY}" )

# on crée le code_circonscription, on renomme le code département et on ne garde que ça
args+=( -rename-fields "code_departement=dep" )
args+=( -each 'code_circonscription = code_departement + "-" + id_circo.slice(-2)' )

args+=( -filter-fields 'code_circonscription,code_departement' )


# On projette en webmercator (EPSG:3857), format généralement utilisé pour la carto web
args+=( -proj crs=epsg:3857 )

# nettoyage de la topologie
args+=( -clean gap-fill-area=1km2 snap-interval=300 )

# On applique les transformations à l'outremer et à l'Île-de-France
deplacer_drom args
deplacer_idf args

# Une simplification au kilomètre près est appliquée
args+=( -simplify resolution=1000 )

# on renomme la couche avant l'export en topojson
args+=( -rename-layers "names=circonscriptions_legislatives" )

# La topologie obtenue est enregistrée au format TopoJSON
args+=( -o format=topojson "${DST_TOPOLOGY}" )

node_modules/.bin/mapshaper "${args[@]}"
