import cython
from utils.proj_eul_math cimport combinatorics

@cython.locals(total=cython.ulonglong)
cpdef unsigned int run_problem(unsigned int n=*)
