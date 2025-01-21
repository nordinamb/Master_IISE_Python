def safe_division(a,b):
    resulta=a/b
    return resulta 
try :
    safe_division(1,10)
except ZeroDivisionError :
    print("vous avez fait une division par zero")
else:
    print(f"la resultat {safe_division(1,10)}")
finally :
    print("la fonctiona a terminee et ferme ")