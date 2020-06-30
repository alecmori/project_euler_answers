A repo containing my solutions to Project Euler questions. In due time I hope
to explain all of the math in each one of the solutions as well, but so far
I've done that for no problems.

I write all of the answers as valid `Python` code, then use a `.pxd` file to
compile it into `C` for speed. Because of some the `Cython` limitations, there
are many un-Pythonic choices in writing the Python, such as avoiding
comprehensions and generators.

# Setup

```
$ make cython
$ export PYTHONPATH=`pwd`
$ python utils/run_all_problems.py
```

If you want to run a subset of the problems, use the `min` and `max` flags in
the `run_all_problems` module.

```
$ python utils/run_all_problems.py --min 5 --max 10
```

If you want to run a single problem with the test case provided by Project
Euler, run the module directly.

```
$ python answers/problem_$NUMBER/run_problem.py
```

# Time Comparison

| Problem Number | Python (s) | Cython (s) |
|----------------|------------|------------|
|              1 |  0.0004523 |   0.000187 |
|              2 |  9.269e-06 |  7.647e-06 |
|              3 |     0.9044 |     0.0783 |
|              4 |    0.02095 |    0.01699 |
|              5 |  1.758e-05 |  7.046e-06 |
|              6 |  5.243e-05 |  4.544e-05 |
|              7 |      1.018 |    0.07193 |
|              8 |    0.00426 |   0.001253 |
|              9 |  8.743e-06 |  1.651e-05 |
|             10 |      2.111 |     0.2221 |
|             11 |    0.01192 |   0.001769 |
|             12 |     0.8725 |    0.08501 |
|             13 |  0.0003897 |  4.358e-05 |
|             14 |      1.094 |     0.4166 |
|             15 |  1.364e-05 |  6.279e-06 |
|             16 |  0.0001364 |  6.163e-05 |
|             17 |   0.002517 |  0.0003155 |
|             18 |  0.0001272 |   5.21e-05 |
|             19 |   0.001544 |   0.001695 |
|             20 |  7.196e-05 |  3.773e-05 |
|             21 |    0.06934 |    0.01571 |
|             22 |      0.644 |       0.67 |
|             23 |       11.7 |        3.3 |
|             24 |  4.196e-05 |  1.323e-05 |
|             25 |   0.004075 |   0.002329 |
|             26 |    0.01993 |   0.001682 |
|             27 |     0.8463 |    0.04977 |
|             28 |  3.539e-06 |  1.424e-06 |
|             29 |  0.0007964 |  0.0003293 |
|             30 |      1.996 |    0.03163 |
|             31 |      2.728 |    0.09936 |
|             32 |      0.203 |    0.06691 |
|             33 |      0.012 |   0.006374 |
|             34 |      4.227 |     0.8411 |
|             35 |      2.235 |     0.1303 |
|             36 |      1.329 |   0.007921 |
|             37 |      0.294 |     0.1345 |
|             38 |     0.2589 |    0.01917 |
|             39 |   0.000232 |  0.0001363 |
|             40 |  1.366e-05 |  4.487e-06 |
|             41 |      8.388 |     0.7984 |
|             42 |     0.4968 |      0.502 |
|             43 |      1.827 |     0.3247 |
|             44 |     0.2144 |     0.2307 |
|             45 |         -1 |         -1 |
|             46 |         -1 |         -1 |
|             47 |         -1 |         -1 |
|             48 |   0.003255 |   0.002057 |
|             49 |         -1 |         -1 |
|             50 |         -1 |         -1 |
|             51 |         -1 |         -1 |
|             52 |         -1 |         -1 |
|             53 |         -1 |         -1 |
|             54 |         -1 |         -1 |
|             55 |         -1 |         -1 |
|             56 |         -1 |         -1 |
|             57 |         -1 |         -1 |
|             58 |         -1 |         -1 |
|             59 |         -1 |         -1 |
|             60 |         -1 |         -1 |
|             61 |         -1 |         -1 |
|             62 |         -1 |         -1 |
|             63 |         -1 |         -1 |
|             64 |         -1 |         -1 |
|             65 |         -1 |         -1 |
|             66 |         -1 |         -1 |
|             67 |     0.5579 |     0.5363 |
|            201 |      254.8 |      86.36 |
