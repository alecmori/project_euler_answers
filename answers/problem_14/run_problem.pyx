# -*- coding: utf-8 -*-
import functools

CACHE_SIZE = int(1e8)

cpdef run_problem(unsigned int max_value=1000000):
    cdef unsigned int max_integer = 0
    cdef unsigned int best_chain_len = 0
    cdef unsigned int curr_chain_len = 0
    for i in range(1, 1 + max_value):
        curr_chain_len = count_collatz(i)
        if curr_chain_len > best_chain_len:
            best_chain_len = curr_chain_len
            max_integer = i
    return max_integer


@functools.lru_cache(maxsize=CACHE_SIZE)
def count_collatz(unsigned int x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return count_collatz(int(x/2)) + 1
    else:
        return count_collatz(3 * x + 1) + 1


if __name__ == '__main__':
    answer = run_problem(max_value=5)
    if answer == 3:
        print('Correct!')
    else:
        print('Incorrect!')
