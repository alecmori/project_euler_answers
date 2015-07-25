#The fun way to do this problem, given a power, find the upper bound, and then brute force it

"""
real	0m4.731s
user	0m4.349s
sys		0m0.086s
"""

import math
PRIMEFACTORS = dict()
POWER = 5

def getLength(num):
	return len(str(num))

def findUpperBound(power):
	power9 = 9**power
	length = getLength(power9)
	return 9**(length + 1 + int(math.log(length, 10)))

def getSumOfDigits(num, power):
	digits = map(int, list(str(num)))
	return sum([x**power for x in digits])

if __name__ == "__main__":
	upperBound = findUpperBound(POWER)
	total = 0
	for num in range(10, upperBound + 1):
		if getSumOfDigits(num, POWER) == num:
			total += num
	print total