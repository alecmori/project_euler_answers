#I don't know any mathematical way to do this other than brute force, with some clever 
#heuristics for reducting the guesses.

#For example, b has to be prime and positive. If not, n = 0 would not work

#Additionally, n^2 + an + b = n(n + a) + b. That means n(n + a) + b has to be prime, and thus
#odd. That means for most cases of b (except when b == 2, which I won't even count because
#I already know there exists a better solution), n(n + a) must be even. When n is even, no
#problem. However, half the time n will be odd, which implies a must also be odd.

#Let's take a to be some negative number. Thus, for all when n == |a|/2, the function is 
#at a minimum. If, at that minimum, we are negative still, we should not count this set.

"""
real	0m2.458s
user	0m2.378s
sys		0m0.028s
"""

PRIMES = []

UPPERBOUND = 1000
PRIMEBOUND = UPPERBOUND
PRIMES = list()

def isPrime(num):
	for prime in PRIMES:
		if prime * prime > num:
			return True
		if num % prime == 0:
			return False
	PRIMEBOUND += 1000
	makePrimes(PRIMEBOUND)
	return isPrime(num)

def makePrimes(bound):
	if PRIMEBOUND == UPPERBOUND:
		PRIMES.append(2)
	for possPrime in range(PRIMEBOUND - UPPERBOUND + 1, PRIMEBOUND, 2):
		if possPrime == 1:
			continue
		if isPrime(possPrime) and possPrime not in PRIMES:
			PRIMES.append(possPrime)

def quadFunc(n, a, b):
	return n * (a + n) + b

def getNSequence(a, b):
	global PRIMEBOUND
	n = 0
	value = quadFunc(n, a, b)
	while value in PRIMES:
		n += 1
		value = quadFunc(n, a, b)
		while value > PRIMES[-1]:
			PRIMEBOUND += UPPERBOUND
			makePrimes(PRIMEBOUND)
	return n - 1


if __name__ == "__main__":
	makePrimes(PRIMEBOUND)
	longestN = -1
	product = 0
	for a in range(-abs(UPPERBOUND), UPPERBOUND):
		#Only condition to skip a
		if a % 2 == 0:
			continue
		for b in PRIMES:
			#Loads of conditions to skip b's
			if quadFunc(abs(a)/2, a, b) < 0:
				continue
			if b == 2:
				continue
			if b > UPPERBOUND:
				break
			n = getNSequence(a, b)
			if n > longestN:
				product = a * b
				longestN = n
	print product