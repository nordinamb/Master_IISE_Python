def intersection(ensemble1, ensemble2) :
#intialisation d'ensemble de retourne
    s=set()
    for i in ensemble1 :
        for j in ensemble2:
            if i == j:
                s.add(j)
    return s
print(intersection({4,'cc',-4,'aaa'},{3,-4,'aaa','ask'}))