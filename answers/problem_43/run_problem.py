# -*- coding: utf-8 -*-
# TODO: Rewrite
import itertools

def is_divisible(x, y, z, divisor):
  return (x * 100 + y * 10 + z) % divisor == 0


def convert_pandigital(l):
  total = 0
  for i in range(len(l)):
    total += l[len(l) - 1 - i] * 10**i
  return total


def run_problem():
  total = 0
  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  divisors = [2, 3, 5, 7, 11, 13, 17]
  # TODO: Generate these smarter
  for permutation in itertools.permutations(digits):
    # d_6 must equal 5
    if permutation[5] != 5:
      continue
    all_divisible = True
    for i, divisor in enumerate(divisors):
      x, y, z = permutation[i + 1], permutation[i + 2], permutation[i + 3]
      all_divisible = all_divisible and is_divisible(x, y, z, divisor)
    if all_divisible:
      total += convert_pandigital(permutation)
  return total


if __name__ == '__main__':
    answer = run_problem()
    if answer == 16695334890:
        print('Correct!')
    else:
        print('Incorrect!')
