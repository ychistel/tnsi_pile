def creer_pile():
    return []

def est_vide(pile):
    return pile == []

def empiler(pile, element):
    pile.append(element)
    return pile

def depiler(pile):
    s = pile.pop()
    return s

def hauteur(pile):
    h = 0
    while not est_vide(pile):
        h += 1
        depiler(pile)
    return h

P = creer_pile()
P = empiler(P,7)
P = empiler(P,3)
P = empiler(P,5)
P = empiler(P,4)
print(P)
haut = hauteur(P)
print(haut,P)


