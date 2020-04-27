# -*- coding: utf-8 -*-
import math

MAX_NUM = 987654321

def _get_non_zero_digits(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n = n // 10
    return digits

def _get_pandigital_if_exists(n):
    if n == 0:
        return -1
    pandigital_components = []
    digits = set()
    multiplier = 1
    while len(digits) != 9:
        curr_num = multiplier * n
        for digit in _get_non_zero_digits(curr_num):
            if digit == 0:
                return -1
            if digit in digits:
                return -1
            digits.add(digit)
        pandigital_components.append(str(curr_num))
        multiplier += 1
    return int(''.join(pandigital_components))

def run_problem(n=MAX_NUM):
    largest_pandigital_number = 0
    for num in range(int(math.sqrt(n))):
        maybe_pandigital = _get_pandigital_if_exists(num)
        if maybe_pandigital != '':
            largest_pandigital_number = max(
                largest_pandigital_number,
                int(maybe_pandigital),
            )
    return largest_pandigital_number


if __name__ == '__main__':
    answer = run_problem()
    if answer == 932718654:
        print('Correct!')
    else:
        print('Incorrect!')
