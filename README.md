# Projet Python – Pollution de l’air et niveau de vie en France

*Auteurs : Luna Piaraly, Quentin Gouiffes, Lucas Vital *

## Présentation

Ce projet est réalisé dans le cadre du cours **Python pour la Data Science (2A ENSAE Paris)**. Il étudie le lien entre **pollution de l’air** et **niveau de vie** en France, à partir de données publiques environnementales et socio‑économiques, agrégées à l’échelle communale.

L’objectif est de proposer :

* une **analyse descriptive** des données ;
* une **analyse statistique simple** afin d’explorer l’existence d’un lien entre pollution et conditions de vie.

---

## Problématique

> Existe‑t‑il une relation statistique entre la pollution de l’air et le niveau de vie des communes françaises ?

---

## Données

Le projet repose sur le croisement de :

* données de **pollution de l’air** (PM2.5 notamment),
* données **INSEE** de niveau de vie et d’inégalités,
* données démographiques communales.

Les données sont nettoyées, harmonisées puis fusionnées pour construire un jeu de données final exploitable.

---

## Organisation des notebooks

Le projet s’articule autour de **trois notebooks**, à exécuter dans l’ordre :

1. **`1_data_collection_cleaning.ipynb`**
   Collecte, nettoyage et préparation des différentes bases de données.

2. **`2_exploratory_analysis.ipynb`**
   Analyse descriptive : statistiques, graphiques et visualisations (Plotly).

3. **`3_modelisation.ipynb`**
   Analyse statistique : corrélations et régressions simples pour étudier le lien entre pollution et niveau de vie.

---

## Méthodologie

* nettoyage et fusion des bases de données ;
* analyse descriptive univariée et bivariée ;
* visualisations ;
* modèles statistiques simples et interprétation économique.

---

## Reproductibilité

* chemins relatifs à la racine du projet ;
* notebooks commentés et exécutables indépendamment ;
* dépendances standards Python (pandas, numpy, plotly, statsmodels).

---

## Remarque

Ce projet a une vocation exploratoire et pédagogique : les résultats mettent en évidence des corrélations mais ne permettent pas d’établir une relation causale stricte.

