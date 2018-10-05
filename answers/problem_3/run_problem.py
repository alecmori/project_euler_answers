# -*- coding: utf-8 -*-
from utils.proj_eul_math import prime


def run_problem(num=600851475143):
    max_prime = -1
    for p in prime.get_primes():
        if num == 1:
            break
        if num % p == 0:
            max_prime = p
            num = reduce_number(num=num, p=p)
    return max_prime


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
