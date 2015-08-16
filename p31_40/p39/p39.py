#This problem was fairly simple - generate Pythagorean Triples using the generator from
#Problem 9, then for each triple (which is guaranteed to be in simplified form), 
#add all multiples of its sum <= MAX to a counting dictionary.

#The only slightly interesting thing is being sure we know when to stop, which will be when
#a + b + c == s**2 + r * s <= MAX. So, when our pair (r, s) is too large, we ought to stop.

"""
real	0m0.002s
user	0m0.000s
sys		0m0.001s
"""

COUNTS = dict()
MAX = 1000
JUMP = 2  # They need to be odd numbers

def generateABC(r, s):
	a = r * s
	b = (s * s - r * r)/2
	c = (s * s + r * r)/2
	return (a, b, c)

def fillCounts(a, b, c):
	total = a + b + c
	currVal = total
	while currVal <= MAX:
		if currVal not in COUNTS:
			COUNTS[currVal] = 0
		COUNTS[currVal] += 1
		currVal += total	

if __name__ == "__main__":
	a = 0
	b = 0
	c = 0
	s = 1
	while s * (s + 1) <= MAX:
		s += JUMP
		for r in range(1, s, JUMP):
			if s * (s + r) > MAX:
				break
			a, b, c = generateABC(r, s)
			fillCounts(a, b, c)
	perimeterCounts = COUNTS.items()
	perimeterCounts.sort(key = lambda keyValues: keyValues[1])
	print perimeterCounts[-1][0]