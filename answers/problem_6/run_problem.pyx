# -*- coding: utf-8 -*-
cpdef run_problem(unsigned int max_value=100):
    sum_of_squares = 0
    for x in range(max_value + 1):
        sum_of_squares += x**2
    return sum(range(max_value + 1))**2 - sum_of_squares


if __name__ == '__main__':
    answer = run_problem(max_value=10)
    if answer == 2640:
        print('Correct!')
    else:
        print('Incorrect!')
