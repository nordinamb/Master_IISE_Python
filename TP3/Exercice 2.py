class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    
    @property
    def nom(self):
        return self.__nom
        
    @nom.setter
    def nom(self,nom):
        self.__nom = nom
    
    
    def getprenom(self):
        return self.__prenom
    

    def setprenom(self,prenom):
        self.__prenom = prenom
    prenom = property(getprenom,setprenom)
    
    @property 
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age > 0:
            self.__age=age
        else:
            raise ValueError("L'age doit etre positif")
    
    def afficher_informations(self):
        return f'Nom: {self.nom}, Prenom : {self.prenom}, Age: {self.age}'
        
p1 = Personne("ait moulay","noreddine",22)
print(p1.nom)
print(p1.prenom)

p1.prenom = "ali"

print(p1.prenom)

print(p1.afficher_informations())

        
    