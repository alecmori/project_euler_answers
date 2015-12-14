#I was going to write out a full prime factorization, but it seemed to be
#overkill - you can just keep track of the largest prime that has yet to be removed

"""
real	0m0.020s
user	0m0.001s
sys		0m0.006s
"""

INITIAL_NUMBER = 600851475143

#Typical function to check whether n is prime or not
def is_prime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

#Removes all instances of a prime from a numbers factors 
def remove_primes(prime, number):
	while number % prime == 0:
		number = number / prime
	return number

if __name__ == "__main__":
	#Because all primes are odd besides 2, it's best to treat 2 as a special case
	#And instead increment by 2.	
	curr_number = INITIAL_NUMBER
	poss_prime = 2
	biggest_prime = -1

	if curr_number % poss_prime == 0:
		curr_number = remove_primes(poss_prime, curr_number)
		biggest_prime = poss_prime


	poss_prime = 3
	while curr_number != 1:
		#If prime is in curr_number, we've found a new largest prime factor!
		if is_prime(poss_prime) and curr_number % poss_prime == 0:
			curr_number = remove_primes(poss_prime, curr_number)
			biggest_prime = poss_prime
		poss_prime += 2
	print biggest_prime