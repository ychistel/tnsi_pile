"""
Module : implémentation d'une File par des listes chainées en POO
Objets
- Maillon : permet de construire chaque élément de la File
- File : permet de construire une liste chainée créant une file.
Fonctions
- creer_file : pour construire une file vide.
"""

class Maillon:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
        
    def __repr__(self):
        if self.suivant is None:
            return str(self.valeur) 
        else:
            return str(self.valeur) + " < " + str(self.suivant)


class File:
    
    """
    type : objet de type liste chainée
    attributs :
    - maillon : objet Maillon ou None si vide
    méthodes:
    - constructeur __init__
    - enfiler : ajoute un objet Cellule à l'objet File
