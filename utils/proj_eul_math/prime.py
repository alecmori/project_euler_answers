# -*- coding: utf-8 -*-
def get_primes(max_num_exclusive=None):
    if not max_num_exclusive:
        max_num_exclusive = float('inf')
    primes_seen_so_far = {2}
    yield 2
    num = 3
    while num < max_num_exclusive:
        if not any(num % prime == 0 for prime in primes_seen_so_far):
            primes_seen_so_far.add(num)
            yield num
        # Skip all even numbers
        # TODO: Make smarter still
        num += 2


def get_prime_factorization(num: int):
    prime_dict = {}
    for prime in get_primes(max_num_exclusive=num):
        if prime > num:
            return prime_dict
        if num % prime == 0:
            num_times_prime_divides = _get_num_times_prime_divides(
                num=num,
                prime=prime,
            )
            prime_dict[prime] = num_times_prime_divides
            num = num / prime**num_times_prime_divides
    return prime_dict


def _get_num_times_prime_divides(num, prime):
    n = 0
    while num % prime == 0:
        num /= prime
        n += 1
    return n
