import cython

@cython.locals(
    total_powers=cython.uint, all_powers=dict, current_power=cython.uint,
)
cpdef unsigned int run_problem(unsigned int n=*)
@cython.locals(
    power=cython.uint, curr_power=cython.uint, d=dict, i=cython.uint,
)
cpdef dict generate_perfect_powers(unsigned int upper_bound=*)
@cython.locals(
    s=set, denom=cython.uint, ratio_factor=cython.ulong,
    num_terms_with_power=cython.uint,
)
cpdef int count_terms_to_remove(
    unsigned int upper_bound=*, unsigned int current_power=*,
)
