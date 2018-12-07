# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASELINE_ORDER = ord('A') - 1
NAMES_FILE = 'names.txt'


cpdef unsigned long long int run_problem(str names_file=NAMES_FILE):
    with open(os.path.join(BASE_DIR, NAMES_FILE)) as fh:
        names_list = sorted(next(fh).split(','))
    cdef unsigned long long int total = 0
    for index, name in enumerate(names_list):
        total += (index + 1) * _get_name_value(name=name)
    return total


cdef unsigned long int _get_name_value(str name=''):
    cdef unsigned long int total = 0
    for c in name:
        if c == '"':
            continue
        total += ord(c) - BASELINE_ORDER
    return total


if __name__ == '__main__':
    answer = run_problem()
    #TODO
    if answer == -1:
        print('Correct!')
    else:
        print('Incorrect!')
