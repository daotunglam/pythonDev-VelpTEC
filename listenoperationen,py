

liste = [32, 23, 5, 23, 23, 6, 66, 23, 12, 12, 535, 654, 4]
quadListe = []

def listenOperation(liste: list, quadListe: list):
    for i in liste:
        quadListe.append(i*i)

    summe = sum(quadListe)

    quadListe = sorted(quadListe)
    quadListe = set(quadListe)
    quadListe = list(quadListe)
    return max(liste), quadListe, summe

print(listenOperation(liste, quadListe))