#Let's start with limiting the size of our product. We know there are 9 total digits between
#the product and its factors

#1dig * 2 dig < 6 digits, so our product must be less that six digits
#n * (6 - n) > 3 digits , so our product is at least four digits

#So, IMO it's simple to check if there are no duplicates or 0 in that number, than checking
#all possible factors to see if one comes up!

"""
real	0m1.455s
user	0m1.406s
sys		0m0.024s
"""

MAX = 100000
MIN = 1234 #First viable number
TEST = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

def getDigits(num):
	if num == 0:
		return []
	digits = getDigits(num / 10)
	digits.append(num % 10)
	return digits

def hasPandigitalProduct(num):
	i = 2
	digits = getDigits(num)

	#If there are duplicates
	if len(digits) != len(set(digits)):
		return False 

	#Can't have 0 either
	if 0 in digits:
		return False

	#Can do strictly less than, because a sqrt would imply the same number and digits twice
	while i * i < num:
		if num % i == 0:
			allDigits = digits + getDigits(i) + getDigits(num / i)
			if set(allDigits) == TEST and len(allDigits) == len(TEST):
				return True
		i += 1
	return False

if __name__ == "__main__":
	total = 0
	for possNum in range(MIN, MAX):
		if hasPandigitalProduct(possNum):
			total += possNum
	print total