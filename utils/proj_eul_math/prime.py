# -*- coding: utf-8 -*-
import math

DEFAULT_SIEVE_OF_ATKIN = 6
DEFAULT_SIEVE_OF_ATKIN_BASE = 10


def get_primes(max_num_inclusive=None):
    if max_num_inclusive:
        poss_primes = _sieve_of_atkin(limit=max_num_inclusive)
        for num in range(len(poss_primes)):
            if poss_primes[num]:
                yield num
    else:
        i = DEFAULT_SIEVE_OF_ATKIN
        prev = 0
        while True:
            limit = DEFAULT_SIEVE_OF_ATKIN_BASE ** i
            # TODO: Use minimum in sieve of atkin to speed things up
            poss_primes = _sieve_of_atkin(limit=limit)
            for num in range(prev, len(poss_primes)):
                if poss_primes[num]:
                    yield num
            prev = limit
            i += 1


# TODO: test the shit out of this function
# TODO: Make poss_prime persist between calls somehow
def _sieve_of_atkin(limit):
    """
    See formula from wikipedia
    https://en.wikipedia.org/wiki/Sieve_of_Atkin
    """
    poss_prime = [
        False
        # Padding zero for simplicity
        for _ in range(limit + 1)
    ]
    if limit >= 2:
        poss_prime[2] = True
    if limit >= 3:
        poss_prime[3] = True
    if limit <= 4:
        return poss_prime
    x = 1
    while x * x < limit:
        y = 1
        while y * y < limit:
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                poss_prime[n] ^= True
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                poss_prime[n] ^= True
            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                poss_prime[n] ^= True
            y += 1
        x += 1
    r = 5
    while(r * r < limit):
        if poss_prime[r]:
            for i in range(r * r, limit, r * r):
                poss_prime[i] = False
        r += 1
    return poss_prime


def get_prime_factorization(num=0):
    if num <= 1:
        raise ValueError
    prime_dict = {}
    upper_bound = int(math.sqrt(num))
    for prime in get_primes(max_num_inclusive=upper_bound):
        if num % prime == 0:
            num_times_prime_divides = _get_num_times_prime_divides(
                num=num,
                prime=prime,
            )
            prime_dict[prime] = num_times_prime_divides
            num = num / prime**num_times_prime_divides
    if num != 1:
        # TODO: Prove that this remainder must be a singular number and a prime
        prime_dict.update(
            {num: 1},
        )
    return prime_dict


def _get_num_times_prime_divides(num, prime):
    n = 0
    while num % prime == 0:
        num /= prime
        n += 1
    return n


def is_prime(num):
    if num <= 1:
        return False
    for prime in get_primes(max_num_inclusive=int(math.sqrt(num))):
        if num % prime == 0:
            return False
    return True
