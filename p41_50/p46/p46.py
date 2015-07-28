#This is a cool problem! The easiest way I found to do it was check all primes under that
#number (besides 2) and then check if the other part of the number is 2 times a square using
#the babylonian method (keeping track for repeats).

"""
real	0m0.108s
user	0m0.086s
sys		0m0.013s
"""

PRIMES = [2, 3, 5, 7]
ISSQUARE = set()
ISNOTSQUARE = set()

#Determines if a number is prime or not
def isPrime(num):
	for prime in PRIMES:
		if prime * prime > num:
			break
		if num % prime == 0:
			return False
	PRIMES.append(num)
	return True

#Based off Babylonian algorithm
def isSquare(value):
	if value in ISNOTSQUARE:
		return False
	if value in ISSQUARE:
		return True
	x = value / 2
	seenValues = set([x])
	while x * x != value:
		if x == 0:
			ISSQUARE.add(value)
			return True
		x = (x + value / x) / 2
		if x in seenValues:
			ISNOTSQUARE.add(value)
			return False
		seenValues.add(x)
	ISSQUARE.add(value)
	return True

#Given an odd and composite number, will check if it follows the criteria in Goldbach's 
#disproved conjecture
def followsConjecture(num):
	for prime in PRIMES:
		if prime == 2:
			continue
		if isSquare((num - prime)/2):
			return True
	return False

if __name__ == "__main__":
	currNum = 9
	while True:
		if not isPrime(currNum):
			if not followsConjecture(currNum):
				break
		currNum += 2
	print currNum