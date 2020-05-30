# -*- coding: utf-8 -*-
import collections
import collections

def generate_all_base_perimeters(max_n):
  # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
  m = 2
  n = 1
  perimeters = []
  while True:
    m2 = m**2
    perimeter = 2 * (m2 + m * n)
    if perimeter > max_n:
      return perimeters
    while m > n:
      perimeters.append(perimeter)
      n += 2
      perimeter = 2 * (m2 + m * n)
      if perimeter > max_n:
        break
    m += 1
    n = 2 if m % 2 else 1
    if m % 2:
      n = 2
    else:
      n = 1


def run_problem(n=1000):
  num_with_perimeter = collections.defaultdict(int)
  perimeters = generate_all_base_perimeters(n)
  for perimeter in perimeters:
    m = 1
    while m * perimeter < n:
      num_with_perimeter[perimeter * m] += 1
      m += 1
  return max(num_with_perimeter.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    answer = run_problem(150)
    if answer == 120:
        print('Correct!')
    else:
        print('Incorrect!')
