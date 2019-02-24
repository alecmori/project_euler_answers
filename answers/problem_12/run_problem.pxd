import cython

@cython.locals(
    n=cython.uint, prime_factorization_1=dict,
    prime_factorization_2=dict, curr_num_divisors=cython.uint,
)
cpdef unsigned int run_problem(unsigned int num_divisors=*)
@cython.locals(total_product=cython.uint)
cdef unsigned int _get_curr_num_divisors(list factorizations)
