# -*- coding: utf-8 -*-
from __future__ import division


def run_problem(n=1001):
    n = int(n / 2)
    return int((16 * n**3 + 30 * n**2 + 26 * n + 3) / 3)


if __name__ == '__main__':
    answer = run_problem(n=5)
    # TODO
    if answer == 101:
        print('Correct!')
    else:
        print('Incorrect!')
