#My initial guess was an O(n**3) algorithm, where for each number, you would subtract each 
#abundant number and check if it is in the array. However, because AbundantNumbers is sorted
#we can just increment or decrement the two numbers we're using until we converge upon
#the proper solution, making this overall runtime O(n**2). I can't think of a better runtime
#solution, but I've been wrong before/might be missing some magic property of the numbers.

#My code runs far slower than most other peoples - I will look further into why later.

"""
real	0m38.905s
user	0m36.070s
sys		0m0.486s
"""

MAX = 28124
ABUNDANTNUMS = list()

#Note we are not counting num as a factor of num in this problem
def findFactors(num):
	factors = set([1])
	i = 2
	while i * i <= num:
		if num % i == 0:
			factors.add(i)
			factors.add(num / i)
		i += 1
	return list(factors)

def findAbundantNumbers():
	for i in xrange(1, MAX):
		factors = findFactors(i)
		if sum(factors) > i:
			ABUNDANTNUMS.append(i)

def isSum(possSum):
	i = 0
	j = len(ABUNDANTNUMS) - 1
	while i <= j:
		if ABUNDANTNUMS[i] + ABUNDANTNUMS[j] == possSum:
			return True
		if ABUNDANTNUMS[i] + ABUNDANTNUMS[j] > possSum:
			j -= 1
		else:
			i += 1
	return False

if __name__ == "__main__":
	findAbundantNumbers()
	total = 0
	for possSum in xrange(MAX):
		if not isSum(possSum):
			total += possSum
	print total