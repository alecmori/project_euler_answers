# -*- coding: utf-8 -*-
# TODO: Rewrite combinatorically a + b - (a \and b)


def run_problem(n=1000, multiple_set={3, 5}):
    return sum(
        num
        for num in range(n)
        if any(
            num % x == 0
            for x in multiple_set
        )
    )


if __name__ == '__main__':
    answer = run_problem(n=10, multiple_set={3, 5})
    if answer == 23:
        print('Correct!')
    else:
        print('Incorrect!')
