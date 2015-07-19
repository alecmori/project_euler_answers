#The pattern is very recursive - once you see it, it's pretty easy to implement.

"""
real	0m0.038s
user	0m0.022s
sys		0m0.012s
"""

SPIRALSIZE = 1001

#This function presumes size is odd
def calcSpiral(size):
	if size == 1:
		return 1
	total = calcSpiral(size - 2)
	#For each corner at current level
	for i in range(4):
		total += size**2 - i * (size - 1)
	return total

if __name__ == "__main__":
	print calcSpiral(SPIRALSIZE)