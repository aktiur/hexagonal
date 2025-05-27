#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob


PAYS="$1"
VILLES="$2"
DST_TOPOLOGY="$3"
DST_DIR="$(dirname "DST_TOPOLOGY")"

mkdir -p "$DST_DIR"

args=()

# on commence par les pays
args+=( -i "${PAYS}" )
args+=( -target ne_10m_admin_0_countries )

# on crée le code_circonscription, on renomme le code département et on ne garde que ça
args+=( -rename-fields "code_a2=ISO_A2,code_a3=ISO_A3,nom=NAME,nom_fr=NAME_FR,nom_en=NAME_EN" )
args+=( -rename-fields "population=POP_EST,population_annee=POP_YEAR,type=TYPE")
args+=( -filter-fields 'code_a2,code_a3,nom,nom_fr,nom_en,population,population_annee,type' )

# Une simplification au kilomètre près est appliquée
args+=( -simplify 20% )

# nettoyage de la topologie
args+=( -clean )

# on importe les lieux peuplés
args+=( -i "${VILLES}")
args+=( -target ne_10m_populated_places )
args+=( -rename-fields "nom=NAME,nom_fr=NAME_FR,nom_en=NAME_EN,code_pays_a2=ISO_A2" )
args+=( -rename-fields "type=FEATURECLA,population_min=POP_MIN,population_max=POP_MAX,population_autre=POP_OTHER" )
args+=( -filter-fields "nom,code_pays_a2,type,nom,nom_fr,nom_en,type,population_min,population_max,population_autre" )

# on renomme les deux couches concernées
args+=( -rename-layers "names=pays,lieux" "target=ne_10m_admin_0_countries,ne_10m_populated_places"  )

# La topologie obtenue est enregistrée au format TopoJSON
args+=( -o format=topojson "target=pays,lieux" "${DST_TOPOLOGY}" )

node_modules/.bin/mapshaper "${args[@]}"
