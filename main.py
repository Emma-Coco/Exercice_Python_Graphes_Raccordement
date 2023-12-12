####################################################################################################

#Cette version est là version de test et débogages


####################################################################################################


import pandas as pd
import numpy as np

# Charger les données
donnees = pd.read_csv("reseau_en_arbre.csv")

# Initialiser la liste des bâtiments pour l'étape une
batiment_etape_une = []
batiment_etape_deux = []

# Obtenez la liste des id_batiment uniques
id_batiments_uniques = donnees['id_batiment'].unique()

# Parcourir chaque id_batiment unique
for id_batiment in id_batiments_uniques:
    # Filtrer les données pour l'id_batiment actuel
    donnees_batiment = donnees[donnees['id_batiment'] == id_batiment]
    
    # Vérifier si toutes les valeurs dans la colonne 'infra_type' sont égales à 'fourreau_existant'
    if all(donnees_batiment['infra_type'] == 'fourreau_existant'):
        # Ajouter l'id_batiment à la liste pour l'étape une
        batiment_etape_une.append(id_batiment)
    else:
        batiment_etape_deux.append(id_batiment)

# # Afficher les résultats pour l'étape une
# print("Les id_batiment pour lesquels toutes les valeurs dans 'infra_type' sont 'fourreau_existant' sont :", batiment_etape_une)
# #print("Les id_batiment pour lesquels au moins une valeur dans 'infra_type' est différente de 'fourreau_existant' sont :", batiment_etape_deux)

# Calcul de l'indice de difficulté (moyenne longueur par maison)
# Définir la fonction calculer_moyenne_longueur_par_maison
def calculer_moyenne_longueur_par_maison(data, batiment_etape_deux):
    # Convertir les données en un tableau NumPy
    data_array = np.array(data)

    # Initialiser un dictionnaire pour stocker les moyennes
    moyennes = {}

    # Parcourir les id_batiments uniques
    for id_batiment in batiment_etape_deux:
        # Sélectionner les lignes correspondant à l'id_batiment en cours
        lignes_id_batiment = data_array[data_array[:, 0] == id_batiment]
        
        # Récuperer le nombre de prises
        nb_prises = lignes_id_batiment[0, 1]
        
        # Rendre nulles les longueurs associées à infra_type "fourreau_existant"
        lignes_id_batiment[lignes_id_batiment[:, 3] == 'fourreau_existant', 4] = 0
        
        # Calculer la moyenne des longueurs par batiment
        moyenne = np.sum(lignes_id_batiment[:, 4]) / nb_prises
            
        # Stocker la moyenne dans le dictionnaire
        moyennes[id_batiment] = moyenne

    return moyennes


# Appeler la fonction de calcul des moyennes
moyennes = calculer_moyenne_longueur_par_maison(donnees, batiment_etape_deux)

# Trier les id_batiments en fonction des moyennes (du plus petit au plus grand)
id_batiments_et_moyennes = sorted(moyennes.items(), key=lambda x: x[1])

# # Afficher les id_batiments ordonnés
# print("Id_batiments ordonnés avant recalcul:")
# for id_batiment, moyenne in id_batiments_et_moyennes:
#     print(f"{id_batiment}: Moyenne = {moyenne}")


# Initialiser la nouvelle liste ordonnée des batiments
liste_ordonnee_bat_etape_deux = []


iteration = 1

infra_ids_mises_a_zero = set()

while batiment_etape_deux:  # Tant que la liste batiment_etape_deux n'est pas vide
    # Appeler la fonction de calcul des moyennes
    moyennes = calculer_moyenne_longueur_par_maison(donnees, batiment_etape_deux)

    # # Afficher l'ensemble des moyennes à chaque itération
    # print(f"Iteration {iteration} - Moyennes de chaque batiment:")
    # for id_batiment, moyenne in moyennes.items():
    #     print(f"{id_batiment}: Moyenne = {moyenne}")

    # Trouver l'id_batiment avec la plus petite moyenne
    id_batiment_min_moyenne = min(moyennes, key=moyennes.get)
    
    # # Afficher les données pour le débogage
    # print(f"Données avant les modifications pour id_batiment {id_batiment_min_moyenne}:")
    # print(donnees[donnees['id_batiment'] == id_batiment_min_moyenne])

    # Récupérer la liste des infra_id associés à cet id_batiment
    infra_ids_min_moyenne = donnees.loc[donnees['id_batiment'] == id_batiment_min_moyenne, 'infra_id'].unique()

    # Récupérer les infra_ids qui ne sont pas déjà à zéro
    infra_ids_a_zero = set(infra_ids_min_moyenne) - infra_ids_mises_a_zero


    
    # # Afficher les infra_ids pour le débogage
    # print(f"Infra_ids associés à l'id_batiment avec la plus petite moyenne ({id_batiment_min_moyenne}):")
    # print(infra_ids_min_moyenne)

    # Rendre nulles les longueurs associées à tous les infra_id de l'id_batiment avec la plus petite moyenne (fourreau_existant)
    donnees.loc[(donnees['id_batiment'] == id_batiment_min_moyenne) & (donnees['infra_type'] == 'fourreau_existant'), 'longueur'] = 0

    # Rendre nulles les longueurs associées à tous les infra_id de l'id_batiment avec la plus petite moyenne (fourreau_non_existant)
    donnees.loc[(donnees['id_batiment'] == id_batiment_min_moyenne) & (donnees['infra_type'] == 'fourreau_non_existant'), 'longueur'] = 0

    # Rendre nulles les longueurs associées à tous les infra_id de tous les batiments ayant le même infra_id que l'id_batiment avec la plus petite moyenne
    donnees.loc[(donnees['infra_id'].isin(infra_ids_min_moyenne)) & (donnees['infra_type'].isin(['fourreau_existant', 'fourreau_non_existant'])), 'longueur'] = 0

    # Mettre à jour les infra_ids qui ont été mis à zéro
    infra_ids_mises_a_zero.update(infra_ids_a_zero)


    # Supprimer l'id_batiment de la liste initiale
    batiment_etape_deux.remove(id_batiment_min_moyenne)
    

    # Ajouter l'id_batiment à la liste ordonnée
    liste_ordonnee_bat_etape_deux.append(id_batiment_min_moyenne)

    # # Afficher les infra_ids associés à l'id_batiment avec la plus petite moyenne
    # print(f"Infra_ids associés à l'id_batiment avec la plus petite moyenne ({id_batiment_min_moyenne}):")
    # print(infra_ids_min_moyenne)

    # Afficher les infra_ids nouvellement mis à zéro pour l'id_batiment avec la plus petite moyenne
    print(f"Infra_ids nouvellement mis à zéro pour l'id_batiment {id_batiment_min_moyenne}:")
    print(infra_ids_a_zero)

    iteration += 1

# # Afficher les résultats finaux
# print("Liste ordonnée des batiments:")
# print(liste_ordonnee_bat_etape_deux)
