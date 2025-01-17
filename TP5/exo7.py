import shutil
import os

# Copier et déplacer des fichiers
try:
    # Copier le fichier "journal.txt" en "journal_copie.txt"
    fichier_original = "journal.txt"
    fichier_copie = "journal_copie.txt"
    
    if os.path.exists(fichier_original):
        shutil.copy(fichier_original, fichier_copie)
        print(f"Le fichier '{fichier_original}' a été copié en '{fichier_copie}'.")
    else:
        print(f"Le fichier '{fichier_original}' n'existe pas.")
    
    # Créer un nouveau dossier "archives" s'il n'existe pas
    dossier_destination = "archives"
    os.makedirs(dossier_destination, exist_ok=True)
    
    # Déplacer le fichier "journal_copie.txt" dans le dossier "archives"
    chemin_destination = os.path.join(dossier_destination, fichier_copie)
    if os.path.exists(fichier_copie):
        shutil.move(fichier_copie, chemin_destination)
        print(f"Le fichier '{fichier_copie}' a été déplacé dans le dossier '{dossier_destination}'.")
    else:
        print(f"Le fichier '{fichier_copie}' n'existe pas.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
