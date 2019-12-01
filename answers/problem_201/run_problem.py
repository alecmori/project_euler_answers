# -*- coding: utf-8 -*-
import collections

starting_set = set()
for x in range(1, 101):
    starting_set.add(x * x)

STARTING_SET = frozenset(starting_set)

def run_problem(S=starting_set, k=50):
    cache = []
    for _ in range(k + 1):
        cache.append(dict())
    # To make updating the cache easier, we invert the locations of
    # everything - the last index refers to have zero elements
    # remaining, the first have k remaining
    cache[k][0] = False
    for element in S:
        update_cache_for_element(
            element=element,
            cache=cache,
        )
    total_sum = 0
    for current_sum, seen_more_than_once in cache[0].items():
        if not seen_more_than_once:
            total_sum += current_sum
    return total_sum

def update_cache_for_element(element=-1, cache=None):
    for num_elements_used in range(1, len(cache)):
        for current_sum, seen_more_than_once in cache[num_elements_used].items():
            new_sum = current_sum + element
            if new_sum in cache[num_elements_used - 1] or seen_more_than_once:
                cache[num_elements_used - 1][new_sum] = True
            else:
                cache[num_elements_used - 1][new_sum] = False


if __name__ == '__main__':
    answer = run_problem(S={1, 3, 6, 8, 10, 11}, k=3)
    if answer == 156:
        print('Correct!')
    else:
        print('Incorrect!')
