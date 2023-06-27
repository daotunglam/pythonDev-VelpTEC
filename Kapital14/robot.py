import os
from os import walk
from os.path import join, normcase
SUCHBERICHT="""
Suchbericht
-----------
{}
Es wurden {} Dateien durchsucht.
{} Dateien waren nicht lesbar.
""" #1
print(os.getcwd())
class suchRobot:
    def __init__(self, suchwort, wurzel):
        self.ergebnis = []
        self.suchwort = suchwort
        self.wurzel = wurzel
        self.nicht_lesbar = 0
        self.durchsucht = 0
        liste = walk(wurzel) #2
        print(liste)
        for pfad, verzeichnisse, dateien in liste:
            for datei in dateien:
                self.durchsucht += 1 #3
                try:
                    f = open(join(pfad, datei), 'r') #4
                    text = f.read() #5
                    f.close()
                    n = text.count(suchwort) #6
                    if n > 0:
                        p = normcase(join(pfad, datei)) #7
                        self.ergebnis += [(n, p)]
                except:
                    self.nicht_lesbar += 1
            self.ergebnis.sort(reverse=True)

def __str__(self): #10
    tabelle = ""
    for (n, pfad) in self.ergebnis:
        tabelle += '{} ({} Vorkommen )\n'.format(pfad, n, self.suchwort)
    return SUCHBERICHT.format(  tabelle,self.durchsucht,self.nicht_lesbar)

# Hauptprogramm
wurzel = '/Users/lam90/IT/pythonDev-VelpTEC/Kapital14'
print('Wir suchen Wort hier', wurzel)
suchwort = input("Suchwort: ")
# wurzel = input("Wurzelverzeichnis: ")
bot = suchRobot(suchwort, wurzel)
print(bot)