# -*- coding: utf-8 -*-
from utils.proj_eul_math import prime


def run_problem(n=1000000):
    all_primes = {
        p for p in prime.get_primes(max_num_inclusive=n)
    }
    # Hard coding 2 because makes all other things easier
    circular_primes = {2}
    for i in _get_numbers_only_odd(upper_bound=n):
        if i not in all_primes:
            continue
        circular_primes = circular_primes.union(
            poss_get_circular_primes(
                n=i, circular_primes=circular_primes, primes=all_primes,
            ),
        )
    return len(circular_primes)


def poss_get_circular_primes(n, circular_primes, primes):
    if n in circular_primes:
        return set()
    num_digits = len(str(n))
    circular_primes = set()
    for i in range(num_digits):
        ten_power = 10**i
        poss_circular_prime = (
            int(n / ten_power) + (n % ten_power) * 10**(num_digits - i)
        )
        if poss_circular_prime not in primes:
            return set()
        circular_primes.add(poss_circular_prime)
    return circular_primes


def _get_numbers_only_odd(upper_bound):
    # TODO: Use some local_vars_constructor for generator and this
    generator_vars = {
        'current_count': 1,
        'current_n': 1,
        'current_threshold': 5,
        'multiplier': 2,
        'thresholds_met': {},
    }
    return_value = set()
    while generator_vars['current_n'] <= upper_bound:
        return_value.add(generator_vars['current_n'])
        # TODO: Reuse a lot of this logic between this and generator
        generator_vars['current_n'] += 2
        for threshold, additive in generator_vars['thresholds_met'].items():
            if generator_vars['current_count'] % threshold == 0:
                generator_vars['current_n'] += additive
        current_threshold = generator_vars['current_threshold']
        if generator_vars['current_count'] == current_threshold:
            generator_vars['current_count'] -= current_threshold
            generator_vars['thresholds_met'][current_threshold] = (
                current_threshold * generator_vars['multiplier']
            )
            generator_vars['multiplier'] *= 2
            generator_vars['current_threshold'] *= 5
        generator_vars['current_count'] += 1
    return return_value


# TODO: Whenever possible, don't use generator - use set/list. Still
#   have to go through all code and replace generators when possible.
def _get_numbers_only_odd_gen():
    current_count = 1
    current_n = 1
    current_threshold = 5
    multiplier = 2
    thresholds_met = {}
    while True:
        yield current_n
        current_n += 2
        for threshold, additive in thresholds_met.items():
            if current_count % threshold == 0:
                current_n += additive
        if current_count == current_threshold:
            current_count -= current_threshold
            thresholds_met[current_threshold] = (
                current_threshold * multiplier
            )
            multiplier *= 2
            current_threshold *= 5
        current_count += 1


if __name__ == '__main__':
    answer = run_problem(n=100)
    # TODO
    if answer == 13:
        print('Correct!')
    else:
        print('Incorrect!')
