# -*- coding: utf-8 -*-
def greatest_common_denominator(a, b):
    if b > a:
        temp = b
        b = a
        a = temp
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a


def least_common_multiple(a, b):
    return int(a * b / greatest_common_denominator(a=a, b=b))
