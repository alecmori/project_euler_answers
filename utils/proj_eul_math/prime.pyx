# -*- coding: utf-8 -*-
import math

DEFAULT_SIEVE_OF_ATKIN = 6
DEFAULT_SIEVE_OF_ATKIN_BASE = 10
MOD = 60
FIRST_WHEEL = {1, 13, 17, 29, 37, 41, 49, 53}
SECOND_WHEEL = {7, 19, 31, 43}
THIRD_WHEEL = {11, 23, 47, 59}
WHEEL = FIRST_WHEEL.intersection(SECOND_WHEEL.intersection(THIRD_WHEEL))

# TODO: Change exclusive to inclusive
def get_primes(*, max_num_exclusive=None):
    if max_num_exclusive and max_num_exclusive <= 2:
        return
    if max_num_exclusive:
        for num in _sieve_of_atkin(
            limit=max_num_exclusive - 1,
            minimum=0,
        ):
            yield num
    else:
        i = DEFAULT_SIEVE_OF_ATKIN
        prev = 0
        while True:
            # TODO: Make limit smarter
            limit = DEFAULT_SIEVE_OF_ATKIN_BASE ** i
            for prime in _sieve_of_atkin(
                limit=limit,
                minimum=prev,
            ):
                yield prime
            prev = limit
            i += 1


# TODO: test the shit out of this function
# TODO: Make poss_prime persist between calls somehow
def _sieve_of_atkin(*, unsigned int limit, unsigned int minimum):
    """
    See formula from wikipedia
    https://en.wikipedia.org/wiki/Sieve_of_Atkin
    """
    poss_prime = [
        False
        for _ in range(limit + 1)
    ]
    poss_prime[2] = True
    poss_prime[3] = True
    cdef unsigned int x = 1
    cdef unsigned int y
    cdef unsigned int n
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
    cdef unsigned int r = 5
    while(r * r < limit):
        if poss_prime[r]:
            for i in range(r * r, limit, r * r):
                poss_prime[i] = False
        r += 1
    for num in range(minimum, len(poss_prime)):
        if poss_prime[num]:
            yield num

def get_prime_factorization(*, unsigned long long int num):
    cdef dict prime_dict = {}
    for prime in get_primes(max_num_exclusive=int(math.sqrt(num)) + 1):
        if prime > num:
            return prime_dict
        if num % prime == 0:
            num_times_prime_divides = _get_num_times_prime_divides(
                num=num,
                prime=prime,
            )
            prime_dict[prime] = num_times_prime_divides
            num = num / prime**num_times_prime_divides
    # If we have gone through all primes and still have found no
    #   divisors, then this number is prime and thus its own prime
    #   factorization.
    return {num: 1}


cdef int _get_num_times_prime_divides(
    unsigned long long int num, unsigned long long int prime,
):
    cdef unsigned int n = 0
    while num % prime == 0:
        num /= prime
        n += 1
    return n


cdef int is_prime(unsigned long long int num):
    return any(
        num % prime
        for prime in get_primes(max_num_exclusive=int(math.sqrt(num)) + 1)
    )
