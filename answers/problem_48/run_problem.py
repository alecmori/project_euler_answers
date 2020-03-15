# -*- coding: utf-8 -*-
MODULUS = 10**10

def run_problem(n=1000):
    total_with_modulus = 0
    for i in range(1, n + 1):
        total_with_modulus += pow(i, i, MODULUS)
    return total_with_modulus % MODULUS


if __name__ == '__main__':
    answer = run_problem(n=10)
    if answer == 405071317:
        print('Correct!')
    else:
        print('Incorrect!')
