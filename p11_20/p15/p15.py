#The obvious thing to do is use combinatorics (of 40 moves to get from
#the top left to the bottom right, choose the 20 that have to go down).

#In my first CS class, we had to do this exact problem with a memoizing
#structure (double array). It's interesting to compare that structure
#with Pascal's triangle. I'll do it for a 4 x 4 array (3 x 3 square)

# 20 10  4  1
# 10  6  3  1
#  4  3  2  1
#  1  1  1  1

#             1
#           1   1
#         1   2   1
#       1   3   3   1
#     1   4   6   4   1
#   1   5   10 10   5   1  
# 1   6   15  20 15    6  1

#If you consider the bottom right corner of the memoizing structure with
#the top of Pascal's Triangle, you can see they are exactly the same.
#This further validates the choice of using combinatorics.

"""
real	0m0.036s
user	0m0.020s
sys		0m0.012s
"""

import math

HEIGHT = 20
WIDTH = 20

print math.factorial(HEIGHT + WIDTH)/(math.factorial(HEIGHT) * 
	math.factorial(WIDTH))
