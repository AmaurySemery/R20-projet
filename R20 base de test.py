import random

def lancerUnDe(n):
    d = random.randint(1,n)
    return d

def lancerDeDes(nbDes,nbFaces):
    listeDesDes = []
    for i in range(nbDes):
        d = lancerUnDe(nbFaces)
        nbFace=10
        listeDesDes.append(d)
    return listeDesDes

def lancer(listeDesDes):
    if d >= 6:
        a=r
    if d == 10:
        a=rc
    if d == 1:
        a=ec
    if d < 6:
        a=e
    return(d,a)

def resultatGlobal(lancerDeDes):
    r = 1
    e = 0
    ec = -1
    res = r + e + ec
    if res < 0:
        print("Echec critique")
    if res == 0:
        print("Echec")
    if res > 0:
        print("Réussite")
    return(res)

nbDes = int(input("Le nombre de dés est de : "))
print("Le résultat du lancer donne :", lancerDeDes(nbDes,nbFaces))
resultatGlobal(lancerDeDes)