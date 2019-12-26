# -*- coding: utf-8 -*-
def run_problem(n=1000000):
    total = 0
    for num in range(1, n, 2):
        s_num = str(num)
        if not _is_palindrome(s_num, start=0, end=len(s_num) - 1):
            continue
        b_num = bin(num)
        if not _is_palindrome(b_num, start=2, end=len(b_num) - 1):
            continue
        total += num
    return total

def _is_palindrome(string, start=0, end=0):
    if end == 0:
        end = len(string) - 1
    while end > start:
        if string[end] != string[start]:
            return False
        end -= 1
        start += 1
    return True

if __name__ == '__main__':
    answer = run_problem()
    if answer == 872187:
        print('Correct!')
    else:
        print('Incorrect!')
