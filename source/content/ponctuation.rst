Activité
========

On rencontre en informatique et en mathématiques des expressions contenant des **ponctuations** comme les parenthèses, les crochets, des accolades et même les guillemets (quotes). 

Par exemple, en python, les structures de données comme les listes ou les dictionnaires utilisent des crochets et des accolades. 

Comment vérifier que la ponctuation d'une expression est correcte ?

#. On donne trois expressions avec ponctuation.

   a. ``(4-(5+2))*3``
   b. ``f(x)=[(x+1)^{2}-2]*(x-1)``
   c. ``d = {'a':[1,2],'b':(3,4),'c':[(5,6),(7,8)]}``

   Comment peut-on s'assurer que la ponctuation est correcte dans ces expressions ?

#. On considère que chaque expression est une chaine de caractères. Écrire en python la fonction ``verifie`` qui prend en paramètre une chaine de caractère et qui renvoie un tableau contenant toute la ponctuation de l'expression. 

   Par exemple, si on applique le script au trois expressions ci-dessus, on obtient les tableaux:

   a. ``['(', '(', ')', ')']``
   b. ``['(', ')', '[', '(', ')', '{', '}', ']', '(', ')']``
   c. ``['{', "'", "'", '[', ']', "'", "'", '(', ')', "'", "'", '[', '(', ')', '(', ')', ']', '}']``

#. Comment reconnaître que la ponctuation d'une expression est correcte en analysant les tableaux renvoyés par la fonction ``verifie`` ?
#. Il existe une structure de données appelée **pile** qui est dite **lifo** pour **last in, first out** (dernier arrivé, premier sorti). L'accès aux valeurs qu'elle contient se fait uniquement sur la dernière valeur insérée appelée **sommet** de la pile. Il est impossible d'accéder à une valeur tant qu'elle n'est pas le sommet de la pile.

   L'interface d'une pile est la suivante:

   - **creer_pile** qui crée une pile vide;
   - **empiler** qui ajoute une valeur à la pile;
   - **depiler** qui retire le sommet de la pile;
   - **est_vide** qui renvoie un booléen vérifiant si la pile est vide ou non.

   a. Une liste python a-t-elle une structure de pile ? Justifier.
   b. Qu'elles sont les méthodes de listes python qui peuvent être utilisées pour qu'une liste soit traitée comme une pile ?

#. Une pile est une structure qui convient pour vérifier la ponctuation d'une expression.

   a. Expliquer comment l'utilisation d'une pile répond au problème.
   b. Modifier la fonction ``verifie`` en utilisant une pile de façon à renvoyer un booléen qui affirme que l'expression est bien ponctuée ou non.