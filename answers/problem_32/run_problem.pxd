import cython

@cython.locals(
    N=cython.uint, pandigital_products=set, first_num=cython.uint,
    first_num_str=str, first_num_digits=set, second_num=cython.uint,
    second_num_str=str, second_num_digits=set, product=cython.uint,
    product_str=str, digit_count=cython.uint, product_digits=set,
    all_digits=set,
)
cpdef unsigned int run_problem()

@cython.locals(digits=set)
cpdef set digit_char_set(num=*)
