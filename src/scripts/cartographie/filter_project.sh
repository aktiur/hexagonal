#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob


SRC_TOPOLOGY="$1"
DST_TOPOLOGY="$2"
NAME="$3"
FILTER="$4"
PROJECTION="$5"

DST_DIR="$(dirname "DST_TOPOLOGY")"

mkdir -p "$DST_DIR"

args=()

args+=( -i "${SRC_TOPOLOGY}" )

args+=( -rename-layers "${NAME}" )

args+=( -filter "$FILTER" )

# on applique la projection
args+=( -proj "$PROJECTION" )

# on simplifie à la centaine de mètres
args+=( -simplify planar interval=100m  )

# La topologie obtenue est enregistrée au format TopoJSON
args+=( -o format=topojson "${DST_TOPOLOGY}" )

node_modules/.bin/mapshaper "${args[@]}"
