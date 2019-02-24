import cython
cimport numpy

from utils.proj_eul_math cimport lexical

cpdef unsigned long int run_problem(unsigned int num_digits=*)
@cython.locals(max_product=cython.ulong, x=cython.uint, y=cython.uint)
cdef unsigned long int _get_largest_down_right_diagonal(
    numpy.ndarray grid,
    unsigned int num,
)
@cython.locals(max_product=cython.ulong)
cdef unsigned long int _get_largest_row(
    numpy.ndarray grid,
    unsigned int num,
)
