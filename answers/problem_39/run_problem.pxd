import collections
import cython


@cython.locals(perimeters=list, m=cython.uint)
cpdef unsigned int run_problem(unsigned int n=*)

@cython.locals(
    m=cython.uint, n=cython.uint, perimeters=list, m2=cython.uint,
    perimeter=cython.uint)
cpdef list generate_all_base_perimeters(unsigned int max_n)
