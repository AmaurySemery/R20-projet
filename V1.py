import random
a=0

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
        if int(i) == 10 or int(i) >= 6:
            res = int(a)+1
        if int(i) < 6:
            res = int(a)+0
        if int(i) == 1:
            res = int(a)-1
        return(res)

def valeur(resultatGlobal):
    for res in range(nbDes):
        if int(res) < 0:
            print("Echec critique")
        if int(res) == 0:
            print("Echec")
        if int(res) > 0:
            print("Réussite")
            
nbDes = int(input("Saisissez le nombre de dés : "))
nbFaces = int(input("Saisissez le nombre de faces pour chaque dé : "))
print("Le résultat du lancer donne : ",lancerDeDes(nbDes,nbFaces))
resultatGlobal(lancerDeDes)
valeur(resultatGlobal)
