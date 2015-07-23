#So, we know we have two primes p_1 and p_2, where p_1 >= 5 and p_2 > p_1 (they're consecutive)
#Let l be the length of p_1 (9876 has a length of 4). We need to find a number N such that

#N === p_1 mod 10^l
#N === 0 mod p_2

#Which would imply

#x * 10^l === -p_1 mod p_2
#This can be heavily reduced to 
#x * (10^l) - p_2 * y = (p_2 - p_1) 

#Using the Euclidean Algorithm, we can find an x, y such that the left hand side is 1.
#Then, we would multiply both sides by p_2 - p_1 to get our solution! (We would, of course),
#reduce x to the smallest positive value

"""
real	0m4.581s
user	0m4.108s
sys		0m0.086s
"""

UPPERBOUND = 1000000
PRIMES = list()

def isPrime(num):
	for prime in PRIMES:
		if prime * prime > num:
			return True
		if num % prime == 0:
			return False
	return True

def makePrimes():
	PRIMES.append(2)
	for possPrime in range(3, UPPERBOUND, 2):
		if isPrime(possPrime):
			PRIMES.append(possPrime)
	while True:
		if isPrime(possPrime):
			PRIMES.append(possPrime)
			break
		possPrime += 2

#Subtracts one 2-tuple from the other
def subtractTuples(tup1, tup2):
	return (tup1[0] - tup2[0], tup1[1] - tup2[1])

#Multiples one 2-tuple by a constant
def multiplyTuple(const, tup):
	return (tup[0] * const, tup[1] * const)

#Given two numbers, will find the x, y such that a*x + b*y = gcd(a,b)
#xyDict contains the coefficients such that, xyDict[key] = (x, y), 

#ORIGINAL_A * x + ORIGINAL_B * y = key
def findCoefficients(a, b, xyDict):
	#Should not occur
	if a < b:
		findCoefficients(b, a, xyDict)
	if len(xyDict) == 0:
		xyDict[a] = (1, 0)
		xyDict[b] = (0, 1)
	if b == 0:
		return xyDict[a]
	newA = b
	newB = a % b
	multiplier = a / b
	xyDict[newB] = subtractTuples(xyDict[a], multiplyTuple(multiplier, xyDict[b]))
	return findCoefficients(newA, newB, xyDict)

#Gets the x and y to solve the linear congruence
def getCoefficients(prime_1, prime_2, tenPower):
	if prime_2 < tenPower:
		x, y = findCoefficients(tenPower, prime_2, dict())
	else:
		y, x = findCoefficients(prime_2, tenPower, dict())
	x *= (prime_2 - prime_1)
	x = x % prime_2
	return x, y

#Finds the sum of all the smallest numbers that hold the quality we need
def calculateSum():
	total = 0
	for i in range(len(PRIMES) - 1):
		if PRIMES[i] < 5:
			continue
		prime_1 = PRIMES[i]
		prime_2 = PRIMES[i + 1]
		prime_1_length = len(str(prime_1))
		buff = 10**prime_1_length
		x, y = getCoefficients(prime_1, prime_2, buff)
		finalNum = x * buff + prime_1
		total += finalNum
	return total

if __name__ == "__main__":
	makePrimes()
	print calculateSum()
