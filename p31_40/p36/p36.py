#There's some filtering we could do - for instance, if it ends in 0, we know it won't be
#a palindrome, but the palindrome function

"""
real	0m0.871s
user	0m0.838s
sys		0m0.025s
"""

import math

UPPERBOUND = 1000000

#Finds the largest power of 2 < num
def findLeadingPower(num):
	return 2**int(math.log(num, 2))

#Converts the number to binary
def convertToBinary(num):
	currPowerOfTwo = findLeadingPower(num)
	binaryNum = ""
	while currPowerOfTwo != 0:
		if currPowerOfTwo <= num:
			num -= currPowerOfTwo
			binaryNum += "1"
		else:
			binaryNum += "0"
		currPowerOfTwo /= 2
	return binaryNum

#Checks if any given number is a palindrome
def isPalindrome(num):
	if len(num) == 0 or len(num) == 1:
		return True
	if num[0] != num[-1]:
		return False
	return isPalindrome(num[1:-1])

if __name__ == "__main__":
	total = 0
	for possNum in range(1, UPPERBOUND):
		if isPalindrome(str(possNum)):
			binPossNum = convertToBinary(possNum)
			if isPalindrome(binPossNum):
				total += possNum
	print total