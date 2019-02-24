# -*- coding: utf-8 -*-
from utils.proj_eul_math import combinatorics


def run_problem(n=20):
    return combinatorics.nCr(n=2 * n, r=n)


if __name__ == '__main__':
    answer = run_problem(n=2)
    if answer == 6:
        print('Correct!')
    else:
        print('Incorrect!')
