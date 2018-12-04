# -*- coding: utf-8 -*-
# NOTE: I do not type the variable `power` because it is easier for
#   Python to deal with larger numbers (AFAIK, should look it up)
cpdef unsigned long int run_problem(power=1000):
    cdef unsigned long int total = 0
    for x in str(2**power):
        total += int(x)
    return total


if __name__ == '__main__':
    answer = run_problem(power=15)
    if answer == 26:
        print('Correct!')
    else:
        print('Incorrect!')
