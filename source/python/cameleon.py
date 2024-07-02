class File:

    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def enfiler(self,valeur):
        self.contenu.append(valeur)

    def defiler(self):
        return self.contenu.pop(0)
    
def creer_file():
    return File()


# File pour cameléon 1 (dessus)
C1 = creer_file()
#C1.enfiler("V")
C1.enfiler("B")
C1.enfiler("V")
C1.enfiler("B")
#C1.enfiler("B")
#C1.enfiler("V")
#C1.enfiler("B")

# File pour caméléon 2 (dessous)
C2 = creer_file()
#C2.enfiler("B")
C2.enfiler("V")
C2.enfiler("B")
C2.enfiler("V")
#C2.enfiler("B")
#C2.enfiler("V")
#C2.enfiler("B")

def cases_en_contact(h,b):
    if (h,b) == ("V","V"):
        return ("B","B")
    elif (h,b) == ("B","V"):
        return ("V","B")
    elif (h,b) == ("V","B"):
        return ("V","V")
    else:
        return ("B","V")
    
def croiser(C1,C2):
    # Caméléon 1 après croisement
    F1 = creer_file()
    # Caméléon 2 après croisement
    F2 = creer_file()

    while not C1.est_vide():
        h = C1.defiler()
        while not C2.est_vide():
            b = C2.defiler()
            h,b = cases_en_contact(h,b)
            F2.enfiler(b)
        while not F2.est_vide():
            C2.enfiler(F2.defiler())
        F1.enfiler(h)
    while not F1.est_vide():
        C1.enfiler(F1.defiler())
    return C1,C2

croiser(C1,C2)
print(C1.contenu,C2.contenu)
    