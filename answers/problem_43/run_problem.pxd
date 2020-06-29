import cython

@cython.locals(
  total=cython.ulong, digits=list, divisors=list, permutation=tuple,
  all_divisble=cython.uint, x=cython.uint, y=cython.uint, z=cython.uint,
  i=cython.uint, divisor=cython.uint,
)
cpdef unsigned int run_problem()

@cython.locals(total=cython.ulong)
cpdef unsigned long convert_pandigital(tuple l)
