import cython

@cython.locals(
    max_integer=cython.uint, best_chain_len=cython.uint,
    curr_chain_len=cython.uint,
)
cpdef unsigned int run_problem(unsigned int max_value=*)
