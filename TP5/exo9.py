def calculer_statistiques(fichier):
    try:
        with open(fichier, "r") as file:
            contenu = file.read()
            lignes = contenu.splitlines()
            mots = contenu.split()
            caracteres = len(contenu.replace("\n","")) 
            
            print(f"Nombre total de lignes : {len(lignes)}")
            print(f"Nombre total de mots : {len(mots)}")
            print(f"Nombre total de caractères : {caracteres}")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier}' n'existe pas.")

# Exemple d'utilisation
calculer_statistiques("exemple.txt")
