# -*- coding: utf-8 -*-
import numpy
from utils.proj_eul_math import prime


def generate_triangle_numbers():
    cdef int n = 0
    while True:
        n += 1
        yield int(n * (n + 1) / 2)


# TODO: Be smarter about this
def get_divisors(unsigned long long int num=0):
    cdef unsigned int n = 1
    while n <= numpy.sqrt(num):
        if num % n == 0:
            yield n
            yield int(num / n )
        n += 1


cdef unsigned int get_num_divisors(unsigned int num):
    total_divisors = 1
    for x in prime.get_prime_factorization(num=num).values():
        total_divisors *= x + 1
    return total_divisors


cdef greatest_common_denominator(
    unsigned long long int a,
    unsigned long long int b,
):
    cdef int temp = 0
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a


cdef least_common_multiple(
    unsigned long long int a,
    unsigned long long int b,
):
    return a * b // greatest_common_denominator(a=a, b=b)
