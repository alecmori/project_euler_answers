import cython

@cython.locals(lcm=cython.ulonglong)
cpdef unsigned long long int run_problem(unsigned int max_value=*)
