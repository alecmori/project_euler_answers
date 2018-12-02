# -*- coding: utf-8 -*-
cpdef run_problem(power=1000):
    total = 0
    for x in str(2**power):
        total += int(x)
    return total


if __name__ == '__main__':
    answer = run_problem(power=15)
    if answer == 26:
        print('Correct!')
    else:
        print('Incorrect!')
