# -*- coding: utf-8 -*-
import fractions

def run_problem(n=2):
    max_num = 10**n
    min_num = 10**(n-1)
    total_frac = fractions.Fraction(1, 1)
    for denom in range(min_num + 1 , max_num):
        for numer in range(min_num, denom):
            first_digit_numer = int(numer / 10)
            second_digit_numer = numer % 10
            first_digit_denom = int(denom / 10)
            second_digit_denom = denom % 10
            if (
                first_digit_numer == 0 or
                second_digit_numer == 0 or
                first_digit_denom == 0 or
                second_digit_denom == 0
            ):
                continue
            new_frac = None
            if first_digit_numer == first_digit_denom:
                new_frac = fractions.Fraction(
                    second_digit_numer,
                    second_digit_denom,
                )
            elif first_digit_numer == second_digit_denom:
                new_frac = fractions.Fraction(
                    second_digit_numer,
                    first_digit_denom,
                )
            elif second_digit_numer == first_digit_denom:
                new_frac = fractions.Fraction(
                    first_digit_numer,
                    second_digit_denom,
                )
            elif second_digit_numer == second_digit_denom:
                new_frac = fractions.Fraction(
                    first_digit_numer,
                    first_digit_denom,
                )
            if not new_frac:
                continue
            orig_frac = fractions.Fraction(numer, denom)
            if new_frac == orig_frac:
                total_frac *= orig_frac
    return total_frac.denominator


if __name__ == '__main__':
    answer = run_problem()
    if answer == 100:
        print('Correct!')
    else:
        print('Incorrect!')
