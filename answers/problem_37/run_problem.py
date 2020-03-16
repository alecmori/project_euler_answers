# -*- coding: utf-8 -*-

from utils.proj_eul_math import prime

NUM_TRUNCATABLE = 11

def run_problem():
    truncatable_primes = []
    all_primes = set()
    for p in prime.get_primes():
        if len(truncatable_primes) == NUM_TRUNCATABLE:
            break
        all_primes.add(p)
        # 2, 3, 5, 7 not considered truncatable primes
        if p < 10:
            continue
        all_truncated_primes = True
        for num in (
            _get_left_truncated_numbers(p) + _get_right_truncated_numbers(p)
        ):
            if num not in all_primes:
                all_truncated_primes = False
        if all_truncated_primes:
            truncatable_primes.append(p)
    return sum(truncatable_primes)

def _get_right_truncated_numbers(n):
    numbers = []
    n = int(n / 10)
    while n > 0:
        numbers.append(n)
        n = int(n / 10)
    return numbers


def _get_left_truncated_numbers(n):
    numbers = []
    incrementer = 10
    while n > incrementer:
        numbers.append(n % incrementer)
        incrementer *= 10
    return numbers


if __name__ == '__main__':
    answer = run_problem()
    print(answer)
    if answer == 3797:
        print('Correct!')
    else:
        print('Incorrect!')
