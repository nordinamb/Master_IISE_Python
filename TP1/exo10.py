def fusionner_dicts(dict1, dict2):
    resultat = dict1.copy() 
    for key in dict2:
        if key in resultat:
            resultat[key] += dict2[key]  
        else:
            resultat[key] = dict2[key]  
    return resultat
dict1 = {'h': 3, 'j': 4, 'd': 5}
dict2 = {'j': 6, 'h': 2, 'd': 4}
print(fusionner_dicts(dict1, dict2))  