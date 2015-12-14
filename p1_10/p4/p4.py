#The quickest way to convert a number into a list of numbers is to first cast it to a string.
#That makes sense though - a palindrome is far more an alphabetic quality rather than
#numeric.

"""
real	0m1.355s
user	0m1.321s
sys		0m0.020s
"""

NUM_DIGITS = 3

def is_palindrome(num):
	num_string = str(num)
	for i in xrange(len(num_string) / 2):
		if num_string[i] != num_string[-i - 1]:
			return False
	return True

if __name__ == "__main__":

	largest_palindrome = -1
	
	#We will just brute force all possible combinations of 3 digits numbers
	for first_number in xrange(10**(NUM_DIGITS - 1), 10**NUM_DIGITS):
		for second_number in xrange(10**(NUM_DIGITS - 1), 10**NUM_DIGITS):
			poss_palindrome = first_number * second_number
			if is_palindrome(poss_palindrome) and poss_palindrome > largest_palindrome:
				largest_palindrome = poss_palindrome
	print largest_palindrome