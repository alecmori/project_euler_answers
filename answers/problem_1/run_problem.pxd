import cython

@cython.locals(total=cython.longlong)
cpdef unsigned long long int run_problem(unsigned int n=*, set multiple_set=*)
cdef unsigned int any_divides(unsigned int num, set multiple_set)
