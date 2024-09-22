# Hexagonal

Ce dépôt agrège toute l'information électorale, administrative et géographique
française pour faciliter l'analyse électorale.

## Installation

2 options:

-   poetry
-   conda/mamba

### Poetry

Pour installer les dépendances:

```bash
poetry install
```

Et pour l'activer:

```bash
poetry shell
```

### Mamba

Pour créer l'environnement à partir du fichier `environment.yml`:

```bash
mamba env create -f environment.yml
```

Et pour l'activer:

```bash
mamba activate hexagonal
```

## Architecture

Les données sont stockées dans le dossier `data` avec les sous-dossiers suivants:

- `01_raw/`: Données brutes (téléchargées)
- `02_clean/`: Données nettoyées (formatées, filtrées)
- `03_main/`: Données prêtes à l'emploi par étude (_feature engineering_, jointures, aggrégats, etc.)

## Utilisation

### Génération et vérification des données

On utilise [dvc](https://dvc.org/) pour gérer le pipeline de données.

Pour lancer le pipeline et générer les données:

```bash
dvc repro --no-commit
```

L'option `--no-commit` permet de ne pas mettre à jour le lockfile `dvc.lock`, ce
qui permet de vérifier si les artefacts générés localement sont
cohérents avec ceux le lockfile.

```bash
dvc status
````

Si les artefacts sont cohérents, on a le message suivant:

```bash
Data and pipelines are up to date.
```

Sinon, dvc nous dira quels artefacts sont incohérents.

### Mise à jour des données

Après un développment, on peut mettre à jour le lockfile avec:

```bash
dvc repro
```

Le fichier `dvc.lock` est modifié et à committer.