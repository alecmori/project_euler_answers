# -*- coding: utf-8 -*-
cpdef unsigned int run_problem(unsigned int summed_value=1000):
    for triple in _generate_base_pythagorean_triples():
        if summed_value % sum(triple.values()) == 0:
            constant_factor = int(summed_value) / sum(triple.values())
            return int(
                triple['a'] * triple['b'] * triple['c'] * constant_factor**3,
            )


def _generate_base_pythagorean_triples():
    r = 1
    s = 3
    while True:
        yield {'a': s * r, 'b': (s**2 - r**2) / 2, 'c': (s**2 + r**2) / 2}
        r += 2
        if r == s:
            s += 2
            r = 1


if __name__ == '__main__':
    answer = run_problem(summed_value=12)
    if answer == 60:
        print('Correct!')
    else:
        print('Incorrect!')
