#By far the easiest (and quickest) way to do this problem is just let python handle all 
#the nitty gritty adding and power issues.

#However, one possible way to this is to find the factors of all the powers, and then
#find the smallest factor such that num**fac > 10**10. Then, we can mod that by 10**10, 
#because we only care about the last ten digits, then repeating the process on the remaining
#factors of (num / factor).

"""
real	0m0.057s
user	0m0.038s
sys		0m0.014s
"""

UPPERBOUND = 1001
NUMDIGITS = 10

if __name__ == "__main__":
	print str(sum(x**x for x in xrange(1, UPPERBOUND)))[-NUMDIGITS:]