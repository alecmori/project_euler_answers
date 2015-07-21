#This problem ended up being a lot easier than I thought it would - in order to ignore
#repeats, I figure the easiest way to do it would be add the coins in increasing order.

#Each time, I either add the current coin in, or move onto the next coin in the series

"""
real	0m0.040s
user	0m0.023s
sys		0m0.013s
"""

AMOUNT = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]
MEMOIZINGSTRUCTURE = dict()

def countWays(total, index):
	if (total, index) in MEMOIZINGSTRUCTURE:
		return MEMOIZINGSTRUCTURE[(total, index)]
	if index >= len(COINS):
		return 0
	if total == AMOUNT:
		return 1
	if total > AMOUNT:
		return 0
	MEMOIZINGSTRUCTURE[(total, index)] = countWays(total + COINS[index], index) + countWays(total, index + 1)
	return MEMOIZINGSTRUCTURE[(total, index)]

if __name__ == "__main__":

	#Our initial total is 0, and our current coin index is 1
	print countWays(0, 0)