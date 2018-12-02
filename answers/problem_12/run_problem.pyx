# -*- coding: utf-8 -*-
from utils.proj_eul_math import prime

cpdef run_problem(unsigned int num_divisors=500):
    cdef unsigned int n = 3
    cdef dict prime_factorization_1 = prime.get_prime_factorization(2)
    cdef dict prime_factorization_2 = prime.get_prime_factorization(3)
    cdef unsigned int curr_num_divisors = _get_curr_num_divisors(
        factorizations=[
            prime_factorization_1,
            prime_factorization_2,
        ],
    )
    while curr_num_divisors < num_divisors:
        n += 1
        prime_factorization_1 = prime_factorization_2
        prime_factorization_2 = prime.get_prime_factorization(n)
        curr_num_divisors = _get_curr_num_divisors(
            factorizations=[
                prime_factorization_1,
                prime_factorization_2,
            ],
        )
    return int(n * (n - 1) / 2)


#TODO: explain logic
cdef unsigned int _get_curr_num_divisors(list factorizations):
    cdef unsigned int total_product = 1
    for factorization in factorizations:
        for key, value in factorization.items():
            if key == 2:
                total_product *= value
            else:
                total_product *= (value + 1)
    return total_product


if __name__ == '__main__':
    answer = run_problem(num_divisors=5)
    if answer == 28:
        print('Correct!')
    else:
        print('Incorrect!')
