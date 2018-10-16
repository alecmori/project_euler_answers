# -*- coding: utf-8 -*-
from utils.proj_eul_math import prime


def run_problem(max_value=2000000):
    return sum(
        p
        for p in prime.get_primes(max_num_inclusive=max_value)
    )


if __name__ == '__main__':
    answer = run_problem(max_value=10)
    if answer == 17:
        print('Correct!')
    else:
        print('Incorrect!')
