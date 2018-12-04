# -*- coding: utf-8 -*-

ONE_THROUGH_NINETEEN = [
    NotImplementedError,
    len('one'),
    len('two'),
    len('three'),
    len('four'),
    len('five'),
    len('six'),
    len('seven'),
    len('eight'),
    len('nine'),
    len('ten'),
    len('eleven'),
    len('twelve'),
    len('thirteen'),
    len('fourteen'),
    len('fifteen'),
    len('sixteen'),
    len('seventeen'),
    len('eighteen'),
    len('nineteen'),
]

TWENTY_THROUGH_NINETY = [
    NotImplementedError,
    NotImplementedError,
    len('twenty'),
    len('thirty'),
    len('forty'),
    len('fifty'),
    len('sixty'),
    len('seventy'),
    len('eighty'),
    len('ninety'),
]

HUNDRED = len('hundred')
THOUSAND = len('thousand')

cpdef unsigned int run_problem(unsigned int max_value=1000):
    cdef unsigned int total_count = 0
    for number in range(1, max_value + 1):
        tens_and_one_count = _get_tens_and_one_count(
            number=number,
        )
        total_count += _get_hundreds_count(
            number=number,
            tens_and_one_count=tens_and_one_count,
        ) + tens_and_one_count + _get_thousand_count(
            number=number,
        )
    return total_count


cdef unsigned int _get_tens_and_one_count(unsigned int number):
    cdef unsigned int last_two_digits = number % 100
    cdef unsigned int first_digit
    cdef unsigned int last_digit
    if last_two_digits == 0:
        return 0
    elif last_two_digits < 20:
        return ONE_THROUGH_NINETEEN[last_two_digits]
    else:
        last_digit = last_two_digits % 10
        first_digit = int(last_two_digits/10)
        if last_digit != 0:
            return (
                ONE_THROUGH_NINETEEN[last_digit] +
                TWENTY_THROUGH_NINETY[first_digit]
            )
        else:
            return TWENTY_THROUGH_NINETY[first_digit]

cdef unsigned int _get_hundreds_count(
    unsigned int number,
    unsigned int tens_and_one_count,
):
    cdef unsigned int hundreds_digit = int(number/100) % 10
    if not hundreds_digit:
        return 0
    elif not tens_and_one_count:
        return HUNDRED + ONE_THROUGH_NINETEEN[hundreds_digit]
    else:
        return (
            HUNDRED +
            ONE_THROUGH_NINETEEN[hundreds_digit] +
            len('and')
        )

# TODO: Generalize this function to get all digits for finite but
#   arbitrarily large number
cdef unsigned int _get_thousand_count(unsigned int number):
    thousand_digit = int(number / 1000)
    if not thousand_digit:
        return 0
    else:
        return THOUSAND + ONE_THROUGH_NINETEEN[thousand_digit]


if __name__ == '__main__':
    answer = run_problem(max_value=5)
    if answer == 19:
        print('Correct!')
    else:
        print('Incorrect!')
