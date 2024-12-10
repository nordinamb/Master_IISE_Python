def analyse_texte(texte):
    mots = texte.split() 
    nb_mots = len(mots) 
    nb_caracteres = len(texte.replace(" ", ""))  
    resultat = {"nombre de mots": nb_mots, "nombre de caracteres": nb_caracteres}
    return resultat
print(analyse_texte("hello world"))  
print(analyse_texte("ça marche je pense"))  