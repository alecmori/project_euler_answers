# -*- coding: utf-8 -*-
from utils.proj_eul_math import general


def run_problem(num_divisors=500):
    for triangle_number in general.generate_triangle_numbers():
        print(triangle_number)
        if general.get_num_divisors(num=triangle_number) > num_divisors:
            return triangle_number


if __name__ == '__main__':
    answer = run_problem(num_divisors=5)
    if answer == 28:
        print('Correct!')
    else:
        print('Incorrect!')
