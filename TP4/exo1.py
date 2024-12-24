class vehicule :
    def __init__(self, marque, modele, annee):
        self.marque =  marque
        self.modele =  modele
        self.annee =  annee
    def afficher_info(self):
        print(f"Marque : {self.marque}")
        print(f"Modele : {self.modele}")
        print(f"Annee : {self.annee}")
class Moteur :
    def __init__(self,puissance,typeDeMotteur):
        self.puissance = puissance
        self.typeDeMotteur = typeDeMotteur
    def afficher_moteur(self):
        print(f"Moteur info : {self.__dict__}")
class Voiture(vehicule,Moteur) :
    def __init__(self, marque, modele, annee,puissance,typeDeMotteur,nbrePlace):
        vehicule.__init__(self,marque, modele, annee)#appel de la methode de la classe vehicule
        Moteur.__init__(self,puissance,typeDeMotteur)
        self.nbrePlace = nbrePlace
    def afficher_info(self):
        vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print(f"nombre de place de la voiture  {self.nbrePlace}")
class Moto(vehicule,Moteur) :
    def __init__(self, marque, modele, annee,puissance,typeDeMotte,typeDeMotteur):
        vehicule.__init__(self,marque, modele, annee)#appel de la meth
        Moteur.__init__(self,puissance,typeDeMotteur)
        self.typeDeMotte = typeDeMotte
    def afficher_info(self):
         vehicule.afficher_info(self)
         Moteur.afficher_moteur(self)
         print(f"Type de moteur de la moto {self.typeDeMotte}")

v1  = Voiture("lambo","urus",2024,600,"v8",5)
m1  = Moto("ducati","treetfighter",2024,214,"sport","v4")
v1.afficher_info()
m1.afficher_info()