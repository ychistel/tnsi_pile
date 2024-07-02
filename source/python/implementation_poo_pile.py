"""
Module : implémentation d'une Pile comme les listes chainées en POO
Objets
- Cellule : permet de construire chaque élément de la Pile
- Pile : permet de construire une liste chainée créant une pile.
Fonctions
- creer_pile : pour construire une pile vide.
"""

class Maillon:
    """
    type : objet
    attributs : 
    - elt qui contient la valeur passée en argument
    - suivant : None par défaut ou un objet Cellule pour construire une liste chainée.
    méthodes:
    - constructeur __init__
    """
    def __init__(self,x,m=None):
        self.elt = x
        self.suivant = m

class Pile:
    """
    type : objet de type liste chainée
    attributs :
    - sommet : valeur au sommet de la pile
    méthodes:
    - constructeur __init__
    - empiler : ajoute un objet Cellule à l'objet Pile
    - depiler : renvoie la tête de la Pile en le supprimant
    - est_vide : renvoie un booléen (True, False) indiquant si la Pile est vide
    - len : fonction qui renvoie la hauteur de la pile;
    - __repr__ pour afficher le contenu de la pile (méthode non définie dans l'interface)
    """
    
    def __init__(self):
        self.sommet = None
        
    def empiler(self,x):
        m = self.sommet
        self.sommet = Maillon(x,m)
        
    def depiler(self):
        if not(self.est_vide()):
            sommet = self.sommet
            self.sommet = sommet.suivant
            return sommet.elt

    def est_vide(self):
        return self.sommet == None
    
    def __repr__(self):
        contenu = ''
        sommet = self.sommet
        while sommet != None:
            contenu += ' ' + str(sommet.elt)+' ]'
            sommet = sommet.suivant
        return contenu

def creer_pile():
    return Pile()

if __name__=='__main__':
    P=creer_pile()
    print("pile vide:",P.est_vide())
    P.empiler(3)
    P.empiler(7)
    print(P)
    P.empiler(9)
    print(P)
    print("pile vide:",P.est_vide())
    print(P)
    while not P.est_vide():
        P.depiler()
    print(P)
