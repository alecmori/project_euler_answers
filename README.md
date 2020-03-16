A repo containing my solutions to Project Euler questions. In due time I hope
to explain all of the math in each one of the solutions as well, but so far
I've done that for no problems.

I write all of the answers as valid `Python` code, then use a `.pxd` file to
compile it into `C` for speed. Because of some the `Cython` limitations, there
are many un-Pythonic choices in writing the Python, such as avoiding
comprehensions and generators.

| Problem Number | Python (s) | Cython (s) |
|----------------|------------|------------|
|              1 |  0.0001751 |  0.0004836 |
|              2 |  1.108e-05 |  9.116e-06 |
|              3 |    0.07117 |     0.7756 |
|              4 |    0.01439 |    0.01999 |
