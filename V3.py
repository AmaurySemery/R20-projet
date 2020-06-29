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
        
nbDes = int(input("Saisissez le nombre de dés : "))
nbFaces = int(input("Saisissez le nombre de faces pour chaque dé : "))
lancer = print("Le résultat du lancer donne : ",lancerDeDes(nbDes,nbFaces))

def resultat(lancer):
    for i in lancerDeDes(nbDes,nbFaces):
        if i > 5:
            print("Réussite")
        else:
            print("Echec")

print(resultat(lancer))
