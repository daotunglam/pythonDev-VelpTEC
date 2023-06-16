import numpy as np

class LinearEquationSolver:
    def __init__(self, matrix, target_vector):
        self.matrix = matrix
        self.target_vector = target_vector
        self.solution = None

    def solve(self):
        # Überprüfen, ob die Anzahl der Unbekannten mit der Anzahl der Gleichungen übereinstimmt
        if self.matrix.shape[0] != self.matrix.shape[1] or self.matrix.shape[0] != len(self.target_vector):
            print("Ungültiges Gleichungssystem. Die Anzahl der Unbekannten stimmt nicht mit der Anzahl der Gleichungen überein.")
            return

        # Lösung des Gleichungssystems
        try:
            self.solution = np.linalg.solve(self.matrix, self.target_vector)
        except np.linalg.LinAlgError:
            print("Das Gleichungssystem ist singulär. Es existiert keine eindeutige Lösung.")
            return

    def print_solution(self):
        if self.solution is None:
            print("Das Gleichungssystem wurde noch nicht gelöst.")
        else:
            print("Lösung des Gleichungssystems:")
            for i, unknown in enumerate(self.solution):
                print(f"Unbekannte x{i+1}: {unknown}")

# Beispielverwendung der Klasse
matrix = np.array([[2, 3], [4, -1]])
target_vector = np.array([9, 5])

solver = LinearEquationSolver(matrix, target_vector)
solver.solve()
solver.print_solution()
