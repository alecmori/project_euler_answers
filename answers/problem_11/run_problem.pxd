cimport numpy

cpdef unsigned long int run_problem(unsigned int num_digits=*)
cdef unsigned long int _get_largest_down_right_diagonal(
    numpy.ndarray grid,
    unsigned int num,
)
cdef unsigned long int _get_largest_row(
    numpy.ndarray grid,
    unsigned int num,
)
