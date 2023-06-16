import math

class MathFunctions:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_sin_squared(self):
        result = math.sin(self.x) ** 2
        return result
    
    def calculate_greatest_common_divisor(self):
        x_int = int(self.x)
        y_int = int(self.y)
        
        # Euklidischer Algorithmus zur Berechnung des größten gemeinsamen Teilers
        while y_int != 0:
            x_int, y_int = y_int, x_int % y_int
            
        return x_int


math_functions = MathFunctions(120, 18)
sin_squared = math_functions.calculate_sin_squared()
gcd = math_functions.calculate_greatest_common_divisor()

print("sin^2(x^y):", sin_squared)
print("Größter gemeinsamer Teiler:", gcd)
