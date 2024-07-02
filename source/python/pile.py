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
        self.elt=x
        self.suivant=m

class Pile:
    """
    type : objet de type liste chainée
    attributs :
    - taille : nombre entier indiquant le nombre de Cellules
    - sommet : valeur au sommet de la pile
    méthodes:
    - constructeur __init__
    - empiler : ajoute un objet Cellule à l'objet Pile
    - depiler : renvoie la tête de la Pile en le supprimant
    - sommet : renvoie la valeur du sommet de la Pile sans la dépiler
    - est_vide : renvoie un booléen (True, False) indiquant si la Pile est vide
    - len : fonction qui renvoie la hauteur de la pile;
    - __repr__ pour afficher le contenu de la pile (méthode non définie dans l'interface)
    """
    
    def __init__(self):
        self.taille=0
        self.top=None
        
    def empiler(self,x):
        m = self.top
        self.top=Maillon(x,m)
        self.taille +=1
        
    def sommet(self):
        if self.taille>0:
            return self.top.elt
        
    def depiler(self):
        if self.taille > 0:
            top=self.top
            self.top = top.suivant
            self.taille -= 1
            return top.elt
     
    def est_vide(self):
        return self.taille == 0
    
    def __len__(self):
        return self.taille
    
    def __repr__(self):
        contenu = ''
        top=self.top
        while top != None:
            #contenu = '[ ' + str(top.elt)+' '+contenu
            contenu += ' ' + str(top.elt)+' ]'
            top=top.suivant
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
    print("hauteur de la pile:",len(P))
    print("sommet:",P.sommet())
    print(P)
    while not P.est_vide():
        P.depiler()
    print(P)
