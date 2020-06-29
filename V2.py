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

def resultatGlobal(lancerDeDes):
    for i in range(nbDes):
        if i == 10 or i >= 6:
            print("Réussite")
        if i < 6:
            print("Echec")
        if i == 1:
            print("Echec critique")
        

nbDes = int(input("Saisissez le nombre de dés : "))
nbFaces = int(input("Saisissez le nombre de faces pour chaque dé : "))
print("Le résultat du lancer donne : ",lancerDeDes(nbDes,nbFaces))
lancerDeDes(nbDes,nbFaces)
resultatGlobal(lancerDeDes)
