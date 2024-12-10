class Personne :
    def __init__(self, nom, prenom, age,amis):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = amis
    def se_presenter(self) :
        print("Bonjour, je m'appelle ",self.prenom," ",self.nom,"et mon age est ",self.age)
    def ajouter_ami(self,ami) :
        self.amis.append(ami)
    def afficher_amis(self) :
        print("Mes amis sont : ")
        for ami in self.amis :
            print(ami.prenom,ami.nom,"  ")
          
p1 = Personne("dali","debois",23,[])
p1.se_presenter()
p2 = Personne("ahmed","samir",24,[])
p1.ajouter_ami(p2)
p1.afficher_amis()
            