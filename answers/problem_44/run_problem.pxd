import cython

@cython.locals(new_num=cython.ulong)
cpdef unsigned int is_pentagonal(unsigned long n)

cpdef unsigned long get_pentagonal(unsigned long n)

@cython.locals(
  seen_pentagonal_numbers=set, curr_pentagonal_index=cython.uint,
  curr_pentagonal_number=cython.ulong, difference=cython.ulong,
  summed=cython.ulong)
cpdef unsigned long run_problem()
