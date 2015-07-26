#There might be a better way to do this (for instance, ONLY add to those that are in the
#truncatable arrays already). However, this is fairly efficient.

"""
real	0m2.806s
user	0m2.626s
sys		0m0.054s
"""

LEFTTRUNCATABLES = list() #Removing from the left
RIGHTTRUNCATABLES = list()
PRIMES = list()

def isPrime(num):
	for prime in PRIMES:
		if prime * prime > num:
			break
		if num % prime == 0:
			return False
	PRIMES.append(num)
	return True

def addToTruncatables(num):
	if len(num) == 1:
		LEFTTRUNCATABLES.append(num)
		RIGHTTRUNCATABLES.append(num)
		return 0 #Don't count these numbers
	else:
		if num[1:] in LEFTTRUNCATABLES:
			LEFTTRUNCATABLES.append(num)
		if num[:-1] in RIGHTTRUNCATABLES:
			RIGHTTRUNCATABLES.append(num)
	if num in LEFTTRUNCATABLES and num in RIGHTTRUNCATABLES:
		return 1
	return 0

def fillTruncatables():
	count = 0
	num = 2 #Starts at 2 as one is not prime
	while count != 11:
		if isPrime(num):
			num = str(num)
			count += addToTruncatables(num)
			num = int(num)
		if num == 2:
			num += 1
		else:
			num += 2


if __name__ == "__main__":
	fillTruncatables()
	total = 0
	for num in LEFTTRUNCATABLES:
		if num in RIGHTTRUNCATABLES:
			total += int(num)
	print total
