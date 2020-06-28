from random import*
def lancer():
    dé = randint(1,10)
    if dé >= 6:
        a="Réussite"
    if dé == 10:
        a="Réussite critique"
    if dé == 1:
        a="Echec critique"
    if dé < 6:
        a="Echec"
    return(dé,a)

lancer = int(input("Décidez du nombre de dés que vous souhaitez lancer :", )