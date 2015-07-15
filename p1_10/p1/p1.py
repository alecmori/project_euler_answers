#My goal was to do this all in one line

MAXVALUE = 1000
"""
real	0m0.046s
user	0m0.027s
sys		0m0.014s
"""

if __name__ == "__main__":

	print sum(x for x in range(MAXVALUE) if x % 3 == 0 or x % 5 == 0)