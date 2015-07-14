#One cool little trick I implemented to generate Pythagorean triples is choosing two distinct
#odd integers, which can make pythagorean triples in constant time. Instead of a solution
#that loops through b and a (and thus makes a lot of bad triples), we can loop through
#variables that give us consistent pythagorean triples

"""
real	0m0.041s
user	0m0.025s
sys		0m0.012s
"""

SUM = 1000
JUMP = 2  # They need to be odd numbers

def generateABC(r, s):
	a = r * s
	b = (s * s - r * r)/2
	c = (s * s + r * r)/2
	return (a, b, c)

a = 0
b = 0
c = 0
s = 1
while a + b + c != SUM:
	s += JUMP
	for r in range(1, s, JUMP):
		a, b, c = generateABC(r, s)
		if a + b + c == SUM:
			break
print a * b * c
