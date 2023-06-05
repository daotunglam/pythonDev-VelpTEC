import random

numbersList1 = [random.randint(0, 100) for _ in range(20)]
numbersList2 = [random.randint(0, 100) for _ in range(20)]

def mengen(list1, list2):
    menge1 = set(list1)
    menge2 = set(list2)
    sames = menge1 & menge2
    differences = menge1 - menge2
    if menge1 <= menge2 :
        print('menge1 ist Teilmengen von menge2 ')
    elif menge2 <= menge1 :
        print('menge2 ist Teilmengen von menge1')
    else:
        print('Keine der Mengen ist eine Teilmenge der anderen')

    print(menge1, menge2, sames)

mengen(numbersList1, numbersList2)

def listComprehenion():
    minmaxListe = []
    for _ in range(20):
        numbersliste = [random.randint(0, 100) for _ in range(20)]
        minmaxListe.append((min(numbersliste), max(numbersliste)))
    return(minmaxListe)

def minAbstand():
    minmaxListe = listComprehenion()
    abstandsListe = [tuple[1] - tuple[0] for tuple in minmaxListe]
    print('abstandsListe', abstandsListe)
    return abstandsListe.index(min(abstandsListe))

print('listComprehenion',minAbstand())