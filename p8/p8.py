#I lost some time for reading in the number from a different file, but I figured this 
#made the code feel far less cluttered and is worth it for pretty.

#Since this is more of a lexical question than a mathematic, the best way is probably
#to do it. I was trying to multiply a new one/divide an old one each time, but that would
#only work if all elements were non-zero.

"""
real	0m0.048s
user	0m0.031s
sys		0m0.014s
"""

FILENAME = "data.txt"
NUMADJDIGITS = 13

#Read in our giant number as a list of integers
def readData():
	fh = open(FILENAME, 'r')
	num = ""
	for row in fh:
		row = row.strip()
		num += row
	return map(int,list(num))

num = readData()
bestProduct = 0
for i in range(len(num) - NUMADJDIGITS):
	currProduct = 1
	for j in range(NUMADJDIGITS):
		currProduct *= num[i + j]
	if currProduct > bestProduct:
		bestProduct = currProduct

print bestProduct