class CompteBancaire :
    def __init__(self , titulaire , solde):
        self.titulaire = titulaire
        self.solde = solde
        
    def deposer(self,montant):
        self.solde += montant
        print("Vous avez deposee ",montant," MAD")
        
    def retirer(self,montant) :
        if montant > self.solde :
            print("Vous n'avez pas assez d'argent dans votre compte")
        self.solde -= montant
        print("Vous avez retiree ",montant," MAD")
        
    def afficher_solde(self):
        print("Votre solde est de ",self.solde," MAD")
        
CMPT1 = CompteBancaire("ALI BABA",10000)
CMPT1.afficher_solde()
CMPT1.deposer(5000)
CMPT1.afficher_solde()
CMPT1.retirer(2000)
CMPT1.afficher_solde()
