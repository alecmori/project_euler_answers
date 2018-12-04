# -*- coding: utf-8 -*-
from utils.proj_eul_math import prime


cpdef unsigned int run_problem(unsigned int num_prime=10001):
    for i, p in enumerate(prime.get_primes()):
        if i + 1 >= num_prime:
            return p


if __name__ == '__main__':
    answer = run_problem(num_prime=6)
    if answer == 13:
        print('Correct!')
    else:
        print('Incorrect!')
