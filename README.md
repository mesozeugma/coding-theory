# Coding theory

## Usage

**Requirements:**

- Python 3 (tested with 3.10.7)

Install dependencies

```sh
python -m venv .venv
source .venv/bin/activate
pip -r requirements.txt
```

Run tests

```sh
python -m unittest
```

## Tasks

1. RSA
    - [x] Miller-Rabin Primality Test [`prime_number.py`](./enc/prime_number.py)
    - [x] Fast Modular Exponentiation [`exponentiation.py`](./enc/exponentiation.py)
    - [x] Euclidean Algorithm [`euclidean_algorithm.py`](./enc/euclidean_algorithm.py)
    - [x] encode & decode message [`rsa.py`](./enc/rsa.py)
2. Solovay–Strassen primality test
    - [x] Jacobi / Legendre symbol [`prime_number.py`](./enc/prime_number.py)
    - [x] Pollard's rho algorithm [`factorization.py`](./enc/factorization.py)
    - [x] Solovay–Strassen primality test [`prime_number.py`](./enc/prime_number.py)
3. Fermat's factorization method
    - [ ] Fermat's factorization method
    - [ ] Z_2 system of linear equations
4. Generator matrix
    - [x] Hamming code encode [`code.py`](./enc/code.py)
    - [x] Hamming code decode using syndrome [`code.py`](./enc/code.py)
5. Finite field arithmetic
    - [ ] find irreducible polynomials
6. Golay code
7. BCH code

## References

- [Prime number generator, tester tool](https://bigprimes.org/)
- [How to find d, given p, q, and e in RSA?](https://stackoverflow.com/a/46989263)
- [Solving a system of linear equations over the field F(2) with python](https://stackoverflow.com/a/70327062)
