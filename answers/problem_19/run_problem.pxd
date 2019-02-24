import cython

@cython.locals(num_sundays=cython.uint)
cpdef unsigned int run_problem(
    unsigned int min_year=*,
    unsigned int max_year=*,
)
