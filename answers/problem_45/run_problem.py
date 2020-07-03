# -*- coding: utf-8 -*-
from utils.proj_eul_math import general

def get_hexagonal(n):
  return n * (2 * n - 1)

def run_problem():
  # 143 is a hexagonal number
  curr_index = 144
  while True:
    hexagonal_number = get_hexagonal(curr_index)
    # All triangular numbers are hexagonal, so we don't need to check.
    if general.is_pentagonal(hexagonal_number):
      return hexagonal_number
    curr_index += 1

if __name__ == '__main__':
  answer = run_problem()
  if answer == 1533776805:
    print('Correct!')
  else:
    print('Incorrect!')
