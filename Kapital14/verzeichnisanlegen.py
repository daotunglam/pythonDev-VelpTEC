from os import makedirs
vorname = input('Vorname: ')
nachname = input('Nachname: ')
verzeichnisname = (vorname[:6]+nachname[:2]).lower() #1
try:
    makedirs('Kapital14/'+verzeichnisname) #2
    print('Verzeichnis angelegt')
except:
    print('Verzeichnis existiert bereits')