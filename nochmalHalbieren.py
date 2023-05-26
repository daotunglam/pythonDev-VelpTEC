def halbieren(zahl):
    zahl = zahl/2
    print(zahl)
    if zahl > 0.1:
        halbieren(zahl)

halbieren(3)