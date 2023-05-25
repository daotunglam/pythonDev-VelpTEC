import random

liste = []

for i in range(0,25):
    random_zahl = random.randint(0,100)

    if random_zahl % 2 != 0:
        random_zahl = random.randint(0,100)
    else:
        liste.append(random_zahl)

produkt=1
for i in liste:
    produkt=produkt*i

print(liste)
print(produkt)

