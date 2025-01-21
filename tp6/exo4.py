
class ageException(Exception) :
    pass
def setAge(age ) :
    
    if age < 0 :
        raise ageException("le age que vous avez donnee et invalid ")
    
try :    
    setAge(-1)
except ageException as e:
    print(e)