# -*- coding: utf-8 -*-
from utils.proj_eul_math import general


def run_problem(max_value=20):
    lcm = 1
    for x in range(1, max_value + 1):
        lcm = general.least_common_multiple(
            a=lcm,
            b=x,
        )
    return lcm


if __name__ == '__main__':
    answer = run_problem(max_value=10)
    if answer == 2520:
        print('Correct!')
    else:
        print('Incorrect!')
