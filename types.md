# Types de données

## `str`


## `int`


## `code_commune`

L'identifiant de la commune attribué par l'INSEE dans le Code Officiel géographique (COG).

Chaque commune est identifié par un code à cinq chiffres (le deuxième chiffre pouvant être en réalité la lettre A ou B
pour les communes corses).

Pour certains fichiers, les codes ne correspondent pas toujours à des communes. Par exemple, le code commune est aussi
utilisé dans le COG pour identifier des communes déléguées ou associées qui sont inclues dans une autre commune. C'est
aussi le cas des arrondissements des trois communes de Paris, Lyon et Marseille (PLM) qui reçoivent aussi un code
commune spécifique.

Dans le cas des résultats électoraux, pour le cas des PLM, c'est un code secteur qui est utilisé en lieu et place du
code commune. Il se présente sous la forme du code commune de la commune principale (Paris, Lyon ou Marseille), suivi
de SR, suivi du numéro de secteur (par exemple, 75056SR05) pour le 5ème secteur.

Dans le cas de Paris avant 2020 et de Lyon, cela correspond toujours à l'arrondissement. Pour Marseille, et pour Paris
après 2020 dans le cas du 1er secteur, les secteurs comportent plusieurs arrondissements, ce qui explique l'utilisation
d'un code distinct.

## `code_departement`

L'identifiant de département tel qu'il est attribué par l'INSEE dans le Code officiel géographique (COG).

Pour les résultats électoraux, la valeur ZX est utilisé pour le cas de Saint-Barthélémy et Saint-Martin.

## `code_region`

## `code_circonscriptionleg`

hexagonal reprend la convention du ministère de l'intérieur de 2024 pour la codification des départements, mais
ajoute un tiret simple entre le numéro de département et le numéro de circonscription sur deux chiffres.

