.. TNSI

Activité
========

Introduction
------------

La pile est un type abstrait de données qui n'existe pas dans Python. Les éléments d'une pile sont gérés de la façon suivante:

- On construit une pile vide au début;
- Un nouvel élément qui est ajouté dans la pile est le sommet de la pile.
- On ne peut accéder qu'au sommet de la pile. 
- Si on veut récupérer un élément quelconque de la pile, il faut enlever les éléments situés au-dessus jusqu'au sommet.

1. On donne sur l'image ci-dessous les différents états d'une pile ``P``. Quelles sont les actions réalisées sur cette pile pour obtenir dans l'ordre ces différents états ?

.. image:: ../img/pile_fig1.svg
   :align: center
   :width: 70%
   
2. On effectue les actions suivantes sur une pile ``Q``:

   - on crée la pile.
   - on ajoute dans l'ordre les valeurs 3 et 7. 
   - on récupère le sommet.
   - on ajoute dans l'ordre les valeurs 8 et 4.
   - on récupère le sommet.

   Représenter les différents états de la pile Q.
   
Interface d'une pile
--------------------

Une interface est l'ensemble des actions que l'on peut réaliser sur une structure de données. L'interface d'une pile contient:

- un **constructeur** qui crée une pile vide : ``creer_pile``
- des **accesseurs** qui donnent des informations sur la pile. Par exemple savoir si la pile est vide ou non : ``est_vide``.
- des **opérateurs** qui permettent d'ajouter et enlever des éléments de la pile : ``empiler`` pour ajouter un élément et ``depiler`` pour enlever le sommet en récupérant sa valeur.

1. On donne les instructions suivantes:

.. code:: python

   T = creer_pile()
   T = empiler(T,2)
   T = empiler(T,5)
   v = depiler(T)
   v = v - 1
   T = empiler(T,v)
   
   Représenter les différents états de la pile en exécutant cette suite d'instructions.
   
2. On reprend la pile ``P`` de la partie précédente. Donner en utilisant l\'**interface** de la pile les instructions qui permettent d'obtenir les différents états de la pile dans l'illustration.

Implémentation d'une pile
-------------------------

On peut **implémenter** en Python l'interface d'une pile en utilisant les listes.

1. Quelles fonctions ou méthodes de listes nous permettent de réaliser les 4 fonctions de notre interface ?
2. Compléter les fonctions suivantes pour implémenter l'interface de la pile avec des listes.

   .. code:: python

      def creer_pile():
         return ...
         
      def est_vide(p):
         ...
         
      def empiler(p,e):
         ...

      def depiler(p):
         ...

3. Vérifier  votre interface en réalisant les piles P, Q et T.
