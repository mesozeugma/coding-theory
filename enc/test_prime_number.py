import unittest
from enc.prime_number import (
    JacobiSymbol,
    LegendreSymbol,
    MillerRabinTest,
    SolovayStrassenTest,
)


class TestJacobiSymbol(unittest.TestCase):
    def test_do_13_3(self):
        self.assertEqual(JacobiSymbol.do(13, 3), 1)

    def test_do_30_3(self):
        self.assertEqual(JacobiSymbol.do(30, 3), 0)

    def test_do_18_53(self):
        self.assertEqual(JacobiSymbol.do(18, 53), -1)


class TestMillerRabinTest(unittest.TestCase):
    def test_calculate_r_m(self):
        self.assertEqual(MillerRabinTest.calculate_r_m(561), (4, 35))

    def test_do_561(self):
        self.assertFalse(MillerRabinTest.do(561))

    def test_do_74891(self):
        self.assertTrue(MillerRabinTest.do(74891))

    def test_do_4467518969(self):
        self.assertTrue(MillerRabinTest.do(4467518969))


class TestLegendreSymbol(unittest.TestCase):
    def test_do_13_3(self):
        self.assertEqual(LegendreSymbol.do(13, 3), 1)

    def test_do_30_3(self):
        self.assertEqual(LegendreSymbol.do(30, 3), 0)

    def test_do_18_53(self):
        self.assertEqual(LegendreSymbol.do(18, 53), -1)


class TestSolovayStrassenTest(unittest.TestCase):
    def test_do_561(self):
        self.assertFalse(SolovayStrassenTest.do(561, 10))

    def test_do_13(self):
        self.assertTrue(SolovayStrassenTest.do(13, 10))
