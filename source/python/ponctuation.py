def verifie_ponctuation(exp):
    pct = ['(',')','[',']','{','}','\'','\"']
    p = []
    for c in exp:
        if c in pct:
            p.append(c)
    return p
def ponctuation_ouvrante_fermante(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    if p1 == '[' and p2 == ']':
        return True
    if p1 == '{' and p2 == '}':
        return True
    if p1 == p2 == '\'':
        return True
    if p1 == p2 == '"':
        return True
    return False


def verifie(exp):
    pct = ['(',')','[',']','{','}','\'','\"']
    # on crée une pile vide
    p = []

    for c in exp:
        if c in pct:
            # on depile le sommet de la pile p si non vide
            if p != []:
                sp = p.pop()
                # on vérifie que les 2 ponctuations sont ouvrantes - fermantes
                if not ponctuation_ouvrante_fermante(sp,c):
                    # si les 2 ponctuations ne sont pas ouvrantes - fermantes, on les empile
                    p.append(sp)
                    p.append(c)
            else:
                # on empile le signe de ponctuation c
                p.append(c)
        print(p)
    return p == []

e1 = '(4-(5+2))*3'
e2 = 'f(x)=[(x+1)^{2}-2]*(x-1)'
e3 = "d={'a':[1,2],'b':(3,4),'c':[(5,6),(7,8)]"
#print(verifie_ponctuation(e1))
print(verifie(e1))
#print(verifie_ponctuation(e2))
print(verifie(e2))
#print(verifie_ponctuation(e3))
print(verifie(e3))