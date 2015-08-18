#The hard part of this was knowing how to speed it up. Thankfully, they give us in the spec
#that there exists an answer that starts with 9 - thus, there is no point at looking at 
#any number NOT starting with 9.

#Additionally, because we need at least two number, we can have at most 4 digits (2 5 digit
#numbers == 10 digits, one too many).

"""
real	0m0.056s
user	0m0.043s
sys		0m0.010s
"""

OFFSET = 9
UPPERBOUND = 10000
NUMDIGITS = 9

def isPandigital(possPan):
	if len(str(possPan)) != NUMDIGITS:
		return False
	digits = set()
	while possPan != 0:
		digits.add(possPan % 10)
		possPan /= 10

	#Must be digits 1-9
	if 0 in digits:
		return False
	if len(digits) != NUMDIGITS:
		return False
	return True

def generateNumber(start):
	newNum = ""
	multiplier = 1
	while len(newNum) < OFFSET:
		newNum += str(start * multiplier)
		multiplier += 1
	return int(newNum)

def findLargestPandigital():
	currLargest = 0
	powerOfTen = 1
	while powerOfTen <= UPPERBOUND:

		#We only care about numbers that start with 9
		for start in range(OFFSET * powerOfTen, OFFSET * powerOfTen + powerOfTen):
			possPan = generateNumber(start)
			if isPandigital(possPan):
				if possPan > currLargest:
					currLargest = possPan
		powerOfTen *= 10
	return currLargest

if __name__ == "__main__":
	largest = findLargestPandigital()
	print largest