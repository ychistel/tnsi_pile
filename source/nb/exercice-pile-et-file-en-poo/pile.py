"""
Module : implémentation d'une Pile comme les listes chainées en POO
Objets
- Maillon : permet de construire chaque élément de la Pile
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
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        if self.suivant is None:
            return "[ "+str(self.valeur)
        else:
            return str(self.suivant) + " [ " +str(self.valeur)
        
class Pile:
    """
    type : objet de type liste chainée
    attributs :
    - taille : nombre entier indiquant le nombre de