from exo3 import read_file
from exo9 import get_positive_integer



def main():
    try:
        # Demander le fichier
        filename = input("Entrez le nom du fichier : ")
        content = read_file(filename)
        if content:  # Si le contenu a été lu avec succès
            print(f"Contenu du fichier '{filename}' :")
            print(content)

        # Demander un entier positif
        number = get_positive_integer()
        print(f"Vous avez saisi l'entier : {number}")

    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == '__main__':
    main()