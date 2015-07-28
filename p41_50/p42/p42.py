#In order for num to be a triangle number, num = .5 * n(n + 1)
#In other words, n^2 + n - 2num = 0, which is quadratic

# (-1 +- sqrt(1 + 8*num))/2 == n, which means the top must be divisible by two,
#which means 1 + 8 * num must be a perfect square (because num is an integer, you are
#sure the inside of the sqrt will be odd, which means we don't need to worry about
#even or odd case.

#Reads in the test words from a file

"""
real	0m0.049s
user	0m0.033s
sys		0m0.011s
"""

def readFile():
	FILENAME = "words.txt"
	fh = open(FILENAME, 'r')
	for row in fh:
		allWords = row.split(",")
	allWords = [word.replace('"', "") for word in allWords]
	return allWords

def getCharValue(c):
	return ord(c) - ord('A') + 1

#Given a word, get it's value by summing its characters' values {A:1, B:2, etc.}
def getWordValue(word):
	value = 0
	for c in word:
		value += getCharValue(c)
	return value

#Based off Babylonian algorithm
def isSquare(value):
	x = value / 2
	seenValues = set([x])
	while x * x != value:
		x = (x + value / x) / 2
		if x in seenValues:
			return False
		seenValues.add(x)
	return True

#See header for justification
def isTriangleNumber(value):
	return isSquare(value * 8 + 1)

if __name__ == "__main__":
	allWords = readFile()
	triangleWords = 0
	for word in allWords:
		wordValue = getWordValue(word)
		if isTriangleNumber(wordValue):
			triangleWords += 1
	print triangleWords