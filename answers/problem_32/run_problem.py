# -*- coding: utf-8 -*-
import functools
import operator

def run_problem():
    N = 9
    pandigital_products = set()
    # Largest number must be 3-4 digits.
    for first_num in range(10**2, 10**4):
        first_num_str = str(first_num)
        first_num_digits = digit_char_set(num=first_num)
        if '0' in first_num_digits:
            continue
        for second_num in range(first_num):
            second_num_str = str(second_num)
            second_num_digits = digit_char_set(num=second_num)
            if '0' in second_num_digits:
                continue
            product = second_num * first_num
            product_str = str(product)
            digit_count = (
                len(product_str) + len(second_num_str) + len(first_num_str)
            )
            # Early stopping if we exceed the digit count
            if digit_count > N:
                break
            product_digits = digit_char_set(num=product)
            all_digits = first_num_digits.union(
                second_num_digits).union(product_digits)
            if (
                digit_count == N and
                len(all_digits) == N and
                '0' not in all_digits
            ):
                pandigital_products.add(product)
    return functools.reduce(operator.add, pandigital_products, 0)

def digit_char_set(num=0):
    digits = set()
    for c in str(num):
        digits.add(c)
    return digits


if __name__ == '__main__':
    answer = run_problem()
    if answer == 45228:
        print('Correct!')
    else:
        print('Incorrect!')
