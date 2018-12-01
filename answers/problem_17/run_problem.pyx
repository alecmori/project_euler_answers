# -*- coding: utf-8 -*-

ONE_THROUGH_NINETEEN = [
    # one
    3,
    # two
    3,
    # three
    5,
    # four
    4,
    # five
    4,
    # six
    3,
    # seven
    5,
    # eight
    5,
    # nine
    4,
    # ten
    3,
    # eleven
    6,
    # twelve
    6,
    # thirteen
    8,
    # fourteen
    8,
    # fifteen
    7,
    # sixteen
    7,
    # seventeen
    9,
    # eighteen
    8,
    # nineteen
    8,
]

TWENTY_TO_NINETY = [
    # twenty
    6,
    # thirty
    6,
    # forty
    5,
    # fifty
    5,
    # sixty
    5,
    # seventy
    7,
    # eighty
    6,
    # ninety,
    6,
]

# HUNDRED
HUNDRED = 7

def run_problem(max_value=1000):
    total_count = 0
    for number in range(1, max_value + 1):
        tens_and_one_count = _get_tens_and_one_count(
            number=number,
        )
        hundreds_count = _get_hundreds_count(
            number=number,
            tens_and_one_count=tens_and_one_count,
        )
    return total_count


def _get_tens_and_one_count(number: int) -> int:
    return 1

def _get_hundreds_count(number:int, tens_and_one_count: int) -> int:
    return 1


if __name__ == '__main__':
    answer = run_problem(max_value=5)
    if answer == 19:
        print('Correct!')
    else:
        print('Incorrect!')
