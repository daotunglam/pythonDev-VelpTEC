class Taschenrechner:
    def __init__(self, zahl1, zahl2):
        self.zahl1 = zahl1
        self.zahl2 = zahl2

    def addieren(self):
        return self.zahl1 + self.zahl2

    def subtrahieren(self):
        return self.zahl1 - self.zahl2

    def multiplizieren(self):
        return self.zahl1 * self.zahl2

    def dividieren(self):
        if self.zahl2 != 0:
            return self.zahl1 / self.zahl2
        else:
            print("Fehler: Division durch Null!")
            return None

# Beispielanwendung
rechner = Taschenrechner(5, 3)
ergebnis_addition = rechner.addieren()
print("Ergebnis der Addition:", ergebnis_addition)

ergebnis_subtraktion = rechner.subtrahieren()
print("Ergebnis der Subtraktion:", ergebnis_subtraktion)

ergebnis_multiplikation = rechner.multiplizieren()
print("Ergebnis der Multiplikation:", ergebnis_multiplikation)

ergebnis_division = rechner.dividieren()
if ergebnis_division is not None:
    print("Ergebnis der Division:", ergebnis_division)
