#Because I did not want to primeFactor and then find all permutations of that factorization
#(that runtime gave me a heart attack), I decided to try a naive approach, which is get
#a triangle number, find its factors, count its factors, and see if it was over 500

#That worked okay (12 seconds), but I wanted an improvement. Memoization time!

#Down to about 6 seconds. Not bad, but I think we can do better.

#Now I'm thinking that we know the factorization of any triangle number (n * (n + 1))/2,
#Which means it's a lot easier computationally to look at n and n + 1 rather than their 
#product.

#Things I still want to do: Memoize prime factorizations, only use dictionaries

import math

"""
real	0m3.643s
user	0m3.566s
sys		0m0.032s
"""

ISPRIME = dict()
NUMDIVISORS = 500

def isPrime(n):
	if n in ISPRIME:
		return ISPRIME[n]
	i = 2
	while i * i <= n:
		if n % i == 0:
			ISPRIME[n] = False
			return False
		i += 1
	ISPRIME[n] = True	
	return True


def findPrimeFactorization(num):
	primeFactorization = []

	#2 is a special case for primes, being the only even one
	possPrime = 2
	while num % possPrime == 0:
		primeFactorization.append(possPrime)
		num /= possPrime

	possPrime = 3
	while num != 1:
		if isPrime(possPrime):
			while num % possPrime == 0:
				primeFactorization.append(possPrime)
				num /= possPrime
		possPrime += 2
	return primeFactorization

def countAllFactors(primeFactors):
	if primeFactors[2] == 1:
		primeFactors = {x : primeFactors[x] for x in primeFactors if x != 2}
	else:
		primeFactors[2] -= 1
	numOfEachPrimeFactor = primeFactors.values()
	product = 1
	for factorCount in numOfEachPrimeFactor:
		product *= (factorCount + 1)
	return product

def combineDict(d1, d2):
	d1 = {x : d1.count(x) for x in set(d1)}
	d2 = {x : d2.count(x) for x in set(d2)}
	for key in d2:
		if key in d1:
			d1[key] += d2[key]
		else:
			d1[key] = d2[key]
	return d1

def findTriangleNum(n):
	return (n * (n + 1))/2

if __name__ == "__main__":
	nTriangleNum = 1
	primeFactors = findPrimeFactorization(nTriangleNum)
	primeFactors2 = findPrimeFactorization(nTriangleNum + 1)
	d = combineDict(primeFactors, primeFactors2)
	while countAllFactors(d) <= NUMDIVISORS:
		nTriangleNum += 1
		primeFactors = primeFactors2
		primeFactors2 = findPrimeFactorization(nTriangleNum + 1)
		d = combineDict(primeFactors, primeFactors2)

	print findTriangleNum(nTriangleNum)