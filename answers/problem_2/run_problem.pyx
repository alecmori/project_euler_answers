# -*- coding: utf-8 -*-
def run_problem(max_value=4000000):
    return sum(
        num
        for num in _fibonacci_iterator(max_value=max_value)
        if num % 2 == 0
    )


def _fibonacci_iterator(max_value):
    n1 = 1
    n2 = 2
    while n1 < max_value:
        yield n1
        temp = n1
        n1 = n2
        n2 = n1 + temp


if __name__ == '__main__':
    answer = run_problem(max_value=100)
    if answer == 44:
        print('Correct!')
    else:
        print('Incorrect!')
