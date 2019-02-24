import cython
from utils.proj_eul_math cimport lexical

@cython.locals(max_product=cython.ulong)
cpdef unsigned long int run_problem(unsigned int num_digits=*, str giant_num_str=*)
