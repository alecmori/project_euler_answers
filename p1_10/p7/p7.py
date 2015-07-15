#Like all other prime problems, I am keeping a list of primes to check and also incrememnting
#by 2 instead of 1

"""
real	0m0.003s
user	0m0.001s
sys		0m0.002s
"""

PRIMES = [2]

def checkPrime(n):
	for prime in PRIMES:
		if prime * prime > n:
			break
		if n % prime == 0:
			return 
	PRIMES.append(n)

if __name__ == "__main__":
	possPrime = 3
	while len(PRIMES) != 10001:
		checkPrime(possPrime)
		possPrime += 2
	print PRIMES[-1]