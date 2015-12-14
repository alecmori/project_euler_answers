#Although there is a more traditional dynamic solution (or storing the last two values),
#I used the closed form, if only to remind myself of what exactly it was!

"""
real	0m0.081s
user	0m0.025s
sys		0m0.023s
"""

import math

PHI = (1 + math.sqrt(5))/2
MAX = 4000000

#The Fibonacci Closed Form - see here!
#https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
def fib_closed_form(n):
	return int((math.pow(PHI, n) - math.pow(-PHI, -n))/math.sqrt(5))

if __name__ == "__main__":
	total = 0
	i = 0
	while fib_closed_form(i) <= MAX:
		if fib_closed_form(i) % 2 == 0:
			total += fib_closed_form(i)
		i += 1

	print total
