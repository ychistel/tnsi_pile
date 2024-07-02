from implementation_poo_pile import *

def hauteur(pile):
    h = 0
    q = creer_pile()
    while not(pile.est_vide()):
        q.empiler(pile.depiler())
        h += 1
    while not(q.est_vide()):
        pile.empiler(q.depiler())
    return h

if __name__ == '__main__':
    P = creer_pile()
    P.empiler(5)
    P.empiler(7)
    P.empiler(4)
    print(P)
    print(hauteur(P))
    x = P.depiler()
    print(f"le sommet {x} et la pile {P}")
    