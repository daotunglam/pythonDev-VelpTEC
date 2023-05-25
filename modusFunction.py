liste = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]

def modus(liste):
    d = {}
    for i in liste:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    modus = []
    max_häufigkeit = max(d.values())
    for i, häufigkeit in d.items():
        if häufigkeit == max_häufigkeit:
            modus.append(i)

    return modus

print(modus(liste))