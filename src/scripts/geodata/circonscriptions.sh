#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

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

# nettoyage de la topologie
# 300m / 6371km * 180 / pi ~= 0.0027
args+=( -clean gap-fill-area=1km2 snap-interval=0.0027 )

# on renomme la couche avant l'export en topojson
args+=( -rename-layers "names=circonscriptions" )

# La topologie obtenue est enregistrée au format TopoJSON
args+=( -o format=topojson "${DST_TOPOLOGY}" )

node_modules/.bin/mapshaper "${args[@]}"
