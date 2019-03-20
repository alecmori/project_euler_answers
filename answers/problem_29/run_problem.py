# -*- coding: utf-8 -*-
import math

from utils.proj_eul_math import general


def run_problem(n=100):
    total_powers = 0
    all_powers = generate_perfect_powers(upper_bound=n)
    for a in range(2, n + 1):
        current_power = all_powers.get(a, 1)
        total_powers += (
            n - count_terms_to_remove(
                upper_bound=n,
                current_power=current_power,
            )
        )
    return total_powers

# TODO(alecmori|2019-03-21): Name these variable more clearly


def generate_perfect_powers(upper_bound=0):
    d = {}
    i = 2
    while i <= int(math.sqrt(upper_bound)):
        power = 2
        curr_power = i ** power
        while curr_power <= upper_bound:
            d[curr_power] = max(power, d.get(curr_power, -1))
            power += 1
            curr_power = i ** power
        i += 1
    return d


def count_terms_to_remove(upper_bound=0, current_power=0):
    if current_power <= 1:
        return 1
    s = set()
    for i in range(1, current_power):
        ratio_factor = general.greatest_common_denominator(
            a=current_power, b=i,
        )
        denom = int(current_power / ratio_factor)
        num_terms_with_powers = int(upper_bound / denom)
        for j in range(1, num_terms_with_powers + 1):
            s.add(i / ratio_factor * j * current_power)
    return len(s)


if __name__ == '__main__':
    answer = run_problem(5)
    if answer == 15:
        print('Correct!')
    else:
        print('Incorrect!')
