import os
from os.path import join, getsize

ABSCHLUSSBERICHT = """
Ich habe {} Verzeichnisse durchsucht. Der gesamte Speicherbedarf beträgt {} Bytes.
"""

class Platzbedarf:
    def __init__(self, wurzel):
        self.ergebnis = []
        liste = os.walk(wurzel)
        for v, u, d in liste:
            groesse = sum([getsize(join(v, name))
                           for name in d])
            self.ergebnis.append((v, groesse))

    def __str__(self):
        bericht = ""
        for v, s in self.ergebnis:
            bericht += ('{} ({} Byte)\n'.format(v, s))
        bericht += ABSCHLUSSBERICHT.format(len(self.ergebnis),
                                           sum([i[1] for i in self.ergebnis]))
        return bericht
    
# Hauptprogramm zum Testen
print(Platzbedarf('/Users/lam90/IT/pythonDev-VelpTEC/Kapital14'))