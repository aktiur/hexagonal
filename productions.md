# Productions

<a name="data/02_clean/annuaire/conseils_departementaux.csv"></a>
## Conseils départementaux

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/annuaire/conseils_departementaux.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/53/09c03e311afead3d83056b4b8688f5> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>id</code></td>
    <td>Identifiant unique</td>
    <td><code>str</code></td>
    <td>Un identifiant interne utilisé par l&#39;annuaire de l&#39;administration.
</td>
  </tr>
<tr>
    <td><code>code_commune</code></td>
    <td>Code commune</td>
    <td><code>code_commune</code></td>
    <td>Le code INSEE de la commune où se trouve le conseil départemental.
</td>
  </tr>
<tr>
    <td><code>siret</code></td>
    <td>SIRET</td>
    <td><code>str</code></td>
    <td>Le code SIRET du Conseil départemental
</td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>emails</code></td>
    <td>emails</td>
    <td><code>str</code></td>
    <td>Les adresses emails indiquées dans l&#39;annuaire, séparées par un saut de ligne simple.
</td>
  </tr>
<tr>
    <td><code>adresse_physique</code></td>
    <td>Adresse</td>
    <td><code>str</code></td>
    <td>Adresse physique complète
</td>
  </tr>
<tr>
    <td><code>adresse_postale</code></td>
    <td>Adresse postale</td>
    <td><code>str</code></td>
    <td>L&#39;adresse postale, si elle est différente de l&#39;adresse physique (boîte postale, par exemple).
</td>
  </tr>
<tr>
    <td><code>telephone</code></td>
    <td>telephone</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>coordonnees</code></td>
    <td>coordonnees</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_accessibilite</code></td>
    <td>type_accessibilite</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>details_accessibilite</code></td>
    <td>details_accessibilite</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>ouverture</code></td>
    <td>ouverture</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Base de données locales de l&#39;annuaire de l&#39;administration](sources.md#data/01_raw/annuaire/annuaire.tar.bz2)
<a name="data/02_clean/annuaire/mairies.csv"></a>
## Liste des mairies

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/annuaire/mairies.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/b8/6ed082ddc5e2897e5fefc593380e34> |

Ce jeu de données extraits de l&#39;annuaire administratif comporte une entrée pour chaque mairie
française.


### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>id</code></td>
    <td>id</td>
    <td><code>str</code></td>
    <td>Un identifiant interne à l&#39;annuaire de l&#39;administration
</td>
  </tr>
<tr>
    <td><code>code_commune</code></td>
    <td>code_commune</td>
    <td><code>code_commune</code></td>
    <td>Le code INSEE de la commune à laquelle appartient la mairie
</td>
  </tr>
<tr>
    <td><code>siret</code></td>
    <td>siret</td>
    <td><code>str</code></td>
    <td>Le numéro de SIRET de cette mairie
</td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>emails</code></td>
    <td>emails</td>
    <td><code>str</code></td>
    <td>Les adresse emails de contact pour cette mairie
</td>
  </tr>
<tr>
    <td><code>adresse_physique</code></td>
    <td>adresse_physique</td>
    <td><code>str</code></td>
    <td>L&#39;adresse physique de la mairie.
</td>
  </tr>
<tr>
    <td><code>adresse_postale</code></td>
    <td>adresse_postale</td>
    <td><code>str</code></td>
    <td>L&#39;adresse postale de la mairie, si elle est différente de l&#39;adresse physique (par exemple boîte postale)
</td>
  </tr>
<tr>
    <td><code>telephone</code></td>
    <td>telephone</td>
    <td><code>str</code></td>
    <td>Numéros de téléphone de contact pour cette mairie.
</td>
  </tr>
<tr>
    <td><code>coordonnees</code></td>
    <td>coordonnees</td>
    <td><code>str</code></td>
    <td>Coordonnées géographiques de cette mairie, selon le système WGS84, au format &lt;code&gt;longitude,latitude&lt;/code&gt;
</td>
  </tr>
<tr>
    <td><code>type_accessibilite</code></td>
    <td>type_accessibilite</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>details_accessibilite</code></td>
    <td>details_accessibilite</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>ouverture</code></td>
    <td>ouverture</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Base de données locales de l&#39;annuaire de l&#39;administration](sources.md#data/01_raw/annuaire/annuaire.tar.bz2)
<a name="data/02_clean/assemblee_nationale/affiliations.csv"></a>
## Affiliation des députés à un groupe parlementaire

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/assemblee_nationale/affiliations.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/6f/f8030680e92e49af80135ef63208e5> |

Ce fichier comporte une ligne pour chaque affiliation d&#39;un député à un groupe parlementaire, à partir de la
XIème législature.


### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>id_personne</code></td>
    <td>Identifiant député·e</td>
    <td><code>str</code></td>
    <td>L&#39;identifiant unique de la personne utilisé par l&#39;Assemblée nationale
</td>
  </tr>
<tr>
    <td><code>id_groupe</code></td>
    <td>Identifiant groupe parlementaire</td>
    <td><code>str</code></td>
    <td>L&#39;identifiant unique du groupe parlementaire concerné.
</td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td>Le prénom de la personne concernée.
</td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td>L
</td>
  </tr>
<tr>
    <td><code>abreviation_groupe</code></td>
    <td>abreviation_groupe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>legislature</code></td>
    <td>legislature</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut</code></td>
    <td>date_debut</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_fin</code></td>
    <td>date_fin</td>
    <td><code>date</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Historique des députés](sources.md#data/01_raw/assemblee-nationale.zip)
<a name="data/02_clean/assemblee_nationale/deputes.csv"></a>
## deputes

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/assemblee_nationale/deputes.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/71/e5e846805211992d03976a5dcd2af2> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>id_personne</code></td>
    <td>id_personne</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>civilite</code></td>
    <td>civilite</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>ville_naissance</code></td>
    <td>ville_naissance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>departement_naissance</code></td>
    <td>departement_naissance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>legislatures</code></td>
    <td>legislatures</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td>profession</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>csp_agregee</code></td>
    <td>csp_agregee</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>csp</code></td>
    <td>csp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Historique des députés](sources.md#data/01_raw/assemblee-nationale.zip)
<a name="data/02_clean/assemblee_nationale/groupes.csv"></a>
## groupes

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/assemblee_nationale/groupes.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/3c/3b5cdbb812161dee7ae3a72b59b05f> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>id_groupe</code></td>
    <td>id_groupe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>legislature</code></td>
    <td>legislature</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>abrege</code></td>
    <td>abrege</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>abreviation</code></td>
    <td>abreviation</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut</code></td>
    <td>date_debut</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_fin</code></td>
    <td>date_fin</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>position</code></td>
    <td>position</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>preseance</code></td>
    <td>preseance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Historique des députés](sources.md#data/01_raw/assemblee-nationale.zip)
<a name="data/02_clean/assemblee_nationale/mandats.csv"></a>
## Liste des mandats des député·es

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/assemblee_nationale/mandats.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/fe/9e69d85766d7ba0dfb3af30d46358b> |

Ce fichier liste l&#39;ensemble des mandats de député·es depuis la 12ème législature.

Chaque mandat correspond à une période uninterrompue pendant laquelle une personne est restée députée, pour une
législature donnée. La réélection d&#39;un·e député·e correspond donc à un nouveau mandat.

De la même façon, le cas d&#39;une personne qui perd son statut de député·e avant de le récupérer sera matérialisé
par deux mandats différents.


### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>id_mandat</code></td>
    <td>Identifiant du mandat</td>
    <td><code>str</code></td>
    <td>L&#39;identifiant unique du mandat.
Il débute par le préfixe &#34;PM&#34;.
</td>
  </tr>
<tr>
    <td><code>id_personne</code></td>
    <td>Identifiant de la personne</td>
    <td><code>str</code></td>
    <td>L&#39;identifiant unique de la personne dépositaire du mandat.
Il débute par le préfixe &#34;PA&#34;.
</td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>Prénom de la personne</td>
    <td><code>str</code></td>
    <td>Le prénom de la personne dépositaire du mandat
</td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>Nom de famille de la personne</td>
    <td><code>str</code></td>
    <td>Le nom de famille de la personne dépositaire du mandat.
</td>
  </tr>
<tr>
    <td><code>legislature</code></td>
    <td>legislature</td>
    <td><code>int</code></td>
    <td>Le numéro de la législature dans le cadre de laquelle se déroule le mandat.
</td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>suppleante</code></td>
    <td>suppleante</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut</code></td>
    <td>date_debut</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_fin</code></td>
    <td>date_fin</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>cause_debut_mandat</code></td>
    <td>cause_debut_mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>cause_fin_mandat</code></td>
    <td>cause_fin_mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>place</code></td>
    <td>place</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Historique des députés](sources.md#data/01_raw/assemblee-nationale.zip)
<a name="data/02_clean/cog/com.csv"></a>
## com

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/cog/com.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/eb/6adcfa64aec45b1de8aa99714ba201> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_departement</code></td>
    <td>code_departement</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_nom</code></td>
    <td>type_nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>article</code></td>
    <td>article</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>charniere</code></td>
    <td>charniere</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Code Officiel Géographique 2024](sources.md#data/01_raw/cog.zip)
<a name="data/02_clean/cog/communes.csv"></a>
## communes

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/cog/communes.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/00/a2dc59d3571339c3c6fffbc5ec881d> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_commune</code></td>
    <td>code_commune</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_commune</code></td>
    <td>type_commune</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_region</code></td>
    <td>code_region</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_departement</code></td>
    <td>code_departement</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_collectivite_departementale</code></td>
    <td>code_collectivite_departementale</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_arrondissement</code></td>
    <td>code_arrondissement</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_canton</code></td>
    <td>code_canton</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_commune_parent</code></td>
    <td>code_commune_parent</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_nom</code></td>
    <td>type_nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>article</code></td>
    <td>article</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>charniere</code></td>
    <td>charniere</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Code Officiel Géographique 2024](sources.md#data/01_raw/cog.zip)
<a name="data/02_clean/cog/communes_com.csv"></a>
## communes_com

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/cog/communes_com.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/c7/ff14be8f5a8d3737c343146cd27a27> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_commune</code></td>
    <td>code_commune</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_commune</code></td>
    <td>type_commune</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_departement</code></td>
    <td>code_departement</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_nom</code></td>
    <td>type_nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>article</code></td>
    <td>article</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>charniere</code></td>
    <td>charniere</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Code Officiel Géographique 2024](sources.md#data/01_raw/cog.zip)
<a name="data/02_clean/cog/communes_historiques.csv"></a>
## communes_historiques

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/cog/communes_historiques.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/2b/61bf920c2ecae8c56bf84a2cdfefca> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_commune</code></td>
    <td>code_commune</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_nom</code></td>
    <td>type_nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>article</code></td>
    <td>article</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>charniere</code></td>
    <td>charniere</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut</code></td>
    <td>date_debut</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_fin</code></td>
    <td>date_fin</td>
    <td><code>date</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Code Officiel Géographique 2024](sources.md#data/01_raw/cog.zip)
<a name="data/02_clean/cog/departements.csv"></a>
## departements

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/cog/departements.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/ac/09c997f36bf573bcd937ba62cc3768> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_departement</code></td>
    <td>code_departement</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_region</code></td>
    <td>code_region</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_chef_lieu</code></td>
    <td>code_chef_lieu</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_nom</code></td>
    <td>type_nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Code Officiel Géographique 2024](sources.md#data/01_raw/cog.zip)
<a name="data/02_clean/elections/2012-presidentielle-bureau_de_vote.csv"></a>
## 2012-presidentielle-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2012-presidentielle-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/dd/1602eeb3aef940be98b633715f98c0> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_tour</code></td>
    <td>numero_tour</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>canton</code></td>
    <td>canton</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats des deux tours de l&#39;élection présidentielle de 2012](sources.md#data/01_raw/elections/2012-presidentielle-bureau_de_vote.csv)
<a name="data/02_clean/elections/2014-europeenne-bureau_de_vote.csv"></a>
## 2014-europeenne-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2014-europeenne-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/86/a735fc59b31007870567dceaa7fc80> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_tour</code></td>
    <td>numero_tour</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats de l&#39;élection européenne de 2014 par bureau de vote](sources.md#data/01_raw/elections/2014-europeenne-bureau_de_vote.csv)
<a name="data/02_clean/elections/2017-legislatives-1-bureau_de_vote.csv"></a>
## 2017-legislatives-1-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2017-legislatives-1-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/d5/c03e199a19ce3fae248e724c51015c> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des élections législatives de 2017 par bureau de vote](sources.md#data/01_raw/elections/2017-legislatives-1-bureau_de_vote.csv)
<a name="data/02_clean/elections/2017-legislatives-2-bureau_de_vote.csv"></a>
## 2017-legislatives-2-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2017-legislatives-2-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/62/41616b484fc40fc433485de522348e> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour des élections législatives de 2017 par bureau de vote](sources.md#data/01_raw/elections/2017-legislatives-2-bureau_de_vote.csv)
<a name="data/02_clean/elections/2017-presidentielle-1-bureau_de_vote.csv"></a>
## 2017-presidentielle-1-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2017-presidentielle-1-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/34/16fd57375d7f99c435b0dcb104dfcc> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour de l&#39;élection présidentielle de 2017 par bureau de vote](sources.md#data/01_raw/elections/2017-presidentielle-1-bureau_de_vote.csv)
<a name="data/02_clean/elections/2017-presidentielle-2-bureau_de_vote.csv"></a>
## 2017-presidentielle-2-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2017-presidentielle-2-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/77/a8f040c5aa96fd0eff112314a5b611> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour de l&#39;élection présidentielle de 2017 par bureau de vote](sources.md#data/01_raw/elections/2017-presidentielle-2-bureau_de_vote.csv)
<a name="data/02_clean/elections/2019-europeenne-bureau_de_vote.csv"></a>
## 2019-europeenne-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2019-europeenne-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/de/7bd1fc201314a1c62b74d026e960e3> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_court</code></td>
    <td>liste_court</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_long</code></td>
    <td>liste_long</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats de l&#39;élection européenne de 2019 par bureau de vote](sources.md#data/01_raw/elections/2019-europeenne-bureau_de_vote.csv)
<a name="data/02_clean/elections/2020-municipales-1-bureau_de_vote.csv"></a>
## 2020-municipales-1-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2020-municipales-1-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/90/c03f20ba4e73fd7f5df4ca7fab2fa9> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_long</code></td>
    <td>liste_long</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des municipales 2020 par bureau de vote](sources.md#data/01_raw/elections/2020-municipales-1-bureau_de_vote_avant_correction.csv)
<a name="data/02_clean/elections/2020-municipales-2-bureau_de_vote.csv"></a>
## 2020-municipales-2-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2020-municipales-2-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/73/fec91deb9763538a41cfd4f09c1c61> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_long</code></td>
    <td>liste_long</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour des municipales 2020 par bureau de vote](sources.md#data/01_raw/elections/2020-municipales-2-bureau_de_vote.csv)
<a name="data/02_clean/elections/2021-departementales-1-bureau_de_vote.csv"></a>
## 2021-departementales-1-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2021-departementales-1-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/00/8adcda97cc2def4029909c41ff91ce> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des élections départementales de 2021 par bureau de vote](sources.md#data/01_raw/elections/2021-departementales-1-bureau_de_vote.csv)
<a name="data/02_clean/elections/2021-departementales-2-bureau_de_vote.csv"></a>
## 2021-departementales-2-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2021-departementales-2-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/c9/ceef10e419a0c0cda2fcb5a1203a9f> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour des élections départementales de 2021 par bureau de vote](sources.md#data/01_raw/elections/2021-departementales-2-bureau_de_vote.csv)
<a name="data/02_clean/elections/2021-regionales-1-bureau_de_vote.csv"></a>
## 2021-regionales-1-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2021-regionales-1-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/f6/abf9e73855205186c075c143261ad8> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_court</code></td>
    <td>liste_court</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_long</code></td>
    <td>liste_long</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des élections régionales de 2021 par bureau de vote](sources.md#data/01_raw/elections/2021-regionales-1-bureau_de_vote.csv)
<a name="data/02_clean/elections/2021-regionales-2-bureau_de_vote.csv"></a>
## 2021-regionales-2-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2021-regionales-2-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/a9/ce190eac00088f2d08512d368dfe8a> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_court</code></td>
    <td>liste_court</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_long</code></td>
    <td>liste_long</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour des élections régionales de 2021 par bureau de vote](sources.md#data/01_raw/elections/2021-regionales-2-bureau_de_vote.csv)
<a name="data/02_clean/elections/2022-legislatives-1-bureau_de_vote.csv"></a>
## 2022-legislatives-1-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-legislatives-1-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/f3/4b36691d23b2f1d4644a0d80fa2870> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des élections législatives de 2022 par bureau de vote](sources.md#data/01_raw/elections/2022-legislatives-1-bureau_de_vote.csv)
<a name="data/02_clean/elections/2022-legislatives-1-candidats.csv"></a>
## 2022-legislatives-1-candidats

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-legislatives-1-candidats.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/88/9400dc852d825436e365d6d2d2f025> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_depot</code></td>
    <td>numero_depot</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td>profession</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant</code></td>
    <td>sortant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe_suppleant</code></td>
    <td>sexe_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_suppleant</code></td>
    <td>nom_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom_suppleant</code></td>
    <td>prenom_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance_suppleant</code></td>
    <td>date_naissance_suppleant</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant_suppleant</code></td>
    <td>sortant_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_lemonde</code></td>
    <td>nom_lemonde</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_lemonde</code></td>
    <td>nuance_lemonde</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>parti_lemonde</code></td>
    <td>parti_lemonde</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_legis_2022</code></td>
    <td>nuance_legis_2022</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>regroupement_om_legis_2022</code></td>
    <td>regroupement_om_legis_2022</td>
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
<a name="data/02_clean/elections/2022-legislatives-1-circonscription.csv"></a>
## 2022-legislatives-1-circonscription

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-legislatives-1-circonscription.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/8f/ee40705cb4d868b49095ad8b269abd> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des élections législatives de 2022 par circonscription législative](sources.md#data/01_raw/elections/2022-legislatives-1-circonscription.csv)
<a name="data/02_clean/elections/2022-legislatives-2-bureau_de_vote.csv"></a>
## 2022-legislatives-2-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-legislatives-2-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/5c/1a2bc94cdcd65377fd0eab32bc62d1> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour des élections législatives de 2022 par bureau de vote](sources.md#data/01_raw/elections/2022-legislatives-2-bureau_de_vote.csv)
<a name="data/02_clean/elections/2022-legislatives-2-candidats.csv"></a>
## 2022-legislatives-2-candidats

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-legislatives-2-candidats.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/dd/9c912a3b89e7bb3d5214f747b9e02d> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_depot</code></td>
    <td>numero_depot</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td>profession</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant</code></td>
    <td>sortant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe_suppleant</code></td>
    <td>sexe_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_suppleant</code></td>
    <td>nom_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom_suppleant</code></td>
    <td>prenom_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance_suppleant</code></td>
    <td>date_naissance_suppleant</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant_suppleant</code></td>
    <td>sortant_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_lemonde</code></td>
    <td>nom_lemonde</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_lemonde</code></td>
    <td>nuance_lemonde</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>parti_lemonde</code></td>
    <td>parti_lemonde</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_legis_2022</code></td>
    <td>nuance_legis_2022</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>regroupement_om_legis_2022</code></td>
    <td>regroupement_om_legis_2022</td>
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
<a name="data/02_clean/elections/2022-legislatives-2-circonscription.csv"></a>
## 2022-legislatives-2-circonscription

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-legislatives-2-circonscription.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/c8/7a80ab75c40d53824137394a34ddb2> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour des élections législatives de 2022 par circonscription](sources.md#data/01_raw/elections/2022-legislatives-2-circonscription.csv)
<a name="data/02_clean/elections/2022-presidentielle-1-bureau_de_vote.csv"></a>
## 2022-presidentielle-1-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-presidentielle-1-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/14/dfa90d1a3b3099cb01817dabc28228> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour de l&#39;élection présidentielle 2022 par bureau de vote](sources.md#data/01_raw/elections/2022-presidentielle-1-bureau_de_vote.csv)
<a name="data/02_clean/elections/2022-presidentielle-1-circonscription.csv"></a>
## 2022-presidentielle-1-circonscription

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-presidentielle-1-circonscription.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/89/56622be06f89a7ae975a292aad6a16> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour de l&#39;élection présidentielle 2022 par circonscription législative](sources.md#data/01_raw/elections/2022-presidentielle-1-circonscription.csv)
<a name="data/02_clean/elections/2022-presidentielle-2-bureau_de_vote.csv"></a>
## 2022-presidentielle-2-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-presidentielle-2-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/67/2d58404e5c7fd088c0a172e089ba34> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour de l&#39;élection présidentielle 2022 par bureau de vote](sources.md#data/01_raw/elections/2022-presidentielle-2-bureau_de_vote.csv)
<a name="data/02_clean/elections/2022-presidentielle-2-circonscription.csv"></a>
## 2022-presidentielle-2-circonscription

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-presidentielle-2-circonscription.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/c3/763d2f15d06df46858af5d74ebd310> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour de l&#39;élection présidentielle 2022 par circonscription législative](sources.md#data/01_raw/elections/2022-presidentielle-2-circonscription.csv)
<a name="data/02_clean/elections/2022-presidentielle-parrainages.csv"></a>
## 2022-presidentielle-parrainages

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2022-presidentielle-parrainages.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/c1/b409e872d55b1ca3ea1e547862bd2a> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>mandat</code></td>
    <td>mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription_mandat</code></td>
    <td>circonscription_mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>departement_mandat</code></td>
    <td>departement_mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>candidat</code></td>
    <td>candidat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_publication</code></td>
    <td>date_publication</td>
    <td><code>date</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Liste des parrainages validés par le Conseil constitutionnel](sources.md#data/01_raw/elections/2022-presidentielle-parrainages.csv)
<a name="data/02_clean/elections/2024-europeenne-bureau_de_vote.csv"></a>
## 2024-europeenne-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-europeenne-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/a8/8ff891a256710c3facdb42fa931630> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_court</code></td>
    <td>liste_court</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_long</code></td>
    <td>liste_long</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats des élections européennes 2024 par bureau de vote](sources.md#data/01_raw/elections/2024-europeenne-bureau_de_vote.csv)
<a name="data/02_clean/elections/2024-europeenne-circonscription.csv"></a>
## 2024-europeenne-circonscription

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-europeenne-circonscription.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/0e/85b5bd51c38919008d4a92f0155a61> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_court</code></td>
    <td>liste_court</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>liste_long</code></td>
    <td>liste_long</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats des élections européennes 2024 par circonscription législative](sources.md#data/01_raw/elections/2024-europeenne-circonscription.csv)
<a name="data/02_clean/elections/2024-legislatives-1-bureau_de_vote.csv"></a>
## 2024-legislatives-1-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-legislatives-1-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/e8/4ceea11f11d2ca3064189a5d719a90> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des élections législatives 2024 par bureau de vote](sources.md#data/01_raw/elections/2024-legislatives-1-bureau_de_vote.csv)
<a name="data/02_clean/elections/2024-legislatives-1-candidats.csv"></a>
## 2024-legislatives-1-candidats

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-legislatives-1-candidats.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/ad/8eaee9ac50795b6bfd3e6edea36336> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_depot</code></td>
    <td>numero_depot</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td>profession</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant</code></td>
    <td>sortant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe_suppleant</code></td>
    <td>sexe_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_suppleant</code></td>
    <td>nom_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom_suppleant</code></td>
    <td>prenom_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance_suppleant</code></td>
    <td>date_naissance_suppleant</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant_suppleant</code></td>
    <td>sortant_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_lfi</code></td>
    <td>nuance_lfi</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sensibilite</code></td>
    <td>sensibilite</td>
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
<a name="data/02_clean/elections/2024-legislatives-1-circonscription.csv"></a>
## 2024-legislatives-1-circonscription

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-legislatives-1-circonscription.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/da/7b4a29378ec8de4691fee6ade31ef3> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des élections législatives 2024 par circonscription législative](sources.md#data/01_raw/elections/2024-legislatives-1-circonscription.csv)
<a name="data/02_clean/elections/2024-legislatives-2-bureau_de_vote.csv"></a>
## 2024-legislatives-2-bureau_de_vote

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-legislatives-2-bureau_de_vote.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/0d/775128e516a561291b20e900c6377b> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour des élections législatives 2024 par bureau de vote](sources.md#data/01_raw/elections/2024-legislatives-2-bureau_de_vote.csv)
<a name="data/02_clean/elections/2024-legislatives-2-candidats.csv"></a>
## 2024-legislatives-2-candidats

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-legislatives-2-candidats.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/5d/c7dc1b36ed7e4f15bf4dd8b2ed27d2> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_depot</code></td>
    <td>numero_depot</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>profession</code></td>
    <td>profession</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant</code></td>
    <td>sortant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe_suppleant</code></td>
    <td>sexe_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom_suppleant</code></td>
    <td>nom_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom_suppleant</code></td>
    <td>prenom_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance_suppleant</code></td>
    <td>date_naissance_suppleant</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sortant_suppleant</code></td>
    <td>sortant_suppleant</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance_lfi</code></td>
    <td>nuance_lfi</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sensibilite</code></td>
    <td>sensibilite</td>
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
<a name="data/02_clean/elections/2024-legislatives-2-circonscription.csv"></a>
## 2024-legislatives-2-circonscription

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-legislatives-2-circonscription.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/c6/cdb9206fcf5986baae64bb036ac19b> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>inscrits</code></td>
    <td>inscrits</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>votants</code></td>
    <td>votants</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>exprimes</code></td>
    <td>exprimes</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>numero_panneau</code></td>
    <td>numero_panneau</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>voix</code></td>
    <td>voix</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du deuxième tour des élections législatives 2024 par circonscription législative](sources.md#data/01_raw/elections/2024-legislatives-2-circonscription.csv)
<a name="data/02_clean/elections/2024-legislatives-correspondances-bureau_de_vote-circonscription.csv"></a>
## 2024-legislatives-correspondances-bureau_de_vote-circonscription

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/elections/2024-legislatives-correspondances-bureau_de_vote-circonscription.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/67/26f0c1acf391480bce453c8911e82b> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>bureau_de_vote</code></td>
    <td>bureau_de_vote</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>circonscription</code></td>
    <td>circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Résultats du premier tour des élections législatives 2024 par bureau de vote](sources.md#data/01_raw/elections/2024-legislatives-1-bureau_de_vote.csv)
- [Liste des candidats au premier tour des élections législatives 2024](sources.md#data/01_raw/elections/2024-legislatives-1-candidats.csv)
- [Liste des candidats du Nouveau Front populaire et de leur sensibilité par circonscription législative](sources.md#data/01_raw/elections/2024-legislatives-nfp-sensibilites.csv)
- [La France insoumise — Nuançage des candidats des élections législatives 2024](sources.md#data/01_raw/elections/2024-legislatives-nuances-lfi.csv)
<a name="data/02_clean/rne/conseillers_arrondissement.csv"></a>
## conseillers_arrondissement

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/rne/conseillers_arrondissement.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/f7/7731f0195164866a3cd370b21dc58c> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_commune</code></td>
    <td>code_commune</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_secteur</code></td>
    <td>code_secteur</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>lieu_naissance</code></td>
    <td>lieu_naissance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>csp</code></td>
    <td>csp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_mandat</code></td>
    <td>date_debut_mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>fonction</code></td>
    <td>fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_fonction</code></td>
    <td>date_debut_fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nuance</code></td>
    <td>nuance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [conseillers_arrondissement](sources.md#data/01_raw/rne/conseillers_arrondissement.csv)
<a name="data/02_clean/rne/conseillers_csp.csv"></a>
## conseillers_csp

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/rne/conseillers_csp.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/8e/673f7e70a13fab98d760bae1bec662> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>type_csp</code></td>
    <td>type_csp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_csp</code></td>
    <td>code_csp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_section</code></td>
    <td>code_section</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>csp</code></td>
    <td>csp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_mandat</code></td>
    <td>date_debut_mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>fonction</code></td>
    <td>fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_fonction</code></td>
    <td>date_debut_fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [conseillers_csp](sources.md#data/01_raw/rne/conseillers_csp.csv)
<a name="data/02_clean/rne/conseillers_departementaux.csv"></a>
## conseillers_departementaux

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/rne/conseillers_departementaux.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/97/f614566d1df5966b4e31ef28bc4103> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_departement</code></td>
    <td>code_departement</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_canton</code></td>
    <td>code_canton</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>csp</code></td>
    <td>csp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_mandat</code></td>
    <td>date_debut_mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>fonction</code></td>
    <td>fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_fonction</code></td>
    <td>date_debut_fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [conseillers_departementaux](sources.md#data/01_raw/rne/conseillers_departementaux.csv)
<a name="data/02_clean/rne/conseillers_municipaux.csv"></a>
## conseillers_municipaux

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/rne/conseillers_municipaux.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/a5/ec3670f065e61ed75e0c2c987795e3> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_departement</code></td>
    <td>code_departement</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_collectivite_sp</code></td>
    <td>code_collectivite_sp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_commune</code></td>
    <td>code_commune</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>csp</code></td>
    <td>csp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_mandat</code></td>
    <td>date_debut_mandat</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>fonction</code></td>
    <td>fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_fonction</code></td>
    <td>date_debut_fonction</td>
    <td><code>date</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nationalite</code></td>
    <td>nationalite</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Répertoire national des élus — conseillers municipaux](sources.md#data/01_raw/rne/conseillers_municipaux.csv)
<a name="data/02_clean/rne/conseillers_regionaux.csv"></a>
## conseillers_regionaux

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/02_clean/rne/conseillers_regionaux.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/0d/bc7593a8b8ea36bb392873f7d2b675> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>code_region</code></td>
    <td>code_region</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_departement</code></td>
    <td>code_departement</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_naissance</code></td>
    <td>date_naissance</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>csp</code></td>
    <td>csp</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_mandat</code></td>
    <td>date_debut_mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>fonction</code></td>
    <td>fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_debut_fonction</code></td>
    <td>date_debut_fonction</td>
    <td><code>str</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [conseillers_regionaux](sources.md#data/01_raw/rne/conseillers_regionaux.csv)
<a name="data/03_main/elections/2022-presidentielle-parrainages.csv"></a>
## 2022-presidentielle-parrainages

| Propriété | Valeur |
| --------- | ------ |
| Chemin interne | `data/03_main/elections/2022-presidentielle-parrainages.csv` |
| Format de fichier | csv |
| URL de téléchargement | <https://hexagonal-data.s3.eu-west-3.amazonaws.com/cache/files/md5/af/2f45460d4570dd60a8445dd1b8115d> |



### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
<tr>
    <td><code>mandat</code></td>
    <td>mandat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>nom</code></td>
    <td>nom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>prenom</code></td>
    <td>prenom</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>sexe</code></td>
    <td>sexe</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>type_code_circonscription</code></td>
    <td>type_code_circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>code_circonscription</code></td>
    <td>code_circonscription</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>candidat</code></td>
    <td>candidat</td>
    <td><code>str</code></td>
    <td></td>
  </tr>
<tr>
    <td><code>date_publication</code></td>
    <td>date_publication</td>
    <td><code>date</code></td>
    <td></td>
  </tr>

</tbody>
</table>

### Sources

Cette production dépend des sources suivantes :

- [Code Officiel Géographique 2024](sources.md#data/01_raw/cog.zip)
- [Liste des parrainages validés par le Conseil constitutionnel](sources.md#data/01_raw/elections/2022-presidentielle-parrainages.csv)
