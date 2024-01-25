from dataclasses import dataclass


class EuclideanAlgorithm:
    @staticmethod
    def do(a: int, b: int) -> int:
        """The greatest common divisor of two integers"""

        r_i = [a, b]
        if b > a:
            r_i = [b, a]

        while r_i[1] > 0:
            r_i = [r_i[1], r_i[0] % r_i[1]]

        return r_i[0]


@dataclass
class ExtendedEuclideanAlgorithmResult:
    a: int
    x: int
    b: int
    y: int

    @property
    def divisor(self) -> int:
        return (self.a * self.x) + (self.b * self.y)


class ExtendedEuclideanAlgorithm:
    @staticmethod
    def do(a: int, b: int) -> ExtendedEuclideanAlgorithmResult:
        """
        The greatest common divisor of two integers a and b is expressible in the following way

        cgd(a, b) = ax + by
        """

        r_i = [a, b]
        if b > a:
            r_i = [b, a]

        x_i = [1, 0]
        y_i = [0, 1]
        n = 0
        while r_i[1] > 0:
            q = r_i[0] // r_i[1]
            r_i = [r_i[1], r_i[0] % r_i[1]]
            x_i = [x_i[1], x_i[1] * q + x_i[0]]
            y_i = [y_i[1], y_i[1] * q + y_i[0]]
            n += 1

        if b > a:
            return ExtendedEuclideanAlgorithmResult(
                a=a,
                b=b,
                x=((-1) ** (n + 1)) * y_i[0],
                y=((-1) ** n) * x_i[0],
            )
        return ExtendedEuclideanAlgorithmResult(
            a=a,
            b=b,
            x=((-1) ** n) * x_i[0],
            y=((-1) ** (n + 1)) * y_i[0],
        )
