import cython

@cython.locals(
    cache=list, total_sum=cython.uint, current_sum=cython.uint,
)
cpdef unsigned long run_problem(set S=*, unsigned int k=*)
@cython.locals(
    num_elements_used=cython.uint, current_sum=cython.ulong, 
    new_sum=cython.ulong,
)
cpdef update_cache_for_element(unsigned int element=*, list cache=*)
