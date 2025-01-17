
    # Ouvrir le fichier en mode lecture
with open("exemple.txt", "r") as fichier:
        # Lire et afficher chaque ligne avec son numéro
        for numero, ligne in enumerate(fichier, start=1):
            print(f"Ligne {numero}: {ligne.strip()}")
