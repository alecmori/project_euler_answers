import cython

@cython.locals(names_list=list, total=cython.ulonglong)
cpdef unsigned long long int run_problem(str names_file=*)
@cython.locals(total=cython.ulonglong)
cdef unsigned long int _get_name_value(str name=*)
