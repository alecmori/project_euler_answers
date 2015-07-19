#Essentially, we want to count the number of times we overflow for the first digit, second 
#digit, etc.

#Example: Let's take 0,1,2,3,And we want to find the 14th permutation when in increasing order

#Each start digit (0, 1, 2, 3) can have (n-1)! (in this case 6) different options. Thus,
#we know the 14th permuation must start with 2, 0 and 1 are both filled (12 options), but
#2 is not. We remove 2 from our pool of digits.

#Now, within the 2xxx, we want to find our SECOND option, because we know 2013 starts the
#13th permutation (again, because 0xxx and 1xxx have 6 apiece.)

#2xxx, 20xx, 203x, 2031 is our number

"""
real	0m0.033s
user	0m0.019s
sys		0m0.011s
"""

INDEXWEWANT = 1000000
MAXNUM = 9
FACTORIALLIST = []

#Builds all the factorials for us for reference later
def buildFactorialList():
	factorialList = [1]
	for i in xrange(1, MAXNUM + 1):
		factorialList.append(factorialList[-1] * i)
	return factorialList

#Given our current index we want to find the next one

#Example: the 12th PERMUTATIONINDEX in the 34xxxx space, find the index of the next digit
def findNextNum(PERMINDEX, currFact):
	index = PERMINDEX / currFact
	return index

if __name__ == "__main__":
	#Index within the permutation, as opposed to an array
	PERMINDEX = INDEXWEWANT -1
	FACTORIALLIST = buildFactorialList()
	NUMLIST = range(MAXNUM + 1)
	permutation = ""
	while len(NUMLIST) > 0:
		nextIndex = findNextNum(PERMINDEX, FACTORIALLIST[-1])
		PERMINDEX = PERMINDEX % FACTORIALLIST[-1]
		#Get the next factorial
		FACTORIALLIST.pop()
		permutation += str(NUMLIST[nextIndex])
		#Ignore the last number we added to our overall permutation
		NUMLIST.pop(nextIndex)
	print permutation