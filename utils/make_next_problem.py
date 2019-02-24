# -*- coding: utf-8 -*-
import argparse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INIT_PATH = '__init__.py'
PROBLEM_DIR_BASE = 'answers'
PROBLEM_DIR_TEMPLATE = 'problem_{num}'
RATIONALE_PATH = 'rationale_in_latex.md'
RUN_PROBLEM_PATH = 'run_problem.py'
RUN_PROBLEM_TEMPLATE_CODE = """
# -*- coding: utf-8 -*-
cpdef run_problem(n):
    pass


if __name__ == '__main__':
    answer = run_problem()
    #TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
"""
RUN_PROBLEM_HEADER_PATH = 'run_problem.pxd'
RUN_PROBLEM_HEADER_TEMPLATE_CODE = """
cpdef unsigned int run_problem(unsigned int n)
"""


def add_problem():
    args = _get_args()
    if args.number:
        problem_number = args.number
    else:
        problem_number = _get_problem_number()
    _make_new_problem_directory(problem_number=problem_number)


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--number',
        help='What number of problem you want to create.',
        type=int,
    )
    return parser.parse_args()


def _get_problem_number():
    problem_directory = os.path.join(BASE_DIR, PROBLEM_DIR_BASE)
    return max(
        int(name.split('_')[1])
        for name in os.listdir(problem_directory)
        if (
            name.startswith('problem')
            and os.path.isdir(os.path.join(problem_directory, name))
        )
    ) + 1


def _make_new_problem_directory(problem_number):
    new_directory = os.path.join(
        BASE_DIR,
        PROBLEM_DIR_BASE,
        PROBLEM_DIR_TEMPLATE.format(num=problem_number),
    )
    if os.path.exists(new_directory):
        return
    print('Making {dir}'.format(dir=new_directory))
    os.makedirs(new_directory)
    with open(os.path.join(new_directory, INIT_PATH), 'w'):
        pass
    with open(os.path.join(new_directory, RATIONALE_PATH), 'w'):
        pass
    with open(os.path.join(new_directory, RUN_PROBLEM_PATH), 'w') as fh:
        fh.write(RUN_PROBLEM_TEMPLATE_CODE.strip())
    with open(os.path.join(new_directory, RUN_PROBLEM_HEADER_PATH), 'w') as fh:
        fh.write(RUN_PROBLEM_HEADER_TEMPLATE_CODE.strip())


if __name__ == '__main__':
    add_problem()
