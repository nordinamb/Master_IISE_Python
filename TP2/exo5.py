class Animal :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def faire_du_bruit(self):
        print("bruit ")
class chein(Animal):
    def __init__(self, name, age, species):
        super().__init__( name, age)
        self.species = species
    def faire_du_bruit(self):
        print("bufff")

class chat(Animal):
    def __init__(self, name, age, species):
        super().__init__( name, age)
        self.species = species
    def faire_du_bruit(self):
        print("Meow")
        
dog = chein("brian",10,"labrador retriever")
dog.faire_du_bruit()
cat = chat("mimi",3,"Sphynx")
cat.faire_du_bruit()