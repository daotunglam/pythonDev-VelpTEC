import numpy as np

class LinearEquationSolver:
    def __init__(self, matrix, target_vector):
        self.matrix = matrix
        self.target_vector = target_vector
        self.solution = None

    def solve_equation(self):
        self.solution = np.linalg.solve(self.matrix, self.target_vector)

    def print_solution(self):
        if self.solution is not None:
            print("Solution:")
            print(self.solution)
        else:
            print("No solution available. Please solve the equation first.")

# Beispielverwendung der Klasse
matrix = np.array([[2, 3], [4, -1]])
target_vector = np.array([9, 5])

solver = LinearEquationSolver(matrix, target_vector)
solver.solve_equation()
solver.print_solution()