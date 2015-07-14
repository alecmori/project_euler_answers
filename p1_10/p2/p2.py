#My goal for doing this problem was non-dynamically.
#I instead used the closed form.

#If you would like to see the other version, look below.

"""
real	0m0.081s
user	0m0.025s
sys		0m0.023s
"""

import math

PHI = (1 + math.sqrt(5))/2
MAX = 4000000

def fibClosedForm(n):
	return int((math.pow(PHI, n) - math.pow(-PHI, -n))/math.sqrt(5))

total = 0
i = 0
while fibClosedForm(i) <= MAX:
	if fibClosedForm(i) % 2 == 0:
		total += fibClosedForm(i)
	i += 1

print total

"""
MAX = 4000000

total = 0
fib_n = 1
fib_n_1 = 1
while fib_n_1 <= MAX:
	if fib_n_1 % 2 == 0:
		total += fib_n_1
	#Increment the fibonacci sequence - fib_n_1 is now the sum of both 
	#previous numbers, and fib_n was the prev value of fib_n_1
	fib_n_1 = fib_n_1 + fib_n
	fib_n = fib_n_1 - fib_n 
print total
"""