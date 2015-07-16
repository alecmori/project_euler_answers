#There is a closed form formula, but that would be terrible to implement a lookup for
#most of the data. Because we have to go through every date in either situation, I would
#prefer to do it this way - it's far cleaner.

"""
real	0m0.038s
user	0m0.022s
sys		0m0.013s
"""

CURRDAY = 1
CURRYEAR = 1900
DAYSOFTHEWEEK = 7
MAXYEAR = 2000
DAYSPERMONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Adjusts February's days according to leap years
def adjustDays(year):
	DAYSPERMONTH[1] = 28
	if year % 400 == 0:
		DAYSPERMONTH[1] = 29
		return
	if year % 100 == 0:
		DAYSPERMONTH[1] = 28
		return
	if year % 4 == 0:
		DAYSPERMONTH[1] = 29


if __name__ == "__main__":
	numSundays = 0
	while CURRYEAR <= MAXYEAR:
		adjustDays(CURRYEAR)
		for month in DAYSPERMONTH:
			#For whatever reason, they don't want us to count this year
			if CURRDAY == 0 and CURRYEAR != 1900:
				numSundays += 1
			CURRDAY = (CURRDAY + month) % DAYSOFTHEWEEK
		CURRYEAR += 1
	print numSundays