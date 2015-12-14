#Like most of the prime problems, this one is easiest to keep two as a special case, then 
#find the rest and manipulate them as you will.

#However, because n is getting relatively large here, it is a lot quicker to keep a list
#of primes and only check those rather than all numbers.

"""
real	0m6.696s
user	0m6.528s
sys		0m0.073s
"""

START_PRIME = 3 #We count 2 already, so we start at 3
UPPER_BOUND = 2000000 
JUMP = 2 #We offset by two each time, so we only check odds
PRIMES = [2]

def check_prime(n):
	for prime in PRIMES:
		if prime * prime > n:
			break
		if n % prime == 0:
			return False
	PRIMES.append(n)
	return True

if __name__ == "__main__":
	for poss_prime in xrange(START_PRIME, UPPER_BOUND, JUMP):
		check_prime(poss_prime)

	print sum(PRIMES)