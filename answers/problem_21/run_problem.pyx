# -*- coding: utf-8 -*-
import functools
from utils.proj_eul_math import general

CACHE_SIZE = int(1e7)

cpdef unsigned int run_problem(unsigned int max_value=10000):
    cdef unsigned int total = 0
    for n in range(1, max_value):
        if is_pair_amicable(n=n):
            total += n
    return total

cdef int is_pair_amicable(unsigned int n=0):
    cdef unsigned int amicable_pair = _get_sum_proper_divisors(
        n=n,
    )
    if amicable_pair == n:
        return False
    return _get_sum_proper_divisors(
        n=amicable_pair,
    ) == n

# NOTE: Decorators and Cython do not play along (AFAIK). Using normal
#   Python syntax instead.
@functools.lru_cache(maxsize=CACHE_SIZE)
def _get_sum_proper_divisors(int n=0) -> int:
    return general.get_sum_divisors(num=n) - n


if __name__ == '__main__':
    answer = run_problem(max_value=10)
    #TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
