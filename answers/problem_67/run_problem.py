# -*- coding: utf-8 -*-
import urllib3

from answers.problem_18 import run_problem as rp_18
# TODO: Move to utils

TRIANGLE_LOCATION = (
    'https://projecteuler.net/project/resources/p067_triangle.txt'
)


def run_problem():
    return rp_18.run_problem(
        triangle='\n'.join(
            x.decode('utf-8')
            for x in urllib3.PoolManager().request(
                'GET', TRIANGLE_LOCATION,
            ).data.splitlines()
        ),
    )


if __name__ == '__main__':
    answer = run_problem()
    # TODO
    if answer == 7273:
        print('Correct!')
    else:
        print('Incorrect!')
