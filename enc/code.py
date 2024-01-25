import galois
import numpy as np
from enc.finite_fields import GF


class HammingDistance:
    @staticmethod
    def do(u: np.ndarray, v: np.ndarray):
        return ((u + v) > 0).astype(int).sum()


class HammingCode:
    @staticmethod
    def encode(G: np.ndarray, c: np.ndarray):
        return c @ G

    @staticmethod
    def encode_using_u(K: int, U: galois.FieldArray, c: np.ndarray):
        GFK = GF.get(K)
        E = GFK(np.eye(U.shape[1], dtype=int))
        G = np.concatenate((E, U), axis=1)
        return HammingCode.encode(G, c)

    @staticmethod
    def max_possible_error_i(K: int, c_length: int):
        return ((K - 1) * c_length) - 1

    @staticmethod
    def possible_error(K: int, c_length: int, i: int):
        GFK = GF.get(K)
        zeros = GFK(np.zeros(c_length, dtype=int))
        zeros[i % c_length] = (i // c_length) + 1
        return zeros

    @staticmethod
    def _find_error(P: galois.FieldArray, s: galois.FieldArray, K: int, u_length: int):
        max_i = HammingCode.max_possible_error_i(K, u_length)
        for i in range(max_i + 1):
            h = HammingCode.possible_error(K, u_length, i)
            h_p = h @ P
            if np.array_equal(s, h_p):
                return h
        return None

    @staticmethod
    def decode(P: galois.FieldArray, u: galois.FieldArray, K: int):
        """
        decode using syndrome
        """
        GFK = GF.get(K)
        s = u @ P

        u_length = u.shape[0]
        h = u.Zeros(u_length)
        if not np.array_equal(s, s.Zeros(s.shape[0])):
            h = HammingCode._find_error(P, s, K, u_length)
        if h is None:
            raise ValueError("too many errors in code")
        return u - h
