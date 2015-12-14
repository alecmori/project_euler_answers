#Interesting problem! Theoretically it's relatively simple - find all the primes you need,
#then multiply them all together (for instance, you'll need 4 2's, because 2^4 = 16).

#There might be a more effective method using gcd, but that's a bit too clever for me to
#think of right now.

"""
real	0m0.051s
user	0m0.026s
sys		0m0.015s
"""

MAX_NUM = 20

#Checks if a given number is prime - could use memoization but not worth it on such a small
#problem.
def is_prime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

#Counts number of times a prime occurs in a number
def count_primes(prime, number):
	counter = 0
	while number % prime == 0:
		number = number / prime
		counter += 1
	return counter

#If a prime is a factor of num, add it to the dictionary for each time it is a factor
def add_to_dictionary(num, dictionary, prime):
	if num % prime == 0:
		#Number of time a prime occurs
		num_primes = count_primes(prime, num)
		num /= prime**num_primes
		dictionary[prime] = num_primes
	return num

def find_prime_factorization(num):
	prime_factorization = dict()

	#2 is a special case for primes, being the only even one
	poss_prime = 2
	num = add_to_dictionary(num, prime_factorization, poss_prime)

	poss_prime = 3
	while num != 1:
		if is_prime(poss_prime):
			num = add_to_dictionary(num, prime_factorization, poss_prime)

		#Increment primes by two to ensure it is odd
		poss_prime += 2
	return prime_factorization

#Takes all elements from a new dictionary and adds it to our cummulative dictionary
def merge_dictionaries(prime_factorization, curr_factors):
	for factor in curr_factors:
		if factor not in prime_factorization or prime_factorization[factor] < curr_factors[factor]:
			prime_factorization[factor] = curr_factors[factor]

if __name__ == "__main__":
	#Finds all prime factorizations of the numbers 1-20, then sees if there are more instances
	#of prime p in the current number than any before it. Keep track of the largest for
	#each prime.
	prime_factorization = dict()
	for num in xrange(1, MAX_NUM):
		curr_factors = find_prime_factorization(num)

		#Merges the overall tracking of prime numbers versus the current prime factors
		merge_dictionaries(prime_factorization, curr_factors)

	#Multiplies them all together
	total = 1
	for factor,occurances in prime_factorization.items():
		total *= factor**occurancess
print total