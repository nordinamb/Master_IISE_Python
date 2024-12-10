class Livre :
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
class Bibliotheque:
    def __init__(self,livres):
        self.livres = livres
    def ajouter_livre(self,livre):
        self.livres.append(livre)
    def afficher_livres(self):
        for livre in self.livres :
            print("titre de livre :",livre.titre," et auteur",livre.auteur," annee de pub ",livre.annee_publication)

l1 = Livre("l1","amro",2018)
l2 = Livre("l2","albert",2019)
l3 = Livre("l3","hugo",1890)
b1 = Bibliotheque([l1,l2])
b1.afficher_livres()
b1.ajouter_livre(l3)
print("################################################")
b1.afficher_livres()