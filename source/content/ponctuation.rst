TP : Ponctuation
==================

On rencontre en informatique et en mathématiques des expressions contenant des **ponctuations** comme les parenthèses, les crochets, des accolades et même les guillemets (quotes). 

Par exemple, en python, les structures de données comme les listes ou les dictionnaires utilisent des crochets et des accolades. 

Comment vérifier que la ponctuation d'une expression est correcte ?

#.  On donne trois expressions avec ponctuation.

    a.  ``(4-(5+2))*3``
    b.  ``f(x)=[(x+1)^{2}-2]*(x-1)``
    c.  ``d = {'a':[1,2],'b':(3,4),'c':[(5,6),(7,8)]}``

    Comment peut-on s'assurer que la ponctuation est correcte dans ces expressions ?

#.  On considère que chaque expression est une chaine de caractères. Écrire en python la fonction ``verifie`` qui prend en paramètre une chaine de caractères et qui renvoie un tableau contenant toute la ponctuation de l'expression. 

    Par exemple, si on applique le script aux trois expressions ci-dessus, on obtient les tableaux:

    a.  ``['(', '(', ')', ')']``
    b.  ``['(', ')', '[', '(', ')', '{', '}', ']', '(', ')']``
    c.  ``['{', "'", "'", '[', ']', "'", "'", '(', ')', "'", "'", '[', '(', ')', '(', ')', ']', '}']``

#.  Comment reconnaître que la ponctuation d'une expression est correcte en analysant les tableaux renvoyés par la fonction ``verifie`` ?

#.  Une pile est une structure qui convient très bien pour vérifier la ponctuation d'une expression.

    a.  Expliquer en quoi l'utilisation d'une pile répond au problème.
    b.  Modifier la fonction ``verifie`` en utilisant une pile de façon à renvoyer un booléen qui affirme que l'expression est bien ponctuée ou non.