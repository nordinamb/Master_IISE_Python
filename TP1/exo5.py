def factorielle(n):
    if n < 0:
        return "error !!"
    elif n == 0 :
        return 1
    else:
        return n * factorielle(n-1)
print(factorielle(4)) 