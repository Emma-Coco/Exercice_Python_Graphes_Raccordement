import pandas as pd

# Supposons que vos données soient stockées dans un fichier CSV appelé "reseau_en_arbre.csv"
# Vous pouvez charger les données de cette manière :
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

# Afficher les résultats pour l'étape une
print("Les id_batiment pour lesquels toutes les valeurs dans 'infra_type' sont 'fourreau_existant' sont :", batiment_etape_une)
print("Les id_batiment pour lesquels toutes les valeurs dans 'infra_type' sont 'fourreau_existant' sont :", batiment_etape_deux)
