import cython

@cython.locals(total=cython.uint, num=cython.uint, s_num=str, b_num=str)
cpdef unsigned int run_problem(unsigned int n=*)

@cython.locals(rev=cython.uint, orig_num=cython.uint)
cpdef cython.bint _is_palindrome(unsigned int num)

@cython.locals(rev=cython.uint, orig_num=cython.uint)
cpdef cython.bint _is_bin_palindrome(unsigned int num)
