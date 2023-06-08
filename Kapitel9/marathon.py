import time
print('Marathon')

print()
nummer = ' ' #1
daten = open('Kapitel9/marathon/daten.txt', 'w')
while nummer != '':
    nummer = input('Startnummer (Ende mit <Enter>): ')
    daten.write(nummer + ': ' + time.asctime() + '\n') #2
    daten.flush() #3
print()
print('Die Daten befinden sich in der Datei Kapitel9/marathon/daten.txt')
daten.close()