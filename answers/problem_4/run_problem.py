# -*- coding: utf-8 -*-
def run_problem(max_value=1000):
    pass


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
