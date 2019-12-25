import cython

@cython.locals(
    upper_bound=cython.uint, factorials=list, sum_of_sums=cython.uint,
    i=cython.uint, num=cython.uint, total=cython.uint, num_copy=cython.uint,
)
cpdef unsigned int run_problem()

cpdef unsigned int _get_upper_bound()
