import cython

@cython.locals(x=cython.uint, y=cython.uint, n=cython.uint, r=cython.uint)
cpdef list _sieve_of_atkin(unsigned long long int limit)
@cython.locals(prime_dict=dict, upper_bound=cython.ulonglong)
cpdef dict get_prime_factorization(unsigned long long int num=*)
@cython.locals(n=cython.uint)
cpdef int _get_num_times_prime_divides(
    unsigned long long int num,
    unsigned long long int prime,
)
cpdef int is_prime(unsigned long long int num)
