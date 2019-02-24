import cython
from utils.proj_eul_math cimport combinatorics

@cython.locals(
    curr_digit=cython.uint, curr_place=cython.uint, factorial=cython.uint,
    digits=list, ordered_digits=list,
)
cpdef unsigned int run_problem(unsigned int place_of_permutation=*)
