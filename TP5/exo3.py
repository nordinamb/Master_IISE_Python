# Script pour demander des phrases et les ajouter à un fichier
try:
    while True:
        # Demander à l'utilisateur s'il souhaite ajouter des phrases
        ajouter = input("Souhaitez-vous ajouter des phrases au fichier 'phrases.txt' ? (oui/non) : ").strip().lower()
        
        if ajouter == "oui":
            # Ouvrir le fichier en mode ajout
            with open("phrases.txt", "a", encoding="utf-8") as fichier:
                print("Vous pouvez ajouter autant de phrases que vous le souhaitez. Tapez 'STOP' pour arrêter.")
                while True:
                    phrase = input("Entrez une phrase (ou 'STOP' pour terminer) : ").strip()
                    if phrase.upper() == "STOP":
                        break
                    # Ajouter la phrase au fichier
                    fichier.write(phrase + "\n")
            print("Les phrases ont été ajoutées au fichier.")
        elif ajouter == "non":
            print("Aucune modification n'a été apportée au fichier.")
            break
        else:
            print("Réponse non reconnue. Veuillez répondre par 'oui' ou 'non'.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")