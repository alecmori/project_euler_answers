import cython

@cython.locals(total=cython.uint)
cpdef unsigned int run_problem(unsigned int max_value=*)
@cython.locals(amicable_pair=cython.uint)
cdef int is_pair_amicable(unsigned int n=*)
