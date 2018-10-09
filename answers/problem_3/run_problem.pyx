# -*- coding: utf-8 -*-
import math
from utils.proj_eul_math import prime


def run_problem(unsigned long long int num=600851475143):
    return max(prime.get_prime_factorization(num=num))


if __name__ == '__main__':
    answer = run_problem(num=13195)
    if answer == 29:
        print('Correct!')
    else:
        print('Incorrect!')
