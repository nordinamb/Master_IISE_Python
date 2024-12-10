class Rectangle :
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def calculer_surface(self):
        return self.largeur * self.hauteur
    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

r1 = Rectangle(3,4)
print("la surface",r1.calculer_surface()) 
print("le perimetre",r1.calculer_perimetre())