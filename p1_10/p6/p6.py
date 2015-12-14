#After trying list comprehension and doing it iteratively, I really can't see any difference
#I prefer list comprehension because I think it's easier to read

#However, if the number was huge (Like..... 10000000000000) we would have to be smarter about
#just randomly making lists
"""
real	0m0.033s
user	0m0.018s
sys		0m0.011s
"""

NUM = 100

def calc_sum_of_squares(nums):
	return sum([x**2 for x in nums])

def calc_square_of_sum(nums):
	return sum(nums)**2

if __name__ == "__main__":
	nums = range(NUM + 1) # NUM is inclusive
	print calc_square_of_sum(nums) - calc_sum_of_squares(nums)