import numpy as np

def matrix_operations():
    # Erzeugung einer zufälligen 3x3-Matrix
    matrix = np.random.rand(3, 3)
    
    # Transponierung der Matrix
    transposed_matrix = np.transpose(matrix)
    
    # Bestimmung des größten und kleinsten Elements
    max_element = np.max(matrix)
    min_element = np.min(matrix)
    
    # Berechnung des Produkts der Matrixelemente
    product = np.prod(matrix)
    
    # Rückgabe der Ergebnisse
    return matrix, transposed_matrix, max_element, min_element, product

# Beispielaufruf der Funktion
result = matrix_operations()
print("Zufallsmatrix:")
print(result[0])
print("Transponierte Matrix:")
print(result[1])
print("Größtes Element:", result[2])
print("Kleinstes Element:", result[3])
print("Produkt der Matrixelemente:", result[4])
