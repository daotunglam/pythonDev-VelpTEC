s = 'Hallo, wie geht es dir? Mir geht es eigentlich gut.'


def wortSeparat(text):
    words = text.split()
    print(words)

    listWords = [list(word) for word in words]
    print(listWords)
    
wortSeparat(s)
