#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

SRC_GEOMETRY="$1"
DST_TOPOLOGY="$2"
DST_DIR="$(dirname "DST_TOPOLOGY")"

mkdir -p "$DST_DIR"

args=()

args+=( -i "${SRC_GEOMETRY}" )

# on renomme les champs et on ne garde que ceux qui sont pertinents
args+=( -rename-fields "code_commune=INSEE_COM,code_arrondissement=INSEE_ARR" )
args+=( -rename-fields "code_canton=INSEE_CAN,code_departement=INSEE_DEP" )
args+=( -rename-fields "code_region=INSEE_REG,siren_epci=SIREN_EPCI" )
args+=( -rename-fields "nom=NOM,population=POPULATION" )
args+=( -filter-fields "code_commune,code_arrondissement,code_canton,code_departement,code_region,siren_epci,nom,population" )

# on renomme la couche avant l'export en topojson
args+=( -rename-layers "names=communes" )

# La topologie obtenue est enregistrée au format TopoJSON
args+=( -o format=topojson "${DST_TOPOLOGY}" )

node_modules/.bin/mapshaper "${args[@]}"
