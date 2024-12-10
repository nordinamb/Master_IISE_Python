def somme_varargs(*args):
  somme = 0
  for arg in args:
    somme += arg
  return somme
print(somme_varargs(9, 10, 20))   
print(somme_varargs(8, 2, 6, 4)) 