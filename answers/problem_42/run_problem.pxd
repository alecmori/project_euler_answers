import cython

@cython.locals(total=cython.uint, c=str)
cpdef unsigned int _score_word(str word)

@cython.locals(num_triangle=cython.uint, word=str, score=cython.uint)
cpdef unsigned int run_problem()
