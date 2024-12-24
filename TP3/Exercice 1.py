from abc import ABC,abstractmethod
import math 

class Forme(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def calculer_surface(self):
        raise NotImplementedError("il faut definer cette method")
    
    


class Cercle(Forme):
    def __init__(self,rayon):
        super().__init__()
        self.rayon = rayon
    
    def calculer_surface(self):
        return '%.2f'% (self.rayon**2*math.pi)
        
class Rectangle(Forme):
    def __init__(self,L,l):
        super().__init__()
        self.L = L
        self.l = l
    
    def calculer_surface(self):
        return '%.2f'%(self.l*self.L)
    
cercle = Cercle(10)
rectangle = Rectangle(3,2)

print(f'Surface du cercle : {cercle.calculer_surface()}')
print(f'Surface de rectangle : {rectangle.calculer_surface()}')