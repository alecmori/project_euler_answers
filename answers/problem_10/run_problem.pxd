import cython

@cython.locals(total=cython.ulonglong)
cpdef unsigned long long int run_problem(unsigned long int max_value=*)
