from abc import ABC,abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer():
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("deplacement d'une Voiture")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("deplacement d'une Bicyclette")
        
v1 = Voiture()
b1 = Bicyclette()
v1.deplacer()
b1.deplacer()