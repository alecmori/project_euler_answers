# -*- coding: utf-8 -*-
import functools

CACHE_SIZE = int(1e8)


def run_problem(max_value=1000000):
    max_integer = 0
    best_chain_len = 0
    curr_chain_len = 0
    for i in range(1, 1 + max_value):
        curr_chain_len = count_collatz(i)
        if curr_chain_len > best_chain_len:
            best_chain_len = curr_chain_len
            max_integer = i
    return max_integer


# NOTE: Cython does not play well withe decorators. Using Python
#   notation to indicate return value.
# TODO: Use own implementation of dict for memoization
@functools.lru_cache(maxsize=CACHE_SIZE)
def count_collatz(x: int) -> int:
    if x == 1:
        return 1
    if x % 2 == 0:
        return count_collatz(int(x / 2)) + 1
    else:
        return count_collatz(3 * x + 1) + 1


if __name__ == '__main__':
    answer = run_problem(max_value=5)
    if answer == 3:
        print('Correct!')
    else:
        print('Incorrect!')
