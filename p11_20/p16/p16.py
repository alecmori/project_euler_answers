#If there is a really clever way to solve this problem, I would love to see it. Off the top
#Of my head I cannot think of anything, but there has to be some relationship (as you get
#bigger, it becomes more formulaic but nothing I can make sense of).

"""
real	0m0.033s
user	0m0.019s
sys		0m0.011s
"""

BASE = 2
POWER = 1000

if __name__ == "__main__":
	print sum(int(digit) for digit in str(BASE**POWER))