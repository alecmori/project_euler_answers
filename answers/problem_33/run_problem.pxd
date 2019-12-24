import cython

@cython.locals(
    max_num=cython.uint, min_num=cython.uint,
    first_digit_numer=cython.uint, first_digit_denom=cython.uint,
    second_digit_numer=cython.uint, second_digit_denom=cython.uint,
)
cpdef unsigned int run_problem(unsigned int n=*)
