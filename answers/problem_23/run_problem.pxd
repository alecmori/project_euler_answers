import cython

@cython.locals(total=cython.ulong, abundant_sums=set)
cpdef unsigned long int run_problem(unsigned int max_abundant_number=*)
@cython.locals(sorted_abundant_number=list, all_summed_abundant_numbers=set)
cdef set _get_all_abundant_sums(unsigned int max_abundant_number=*)
@cython.locals(abundant_numbers=list)
cdef list _get_sorted_abundant_numbers(unsigned int max_abundant_number=*)
cdef unsigned int _get_sum_proper_divisors(unsigned int n=*)
