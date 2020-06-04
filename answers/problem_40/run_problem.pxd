import cython
@cython.locals(
    curr_digit_count=cython.uint, curr_multiple=cython.uint,
    curr_lower_bound=cython.uint, final_number=cython.uint,
    final_digit=cython.uint)
cpdef unsigned int get_nth_digit(unsigned int n)

@cython.locals(total=cython.uint, i=cython.uint)
cpdef unsigned int run_problem(list digits=*)
