import math


# https://observablehq.com/@beardofdoom/fast-modular-exponentiation
class FastModularExponentiation:
    @staticmethod
    def convert_exponent(b: int) -> list[int]:
        """
        The conversion of the exponent to the sum of the powers of 2

        e.g b = 73
        73 = 2**0 + 2**3 + 2**6
        -> [0, 3, 6]
        """
        result = []
        i = 0
        current_value = b
        while current_value != 0:
            r = current_value % 2
            current_value //= 2
            if r > 0:
                result.append(i)
            i += 1
        return result

    @staticmethod
    def do_repeated_exponentiation(a: int, b_converted: list[int], m: int) -> list[int]:
        result = []

        last_mod_value = a % m
        if 0 in b_converted:
            result.append(last_mod_value)

        for i in range(1, b_converted[-1] + 1):
            last_mod_value = last_mod_value**2 % m
            if i in b_converted:
                result.append(last_mod_value)

        return result

    @staticmethod
    def do(a: int, b: int, m: int) -> int:
        """
        b > 1
        m > 0

        Returns a**b (mod m)
        """
        b_converted = FastModularExponentiation.convert_exponent(b)
        x1 = FastModularExponentiation.do_repeated_exponentiation(a, b_converted, m)
        return math.prod(x1) % m
