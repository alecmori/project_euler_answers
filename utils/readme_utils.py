# -*- coding: utf-8 -*-
import os
import re
import typing


HEADERS = {
    'Problem': ' Problem Number ',
    'Cython': ' Cython (s) ',
    'Python': ' Python (s) ',
}
# TODO: Stronger float matching for second two groups.
LINE_REGEX = r'\|\s+(\d+) \|\s+(.+) \|\s+(.+) \|'
README_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'README.md')
print(README_FILE)

def adjust_time_for_problem(
    problem_number: typing.Text, version: typing.Text, new_time: typing.Text,
    dry_run: bool=True,
):
    problem_number = str(problem_number)
    with open(README_FILE, 'r') as fh:
        lines = fh.read().split('\n')
    for i, line in enumerate(lines):
        matching = re.match(LINE_REGEX, line)
        if matching:
            curr_problem_number, python_time, cython_time = matching.group(1, 2, 3)
            if problem_number == curr_problem_number:
                lines[i] = _get_new_line(
                    problem_number=problem_number,
                    python_time=python_time,
                    cython_time=cython_time,
                        new_time=new_time,
                    version=version,
                )
    if not dry_run:
        with open(README_FILE, 'w') as fh:
            fh.write('\n'.join(lines))

def _get_new_line(
    problem_number: typing.Text, python_time: typing.Text,
    cython_time: typing.Text, new_time: typing.Text, version: typing.Text,
) -> typing.Text:
    new_line = '|'.join(
        [
            _generate_section(
                header=HEADERS['Problem'],
                value=problem_number,
            ),
            _generate_section(
                header=HEADERS['Python'],
                value=python_time if version != 'Python' else new_time,
            ),
            _generate_section(
                header=HEADERS['Cython'],
                value=cython_time if version != 'Cython' else new_time,
            ),
        ]
    )
    return '|' + new_line + '|'

def _generate_section(header: typing.Text, value: typing.Text) -> typing.Text:
    right_side_value = value + ' '
    num_spaces = len(header) - len(right_side_value)
    return ' ' * num_spaces + right_side_value

if __name__ == '__main__':
    adjust_time_for_problem('1', 'Cython', '3.1593')

