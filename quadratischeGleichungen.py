import math

print('Wir lösen quadratische Gleichungen ax^2 + bx + c = 0')

a = float(input('Gib a ein Zahl ein: '))
b = float(input('Gib b ein Zahl ein: '))
c = float(input('Gib c ein Zahl ein: '))


def loesung(a, b, c):
    delta = b**2 - 4*a*c
    if a == 0:
        if b == 0:
            if c == 0:
                print('Jede x ist die Lösung')
            else:
                print('Keine Lösung')
        else:
            print('x =', -c/b)
    else:
        if delta < 0:
            print('Keine Lösung')
        elif delta == 0:
            print('x =', -b / (2*a))
        else:
            print('x1 =', (-b + math.sqrt(delta))/2*a)
            print('x2 =', (-b - math.sqrt(delta))/2*a)


loesung(a, b, c)
