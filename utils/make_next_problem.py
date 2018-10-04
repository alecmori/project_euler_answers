# -*- coding: utf-8 -*-
import argparse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INIT_PATH = '__init__.py'
PROBLEM_DIR_BASE = 'answers'
PROBLEM_DIR_TEMPLATE = 'problem_{num}'
RATIONALE_PATH = 'rationale.md'
RUN_PROBLEM_PATH = 'run_problem.py'
RUN_PROBLEM_TEMPLATE_CODE = """
# -*- coding: utf-8 -*-
def run_problem():
    pass


if __name__ == '__main__':
    answer = run_problem()
    #TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
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
    pass

# TODO add arguments


def _make_new_problem_directory(problem_number):
    new_directory = os.path.join(
        BASE_DIR,
        PROBLEM_DIR_BASE,
        PROBLEM_DIR_TEMPLATE.format(num=problem_number),
    )
    if os.path.exists(new_directory):
        return
    os.makedirs(new_directory)
    with open(os.path.join(new_directory, INIT_PATH), 'w'):
        pass
    with open(os.path.join(new_directory, RATIONALE_PATH), 'w'):
        pass
    with open(os.path.join(new_directory, RUN_PROBLEM_PATH), 'w') as fh:
        fh.write(RUN_PROBLEM_TEMPLATE_CODE.strip())


if __name__ == '__main__':
    add_problem()
