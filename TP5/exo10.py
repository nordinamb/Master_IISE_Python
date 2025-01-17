import csv

def ajouter_contact(nom, telephone, email):
    with open("contacts.csv", mode="a") as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, telephone, email])
        print("Contact ajouté avec succès.")

def afficher_contacts():
    try:
        with open("contacts.csv", mode="r") as fichier:
            reader = csv.reader(fichier)
            next(reader)
            for row in reader:
                if len(row) >= 3:
                    print(f"Nom: {row[0]}, Téléphone: {row[1]}, Email: {row[2]}")
                
    except FileNotFoundError:
        print("Erreur : Le fichier des contacts n'existe pas.")


def rechercher_contact(nom_recherche):
    try:
        with open("contacts.csv", mode="r") as fichier:
            reader = csv.reader(fichier)
            trouve = False
            for row in reader:
                if row[0].lower() == nom_recherche.lower():
                    print(f"Nom: {row[0]}, Téléphone: {row[1]}, Email: {row[2]}")
                    trouve = True
            if not trouve:
                print("Contact non trouvé.")
    except FileNotFoundError:
        print("Erreur : Le fichier des contacts n'existe pas.")

def supprimer_contact(nom_supprime):
    try:
        with open("contacts.csv", mode="r") as fichier:
            reader = csv.reader(fichier)
            contacts = [row for row in reader if row[0].lower() != nom_supprime.lower()]
        with open("contacts.csv", mode="w", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerows(contacts)
            print("Contact supprimé avec succès.")
    except FileNotFoundError:
        print("Erreur : Le fichier des contacts n'existe pas.")

# Menu interactif
def menu():
    while True:
        print("\n--- Gestion des Contacts ---")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom : ")
            telephone = input("Téléphone : ")
            email = input("Email : ")
            ajouter_contact(nom, telephone, email)
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            nom_recherche = input("Entrez le nom du contact à rechercher : ")
            rechercher_contact(nom_recherche)
        elif choix == "4":
            nom_supprime = input("Entrez le nom du contact à supprimer : ")
            supprimer_contact(nom_supprime)
        elif choix == "5":
            print("Fermeture de l'application.")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Lancer le menu
menu()
