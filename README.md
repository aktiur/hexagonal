# Hexagonal

Ce dépôt agrège toute l'information électorale, administrative et géographique
française pour faciliter l'analyse électorale.

## Installation

L'installation du projet se fait avec uv

```bash
uv sync
```

## Organisation du projet

Les données sont stockées dans le dossier `data` avec les sous-dossiers suivants:

- `01_raw/`: Données brutes (téléchargées)
- `02_clean/`: Données nettoyées (formatées, filtrées)
- `03_main/`: Données prêtes à l'emploi par étude (_feature engineering_, jointures,
  aggrégats, etc.)

## Utilisation

### Récupération des données

Pour éviter d'avoir à faire tourner le pipeline en entier, la version des données
correspondant à un commit
peut être récupérée depuis le cache en ligne avec la commande suivante :

```bash
uv run dvc pull
```

### Génération et vérification des données

On utilise [dvc](https://dvc.org/) pour gérer le pipeline de données.

Pour lancer le pipeline et générer les données:

```bash
uv run dvc repro --no-commit
```

L'option `--no-commit` permet de ne pas mettre à jour le lockfile `dvc.lock`, ce
qui permet de vérifier si les artefacts générés localement sont
cohérents avec ceux de la lockfile.

```bash
dvc status
````

Si les artefacts sont cohérents, on a le message suivant:

```
Data and pipelines are up to date.
```

Sinon, dvc nous dira quels artefacts sont incohérents.

### Mise à jour des données

Après un développment, on peut mettre à jour le lockfile avec:

```bash
dvc repro
```

Le fichier `dvc.lock` est modifié et à committer.

### Mettre à jour une des sources

Les sources ne sont pas mises à jour automatiquement. Pour les mises à jour, il y a deux
cas de figure.

#### L'URL de la source ne change pas

Pour certains fichiers, l'URL de téléchargement renvoit un état actuel de la source de
données qui peut donc changer à n'importe quel moment. C'est par exemple le cas pour les
données de l'Assemblée nationale. Il suffit alors de faire tourner la commande :

```bash
uv run dvc update <chemin du fichier dans data/01_raw> 
```

Cette commande interroge le serveur d'origine, télécharge la nouvelle version le cas
échéant, et met à jour le fichier .dvc.

#### L'URL de la source change

Pour d'autres fichiers, l'URL correspond à une édition particulière du fichier, et il
faut donc la changer pour mettre à jour le fichier. C'est par exemple le cas du COG.