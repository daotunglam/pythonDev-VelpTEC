def calculateFactorial(n):
    if n == 0:
        return 1
    else:
        return n * calculateFactorial(n-1)

a = input('Wir berechnen Fakultät von Nummer: ')
print('Ergebnis:', calculateFactorial(int(a)))