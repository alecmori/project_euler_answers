# -*- coding: utf-8 -*-
import os
from distutils import core

import numpy
from Cython.Build import cythonize

# TODO: Combine code from here with code from `utils/run_all_problems
ANSWER_DIRECTORY = 'answers'
RUN_PROBLEM = 'run_problem.pyx'


def main():
    core.setup(
        ext_modules=cythonize(
            # TODO: Use kwarg
            [
                'utils/proj_eul_math/combinatorics.pyx',
                'utils/proj_eul_math/general.pyx',
                'utils/proj_eul_math/lexical.pyx',
                'utils/proj_eul_math/prime.pyx',
            ] + _get_all_run_problems(
                answer_dir=ANSWER_DIRECTORY,
                module_name=RUN_PROBLEM,
            ),
            include_path=[numpy.get_include()],
        ),
        include_dirs=[numpy.get_include()],
    )


def _get_all_run_problems(answer_dir, module_name):
    """TODO"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return [
        os.path.join(
            answer_dir,
            problem_directory,
            module_name,
        )
        for problem_directory in os.listdir(
            os.path.join(
                base_dir,
                answer_dir,
            ),
        )
        if os.path.isfile(
            os.path.join(
                base_dir,
                answer_dir,
                problem_directory,
                module_name,
            ),
        )
    ]


if __name__ == '__main__':
    main()
