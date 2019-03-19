import cython

from utils.proj_eul_math cimport prime

@cython.locals(
    primes_generated=cython.uint, best_a=cython.int, best_b=cython.uint,
    a=cython.int, b=cython.uint, max_prime=cython.uint,
)
cpdef int run_problem(unsigned int n=*)
@cython.locals(n=cython.uint, poss_prime=cython.int)
cpdef unsigned int get_consecutive_primes_generated(
    int a, unsigned int b, set prime_cache, unsigned long max_prime,
)
