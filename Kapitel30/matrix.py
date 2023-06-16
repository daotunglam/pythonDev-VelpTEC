import numpy as np

def matrix_operation():
    # Erzeugung einer 3x3-Einheitsmatrix
    matrix_einheit = np.eye(3)

    # Erzeugung einer quadratischen Matrix aus Einsen
    matrix_einsen = np.ones((3, 3))

    # Erzeugung einer quadratischen Matrix aus zufälligen Elementen
    matrix_zufall = np.random.random((3, 3))

    # Addition der Matrizen
    matrix_summe = matrix_einheit + matrix_einsen + matrix_zufall

    # Multiplikation der Matrizen mit der letzten Zeile auf 0 setzen
    matrix_produkt = matrix_einheit * matrix_einsen * matrix_zufall
    matrix_produkt[-1, :] = 0
    print('matrix_produkt')
    print(matrix_produkt)

    # Multiplikation der Matrizen mit der letzten Zeile auf 0 setzen
    p=np.dot(np.dot(matrix_einheit,matrix_einsen),matrix_zufall)
    p[-1, :] = 0
    print('p')
    print(p)

    return matrix_zufall, matrix_summe, matrix_produkt

# Beispielaufruf der Funktion
zufallsmatrix, summe, produkt = matrix_operation()

print("Zufallsmatrix:")
print(zufallsmatrix)
print("\nSumme:")
print(summe)
print("\nProdukt:")
print(produkt)
