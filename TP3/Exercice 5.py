class Employe:
    def __init__(self,nom,prenom,salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
    
class Manager(Employe):
    def __init__(self,nom,prenom,salaire,liste_Emp=None):
        super().__init__(nom,prenom,salaire)
        self.liste_Emp = liste_Emp 
    
    def ajouter_emp(self,employe):
        if employe not in self.liste_Emp:
            self.liste_Emp.append(employe)
        else:
            print(f"L'employe {employe.nom} vous avez déja ajouter")
    
    def afficher_emp(self):
        for index,employe in enumerate(self.liste_Emp,start=1):
            print(f"Employe {index} supervisé par {self.nom}")
            print(f"  - Nom : {employe.nom}")
            print(f"  - Prenom : {employe.prenom}")
            print(f"  - Salaire : {employe.salaire} DHs")

emp1 = Employe("ali","reda",8500)
emp2 = Employe("benani","omar",9800)
emp3 = Employe("berada","hayat",10000)

liste = [emp1,emp2]

manager = Manager("nori","azzedine",18000,liste)
manager.ajouter_emp(emp3)
manager.afficher_emp()
