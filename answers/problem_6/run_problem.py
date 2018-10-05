# -*- coding: utf-8 -*-
def run_problem(max_value=100):
    return (
        sum(range(max_value + 1))**2 -
        sum(x**2 for x in range(max_value + 1))
    )


if __name__ == '__main__':
    answer = run_problem(max_value=10)
    if answer == 2640:
        print('Correct!')
    else:
        print('Incorrect!')
