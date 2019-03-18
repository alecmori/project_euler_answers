# -*- coding: utf-8 -*-
from utils.proj_eul_math import prime


def run_problem(n=1000):
    if n % 2 == 0:
        n -= 1
    primes_generated = 1
    best_a = 0
    best_b = 0
    prime_cache = set(prime.get_primes(max_num_inclusive=n * n))
    for a in range(-1 * n, n + 1, 2):
        for b in prime.get_primes(max_num_inclusive=n):
            current_primes_generated = get_consecutive_primes_generated(
                a=a, b=b, prime_cache=prime_cache, max_prime=n * n,
            )
            if current_primes_generated > primes_generated:
                primes_generated = current_primes_generated
                best_a = a
                best_b = b
    return best_a * best_b


def get_consecutive_primes_generated(a, b, prime_cache, max_prime):
    n = 1
    while True:
        poss_prime = n * n + a * n + b
        if poss_prime in prime_cache:
            n += 1
        elif poss_prime <= 0:
            return n
        elif not prime.is_prime(poss_prime):
            return n
        else:
            n += 1


if __name__ == '__main__':
    answer = run_problem(n=41)
    if answer == -41:
        print('Correct!')
    else:
        print('Incorrect!')
