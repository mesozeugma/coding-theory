import unittest
from enc.exponentiation import FastModularExponentiation


class TestFastModularExponentiation(unittest.TestCase):
    def test_convert_exponent(self):
        self.assertEqual(FastModularExponentiation.convert_exponent(73), [0, 3, 6])

    def test_do_repeated_exponentiation(self):
        self.assertEqual(
            FastModularExponentiation.do_repeated_exponentiation(6, [0, 3, 6], 100),
            [6, 16, 96],
        )

    def test_do_6_73_100(self):
        self.assertEqual(FastModularExponentiation.do(6, 73, 100), 16)

    def test_do_8_15_105(self):
        self.assertEqual(FastModularExponentiation.do(8, 15, 105), 92)
