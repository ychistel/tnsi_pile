Exercice pratique
=================

Nous avons l'habitude de noter les expressions arithmétiques avec des parenthèses comme par exemple : (2 + 3) × 5.

Il existe une autre notation utilisée par certaines calculatrices, appelée notation postfixe, qui
n'utilise pas de parenthèses. L'expression arithmétique précédente est alors obtenue en
saisissant successivement 2, puis 3, puis l'opérateur +, puis 5, et enfin l'opérateur ×. On
modélise cette saisie par le tableau ``[2, 3, '+', 5, '*']``.

Autre exemple, la notation postfixe de 3 × 2 + 5 est modélisée par le tableau : ``[3, 2, '*', 5, '+']``.

D'une manière plus générale, la valeur associée à une expression arithmétique en notation
postfixe est déterminée à l'aide d’une pile en parcourant l'expression arithmétique de gauche
à droite de la façon suivante :

-  si l'élément parcouru est un nombre, on le place au sommet de la pile ;
-  si l'élément parcouru est un opérateur, on récupère les deux éléments situés au sommet de la pile et on leur applique l'opérateur. On place alors le résultat au sommet de la pile ;
-  à la fin du parcours, il reste alors un seul élément dans la pile qui est le résultat de l'expression arithmétique.

Dans le cadre de cet exercice, on se limitera aux opérations × et +.

Pour cet exercice, on dispose d’une classe ``Pile`` qui implémente les méthodes de base sur la structure de pile.

Compléter le script de la fonction eval_expression qui reçoit en paramètre une liste python représentant la notation postfixe d'une expression arithmétique et qui renvoie sa valeur associée.

.. literalinclude:: ../python/ep_pr_1.py