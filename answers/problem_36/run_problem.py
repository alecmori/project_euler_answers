# -*- coding: utf-8 -*-
def run_problem(n=1000000):
    total = 0
    for num in range(1, n, 2):
        if not _is_palindrome(num):
            continue
        if not _is_bin_palindrome(num):
            continue
        total += num
    return total

def _is_palindrome(num):
    rev = 0
    orig_num = num
    while num > 0:
        rev *= 10
        rev += num % 10
        num = num // 10
    return rev == orig_num

def _is_bin_palindrome(num):
    rev = 0
    orig_num = num
    while num > 0:
        rev = rev << 1
        rev = rev | (num & 1)
        num = num >> 1
    return rev == orig_num

if __name__ == '__main__':
    answer = run_problem()
    if answer == 872187:
        print('Correct!')
    else:
        print('Incorrect!')
