# -*- coding: utf-8 -*-
# NOTE: These functions create values too big to convert to BigInteger.
#   I have to find the best way to Cythonize this.


def factorial(n):
    i = 1
    while n > 1:
        i *= n
        n -= 1
    return i


def nCr(n, r):
    r = min(r, n - r)
    return int(nPr(n, r) / nPr(r, r))


def nPr(n, r):
    product = 1
    while r > 0:
        product *= n
        n -= 1
        r -= 1
    return product
