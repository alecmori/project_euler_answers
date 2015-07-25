#This is more of a lexical question than a mathematic one, and it's a really small range
#I do a bit of filtering to remove "trivial" answers but that's it. Not too hard all and 
#all - I use a fraction class to make finding the reduced form denominator easier (i.e. 
#without factoring)

"""
real	0m0.099s
user	0m0.077s
sys		0m0.017s
"""

from fractions import Fraction

LOWERBOUND = 10
UPPERBOUND = 100

#Given a numerator and denominator, incorrectly reduce them (47, 78) -> (4/8) 
def convertToFloat(lst):
	newFloat = "".join(digit for digit in lst)
	if newFloat == "":
		return 0
	return float("".join(digit for digit in lst))

def findWrongReduction(num, den):
	num = list(str(num))
	den = list(str(den))
	for i,digit in enumerate(num):
		if digit in den:
			num[i] = ""
			den[den.index(digit)] = ""
	newNum = convertToFloat(num)
	newDen = convertToFloat(den)
	return (newNum, newDen)


if __name__ == "__main__":
	overallNum = 1
	overallDen = 1
	for den in range(LOWERBOUND, UPPERBOUND):
		for num in range(LOWERBOUND, UPPERBOUND):
			if den <= num:
				break
			if den % 10 == 0 and num % 10 == 0:
				continue
			newNum, newDen = findWrongReduction(num, den)
			if newNum == num:
				continue

			if newDen == 0:
				reducedFrac = float('inf')
			else:
				reducedFrac = newNum/newDen

			if reducedFrac == float(num)/den:
				overallNum *= num
				overallDen *= den
	print Fraction(overallNum, overallDen).denominator