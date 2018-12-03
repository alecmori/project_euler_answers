# -*- coding: utf-8 -*-
import datetime

NUM_MONTHS = 12
SUNDAY = 6

cpdef run_problem(unsigned int min_year=1901, unsigned int max_year=2000):
    num_sundays = 0
    for year in range(min_year, max_year + 1):
        for month in range(1, NUM_MONTHS + 1):
            num_sundays += (
                datetime.datetime(
                    year=year,
                    month=month,
                    day=1,
                ).weekday() == SUNDAY
            )
    return num_sundays


if __name__ == '__main__':
    answer = run_problem(min_year=1901, max_year=1901)
    if answer == 2:
        print('Correct!')
    else:
        print('Incorrect!')
