import numpy as np


class LinearSystem:
    def solve(A: np.ndarray, b: np.ndarray):
        return np.linalg.solve(A, b)
