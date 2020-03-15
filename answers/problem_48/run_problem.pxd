import cython

@cython.locals(total_with_modulus=cython.ulong, i=cython.uint)
cpdef unsigned long int run_problem(unsigned int n=*)
