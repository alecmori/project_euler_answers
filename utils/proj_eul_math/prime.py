# -*- coding: utf-8 -*-
DEFAULT_SIEVE_OF_ATKIN = 100000
MOD = 60
FIRST_WHEEL = {1, 13, 17, 29, 37, 41, 49, 53}
SECOND_WHEEL = {7, 19, 31, 43}
THIRD_WHEEL = {11, 23, 47, 59}
WHEEL = FIRST_WHEEL.intersection(SECOND_WHEEL.intersection(THIRD_WHEEL))

# TODO: Change exclusive to inclusive


def get_primes(max_num_exclusive=None):
    if max_num_exclusive:
        for num in _sieve_of_atkin(
            limit=max_num_exclusive - 1,
            minimum=0,
        ):
            yield num
    else:
        i = 1
        while True:
            # TODO: Make limit smarter
            for prime in _sieve_of_atkin(
                limit=DEFAULT_SIEVE_OF_ATKIN * i,
                minimum=DEFAULT_SIEVE_OF_ATKIN * (i - 1),
            ):
                yield prime


# TODO: test the shit out of this function
# TODO: Make poss_prime persist between calls somehow
def _sieve_of_atkin(limit: int, minimum: int):
    """
    See formula from wikipedia
    https://en.wikipedia.org/wiki/Sieve_of_Atkin
    """
    poss_prime = [
        False
        for _ in range(limit + 1)
    ]
    # NOTE(alecmori): Hardcoded in
    poss_prime[2] = True
    poss_prime[3] = True
    x = 1
    # TODO(alecmori): Explain this in rationale
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
        if (poss_prime[r]):
            for i in range(r * r, limit, r * r):
                poss_prime[i] = False
        r += 1
    for num in range(minimum, len(poss_prime)):
        if poss_prime[num]:
            yield num


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
