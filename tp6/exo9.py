def get_positive_integer():
    while True:
        try :
            num=int(input("Entrez un entier positif:"))
            if num > 0:
                print(f"vous avez entré : {num}")
                return  num
                break
            else :
                print("entier n'est pas positif")
        except ValueError:
            print("Erreur: entrer un nombre entier valide")
            
if __name__ == '__main__':
    get_positive_integer()