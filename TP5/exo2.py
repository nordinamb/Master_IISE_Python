
with open("phrases.txt", "w") as fichier:
        print("Veuillez entrer trois phrases :")
        for i in range(1, 4):
            phrase = input(f"Entrez la phrase {i} : ")
            fichier.write(phrase + "\n")
print("Les phrases ont été enregistrées dans 'phrases.txt'.")
