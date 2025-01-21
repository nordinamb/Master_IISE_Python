def read_file(filename):
    try:
        fichier = open(filename,"r")
        lines = fichier.readlines()
        for line in lines:
            print(line)
    except FileNotFoundError:
        print("erreur: fichier non trouve")

    finally:
        if 'fichier' in locals():
             fichier.close()


if __name__ == '__main__' :
    filename = "fichierUnexistant.txt"
    read_file(filename)