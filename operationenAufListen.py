orte = ["Berlin", "München", "Leipzig", "Hannover", "Frankfurt", "Hamburg"]

# Original-Liste ausgeben
print(orte)

# 3. Eintrag durch "Garching" ersetzen und neue Liste ausgeben
orte[2] = "Garching"
print(orte)

# 2. bis 4. Eintrag durch "Nancy", "Lille" und "Nice" ersetzen und neue Liste ausgeben
orte[1:4] = ["Nancy", "Lille", "Nice"]
print(orte)

# Alle Einträge bis zum 3. löschen und Liste ausgeben
del orte[:3]
print(orte)

# Erstes Element durch ["Berlin Mitte", "Wedding"] ersetzen und Liste ausgeben
orte[0] = ["Berlin Mitte", "Wedding"]
print(orte)
