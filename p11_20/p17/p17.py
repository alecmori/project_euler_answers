#This is not a fun problem - it is not math and more code organization. I only planned for 
#numbers up to 10000, so it would need to be modified if MAX >= 10000.

#It sucks that the scenarios they gave us were all more or less "special cases": once you
#get into the thousands, millions, etc. it becomes a lot more fomulaic

#I did this kind of inefficiently, creating the full strings, but I figured in a real world
#scenario there would be value in that.

"""
real	0m0.039s
user	0m0.022s
sys		0m0.012s
"""

import math

MAX = 1000
CUTOFFTEEN = 20

LESSTHANTWENTY = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
	"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
	"eighteen", "nineteen"]

MORETHANTWENTY = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
	"ninety"]

MORETHANHUNDRED = ["", "", "hundred", "thousand"]

def makeWord(currNum):
	strNum = ""
	lastTwoDigits = currNum % 100
	if lastTwoDigits < CUTOFFTEEN:
		strNum = LESSTHANTWENTY[lastTwoDigits]
	else:
		firstDigit = lastTwoDigits % 10
		secondDigit = lastTwoDigits // 10
		strNum = LESSTHANTWENTY[firstDigit]
		strNum = MORETHANTWENTY[secondDigit] + strNum
	if currNum >= 100: #Cutoff for three digits
		if lastTwoDigits != 0:
			strNum = "and" + strNum
		powerTen = len(str(currNum)) - 1

		for power in range(2, powerTen + 1):
			currPlace = (currNum / 10**power) % 10
			if currPlace != 0:
				strNum = MORETHANHUNDRED[power] + strNum
			strNum = LESSTHANTWENTY[currPlace] + strNum
	return strNum

if __name__ == "__main__":
	total = 0
	for currNum in range(MAX + 1):
		num = makeWord(currNum)
		total += len(num)
	print total