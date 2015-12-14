#My goal was to do this all in one line to remind myself how list 
#comprehension works in python

"""
real	0m0.046s
user	0m0.027s
sys		0m0.014s
"""

MAX_VALUE = 1000

if __name__ == "__main__":
	print sum(x for x in range(MAX_VALUE) if x % 3 == 0 or x % 5 == 0)