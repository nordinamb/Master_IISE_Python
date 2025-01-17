import csv

# Script pour lire un fichier CSV et afficher les informations
try:
    # Ouvrir le fichier CSV en mode lecture
    with open("contacts.csv", "r") as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)  # Lire le fichier CSV
        entetes = next(lecteur_csv)  # Lire la première ligne (les en-têtes)
        
        print("Informations des contacts :")
        for ligne in lecteur_csv:
            # Correspondance avec les colonnes
            nom = ligne[0]
            age = ligne[1]
            ville = ligne[2]
            # Afficher les informations dans un format lisible
            print(f"Nom : {nom}, Âge : {age}, Ville : {ville}")
except FileNotFoundError:
    print("Le fichier 'contacts.csv' n'a pas été trouvé. Assurez-vous qu'il existe.")
except IndexError:
    print("Erreur : Le fichier CSV ne contient pas toutes les colonnes nécessaires.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
