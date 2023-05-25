# Entwickle ein kleines Geografie-Spiel! Über die Eingabekonsole soll der/die Spieler*in Hauptstädte von Ländern erraten. Das Spiel sollte folgende Eigenschaften haben:

# Bei richtiger Antwort kommt ein „Richtig!”.
# Bei falscher Antwort kommt ein „Falsche Antwort! Die richtige Antwort ist: “ und dann die richtige Antwort.
# Im Hintergrund zählt das Spiel die Anzahl der richtigen Antworten mit und sagt dem/der Spieler*in am Ende, wie viel Prozent seiner/ihrer Antworten richtig waren.
# Zu Beginn des Spiels musst du ein Dictionary mit Ländern und Städten definieren.
# 		Nutze die items()-Funktion, um die Elemente des Dictionaries iterierbar zu machen.


# Dictionary mit Ländern und Hauptstädten
laender_hauptstaedte = {
    'Deutschland': 'Berlin',
    'Frankreich': 'Paris',
    'Vietnam': 'Hanoi',
    'Italien': 'Rom',
    'Spanien': 'Madrid',
    'Österreich': 'Wien',
    'Schweiz': 'Bern',
    'Niederlande': 'Amsterdam',
    'Belgien': 'Brüssel',
    'Polen': 'Warschau',
    'Portugal': 'Lissabon'
}

laender_hauptstaedte = laender_hauptstaedte.items()
print(laender_hauptstaedte)

score = 0

for land, hauptstadt in laender_hauptstaedte:
    answer=input('Hauptstadt von ' + land + ' ist:')
    if answer==hauptstadt:
        score += 1
        print('Richtig')
    else:
        print('Falsch.', hauptstadt)

prozentsatz_richtig = 100*score/len(laender_hauptstaedte)
print('Du hast '+ str(prozentsatz_richtig) + '% richtig geanwortet')