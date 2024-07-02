def creer_pile():
    return []

def est_vide(p):
    return p == []

def empiler(p,e):
    p.append(e)
    return p

def depiler(p):
    e = p.pop()
    return e

T = creer_pile()
T = empiler(T,2)
empiler(T,5)
v = depiler(T)
v = v - 3
empiler(T,v)
