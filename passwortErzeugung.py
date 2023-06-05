import random

name = input('den Namen : ')
alter = input('das Alter : ')
gehalt = input('das Gehalt : ')

eingabe = name + gehalt + str(alter)
passwort = ''.join(random.choice(eingabe) for _ in eingabe)
dic = {'Name': name, 'Alter': alter, 'Gehalt': gehalt, 'Passwort': passwort}
print(dic)

print(iter((set(passwort))))