import cython

@cython.locals(total=cython.ulong)
cpdef unsigned long run_problem(unsigned int power=*)

@cython.locals(i=cython.ulong, aggregate_sum_of_powers=cython.ulong)
cpdef unsigned long _get_upper_bound(unsigned int power=*)

@cython.locals(total=cython.ulong, num_iter=cython.ulong)
cpdef unsigned short _is_sum_of_power_of_digits(
    unsigned long num=*, unsigned int power=*,
)
