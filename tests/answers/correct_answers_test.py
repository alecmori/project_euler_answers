# -*- coding: utf-8 -*-
import importlib

# TODO: Configurize this along with utils/run_all_problems consts
ANSWER_DIRECTORY = 'answers'
RUN_PROBLEM = 'run_problem'

PROBLEM_DIRECTORY_TO_ANSWER = {
    'problem_1': 233168,
    'problem_2': 4613732,
    'problem_3': 6857,
    'problem_4': 906609,
    'problem_5': 232792560,
    'problem_6': 25164150,
    'problem_7': 104743,
    'problem_8': 23514624000,
    'problem_9': 31875000,
    'problem_10': 142913828922,
    'problem_11': 70600674,
    'problem_12': 76576500,
    'problem_13': 5537376230,
    'problem_14': 837799,
    'problem_15': 137846528820,
    'problem_16': 1366,
    'problem_17': 21124,
    'problem_18': 1074,
    'problem_19': 171,
    'problem_20': 648,
    'problem_21': 31626,
    'problem_22': 871198282,
    'problem_23': 4179871,
    'problem_24': 2783915460,
}


class TestAnswersCorrect:

    def test_all_answers_correct(self):
        for problem_dir, answer in PROBLEM_DIRECTORY_TO_ANSWER.items():
            module_to_run = '{answer_dir}.{problem_dir}.{run_problem}'.format(
                answer_dir=ANSWER_DIRECTORY,
                problem_dir=problem_dir,
                run_problem=RUN_PROBLEM,
            )
            assert (
                importlib.import_module(module_to_run).run_problem() ==
                answer
            )
