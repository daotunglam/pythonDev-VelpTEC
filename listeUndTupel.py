import random

numbersList = [random.randint(0, 5) for _ in range(10)]

def countElement(numbersList):
    tupel_liste = []
    for element in numbersList:
        anzahl = numbersList.count(element)
        tupel = (element, anzahl)
        tupel_liste.append(tupel)

    print(tupel_liste)
    print('set',(tupel_liste))
    tupel_liste = sorted(list(set(tupel_liste)))
    print(tupel_liste)

countElement(numbersList)