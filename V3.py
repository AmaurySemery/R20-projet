from random import randint

def lancerUnDe(n):
    d = randint(1,n)
    return d

def lancerDeDes(nbDes,nbFaces):
    listeDesDes = []
    for i in range(nbDes):
        d = lancerUnDe(nbFaces)
        listeDesDes.append(d)
    return listeDesDes
 
def resultat(lancer):
    s = 0
    reu = 0
    for i in lancer:
        if i >= SR:
            s=s+1
        if i > 1 and i < SR:
            s=s
        if i == 1:
            s=s-1
        if s < 0:
            r="Echec critique"
        if s == 0:
            r="Echec"
        if s > 0:
            r="Valeur de la réussite", s
    print(r)
        
nbDes = int(input("Saisissez le nombre de dés : "))
nbFaces = int(input("Saisissez le nombre de faces pour chaque dé : "))
SR = int(input("Définissez la difficulté de votre lancer : "))
l=lancerDeDes(nbDes,nbFaces)

print("Le résultat du lancer donne : ", l)

print(resultat(l))
