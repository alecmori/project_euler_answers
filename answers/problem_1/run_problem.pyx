# -*- coding: utf-8 -*-
# TODO: Rewrite combinatorically a + b - (a \and b)


cpdef unsigned long long int run_problem(unsigned int n=1000, set multiple_set={3, 5}):
    cdef unsigned long long int total = 0
    for num in range(n):
        if any_divides(num=num, multiple_set=multiple_set):
            total += num
    return total


cdef unsigned int any_divides(unsigned int num, set multiple_set):
    return any(
        num % x == 0
        for x in multiple_set
    )

if __name__ == '__main__':
    answer = run_problem(n=10, multiple_set={3, 5})
    if answer == 23:
        print('Correct!')
    else:
        print('Incorrect!')
