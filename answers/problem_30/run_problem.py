# -*- coding: utf-8 -*-
def run_problem(power=5):
    total = 0
    # Problem arbitrates that `1` does not count.
    for num in range(2, _get_upper_bound(power=power)):
        if _is_sum_of_power_of_digits(num=num, power=power):
            total += num
    return total

def _get_upper_bound(power=5):
    i = 10
    aggregate_sum_of_powers = 9**power
    while i < aggregate_sum_of_powers:
        i *= 10
        aggregate_sum_of_powers += 9**power
    return aggregate_sum_of_powers

def _is_sum_of_power_of_digits(num=0, power=5):
    total = 0
    num_iter = num
    while num_iter:
        total += (num_iter % 10)**power
        num_iter = int(num_iter / 10)
    return total == num

if __name__ == '__main__':
    answer = run_problem(power=4)
    if answer == 19316:
        print('Correct!')
    else:
        print('Incorrect!')
