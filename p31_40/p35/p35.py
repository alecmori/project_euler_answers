#Doing this efficiently was slighty more difficult than I imagined, but it wasn't too bad
#You have to make all the primes beforehand (kind of obvious), then filter out the primes
#with ANY even digits or ANY fives (increment by two at the end to includ 2 and 5)

"""
real	0m3.100s
user	0m2.977s
sys		0m0.050s
"""

UPPERBOUND = 1000000
PRIMES = list()

def onlyOddDigits(prime):
	if prime == 0:
		return True
	if prime % 2 == 0:
		return False
	return onlyOddDigits(prime / 10)


def hasNoFives(prime):
	if prime == 0:
		return True
	if prime % 10 == 5:
		return False
	return onlyOddDigits(prime / 10)

def isPrime(num):
	for prime in PRIMES:
		if num % prime == 0:
			return False
		if prime * prime > num:
			break
	return True

def makePrimes():
	for possPrime in range(2, UPPERBOUND):
		if isPrime(possPrime):
			PRIMES.append(possPrime)

def filterPrimes():
	newPrimes = list()
	for prime in PRIMES:
		if onlyOddDigits(prime) and hasNoFives(prime):
			newPrimes.append(prime)
	return newPrimes

def rotateNum(num):
	return num[-1] + num[:-1]

def isRotatable(num):
	template = str(num)
	for i in xrange(len(template)):
		if int(template) not in PRIMES:
			return False
		template = rotateNum(template)
	return int(template)

def rotatedPrimesSum():
	total = 2 #2 would not be in primes, nor would 5
	for prime in PRIMES:
		if isRotatable(prime):
			total += 1
	return total

if __name__ == "__main__":
	makePrimes()
	PRIMES = filterPrimes()
	total = rotatedPrimesSum()
	print total
