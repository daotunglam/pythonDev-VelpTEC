import math
import random

n = random.uniform(0, 10)
print("Zufällige Zahl:", n)

# Berechne die Quadratwurzel auf zwei Nachkommastellen genau
square_root = round(math.sqrt(n), 2)
print("Quadratwurzel:", square_root)

# Berechne den natürlichen Logarithmus
natural_logarithm = math.log(n)
print("Natürlicher Logarithmus:", natural_logarithm)

# Berechne den Logarithmus zur Basis 10
log_base_10 = math.log10(n)
print("Logarithmus zur Basis 10:", log_base_10)

# Berechne die Fakultät der zufälligen Zahl
factorial = math.factorial(int(n))
print("Fakultät:", factorial)

# Berechne (r hoch r) + r
result = math.pow(n, n) + n

# Berechne den größten gemeinsamen Teiler zwischen r und der neuen Zahl
gcd = math.gcd(int(n), int(result))
print("Größter gemeinsamer Teiler:", gcd)
