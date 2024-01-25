import random
from dataclasses import dataclass
from enc.euclidean_algorithm import EuclideanAlgorithm, ExtendedEuclideanAlgorithm
from enc.exponentiation import FastModularExponentiation
from enc.prime_number import MillerRabinTest


@dataclass
class RSAPublicKey:
    n: int
    e: int


@dataclass
class RSAPrivateKey:
    d: int


# https://observablehq.com/@beardofdoom/rsa
class RSA:
    @staticmethod
    def _create_prime_number(digits: int) -> int:
        while True:
            min = 10 ** (digits - 1)
            p = random.randint(min, min * 10 - 1)
            if p % 2 == 0:
                continue
            if MillerRabinTest.do(p):
                return p

    @staticmethod
    def create_p_q(digits: int) -> tuple[int, int]:
        p = RSA._create_prime_number(digits)
        q = RSA._create_prime_number(digits)
        return p, q

    @staticmethod
    def calculate_euler(p: int, q: int) -> int:
        """number of the relatively prime numbers to n from the set {1,2,…,n}."""
        return (p - 1) * (q - 1)

    @staticmethod
    def is_relatively_prime(a: int, b: int) -> bool:
        return EuclideanAlgorithm.do(a, b) == 1

    @staticmethod
    def create_e(euler: int) -> int:
        """pick a number 1 < e < euler that is relatively prime to euler"""
        while True:
            e = random.randint(2, euler - 1)
            if RSA.is_relatively_prime(e, euler):
                return e

    @staticmethod
    def calculate_d(e: int, euler: int) -> int:
        """
        e*d = 1 mod euler
        cgd(e, euler) = 1
        cgd(a, b) = a*x + b*y (Extended Euclidean Algorithm)

        cgd(e, euler) = e * x + euler * y = 1

        d = x + euler (reason: e*d = 1 mod euler)
        """
        eea_result = ExtendedEuclideanAlgorithm.do(e, euler)
        return eea_result.x + euler

    @staticmethod
    def create_keys(prime_number_digits: int):
        p, q = RSA.create_p_q(prime_number_digits)
        euler = RSA.calculate_euler(p, q)
        e = RSA.create_e(euler)
        d = RSA.calculate_d(e, euler)
        n = p * q
        return RSAPublicKey(n=n, e=e), RSAPrivateKey(d=d)

    @staticmethod
    def encrypt_m(m: int, public_key: RSAPublicKey) -> int:
        """m**e mod n"""
        return FastModularExponentiation.do(m, public_key.e, public_key.n)

    @staticmethod
    def decrypt_m(
        encrypted_m: int, public_key: RSAPublicKey, private_key: RSAPrivateKey
    ) -> int:
        """
        using Fast Modular Exponentiation: encrypted_m**d mod n

        faster alternative would be chinese remainder theorem
        """
        return FastModularExponentiation.do(encrypted_m, private_key.d, public_key.n)
