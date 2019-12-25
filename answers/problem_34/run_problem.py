# -*- coding: utf-8 -*-
from utils.proj_eul_math import combinatorics

def run_problem():
    upper_bound = _get_upper_bound()
    factorials = []
    sum_of_sums = 0
    for i in range(10):
        factorials.append(combinatorics.factorial(i))
    for num in range(10, upper_bound):
        total = 0
        num_copy = num
        while num_copy != 0:
            total += factorials[num_copy % 10]
            num_copy = num_copy // 10
        if num == total:
            sum_of_sums += num
    return sum_of_sums

def _get_upper_bound():
    counter = 1
    nine_fact = combinatorics.factorial(9)
    while True:
        if counter * nine_fact < 10**counter:
            return counter * nine_fact
        else:
            counter += 1

if __name__ == '__main__':
    answer = run_problem()
    if answer == 40730:
        print('Correct!')
    else:
        print('Incorrect!')
