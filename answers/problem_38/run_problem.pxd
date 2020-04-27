import cython

@cython.locals(
    largest_pandigital_number=cython.ulong, maybe_pandigital=cython.ulong,
    num=cython.uint,
)
cpdef unsigned int run_problem(unsigned int n=*)

@cython.locals(digits=list)
cpdef list _get_non_zero_digits(unsigned int n)

@cython.locals(
    pandigital_components=list, digits=set, multiplier=cython.ushort,
    curr_num=cython.uint)
cpdef unsigned int _get_pandigital_if_exists(unsigned int n)
