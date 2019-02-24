# -*- coding: utf-8 -*-
from utils.proj_eul_math import general

cpdef unsigned int run_problem(unsigned int n=1000):
    cached_values = dict()
    best_order_mod = 0
    best_int = 0
    for i in range(1, n):
        order_mod = get_order_mod(n=i, cached_values=cached_values)
        if order_mod > best_order_mod:
            best_int = i
            best_order_mod = order_mod
    return best_int


cpdef unsigned int get_order_mod(
    unsigned int n, unsigned int base=10, dict cached_values=None,
):
    """Gets the order modulus of (n, b)

    Technically does not - that requires gcd(`n`, `b`) == 1. However,
    for our purposes, we also care about other numbers. Thus, we remove
    all common prime factors between `n` and `b` and see check order
    from the remaining number.
    """
    if not cached_values:
        cached_values = dict()
    gcd = general.greatest_common_denominator(n, base)
    # You can remove all common primes with the base and still get the
    #   same order.
    while gcd != 1:
        n /= gcd
        gcd = general.greatest_common_denominator(n, base)
    # If the prime factorization of n is composed of the same primes as
    #   the factorization of the base, then the order is non-existant.
    #   Due to type restrictions, that is zero here
    if n == 1:
        return 0
    if n in cached_values:
        return cached_values[n]
    order = 1
    result = base % n
    while result != 1:
        result = base * result % n
        order += 1
    cached_values[n] = order
    return order



if __name__ == '__main__':
    answer = run_problem(10)
    if answer == 7:
        print('Correct!')
    else:
        print('Incorrect!')
