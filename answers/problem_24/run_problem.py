# -*- coding: utf-8 -*-
from utils.proj_eul_math import combinatorics

NUM_DIGITS = 10


def run_problem(place_of_permutation=1000000):
    curr_digit = NUM_DIGITS
    curr_place = place_of_permutation - 1
    digits = [
        x
        for x in range(NUM_DIGITS)
    ]
    ordered_digits = []
    while curr_digit > 0:
        factorial = combinatorics.factorial(curr_digit - 1)
        index_of_next_number = int(
            curr_place / factorial,
        )
        curr_place -= index_of_next_number * factorial
        ordered_digits.append(str(digits[index_of_next_number]))
        del digits[index_of_next_number]
        curr_digit -= 1
    return int(''.join(ordered_digits))


if __name__ == '__main__':
    answer = run_problem()
    # TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
