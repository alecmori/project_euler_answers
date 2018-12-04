# NOTE: These functions create values too big to convert to BigInteger.
#   I have to find the best way to Cythonize this.
cdef factorial(unsigned int n):
    i = 1
    while n > 1:
        i *= n
        n -= 1
    return i

cdef nCr(unsigned int n, unsigned int r):
    r = min(r, n-r)
    return int(nPr(n, r) / nPr(r, r))


cdef nPr(unsigned int n, unsigned int r):
    product = 1
    while r > 0:
        product *= n
        n -= 1
        r -= 1
    return product
