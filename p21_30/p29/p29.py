#I was gonna check prime factorization and see if the powers had a gcd > 1, but it seems
#foolish not to take advantage of sets.

"""
real	0m0.144s
user	0m0.051s
sys		0m0.033s
"""

UPPERBOUND = 100
POWERS = set()

if __name__ == "__main__":
	for a in xrange(2, UPPERBOUND + 1):
		for b in xrange(2, UPPERBOUND + 1):
			POWERS.add(a**b)
	print len(POWERS)