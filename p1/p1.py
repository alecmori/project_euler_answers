#My goal was to do this all in one line

"""
real	0m0.046s
user	0m0.027s
sys		0m0.014s
"""

maxValue = 1000

print sum(x for x in range(maxValue) if x % 3 == 0 or x % 5 == 0)