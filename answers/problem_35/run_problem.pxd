import cython
from utils.proj_eul_math cimport prime

@cython.locals(all_primes=set, circular_primes=set, i=cython.uint)
cpdef unsigned int run_problem(unsigned int n=*)
@cython.locals(
    num_digits=cython.uint, circular_primes=set, i=cython.uint,
    ten_power=cython.uint, poss_circular_prime=cython.ulong,
)
cpdef set poss_get_circular_primes(
    unsigned int n, set circular_primes, set primes,
)
cpdef set _get_numbers_only_odd(unsigned int upper_bound)
