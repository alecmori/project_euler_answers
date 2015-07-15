#For these types of problems (with a "check all" of a grid), I never know what to do for
#the cleanest code. This is how I implemented movement for a chess game for a class in
#school, and I figured out it transferred relaively well.

"""
real	0m0.052s
user	0m0.027s
sys		0m0.012s
"""

FILENAME = "data.txt"
NUMADJDIGITS = 4

def readData():
	fh = open(FILENAME, 'r')
	matrix = []
	for row in fh:
		row = list(row.strip().split(" ")) #Removing the newline and turning it from a single string to 
								#list of characters
		matrix.append(map(int, row))	#Turn all characters into integers
	return matrix

#Returns (xOffset, yOffset) for all possible traversals
#One ugly, long function to write clean code
def findViableOptions(x, y, WIDTH, HEIGHT):
	viableOptions = []
	#Right
	if x <= WIDTH - NUMADJDIGITS:
		viableOptions.append((1, 0))
	#Down
	if y <= HEIGHT - NUMADJDIGITS:
		viableOptions.append((0, 1))
	#Down-Right
	if y <= HEIGHT - NUMADJDIGITS and x <= WIDTH - NUMADJDIGITS:
		viableOptions.append((1, 1))
	#Up-Right
	if y >= NUMADJDIGITS - 1 and x <= WIDTH - NUMADJDIGITS:
		viableOptions.append((1, -1))

	return viableOptions

def findBestOption(x, y, MATRIX, viableOptions):
	bestProduct = 0
	for dx, dy in viableOptions:
		currProduct = 1
		for i in range(NUMADJDIGITS):
			currProduct *= MATRIX[x + dx * i][y + dy * i]
		if currProduct > bestProduct:
			bestProduct = currProduct
	return bestProduct

if __name__ == "__main__":
	MATRIX = readData()
	WIDTH = len(MATRIX)
	HEIGHT = len(MATRIX[0])
	bestProduct = 0
	for x in range(WIDTH):
		for y in range(HEIGHT):
			viableOptions = findViableOptions(x, y, WIDTH, HEIGHT)
			bestOption = findBestOption(x, y, MATRIX, viableOptions)
			if bestOption > bestProduct:
				bestProduct = bestOption
	print bestProduct