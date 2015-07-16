#With Python's sort function this problem becomes a lot easier. It's pretty straightforward
#after that.

"""
real	0m0.050s
user	0m0.034s
sys		0m0.012s
"""

def readFromFile():
	FILENAME = "names.txt"
	fh = open(FILENAME, 'r')
	names = []
	for name in fh:
		names = name.split(",")
	names = [name.replace("\"","") for name in names]
	return sorted(names)

def getNameScore(name):
	name = name.upper()
	score = 0
	for character in name:
		score += ord(character) - ord('A') + 1
	return score

if __name__ == "__main__":
	names = readFromFile()
	totalScore = 0
	for index, name in enumerate(names):
		totalScore += (index + 1) * getNameScore(name)
	print totalScore