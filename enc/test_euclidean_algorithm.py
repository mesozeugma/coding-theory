import unittest
from enc.euclidean_algorithm import (
    EuclideanAlgorithm,
    ExtendedEuclideanAlgorithm,
    ExtendedEuclideanAlgorithmResult,
)


class TestEuclideanAlgorithm(unittest.TestCase):
    def test_do_360_225(self):
        self.assertEqual(EuclideanAlgorithm.do(360, 225), 45)

    def test_do_225_360(self):
        self.assertEqual(EuclideanAlgorithm.do(225, 360), 45)

    def test_do_402_123(self):
        self.assertEqual(EuclideanAlgorithm.do(402, 123), 3)


class TestExtendedEuclideanAlgorithm(unittest.TestCase):
    def test_do_360_225(self):
        result = ExtendedEuclideanAlgorithm.do(360, 225)
        self.assertEqual(
            result, ExtendedEuclideanAlgorithmResult(a=360, x=2, b=225, y=-3)
        )
        self.assertEqual(result.divisor, 45)

    def test_do_225_360(self):
        result = ExtendedEuclideanAlgorithm.do(225, 360)
        self.assertEqual(
            result, ExtendedEuclideanAlgorithmResult(b=360, y=2, a=225, x=-3)
        )
        self.assertEqual(result.divisor, 45)

    def test_do_402_123(self):
        result = ExtendedEuclideanAlgorithm.do(402, 123)
        self.assertEqual(result.x, 15)
        self.assertEqual(result.y, -49)
        self.assertEqual(result.divisor, 3)
