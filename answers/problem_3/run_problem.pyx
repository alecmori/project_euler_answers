# -*- coding: utf-8 -*-
import math
from utils.proj_eul_math import prime


def run_problem(num=600851475143):
    max_prime = -1
    if prime.is_prime(num=num):
        return num
    return max(prime.get_prime_factorization(num=num))


def reduce_number(num, p):
    while num % p == 0:
        num = num / p
    return num


if __name__ == '__main__':
    answer = run_problem(num=13195)
    if answer == 29:
        print('Correct!')
    else:
        print('Incorrect!')
