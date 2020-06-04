# -*- coding: utf-8 -*-
_DIGITS = [1, 10, 100, 1000, 10000, 100000, 1000000]

def get_nth_digit(n):
    n = n - 1
    curr_digit_count = 1
    curr_multiple = 9
    curr_lower_bound = 1
    while n > curr_multiple * curr_digit_count:
        n -= curr_multiple * curr_digit_count
        curr_multiple *= 10
        curr_lower_bound *= 10
        curr_digit_count += 1
    final_number = int(n / curr_digit_count) + curr_lower_bound
    final_digit = n % curr_digit_count
    return int(str(final_number)[final_digit])


def run_problem(digits=_DIGITS):
    total = 1
    for i in digits:
        total *= get_nth_digit(i)
    return total


if __name__ == '__main__':
    answer = run_problem([1, 3, 5, 10])
    if answer == 15:
        print('Correct!')
    else:
        print('Incorrect!')
