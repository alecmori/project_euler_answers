import cython

@cython.locals(DENOMINATIONS=list)
cpdef unsigned long run_problem(unsigned int n=*)

cpdef unsigned long _count_denominations(
    int n=*, unsigned int pos=*, list denominations=*)
