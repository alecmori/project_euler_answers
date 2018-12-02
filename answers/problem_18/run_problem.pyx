# -*- coding: utf-8 -*-
TINY_TRIANGLE = """
                                       3
                                      7 4
                                     2 4 6
                                    8 5 9 3
"""
BIG_TRIANGLE = """
                                       75
                                     95 64
                                    17 47 82
                                  18 35 87 10
                                 20 04 82 47 65
                               19 01 23 75 03 34
                              88 02 77 73 07 63 67
                            99 65 04 28 06 16 70 92
                           41 41 26 56 83 40 80 70 33
                         41 48 72 33 47 32 37 16 94 29
                        53 71 44 65 25 43 91 52 97 51 14
                      70 11 33 28 77 73 17 78 39 68 17 57
                     91 71 52 38 17 14 91 43 58 50 27 29 48
                   63 66 04 68 89 53 67 30 73 16 69 87 40 31
                  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


cpdef run_problem(str triangle=BIG_TRIANGLE):
    parsed_triangle = _parse_triangle(triangle)
    curr_row_index = len(parsed_triangle) - 1
    previously_summed_row = parsed_triangle[curr_row_index]
    while curr_row_index > 0:
        curr_row_index -= 1
        curr_row = parsed_triangle[curr_row_index]
        previously_summed_row = [
            curr_row[i] + max(
                previously_summed_row[i],
                previously_summed_row[i + 1],
            )
            for i in range(len(curr_row))
        ]
    assert len(previously_summed_row) == 1
    return previously_summed_row[0]


def _parse_triangle(triangle):
    return [
        [int(x) for x in row.strip().split(' ')]
        for row in triangle.strip().split('\n')
    ]


if __name__ == '__main__':
    answer = run_problem(triangle=TINY_TRIANGLE)
    if answer == 23:
        print('Correct!')
    else:
        print('Incorrect!')
