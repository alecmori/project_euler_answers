#Admittedly, my heuristic for upper bound might be a bit too lazy : there's DEFINITELY
#a smarter one out there. Other than that it's a pretty straightforward problem.

"""
real	0m6.219s
user	0m5.951s
sys		0m0.077s
"""

FACTORIALS = list()

#To be called once, to calculate the factorials for the digits 0-9
def fillFactorials():
	FACTORIALS = list()
	FACTORIALS.append(1) #For zero

	for i in range(1,10): #For digits 1-9
		FACTORIALS.append(FACTORIALS[-1] * i)
	return FACTORIALS

#Calculates the largest number that could POSSIBLY be the sum of all of its digits' factorials
def findUpperBound():
	UPPERBOUNDPOWER = 1
	while 9*10**(UPPERBOUNDPOWER - 1) <= UPPERBOUNDPOWER * FACTORIALS[-1]:
		UPPERBOUNDPOWER += 1
	return 9 * 10**(UPPERBOUNDPOWER - 2)

#Adds up the factorials of all the digits
def factorialSum(num):
	digits = list(str(num))
	total = 0
	for digit in digits:
		total += FACTORIALS[int(digit)]
	return total

if __name__ == "__main__":
	FACTORIALS = fillFactorials()
	UPPERBOUND = findUpperBound()
	total = 0
	for possNum in range(10, UPPERBOUND):
		if possNum == factorialSum(possNum):
			total += possNum
	print total