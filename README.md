# projet-python-data-science

dcp on est d'accord que la problématique ça serait : 
Existe-il un lien géographique entre pollution de l'air et niveau de vie en France?

et pour les données de pollution, j'ai trouver un dataset bien carré je pense, voici le lien :
https://sites.wustl.edu/acag/surface-pm2-5/#V6.GL.02.04

j'ai pris le dataset résolution 0,01° × 0,01°, EU -> ANNUEL -> 2019 par exemple mais on pourra prendre d'autres données.

je pense que c'est un dataset pertinent parce qu'il a été utilisé dans l'enquête INSEE : Mobilité résidentielle et inégalités à la pollution de l’air : décrire les disparités d’exposition à la pollution de l’air tout au long de la vie selon le revenu.

et pour les données géographiques, je pense qu'on peut utiliser les donénes de l'INSEE : Revenus, pauvreté et niveau de vie en 2019 - Données carroyées (carreau 200m*200m)

1er oje

J'ai trouvé ce site pour la france : https://www.geodair.fr/donnees/consultation

pour faire les stats descriptives j'ai trouvé https://www.data.gouv.fr/datasets/indice-de-la-qualite-de-lair-quotidien-par-commune-indice-atmo c'est des stats quotidiennes de la qualité de l'air par commune avec ça on pourra facilement faire la moyenne sur l'année en plus y a une API c'est pratique à utiliser

pour le niveau de vie il y a https://www.data.gouv.fr/datasets/niveau-de-vie-median-et-taux-de-pauvrete-par-type-de-menage/?utm_source=chatgpt.com qui a l'air très complet, il y a les données disponibles pour les communes mais aussi d'autres découpages administratrifs, normalement c'est possible de faire une jointure avec l'autre dataset en utilisant le code la commune, jepense que le mieux c'est d'abord de regarder le premier dataset, le transformer en une ligne par commmune avec juste 3 colonnes, la moyenne de qualité de l'air sur l'année et le code de la commune et le nom de la commune puis faire la jointure avec le deuxième dataset en utilisant le code de commune et éventuellement faire en sorte que y ait que 4 colonnes, niveau de vie, qualoté de l'air, nom de commune et le code de la commune

https://www.insee.fr/fr/statistiques/6036907? 
