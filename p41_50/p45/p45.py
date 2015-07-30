#Man I am loving this Babylonian method for finding squares.

#It is easy to generate any individual pentagonal, hexagonal, or triangular number, so once
#we have that, how do we go about verifying if is one of the other two? The quadratic formula
#of course!
#Triangular number == (n^2 + n)/2 = x, or n^2 + n - 2*x = 0. 
#n = (-1 +- sqrt(1 + 8x))/2
#It is critical that n is an integer, which implies 1 + 8x must be odd and a square.
#Similarly for Pentagonal numbers (3*n^2 - n)/2, we get
#n = (1 +- sqrt(1 + 24x))/6
#with the same constraints for the determinent (odd and square).

#ACTUALLY
#Though that method is mathematically sound, sqrt is an expensive function on a computer
#It's a lot easier to just generate them all, and, since hexagonal is guaranteed to grow
#the quickest and triangle the slowest (such that, for all values of n > 1, 
#TriNum(n) < PentNum(n) < HexNum(n))

#So, if it were space constrained, I'd use the first method. Because it's not, I'll use the 
#second. (the code for the first is one the bottom.)

"""
real	0m0.165s
user	0m0.143s
sys		0m0.018s
"""

TRIANGLENUMS = set()
PENTAGONALNUMS = set()
HEXAGONALNUMS = set()
STARTNUM = 286

def findTriangularNumber(n):
	return (n * n + n)/2

def findPentagonalNumber(n):
	return (3 * n * n - n)/2

def findHexagonalNumber(n):
	return 2 * n * n - n

if __name__ == "__main__":
	for n in range(STARTNUM):
		TRIANGLENUMS.add(findTriangularNumber(n))
		PENTAGONALNUMS.add(findPentagonalNumber(n))
		HEXAGONALNUMS.add(findHexagonalNumber(n))
	n = STARTNUM
	triNum = findTriangularNumber(n)
	while triNum not in PENTAGONALNUMS or triNum not in HEXAGONALNUMS:
		TRIANGLENUMS.add(triNum)
		PENTAGONALNUMS.add(findPentagonalNumber(n))
		HEXAGONALNUMS.add(findHexagonalNumber(n))
		n += 1
		triNum = findTriangularNumber(n)
	print triNum



"""
ISSQUARE = set()
ISNOTSQUARE = set()
STARTNUM = 144

def findHexagonalNumber(n):
	return 2 * n * n - n

#Based off Babylonian algorithm (safe for integers)
def isSquare(value):
	if value == 0 or value == 1:
		return True
	if value in ISNOTSQUARE:
		return False
	if value in ISSQUARE:
		return True
	x = value / 2
	seenValues = set([x])
	while x * x != value:
		x = (x + value / x) / 2
		if x in seenValues:
			ISNOTSQUARE.add(value)
			return False
		seenValues.add(x)
	ISSQUARE.add(value)
	return True

def isTriangularNum(num):
	if num % 2 == 0:
		return False
	return isSquare(num * 8 + 1)

def isPentagonalNum(num):
	if isSquare(num * 24 + 1):
		return (1 + int(math.sqrt(num * 24 + 1))) % 6 == 0
	return False

if __name__ == "__main__":
	hexGenerator = STARTNUM
	hexNum = findHexagonalNumber(hexGenerator)
	while not isTriangularNum(hexNum) or not isPentagonalNum(hexNum):
		hexGenerator += 1
		hexNum = findHexagonalNumber(hexGenerator)
	print hexNum
"""