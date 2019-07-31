# -*- coding: utf-8 -*-
import argparse
import hashlib
import importlib
import os
import timeit
import traceback

ANSWER_DIRECTORY = 'answers'
NUM_TRIALS = 10
# TODO: Hack this better
PROBLEM_UPPER_BOUND = 1000000
RUN_PROBLEM = 'run_problem'

# TODO: Break this up into own modules


def run_all_problems():
    args = _get_args()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for problem_directory in sorted(
        os.listdir(
            os.path.join(
                base_dir,
                ANSWER_DIRECTORY,
            ),
        ),
        key=_get_problem_number,
    ):
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
        problem_number = _get_problem_number(
            possible_problem_directory=problem_directory,
        )
        if problem_number < args.min or problem_number > args.max:
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
                    # TODO: Pretty print
                    sec=(
                        '%.4g' %
                        float(
                            timeit.timeit(
                                problem,
                                number=args.num_trials,
                            ) / args.num_trials,
                        )
                    ),
                ),
            )
        except Exception as e:
            print('Error Running Problem: {error}'.format(error=e))
            traceback.print_exc()


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--min',
        help='The smallest problem number you want to run',
        type=int,
        default=1,
    )
    parser.add_argument(
        '-a',
        '--max',
        help='The largest problem number you want to run',
        type=int,
        default=PROBLEM_UPPER_BOUND,
    )
    parser.add_argument(
        '-n',
        '--num-trials',
        dest='num_trials',
        help='The number of times you want each problem to run',
        type=int,
        default=NUM_TRIALS,
    )
    return parser.parse_args()


def _get_problem_number(possible_problem_directory):
    if not possible_problem_directory.startswith('problem'):
        return -1
    return int(possible_problem_directory.split('_')[1])


if __name__ == '__main__':
    run_all_problems()
