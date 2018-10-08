# -*- coding: utf-8 -*-
import math


def run_problem(max_value=1000):
    for v_1, v_2 in _iterate_by_max_product(max_value_inclusive=max_value - 1):
        possible_palindrome = v_1 * v_2
        if _is_palindromic(s=str(possible_palindrome)):
            return possible_palindrome


def _iterate_by_max_product(max_value_inclusive):
    for combination_sum in range(max_value_inclusive * 2, 0, -1):
        first_value = math.ceil(combination_sum / 2)
        second_value = math.floor(combination_sum / 2)
        while first_value <= max_value_inclusive and second_value >= 0:
            yield first_value, second_value
            first_value += 1
            second_value -= 1


def _is_palindromic(s: str):
    last_char_index = len(s) - 1
    return all(
        s[i] == s[last_char_index - i]
        for i in range(int(len(s) / 2))
    )


if __name__ == '__main__':
    answer = run_problem(max_value=100)
    if answer == 9009:
        print('Correct!')
    else:
        print('Incorrect!')
