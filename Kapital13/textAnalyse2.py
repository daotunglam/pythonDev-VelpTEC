import numpy
daten = open('Kapital13/sometext.txt', mode='r',encoding='utf-8')
text=daten.read()
daten.close()
print(text)

def func(text):

    text = text.lower()
    worte = text.split()
    wortliste = []
    anzahlliste = []

    for wort in worte:
        number = wort.count('e')
        dic = {'Wort': wort, '#e': number}
        anzahlliste.append(number)
        wortliste.append(dic)

    maxindex = numpy.argmax(anzahlliste)
    max_wort= wortliste[maxindex]

    text = text.encode()
    return max_wort, text, wortliste

print(func(text))