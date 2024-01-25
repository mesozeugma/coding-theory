import math
from typing import Callable
from enc.euclidean_algorithm import EuclideanAlgorithm


class TrivialFactorFound(Exception):
    def __init__(self, d: int) -> None:
        super().__init__(f"trivial factor {d} found")


class PollardRhoF:
    @staticmethod
    def x2_1(x: int) -> int:
        return x**2 + 1


# https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
class PollardRho:
    @staticmethod
    def do(n: int, f: Callable[[int], int] = PollardRhoF.x2_1, x0: int = 1):
        """
        The algorithm is used to factorize a number n = p*q,
        where p is a non-trivial factor.

        A polynomial modulo, called f(x) (e.g. x**2 + 1 (mod n)),
        is used to generate a pseudorandom sequence.
        """
        x = x0
        y = x
        d = 1

        while d == 1:
            x = f(x)
            y = f(f(y))
            # TODO replace Exteneded Euclidean with "normal"
            d = EuclideanAlgorithm.do(abs(x - y), n)

        if d == n:
            raise TrivialFactorFound(d)
        return d
