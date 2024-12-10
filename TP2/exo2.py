class Voiture :
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def afficher_info(self):
        print(self.__dict__)
        
dacia = Voiture("dacia","logan",2024)
renault = Voiture("renault","kadjar",2022)
dacia.afficher_info()

        