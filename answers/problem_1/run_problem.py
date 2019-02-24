# -*- coding: utf-8 -*-
# TODO: Rewrite combinatorically a + b - (a \and b)


def run_problem(n=1000, multiple_set={3, 5}):
    total = 0
    for num in range(n):
        if any_divides(num=num, multiple_set=multiple_set):
            total += num
    return total


def any_divides(num, multiple_set):
    for x in multiple_set:
        if num % x == 0:
            return True
    return False


if __name__ == '__main__':
    answer = run_problem(n=10, multiple_set={3, 5})
    if answer == 23:
        print('Correct!')
    else:
        print('Incorrect!')
