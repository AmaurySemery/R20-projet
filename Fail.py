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

def resultatGlobal(listeDesDes):
    if int(d) == 10:
        print("Réussite critique")
        rc = +1
    if int(d) >= 6:
        print("Réussite")
        r = +1
    if int(d) < 6:
        print("Echec")
        e = +0
    if int(d) == 1:
        print("Echec critique")
        ec = -1
    res = int(rc) + int(r) + int(e) + int(ec)
    return(res)

def valeur(res):
    if int(res) < 0:
        print("Echec critique")
    if int(res) == 0:
        print("Echec")
    if int(res) > 0:
        print("Réussite")

res = resultatGlobal
nbDes = int(input("Le nombre de dés est de : "))
nbFaces = int(input("Le nombre de faces est de : "))
print("Le résultat du lancer donne :", lancerDeDes(nbDes,nbFaces))
resultatGlobal(listeDesDes)