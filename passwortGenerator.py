import random

print('Diese File erzeugt ein Passwort mit zehn Stellen \
      \n durch eine zufällige Kombination von Buchstaben und Zahlen!')

alphabet = "abcdefghijklmnopqrstuvwxyz"
password = ""
password_length = 10

for i in range(password_length):
    # Wähle einen zufälligen Buchstaben aus einer Alphabetsliste aus:
    randomIndex = random.randint(0, len(alphabet)-1)
    buchstabe = alphabet[randomIndex]

    # Die erste Stelle und jede dritte Stelle des Passworts sollen
    # eine Zahl zwischen 0 und 9 sein:
    if i % 3 == 0:
        random_zahl = random.randint(0, 9)
        password = password + str(random_zahl)
    else:
        password = password + buchstabe

print(password)
