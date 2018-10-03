# -*- coding: utf-8 -*-
import importlib
import os
import timeit

ANSWER_DIRECTORY = 'answers'
RUN_PROBLEM = 'run_problem'

# TODO: Allow for subset of problems to be run
# TODO: Allow for problems to be timed
# TODO: Break this up into own modules


def run_all_problems():
    # TODO: use argnames
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for problem_directory in sorted(
        os.listdir(
            os.path.join(
                base_dir,
                ANSWER_DIRECTORY,
            ),
        ),
        # Sort by
        key=_get_problem_number,
    ):
        # TODO: Determine logic here
        if not os.path.isfile(
            os.path.join(
                base_dir,
                ANSWER_DIRECTORY,
                problem_directory,
                '{run_problem}.py'.format(
                    run_problem=RUN_PROBLEM,
                ),
            ),
        ):
            continue
        module_to_run = '{answer_dir}.{problem_dir}.{run_problem}'.format(
            answer_dir=ANSWER_DIRECTORY,
            problem_dir=problem_directory,
            run_problem=RUN_PROBLEM,
        )
        try:
            problem = importlib.import_module(module_to_run).run_problem
            print(
                'Problem {num}: Answer {answer}, took {sec} seconds'.format(
                    num=_get_problem_number(
                        possible_problem_directory=problem_directory,
                    ),
                    answer=problem(),
                    sec=timeit.timeit(problem, number=100),
                ),
            )
        except BaseException:
            print('Uh oh')


def _get_problem_number(possible_problem_directory):
    if not possible_problem_directory.startswith('problem'):
        return -1
    return int(possible_problem_directory.split('_')[1])


if __name__ == '__main__':
    run_all_problems()
