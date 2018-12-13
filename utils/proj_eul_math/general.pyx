# -*- coding: utf-8 -*-
import numpy
from utils.proj_eul_math import prime


def fibonacci_iterator(max_value=0):
    if not max_value:
        max_value = float('inf')
    n1 = 1
    n2 = 1
    while n1 < max_value:
        yield n1
        temp = n1
        n1 = n2
        n2 = n1 + temp


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
            other_factor = int(num / n)
            if other_factor != n:
                yield other_factor
        n += 1


cpdef unsigned long int get_sum_divisors(unsigned int num=0):
    # TODO: Explain combinatorically
    if num == 0 or num == 1:
        return num
    cdef unsigned long int total_sum = 1
    cdef unsigned long int current_sum
    for p, num_primes in prime.get_prime_factorization(num=num).items():
        current_sum = 0
        for i in range(num_primes + 1):
            current_sum += p**i
        total_sum *= current_sum
    return total_sum

cdef unsigned int get_num_divisors(unsigned int num=0):
    # TODO: Explain combinatorically
    cdef unsigned int total_divisors = 1
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
