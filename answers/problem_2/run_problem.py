# -*- coding: utf-8 -*-
from utils.proj_eul_math import general


def run_problem(max_value=4000000):
    total = 0
    for num in general.fibonacci_iterator(max_value=max_value):
        if num % 2 == 0:
            total += num
    return total


if __name__ == '__main__':
    answer = run_problem(max_value=100)
    if answer == 44:
        print('Correct!')
    else:
        print('Incorrect!')
