# -*- coding: utf-8 -*-
from utils.proj_eul_math cimport combinatorics

cpdef unsigned int run_problem(unsigned int n=100):
    total = 0
    for x in str(combinatorics.factorial(n=n)):
        total += int(x)
    return total


if __name__ == '__main__':
    answer = run_problem(n=10)
    if answer == 27:
        print('Correct!')
    else:
        print('Incorrect!')
