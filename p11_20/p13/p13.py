#The quickest way by far to this in python is just add them all up, but I also
#want to solve the problem without relying on python's addition.

"""
real	0m0.043s
user	0m0.026s
sys		0m0.012s
"""


NUMDIGITS = 10

def readFromFile():
	FILENAME = "data.txt"
	fh = open(FILENAME, 'r')
	allNumbers = []
	for num in fh:
		#I reverse the numbers so I can iterate through the digits small-large
		allNumbers.append(num[::-1].strip())
	return allNumbers

#Add one column of digits, the same way we do normal addition
def addRow(index, nums, carry, newNum):
	total = carry
	for num in nums:
		if len(num) <= index:
			break
		total += int(num[index])
	newNum.append(total % 10)
	return total / 10

if __name__ == "__main__":
	carry = 0
	nums = readFromFile()
	NUMLENGTH = len(nums[0])
	index = 0
	newNum = []
	#Iterate through all the digits, plus whatever is leftover in the carry
	while index < NUMLENGTH or carry != 0:
		carry = addRow(index, nums, carry, newNum)
		index += 1
	newNum = newNum[::-1]
	print newNum[:10]