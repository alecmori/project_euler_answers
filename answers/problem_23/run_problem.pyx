# -*- coding: utf-8 -*-
from utils.proj_eul_math import general

MAX_POSS_ABUNDANT_SUM_NUMBER = 28123

cpdef unsigned long int run_problem(
    unsigned int max_abundant_number=MAX_POSS_ABUNDANT_SUM_NUMBER,
):
    cdef unsigned long int total = 0
    cdef set abundant_sums = _get_all_abundant_sums(
        max_abundant_number=max_abundant_number,
    )
    for i in range(max_abundant_number):
        if i not in abundant_sums:
            total += i
    return total


cdef set _get_all_abundant_sums(
    unsigned int max_abundant_number=MAX_POSS_ABUNDANT_SUM_NUMBER,
):
    cdef list sorted_abundant_numbers = _get_sorted_abundant_numbers(
        max_abundant_number=max_abundant_number,
    )
    cdef set all_summed_abundant_numbers = set()
    for n1 in sorted_abundant_numbers:
        for n2 in sorted_abundant_numbers:
            if n1 + n2 > max_abundant_number:
                break
            all_summed_abundant_numbers.add(n1 + n2)
    return all_summed_abundant_numbers


cdef list _get_sorted_abundant_numbers(
    unsigned int max_abundant_number=MAX_POSS_ABUNDANT_SUM_NUMBER,
):
    cdef list abundant_numbers = []
    for i in range(max_abundant_number):
        # TODO: Proof. If a is abundant number, then any number c*a is
        if any(
            i % abundant_number == 0
            for abundant_number in abundant_numbers
        ):
            abundant_numbers.append(i)
            # Getting sum of divisors is expensive
            continue
        if _get_sum_proper_divisors(n=i) > i:
            abundant_numbers.append(i)
    return abundant_numbers


cdef unsigned int _get_sum_proper_divisors(unsigned int n=0):
    cdef unsigned int total = 0
    for d in general.get_divisors(num=n):
        if d == n:
            continue
        total += d
    return total


if __name__ == '__main__':
    answer = run_problem()
    #TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
