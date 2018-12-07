# -*- coding: utf-8 -*-
import requests

BASELINE_ORDER = ord('A') - 1
NAMES_URL = 'https://projecteuler.net/project/resources/p022_names.txt'


cpdef unsigned long long int run_problem(str names_file=NAMES_URL):
    cdef list names_list = sorted(
        requests.get(NAMES_URL).text.split(','),
    )
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
