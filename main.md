# Productions


- [Organisation administrative](#organisation-administrative)
  - [Liste des communes](#data/03_main/cog/communes.csv)
- [Élections](#elections)
  - [Liste qualifiée des candidats au premier tour des législatives de 2022](#data/03_main/elections/2022-legislatives-1-candidats.csv)
  - [Liste qualifiée des candidats au second tour des législatives 2022](#data/03_main/elections/2022-legislatives-2-candidats.csv)
  - [2024-legislatives-1-candidats](#data/03_main/elections/2024-legislatives-1-candidats.csv)
  - [2024-legislatives-2-candidats](#data/03_main/elections/2024-legislatives-2-candidats.csv)



<a name="organisation-administrative"></a>
## Organisation administrative

<a name="data/03_main/cog/communes.csv"></a>
### Liste des communes

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/03_main/cog/communes.csv` |
| Format de fichier | text/csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/75/c454596f947d39b09b6163d5bff67f> |




### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_commune</code></td>
    <td><code>code_commune</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_commune</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_region</code></td>
    <td><code>code_region</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_departement</code></td>
    <td><code>code_departement</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_collectivite_departementale</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_arrondissement</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_canton</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_commune_parent</code></td>
    <td><code>code_commune</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_nom</code></td>
    <td><code>entier</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>forme_possessive</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>population_municipale_2022</code></td>
    <td><code>entier</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Code Officiel Géographique 2024](sources.md#data/01_raw/cog.zip)
- [Séries historiques de population par commune (1876 à 2022)](sources.md#data/01_raw/population_municipale.xlsx)


<a name="elections"></a>
## Élections

<a name="data/03_main/elections/2022-legislatives-1-candidats.csv"></a>
### Liste qualifiée des candidats au premier tour des législatives de 2022

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/03_main/elections/2022-legislatives-1-candidats.csv` |
| Format de fichier | text/csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/84/a9b4583202e57f5716bcfb204670ab> |




### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_depot</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant</code></td>
    <td><code>bool</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant_suppleant</code></td>
    <td><code>bool</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_lemonde</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>parti_lemonde</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_legis_2022</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>regroupement_om_legis_2022</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Liste des candidats au premier tour des élections législatives 2022](sources.md#data/01_raw/elections/2022-legislatives-1-candidats.csv)
- [LEGIS-2022 - Codage des nuances politiques des candidats aux élections législatives des 12 et 19 juin 2022](sources.md#data/01_raw/elections/2022-legislatives-nuances-legis-2022.csv)
- [Le Monde — Liste des candidats et leur nuance politique](sources.md#data/01_raw/elections/2022-legislatives-nuances-lemonde.csv)
<a name="data/03_main/elections/2022-legislatives-2-candidats.csv"></a>
### Liste qualifiée des candidats au second tour des législatives 2022

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/03_main/elections/2022-legislatives-2-candidats.csv` |
| Format de fichier | text/csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/c7/75b7da4a1a92fbdc4a3d7e4eb76c5d> |




### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_depot</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant</code></td>
    <td><code>bool</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant_suppleant</code></td>
    <td><code>bool</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_lemonde</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>parti_lemonde</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_legis_2022</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>regroupement_om_legis_2022</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Liste des candidats au deuxième tour des élections législatives de 2022](sources.md#data/01_raw/elections/2022-legislatives-2-candidats.csv)
- [LEGIS-2022 - Codage des nuances politiques des candidats aux élections législatives des 12 et 19 juin 2022](sources.md#data/01_raw/elections/2022-legislatives-nuances-legis-2022.csv)
- [Le Monde — Liste des candidats et leur nuance politique](sources.md#data/01_raw/elections/2022-legislatives-nuances-lemonde.csv)
<a name="data/03_main/elections/2024-legislatives-1-candidats.csv"></a>
### 2024-legislatives-1-candidats

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/03_main/elections/2024-legislatives-1-candidats.csv` |
| Format de fichier | text/csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/2b/8f8aafd90d405b32f87250a52a34ad> |




### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>departement</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_depot</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant</code></td>
    <td><code>bool</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant_suppleant</code></td>
    <td><code>bool</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_lfi</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sensibilite</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Liste des candidats au premier tour des élections législatives 2024](sources.md#data/01_raw/elections/2024-legislatives-1-candidats.csv)
- [Liste des candidats du Nouveau Front populaire et de leur sensibilité par circonscription législative](sources.md#data/01_raw/elections/2024-legislatives-nfp-sensibilites.csv)
- [La France insoumise — Nuançage des candidats des élections législatives 2024](sources.md#data/01_raw/elections/2024-legislatives-nuances-lfi.csv)
<a name="data/03_main/elections/2024-legislatives-2-candidats.csv"></a>
### 2024-legislatives-2-candidats

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/03_main/elections/2024-legislatives-2-candidats.csv` |
| Format de fichier | text/csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/59/0e8d560245a7a23c90005fdc9da4ea> |




### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>departement</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_depot</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant</code></td>
    <td><code>bool</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance_suppleant</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant_suppleant</code></td>
    <td><code>bool</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_lfi</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sensibilite</code></td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Liste des candidats au deuxième tour des élections législatives de 2024](sources.md#data/01_raw/elections/2024-legislatives-2-candidats.csv)
- [Liste des candidats du Nouveau Front populaire et de leur sensibilité par circonscription législative](sources.md#data/01_raw/elections/2024-legislatives-nfp-sensibilites.csv)
- [La France insoumise — Nuançage des candidats des élections législatives 2024](sources.md#data/01_raw/elections/2024-legislatives-nuances-lfi.csv)

