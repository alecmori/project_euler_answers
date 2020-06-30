import cython

@cython.locals(new_num=cython.ulong)
cpdef unsigned int is_pentagonal(unsigned long n)

cpdef unsigned long get_pentagonal(unsigned long n)

# TODO: Read
# https://projecteuler.net/quote_post=353019-a04847b123c46f1b3a3cd9064df92c0bddacb588
@cython.locals(
  seen_pentagonal_numbers=set, curr_pentagonal_index=cython.uint,
  curr_pentagonal_number=cython.ulong, difference=cython.ulong,
  summed=cython.ulong)
cpdef unsigned long run_problem()
