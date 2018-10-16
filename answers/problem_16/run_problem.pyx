# -*- coding: utf-8 -*-
def run_problem(power=1000):
    return sum(
        int(x)
        for x in str(2**power)
    )


if __name__ == '__main__':
    answer = run_problem(power=15)
    if answer == 26:
        print('Correct!')
    else:
        print('Incorrect!')
