#Interesting problem! Theoretically it's relatively simple - find all the primes you need,
#then multiply them all together (for instance, you'll need 4 2's, because 2^4 = 16).

#There might be a more effective method using gcd, but that's a bit to clever for me to
#think of right now.

"""
real	0m0.051s
user	0m0.026s
sys		0m0.015s
"""

MAXNUM = 20

def isPrime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

#Counts number of times a prime occurs in a number
def countPrimes(prime, number):
	counter = 0
	while number % prime == 0:
		number = number / prime
		counter += 1
	return counter

#If a prime is a factor of num, add it to the dictionary for each time it is a factor
def addToDictionary(num, dictionary, prime):
	if num % prime == 0:
		#Number of time a prime occurs
		numPrime = countPrimes(prime, num)
		num /= prime**numPrime
		dictionary[prime] = numPrime
	return num

def findPrimeFactorization(num):
	primeFactorization = dict()

	#2 is a special case for primes, being the only even one
	possPrime = 2
	num = addToDictionary(num, primeFactorization, possPrime)

	possPrime = 3
	while num != 1:
		if isPrime(possPrime):
			num = addToDictionary(num, primeFactorization, possPrime)
		possPrime += 1
	return primeFactorization

def mergeDictionaries(primeFactorization, currFactors):
	for factor in currFactors:
		if factor not in primeFactorization or primeFactorization[factor] < currFactors[factor]:
			primeFactorization[factor] = currFactors[factor]

if __name__ == "__main__":
	#Finds all prime factorizations of the numbers 1-20, then sees if there are more instances
	#of prime p in the current number than any before it. Keep track of the largest for
	#each prime.
	primeFactorization = dict()
	for num in range(1, MAXNUM):
		currFactors = findPrimeFactorization(num)

		#Merges the overall tracking of prime numbers versus the current prime factors
		mergeDictionaries(primeFactorization, currFactors)

	#Multiplies them all together
	total = 1
	for factor,occurs in primeFactorization.items():
		total *= factor**occurs
print total