#I really am at a loss on how to do these digit sum problems efficiently. It seems like such
#a waste of time to have to do all this computation.

"""
real	0m0.036s
user	0m0.020s
sys		0m0.011s
"""

import math

NUM = 100

if __name__ == "__main__":
	print sum(int(digit) for digit in str(math.factorial(NUM)))