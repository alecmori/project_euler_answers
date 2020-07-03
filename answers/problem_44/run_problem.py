# -*- coding: utf-8 -*-
from utils.proj_eul_math import general

def get_pentagonal(n):
  return n * (3 * n - 1) >> 1

def run_problem():
  seen_pentagonal_numbers = set()
  curr_pentagonal_index = 1
  while True:
    curr_pentagonal_number = get_pentagonal(curr_pentagonal_index)
    for other_pentagonal_number in seen_pentagonal_numbers:
      difference = curr_pentagonal_number - other_pentagonal_number
      if difference not in seen_pentagonal_numbers:
        continue
      summed = curr_pentagonal_number + other_pentagonal_number
      if not general.is_pentagonal(summed):
        continue
      return difference
    curr_pentagonal_index += 1
    seen_pentagonal_numbers.add(curr_pentagonal_number)

if __name__ == '__main__':
  answer = run_problem()
  if answer == 5482660:
    print('Correct!')
  else:
    print('Incorrect!')
