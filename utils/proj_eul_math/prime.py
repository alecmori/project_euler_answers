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
