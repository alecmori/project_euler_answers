#Thinking through this problem was difficult, but I think I finally got it

#Because we only care about the repetition AFTER the decimal, if divisor (n) > dividend (n2),
#We can treat n as n % n2.

#THIS IS NOT A PROOF - IT IS MY OWN MENTAL JUSTIFICATION. In a real world scenario, I would
#definitely back this up with a proof of some kind.

#First, we have to think of how division works (at least the way I learned in 4th grade)
#We take a number n, and try to divide it by n2. If n2 < n, great - we count how many times 
#it goes into n (t), then subtract n2 * t from n, and repeat. If not, we had to add a 0 at the
#end of n (for instance, it would turn n = 2 to n= 20, then try to divide). We would stop all
#this if n never equaled 0 (repeating decimals never hit 0).

#For any given problem, if we run into the same n twice, it means it's repeating, which makes
#sense. Thus, that is the formula for which I will solve the problem.

#However, we can also reduce which numbers we need to check. Let's say that, for any number 
#1/d, we can reduce it to 1 * (1/p) * (1/p2) * ... for the prime factorization of d. If the
#first p makes it repeat m times, p2 makes it repeat m2 times, etc. If my instinct is correct
#(i.e. NOT A PROOF), 1/d will repeat at most max(m) times, because that is just a repetition 
#of some other number with a different repetition property.

#Because of this, we only need to check primes less than our max number, because any other
#number n < max will have to check p <= n < max, and repeatDigits(n) <= repeatDigits(p).
#Because we are only dealing with primes (GUT INSTINCT AGAIN), we only need to look at the
#first digit to find the repeated n.

"""
real	0m0.057s
user	0m0.039s
sys		0m0.012s
"""

MAXNUM = 1000
NUMERATOR = 1

def isPrime(num):
	i = 2
	while i * i <= num:
		if num % i == 0:
			return False
		i += 1
	return True

#Counts the length of our repeated digit sequence
def countRepeatedDigits(num):
	numerator = NUMERATOR % num
	nextN = numerator * 10 % num
	seenNs = [nextN]
	nextN = nextN * 10 % num
	if nextN == seenNs[0]:
		return 0
	while nextN != seenNs[0]:
		seenNs.append(nextN)
		nextN = nextN * 10 % num

	return len(seenNs)

if __name__ == "__main__":
	longestLength = 0
	bestIndex = -1
	for currNum in xrange(2, MAXNUM):
		if isPrime(currNum):
			currLength = countRepeatedDigits(currNum)
			if currLength > longestLength:
				longestLength = currLength
				bestIndex = currNum
	print bestIndex



