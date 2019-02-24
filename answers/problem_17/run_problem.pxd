import cython

@cython.locals(total_count=cython.uint)
cpdef unsigned int run_problem(unsigned int max_value=*)
@cython.locals(
    last_two_digits=cython.uint, first_digit=cython.uint,
    last_digit=cython.uint,
)
cdef unsigned int _get_tens_and_one_count(unsigned int number)
@cython.locals(hundreds_digit=cython.uint)
cdef unsigned int _get_hundreds_count(
    unsigned int number,
    unsigned int tens_and_one_count,
)
@cython.locals(thousand_digit=cython.uint)
cdef unsigned int _get_thousand_count(unsigned int number)
