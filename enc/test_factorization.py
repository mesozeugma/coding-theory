import unittest
from enc.factorization import PollardRho


class TestPollardRho(unittest.TestCase):
    def test_do_91(self):
        self.assertEqual(PollardRho.do(91), 7)

    def test_do_8051(self):
        self.assertEqual(PollardRho.do(8051, x0=2), 97)
