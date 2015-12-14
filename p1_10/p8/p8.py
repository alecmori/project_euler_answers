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

FILE_NAME = "data.txt"
NUM_ADJ_DIGITS = 13

#Read in our giant number as a list of integers
def read_data():
	fh = open(FILE_NAME, 'r')
	num = ""
	for row in fh:
		row = row.strip()
		num += row
	return map(int,list(num))

if __name__ == "__main__":
	num = read_data()
	best_product = 0

	for i in xrange(len(num) - NUM_ADJ_DIGITS):
		curr_product = 1

		for j in xrange(NUM_ADJ_DIGITS):
			curr_product *= num[i + j]
		if curr_product > best_product:
			best_product = curr_product

	print best_product