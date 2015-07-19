#The last fibonacci problem I did algebraicly, using the fibonacci formula - this time,
#I'll do it programmatically.

"""
real	0m0.149s
user	0m0.072s
sys		0m0.027s
"""

NUMDIGITS = 1000

def countDigits(num):
	return len(str(num))

if __name__ == "__main__":
	fibn = 1
	fibn2 = 1

	currIndex = 2
	while countDigits(fibn2) != NUMDIGITS:
		#Changes both Fibonacci numbers in place (fibn2 becomes fibn3, and fibn becomes fibn2)
		fibn2 += fibn
		fibn = fibn2 - fibn
		currIndex += 1
	print currIndex