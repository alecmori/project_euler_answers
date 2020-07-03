import cython

@cython.locals(total_sum=cython.ulong, current_sum=cython.ulong)
cpdef unsigned long int get_sum_divisors(unsigned int num=*)

@cython.locals(x=cython.ulonglong, seen=set)
cpdef unsigned int is_square(unsigned long long int n)

@cython.locals(total_divisors=cython.uint)
cpdef unsigned int get_num_divisors(unsigned int num=*)

@cython.locals(temp=cython.uint)
cpdef greatest_common_denominator(
    unsigned long long int a,
    unsigned long long int b,
)

cpdef least_common_multiple(
    unsigned long long int a,
    unsigned long long int b,
)

@cython.locals(new_num=cython.ulong)
cpdef unsigned int is_pentagonal(unsigned long long int n)

cpdef unsigned int is_triangular(unsigned long long int n)
