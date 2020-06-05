# -*- coding: utf-8 -*-
import requests                                            
from utils.proj_eul_math import general

WORDS_URL = 'https://projecteuler.net/project/resources/p042_words.txt'       

def _score_word(word):
    total = 0
    for c in word:
        total += ord(c) - ord('A') + 1
    return total

def run_problem():
    num_triangle = 0                                       
    for word in requests.get(WORDS_URL).text.split(','):
        score = _score_word(word.strip('"'))
        # triangle_number -> (n^2 + n)/2 = score ->
        # n^2 + n - 8 * score = 0
        # If discriminant of quad formula is square, then n has integer
        # solution.
        if general.is_square(8 * score + 1):
          num_triangle += 1
    return num_triangle

if __name__ == '__main__':
    answer = run_problem()
    if answer == 162:
        print('Correct!')
    else:
        print('Incorrect!')
