cpdef unsigned int run_problem(unsigned int max_value=*)
cdef unsigned int _get_tens_and_one_count(unsigned int number)
cdef unsigned int _get_hundreds_count(
    unsigned int number,
    unsigned int tens_and_one_count,
)
cdef unsigned int _get_thousand_count(unsigned int number)
