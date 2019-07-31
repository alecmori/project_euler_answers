# -*- coding: utf-8 -*-

# TODO: See if generating functions are quicker
def run_problem(n=200):
    DENOMINATIONS = sorted(
        [200, 100, 50, 20, 10, 5, 2, 1],
        reverse=True,
    )
    return _count_denominations(
        n=n,
        pos=0,
        denominations=DENOMINATIONS,
    )

def _count_denominations(n=0, pos=0, denominations=[]):
    if n < 0:
        return 0
    if pos >= len(denominations):
        return 0
    if n == 0:
        return 1
    return _count_denominations(
        n=n - denominations[pos],
        pos=pos,
        denominations=denominations,
    ) + _count_denominations(
        n=n,
        pos=pos + 1,
        denominations=denominations,
    )

if __name__ == '__main__':
    answer = run_problem(5)
    if answer == 4:
        print('Correct!')
    else:
        print('Incorrect!')
