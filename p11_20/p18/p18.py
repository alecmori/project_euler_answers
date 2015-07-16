#Once you have a memoizing structure in place it isn't so bad. You shouldn't have to calculate
#the path for some node more than one time.

#I may play around with data structures a little bit more on this one, it's not particularly
#"pretty" right now.

"""
real	0m0.034s
user	0m0.019s
sys		0m0.010s
"""

MEMOIZE = dict()

def read_data():
	FILENAME = "data.txt"
	fh = open(FILENAME, 'r')
	dag = []
	for row in fh:
		dag.append(map(int, row.strip().split(" ")))
	return dag

def findLongestPath(dag, currLevel, currIndex):
	if currLevel >= len(dag):
		return 0
	if currIndex >= len(dag[currLevel]):
		return 0
	if (currLevel, currIndex) in MEMOIZE:
		return MEMOIZE[(currLevel, currIndex)]

	leftPath = findLongestPath(dag, currLevel + 1, currIndex)
	rightPath = findLongestPath(dag, currLevel + 1, currIndex + 1)
	MEMOIZE[(currLevel, currIndex)] = max(leftPath, rightPath) + dag[currLevel][currIndex]
	return MEMOIZE[(currLevel, currIndex)]


if __name__ == "__main__":
	dag = read_data()
	STARTINDEX = 0
	STARTLEVEL = 0
	longestPath = findLongestPath(dag, STARTLEVEL, STARTINDEX)
	print longestPath