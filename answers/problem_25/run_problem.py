# -*- coding: utf-8 -*-
import math

from utils.proj_eul_math import general


def run_problem(num_digits=1000):
    for index, num in enumerate(general.fibonacci_iterator()):
        if math.log10(num) >= num_digits - 1:
            return index + 1


if __name__ == '__main__':
    answer = run_problem()
    # TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
