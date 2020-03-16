import cython

@cython.locals(
    truncatable_primes=list, all_primes=set, p=cython.ulong,
    num=cython.uint, all_truncated_primes=cython.uint,
)
cpdef unsigned int run_problem()

@cython.locals(numbers=list)
cpdef list _get_right_truncated_numbers(unsigned int n)

@cython.locals(numbers=list, incrementer=cython.ulong)
cpdef list _get_left_truncated_numbers(unsigned int n)
