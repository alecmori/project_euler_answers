import cython

cpdef unsigned int run_problem(unsigned int n=*)
@cython.locals(gcd=cython.int, order=cython.int, result=cython.int)
cpdef unsigned int get_order_mod(
    unsigned int n, unsigned int base=*, dict cached_values=*,
)
