# -*- coding: utf-8 -*-
from utils.proj_eul_math import general

MAX_POSS_ABUNDANT_SUM_NUMBER = 28123


def run_problem(max_abundant_number=MAX_POSS_ABUNDANT_SUM_NUMBER):
    total = 0
    abundant_sums = _get_all_abundant_sums(
        max_abundant_number=max_abundant_number,
    )
    for i in range(max_abundant_number):
        if i not in abundant_sums:
            total += i
    return total


def _get_all_abundant_sums(max_abundant_number=MAX_POSS_ABUNDANT_SUM_NUMBER):
    sorted_abundant_numbers = _get_sorted_abundant_numbers(
        max_abundant_number=max_abundant_number,
    )
    all_summed_abundant_numbers = set()
    for n1 in sorted_abundant_numbers:
        for n2 in sorted_abundant_numbers:
            if n1 + n2 > max_abundant_number:
                break
            all_summed_abundant_numbers.add(n1 + n2)
    return all_summed_abundant_numbers


def _get_sorted_abundant_numbers(
    max_abundant_number=MAX_POSS_ABUNDANT_SUM_NUMBER,
):
    abundant_numbers = []
    for i in range(2, max_abundant_number):
        if _get_sum_proper_divisors(n=i) > i:
            abundant_numbers.append(i)
    return abundant_numbers


def _get_sum_proper_divisors(n=0):
    return general.get_sum_divisors(num=n) - n


if __name__ == '__main__':
    answer = run_problem()
    # TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
