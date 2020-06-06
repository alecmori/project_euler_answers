# -*- coding: utf-8 -*-
import math
from utils.proj_eul_math import prime

# Any num with 9/8 would be divisible by 3
MAX_NUM = 7654321

def _is_pandigital(n):
    assert n <= MAX_NUM
    nums = set()
    max_length = math.floor(math.log(n, 10)) + 1
    while n:
        digit = n % 10
        if digit > max_length:
            return False
        nums.add(digit)
        n = n // 10
    return len(nums) == max_length


def run_problem():
    all_primes = []
    for p in prime.get_primes(max_num_inclusive=MAX_NUM):
        all_primes.append(p)
    for i in range(len(all_primes) - 1, -1, -1):
        if _is_pandigital(all_primes[i]):
            return all_primes[i]
    return -1




if __name__ == '__main__':
    answer = run_problem()
    if answer == 7652413:
        print('Correct!')
    else:
        print('Incorrect!')
