# -*- coding: utf-8 -*-
from utils.proj_eul_math cimport general


cpdef run_problem(unsigned int max_value=20):
    cdef unsigned long long int lcm = 1
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
