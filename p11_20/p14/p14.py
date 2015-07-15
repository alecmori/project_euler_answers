#Nothing too interesting - just a memoizing structure. I am curious to know,
#however, if there is some mathematical way to see for which f building 
#an array of length f(n), where n is the amount of numbers we are checking,
#is more efficient than building adictionary.

"""
real	0m3.246s
user	0m2.821s
sys		0m0.245s
"""

totalNumbers = 1000000
collatzDict = dict()

def collatz(n):
	if n == 1 or n == 0:
		return 1
	if n in collatzDict:
		return collatzDict[n]
	if n % 2 == 0:
		collatzDict[n] = collatz(n / 2) + 1
	else:
		collatzDict[n] = collatz(3 * n + 1) + 1
	return collatzDict[n]

best = -1
longestNum = -1
for i in range(totalNumbers):
	possBest = collatz(i)
	if possBest > best:
		best = possBest
		longestNum = i
print longestNum