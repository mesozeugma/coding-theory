import unittest
from enc.rsa import RSA, RSAPrivateKey, RSAPublicKey


class TestRSA(unittest.TestCase):
    def test_calculate_euler(self):
        self.assertEqual(RSA.calculate_euler(463, 547), 252252)

    def test_is_relatively_prime_47_252252(self):
        self.assertTrue(RSA.is_relatively_prime(47, 252252))

    def test_is_relatively_prime_45_90(self):
        self.assertFalse(RSA.is_relatively_prime(45, 90))

    def test_calculate_d_47_252252(self):
        self.assertEqual(RSA.calculate_d(47, 252252), 166379)

    def test_encrypt_m(self):
        public_key = RSAPublicKey(n=253261, e=47)
        self.assertEqual(RSA.encrypt_m(49, public_key), 148078)

    def test_decrypt_m(self):
        public_key = RSAPublicKey(n=253261, e=47)
        private_key = RSAPrivateKey(d=166379)
        self.assertEqual(RSA.decrypt_m(148078, public_key, private_key), 49)

    def test_create_keys(self):
        public_key, private_key = RSA.create_keys(100)
        m = 3
        encrypted_m = RSA.encrypt_m(m, public_key)
        self.assertEqual(RSA.decrypt_m(encrypted_m, public_key, private_key), m)
