from random import randint

def lancerUnDe(n):
    d = randint(1,n)
    return d

def lancerDeDes(nbDes,nbFaces):
    listeDesDes = []
    for i in range(nbDes):
        d = lancerUnDe(nbFaces)
        nbFaces=10
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
            r="Echec critique", s
        if s == 0:
            r="Echec"
        if s > 0:
            r="Valeur de la réussite", s
        if s > 5:
            r="Réussite critique", s
    print(r)
        
nbDes = int(input("Saisissez le nombre de dés : "))
SR = int(input("Définissez la difficulté de votre lancer : "))
l=lancerDeDes(nbDes,nbFaces)

print("Le résultat du lancer donne : ", l)

print(resultat(l))
