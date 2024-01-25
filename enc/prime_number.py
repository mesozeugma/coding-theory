import random
from enc.exponentiation import FastModularExponentiation


# https://en.wikipedia.org/wiki/Jacobi_symbol
class JacobiSymbol:
    def do(a: int, n: int) -> int:
        a = a % n
        t = 1
        r = 0

        while a != 0:
            while a % 2 == 0:
                a /= 2
                r = n % 8
                if r == 3 or r == 5:
                    t = -t

            r = n
            n = a
            a = r
            if a % 4 == 3 and n % 4 == 3:
                t = -t
            a = a % n

        if n == 1:
            return t
        return 0


class LegendreSymbol:
    def do(a: int, p: int) -> int:
        """
        p = 1 (mod 2)

        0 if a = 0 (mod p)
        1 if a is a quadratic residue modulo p and a != 0 (mod p)
        -1 if a is a quadratic nonresidue modulo p

        The Jacobi symbol is equal to the Legendre symbol.
        """
        return JacobiSymbol.do(a, p)


# https://observablehq.com/@beardofdoom/miller-rabin-primality-test
class MillerRabinTest:
    @staticmethod
    def calculate_r_m(p: int) -> tuple[int, int]:
        """p - 1 = 2^r * m"""

        p_even = p - 1
        m = p_even
        r = 0
        while m % 2 == 0:
            m //= 2
            r += 1

        return r, m

    @staticmethod
    def do(p: int, a: int = 2) -> bool:
        """
        p = 1 (mod 2)
        1 <= a <= p - 1

        p - 1 = 2**r * m

        True if
        a**m = 1 (mod p)
        or
        i = 0..r
        a**((2**i)*m) = -1 (mod p) and a**((2**i)*m) = -1 (mod p)
        """

        r, m = MillerRabinTest.calculate_r_m(p)

        first_mod_value = FastModularExponentiation.do(a, m, p)
        if first_mod_value == 1:
            return True

        last_mod_value = first_mod_value
        for i in range(1, r + 1):
            mod_value = last_mod_value**2 % p
            if mod_value == 1:
                return last_mod_value == p - 1
            last_mod_value = mod_value

        return False


class SolovayStrassenTest:
    @staticmethod
    def do(n: int, k: int) -> bool:
        """
        n > 1
        n = 1 (mod 2)
        k determines the accuracy of the test

        return true if n is probably prime
        """

        for i in range(k):
            a = random.randint(2, n - 1)
            x = JacobiSymbol.do(a, n)
            if x == 0 or (x % n) != FastModularExponentiation.do(a, (n - 1) // 2, n):
                return False
        return True
