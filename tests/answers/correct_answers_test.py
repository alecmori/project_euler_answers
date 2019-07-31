# -*- coding: utf-8 -*-
import hashlib
import importlib

# TODO: Configurize this along with utils/run_all_problems consts
ANSWER_DIRECTORY = 'answers'
RUN_PROBLEM = 'run_problem'

PROBLEM_DIRECTORY_TO_ANSWER = {
    'problem_1': 'e1edf9d1967ca96767dcc2b2d6df69f4',
    'problem_2': '4194eb91842c8e7e6df099ca73c38f28',
    'problem_3': '94c4dd41f9dddce696557d3717d98d82',
    'problem_4': 'd4cfc27d16ea72a96b83d9bdef6ce2ec',
    'problem_5': 'bc0d0a22a7a46212135ed0ba77d22f3a',
    'problem_6': '867380888952c39a131fe1d832246ecc',
    'problem_7': '8c32ab09ec0210af60d392e9b2009560',
    'problem_8': '0f53ea7949d32ef24f9186207600403c',
    'problem_9': '24eaa9820350012ff678de47cb85b639',
    'problem_10': 'd915b2a9ac8749a6b837404815f1ae25',
    'problem_11': '678f5d2e1eaa42f04fa53411b4f441ac',
    'problem_12': '8091de7d285989bbfa9a2f9f3bdcc7c0',
    'problem_13': '361113f19fd302adc31268f8283a4f2d',
    'problem_14': '5052c3765262bb2c6be537abd60b305e',
    'problem_15': '928f3957168ac592c4215dcd04e0b678',
    'problem_16': '6a5889bb0190d0211a991f47bb19a777',
    'problem_17': '6a979d4a9cf85135408529edc8a133d0',
    'problem_18': '708f3cf8100d5e71834b1db77dfa15d6',
    'problem_19': 'a4a042cf4fd6bfb47701cbc8a1653ada',
    'problem_20': '443cb001c138b2561a0d90720d6ce111',
    'problem_21': '51e04cd4e55e7e415bf24de9e1b0f3ff',
    'problem_22': 'f2c9c91cb025746f781fa4db8be3983f',
    'problem_23': '2c8258c0604152962f7787571511cf28',
    'problem_24': '7f155b45cb3f0a6e518d59ec348bff84',
    'problem_25': 'a376802c0811f1b9088828288eb0d3f0',
    'problem_26': '6aab1270668d8cac7cef2566a1c5f569',
    'problem_27': '69d9e3218fd7abb6ff453ea96505183d',
    'problem_28': '0d53425bd7c5bf9919df3718c8e49fa6',
    'problem_29': '6f0ca67289d79eb35d19decbc0a08453',
    'problem_30': '27a1779a8a8c323a307ac8a70bc4489d',
    'problem_31': '142dfe4a33d624d2b830a9257e96726d',
    'problem_35': 'b53b3a3d6ab90ce0268229151c9bde11',
    'problem_67': '9d702ffd99ad9c70ac37e506facc8c38',
}


class TestAnswersCorrect:

    def test_all_answers_correct(self):
        for problem_dir, hash_answer in PROBLEM_DIRECTORY_TO_ANSWER.items():
            module_to_run = '{answer_dir}.{problem_dir}.{run_problem}'.format(
                answer_dir=ANSWER_DIRECTORY,
                problem_dir=problem_dir,
                run_problem=RUN_PROBLEM,
            )
            answer = importlib.import_module(module_to_run).run_problem()
            assert hashlib.md5(str(answer).encode()).hexdigest() == hash_answer
