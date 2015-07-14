#After trying list comprehension and doing it by hand, I really can't see any difference
#I prefer list comprehension because I think it's easier to read

"""
real	0m0.033s
user	0m0.018s
sys		0m0.011s
"""

NUM = 100

def calcSquareOfSums(nums):
	nums = [x**2 for x in nums]
	return sum(nums)

def calcSumOfSquares(nums):
	return sum(nums)**2

nums = range(NUM + 1) # NUM is inclusive
print calcSumOfSquares(nums) - calcSquareOfSums(nums)