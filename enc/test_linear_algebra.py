import numpy as np
import unittest
from enc.finite_fields import GF
from enc.linear_algebra import LinearSystem


class TestLinearSystem(unittest.TestCase):
    def test_solve(self):
        GF2 = GF.get(2)
        A = GF2(
            [
                [0, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
            ]
        )
        b = GF2([0, 0, 1, 1])
        np.testing.assert_array_equal(LinearSystem.solve(A, b), GF2([1, 0, 1, 1]))
