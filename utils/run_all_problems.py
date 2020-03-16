# -*- coding: utf-8 -*-
import argparse
import hashlib
import importlib
import os
import timeit
import traceback

from utils import readme_utils

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
        run_problem(problem_directory=problem_directory, args=args)

def run_problem(problem_directory, args):
    module_to_run = '{answer_dir}.{problem_dir}.{run_problem}'.format(
        answer_dir=ANSWER_DIRECTORY,
        problem_dir=problem_directory,
        run_problem=RUN_PROBLEM,
    )
    try:
        problem = importlib.import_module(module_to_run).run_problem
        if args.show_answers:
            answer_str = 'Answer {answer}, took '.format(answer=problem())
        else:
            answer_str = ''
        avg_time = '%.4g' % float(
            timeit.timeit(
                problem,
                number=args.num_trials,
            ) / args.num_trials
        )
        print(
            'Problem {num}: {answer_str}{sec} seconds'.format(
                num=_get_problem_number(
                    possible_problem_directory=problem_directory,
                ),
                answer_str=answer_str,
                # TODO: Pretty print
                sec=avg_time,
            ),
        )
        if args.write_results:
           readme_utils.adjust_time_for_problem(
               problem_number=_get_problem_number(
                   possible_problem_directory=problem_directory,
               ),
               version=args.version,
               new_time=avg_time,
               dry_run=False,
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
    parser.add_argument(
        '-s',
        '--show-answers',
        dest='show_answers',
        help='Whether or not to show the answer',
        action='store_true',
    )
    parser.add_argument(
        '-w',
        '--write-results',
        dest='write_results',
        default=False,
        help='Whether or not write the results to a file',
        action='store_true',
    )
    parser.add_argument(
        '-v',
        '--version',
        dest='version',
        help=(
            'Which version of the code you are running. Currently supported '
            'verions: Cython | Python'
        ),
    )
    return parser.parse_args()


def _get_problem_number(possible_problem_directory):
    if not possible_problem_directory.startswith('problem'):
        return -1
    return int(possible_problem_directory.split('_')[1])


if __name__ == '__main__':
    run_all_problems()
