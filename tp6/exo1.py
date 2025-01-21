def safe_division(a,b):
    
    return a/b
try :
    safe_division
except ZeroDivisionError :
    print("vous avez fait une division par zero")
    
if __name__ == '__main__' :
    safe_division(10,0)