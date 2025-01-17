import os

# Renommer et supprimer un fichier
try:
    # Renommer le fichier "phrases.txt" en "anciennes_phrases.txt"
    ancien_nom = "phrases.txt"
    nouveau_nom = "anciennes_phrases.txt"
    
    if os.path.exists(ancien_nom):
        os.rename(ancien_nom, nouveau_nom)
        print(f"Le fichier '{ancien_nom}' a été renommé en '{nouveau_nom}'.")
    else:
        print(f"Le fichier '{ancien_nom}' n'existe pas.")
    
    # Supprimer le fichier "anciennes_phrases.txt"
    if os.path.exists(nouveau_nom):
        os.remove(nouveau_nom)
        print(f"Le fichier '{nouveau_nom}' a été supprimé.")
    else:
        print(f"Le fichier '{nouveau_nom}' n'existe pas.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
