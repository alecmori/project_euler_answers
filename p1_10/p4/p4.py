#I could not think of a clever way to convert a number into a list
#other than directly casting to a string.

"""
real	0m1.355s
user	0m1.321s
sys		0m0.020s
"""

def isPalindrome(num):
	numString = str(num)
	for i in range(len(numString) / 2):
		if numString[i] != numString[-i - 1]:
			return False
	return True

largestPalin = -1
for firstNumber in range(100, 1000):
	for secondNumber in range(100, 1000):
		possPalin = firstNumber * secondNumber
		if isPalindrome(possPalin) and possPalin > largestPalin:
			largestPalin = possPalin
print largestPalin