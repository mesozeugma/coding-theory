import numpy as np
import unittest
from enc.code import HammingDistance, HammingCode
from enc.finite_fields import GF


class TestHammingDistance(unittest.TestCase):
    def test_do_f2(self):
        GF2 = GF.get(2)
        a = GF2([0, 1, 0])
        b = GF2([1, 0, 0])
        self.assertEqual(HammingDistance.do(a, b), 2)

    def test_do_f3(self):
        GF3 = GF.get(3)
        u = GF3([0, 1, 2])
        v = GF3([1, 0, 0])
        self.assertEqual(HammingDistance.do(u, v), 3)


class TestHammingCode(unittest.TestCase):
    def test_encode(self):
        GF3 = GF.get(3)
        G = GF3(
            [
                [1, 0, 1, 1],
                [0, 1, 1, 2],
            ]
        )
        c = GF3([1, 2])
        np.testing.assert_array_equal(HammingCode.encode(G, c), GF3([1, 2, 0, 2]))

    def test_encode_using_u(self):
        GF3 = GF.get(3)
        U = GF3(
            [
                [1, 1],
                [1, 2],
            ]
        )
        c = GF3([1, 2])
        np.testing.assert_array_equal(
            HammingCode.encode_using_u(GF3.order, U, c), GF3([1, 2, 0, 2])
        )

    def test_max_possible_error_i(self):
        self.assertEqual(HammingCode.max_possible_error_i(2, 2), 1)

    def test_possible_error(self):
        GF3 = GF.get(3)
        np.testing.assert_array_equal(
            HammingCode.possible_error(3, 4, 4), GF3([2, 0, 0, 0])
        )

    def test_decode_zero_error(self):
        GF3 = GF.get(3)
        P = GF3(
            [
                [2, 2],
                [2, 1],
                [1, 0],
                [0, 1],
            ]
        )
        v = GF3([1, 2, 0, 2])
        np.testing.assert_array_equal(HammingCode.decode(P, v, GF3.order), v)

    def test_decode_1_error(self):
        GF2 = GF.get(2)
        P = GF2(
            [
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1],
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ]
        )
        v = GF2([1, 1, 1, 0, 1, 0, 1])
        np.testing.assert_array_equal(
            HammingCode.decode(P, v, GF2.order), GF2([1, 0, 1, 0, 1, 0, 1])
        )
