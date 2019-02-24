# -*- coding: utf-8 -*-
import math
import queue

import cython


def run_problem(max_value=1000):
    for product in _iterate_by_max_product(max_value_inclusive=max_value - 1):
        if _is_palindromic(num=product):
            return product


# TODO: Explain this behemoth of a function
@cython.locals(
    combination_sum=cython.uint, first_value=cython.uint,
    second_value=cython.uint, value=cython.uint,
)
def _iterate_by_max_product(max_value_inclusive=0):
    combination_sum = max_value_inclusive * 2
    first_value = math.ceil(combination_sum / 2)
    second_value = math.floor(combination_sum / 2)
    value = 0
    priority_queue = queue.PriorityQueue()
    while combination_sum > 0:
        if priority_queue.empty():
            for product in _get_all_products(
                combination_sum=combination_sum,
                max_value_inclusive=max_value_inclusive,
            ):
                priority_queue.put(-1 * product)
            combination_sum -= 1
            first_value = math.ceil(combination_sum / 2)
            second_value = math.floor(combination_sum / 2)
        value = -1 * priority_queue.get()
        if first_value * second_value > value:
            priority_queue.put(-1 * value)
            for product in _get_all_products(
                combination_sum=combination_sum,
                max_value_inclusive=max_value_inclusive,
            ):
                priority_queue.put(-1 * product)
            combination_sum -= 1
            first_value = math.ceil(combination_sum / 2)
            second_value = math.floor(combination_sum / 2)
        else:
            yield value


@cython.locals(first_value=cython.uint, second_value=cython.uint)
def _get_all_products(combination_sum, max_value_inclusive,):
    first_value = math.ceil(combination_sum / 2)
    second_value = math.floor(combination_sum / 2)
    while first_value <= max_value_inclusive and second_value >= 0:
        yield first_value * second_value
        first_value += 1
        second_value -= 1


def _is_palindromic(num=0):
    s = str(num)
    last_char_index = len(s) - 1
    for i in range(int(len(s) / 2)):
        if s[i] != s[last_char_index - i]:
            return False
    return True


if __name__ == '__main__':
    answer = run_problem(max_value=100)
    if answer == 9009:
        print('Correct!')
    else:
        print('Incorrect!')
