# -*- coding: utf-8 -*-
from utils.proj_eul_math import combinatorics

def run_problem(n=100):
    return sum(
        int(x)
        for x in str(combinatorics.factorial(n))
    )


if __name__ == '__main__':
    answer = run_problem(n=10)
    if answer == 27:
        print('Correct!')
    else:
        print('Incorrect!')
