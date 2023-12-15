# L'énnoncé du problème

 Cas d'usage: Planification du raccordement électrique de bâtiments

Contexte
Vous avez été fournis avec deux shapefiles et un fichier CSV. Ces fichiers représentent respectivement les bâtiments à raccorder, les lignes électriques à déployer pour le raccordement, et l'arbre linéaire du réseau qui décrit les connexions à mettre en œuvre et les coûts de raccordement.
Objectifs du Cas d'Utilisation
Votre mission est de créer un plan de raccordement qui priorise les bâtiments les plus simples à raccorder (en minimisant les coûts) tout en maximisant le nombre de prises raccordées. Vous devrez prendre en compte la mutualisation des lignes électriques entre plusieurs bâtiments pour optimiser le plan.

Données Fournies

1.	Shapefile des Bâtiments: Contient les données géospatiales des bâtiments, y compris leurs emplacements.
2.	Shapefile des Lignes Électriques: Contient les données géospatiales des lignes électriques à déployer pour le raccordement.
3.	Fichier CSV de l'Arbre Linéaire: Fournit une représentation linéaire du réseau, indiquant les connexions et les coûts de raccordement.
   
Instructions

1.	Analyse Préliminaire:
   
○	Examinez les shapefiles pour comprendre la disposition géographique des bâtiments et des lignes électriques.
○	Analysez le fichier CSV pour comprendre la structure de l'arbre linéaire du réseau et les coûts associés à chaque connexion.

3.	Modélisation du Réseau:
○	Modélisez le réseau électrique en utilisant la théorie des graphes, où les bâtiments sont des nœuds et les lignes électriques sont des arêtes.
○	Intégrez les données de coût dans les arêtes de votre modèle de graphe.

5.	Développement de la Métrique de Priorisation:
○	Élaborez une métrique qui évalue chaque bâtiment en fonction de la facilité de raccordement et du coût.
○	La métrique doit favoriser les bâtiments qui peuvent être raccordés avec le moins de dépenses et le maximum de mutualisation des lignes.

6.	Planification du Raccordement:
○	Utilisez votre métrique pour établir un ordre de priorité pour le raccordement des bâtiments.
○	Proposez un plan d'action qui détaille l'ordre dans lequel les bâtiments doivent être raccordés.

8.	Optimisation:
○	Identifiez les opportunités de mutualisation des lignes pour réduire les coûts.
○	Ajustez votre plan pour maximiser le nombre de prises raccordées.

9.	Rapport:
○	Rédigez un rapport expliquant votre méthodologie, votre métrique de priorisation, et le plan de raccordement proposé.
○	Justifiez vos choix et démontrez comment votre plan atteint l'objectif de maximisation des prises raccordées et de minimisation des coûts.


Livraison Attendue

Un rapport détaillé incluant :

●	Une description de votre métrique de priorisation.
●	Le plan de raccordement des bâtiments avec l'ordre de priorité.
●	Une analyse des coûts et des bénéfices de votre planification.
●	Des cartes issues des shapefiles illustrant le plan de raccordement proposé.
●	Un résumé des défis rencontrés et des solutions apportées.

# Ma résolution
[TP - Raccordements.pptx](https://github.com/Emma-Coco/Exercice_Python_Graphes_Raccordement/files/13679667/TP.-.Raccordements.pptx)

