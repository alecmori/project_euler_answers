import cython

@cython.locals(total=cython.uint, num=cython.uint, s_num=str, b_num=str)
cpdef unsigned int run_problem(unsigned int n=*)

@cython.locals(start=cython.uint, end=cython.uint, string=str)
cpdef cython.bint _is_palindrome(
    str string, unsigned int start=*, unsigned int end=*,
)
