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
    if d == 10:
        print("Réussite critique")
        res = +1
    if d >= 6:
        print("Réussite")
        res = +1
    if d < 6:
        print("Echec")
        res = +0
    if d == 1:
        print("Echec critique")
        res = -1
    return(res)

def valeur(res):
    if res < 0:
        print("Echec critique")
    if res == 0:
        print("Echec")
    if res > 0:
        print("Réussite")

res = resultatGlobal
nbDes = int(input("Le nombre de dés est de : "))
print("Le résultat du lancer donne :", lancerDeDes(nbDes,nbFaces))
resultatGlobal(listeDesDes)