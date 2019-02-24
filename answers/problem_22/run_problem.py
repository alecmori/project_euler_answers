# -*- coding: utf-8 -*-
import requests

BASELINE_ORDER = ord('A') - 1
NAMES_URL = 'https://projecteuler.net/project/resources/p022_names.txt'


def run_problem(names_file=NAMES_URL):
    names_list = sorted(
        requests.get(NAMES_URL).text.split(','),
    )
    total = 0
    for index, name in enumerate(names_list):
        total += (index + 1) * _get_name_value(name=name)
    return total


def _get_name_value(name=''):
    total = 0
    for c in name:
        if c == '"':
            continue
        total += ord(c) - BASELINE_ORDER
    return total


if __name__ == '__main__':
    answer = run_problem()
    # TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
