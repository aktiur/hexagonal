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
args+=( -rename-fields "code_a2=ISO_A2_EH,code_a3=ISO_A3_EH,nom=NAME,nom_fr=NAME_FR,nom_en=NAME_EN" )
args+=( -rename-fields "population=POP_EST,population_annee=POP_YEAR,type=TYPE")
args+=( -rename-fields "continent=CONTINENT,region_un=REGION_UN,region=SUBREGION" )
args+=( -filter-fields 'code_a2,code_a3,nom,nom_fr,nom_en,population,population_annee,type,continent,region,region_un' )

# Une simplification au kilomètre près est appliquée
args+=( -simplify 20% )

# nettoyage de la topologie
args+=( -clean )

# on importe les lieux peuplés
args+=( -i "${VILLES}")
args+=( -target cities1000 )
args+=( -filter-fields "geoname_id,nom,noms_alt,code_pays_a2,nom,population,fclass,fcode" )
args+=( -filter "population >= 10000" )

# on renomme les deux couches concernées
args+=( -rename-layers "names=pays,lieux" "target=ne_10m_admin_0_countries,cities1000"  )

# La topologie obtenue est enregistrée au format TopoJSON
args+=( -o format=topojson "target=pays,lieux" "id-field=code_a2,geoname_id" "${DST_TOPOLOGY}" )

node_modules/.bin/mapshaper "${args[@]}"
