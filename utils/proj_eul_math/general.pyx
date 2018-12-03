# -*- coding: utf-8 -*-
import numpy
from utils.proj_eul_math import prime


def generate_triangle_numbers():
    cdef int n = 0
    while True:
        n += 1
        yield int(n * (n + 1) / 2)


def get_num_divisors(*, unsigned int num):
    return numpy.product(
        [
            x + 1
            for x in prime.get_prime_factorization(num=num).values()
        ],
    )


def greatest_common_denominator(
    *,
    unsigned long long int a,
    unsigned long long int b,
):
    cdef int temp = 0
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a


def least_common_multiple(
    *,
    unsigned long long int a,
    unsigned long long int b,
):
    return int(a * b / greatest_common_denominator(a=a, b=b))
