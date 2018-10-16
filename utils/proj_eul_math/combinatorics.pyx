cpdef factorial(unsigned int n):
    i = 1
    while n > 1:
        i *= n
        n -= 1
    return i

cpdef nCr(unsigned int n, unsigned int r):
    r = min(r, n-r)
    return int(nPr(n, r) / nPr(r, r))


cpdef nPr(unsigned int n, unsigned int r):
    product = 1
    while r > 0:
        product *= n
        n -= 1
        r -= 1
    return product
