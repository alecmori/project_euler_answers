#I was going to write out a full prime factorization, but it seemed to be
#overkill - you can just keep track of the largest

"""
real	0m0.020s
user	0m0.001s
sys		0m0.006s
"""

INITIALNUMBER = 600851475143

def isPrime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def removePrimes(prime, number):
	while number % prime == 0:
		number = number / prime
	return number

currNumber = INITIALNUMBER

#Because all primes are odd besides 2, it's best to treat 2 as a special case
#And instead increment by 2.	
possPrime = 2
biggestPrime = -1
if currNumber % possPrime == 0:
	currNumber = removePrimes(possPrime, currNumber)
	biggestPrime = possPrime


possPrime = 3
while currNumber != 1:
	#If prime is in currNumber, new largest prime factor!
	if isPrime(possPrime) and currNumber % possPrime == 0:
		currNumber = removePrimes(possPrime, currNumber)
		biggestPrime = possPrime
	possPrime += 2
print biggestPrime