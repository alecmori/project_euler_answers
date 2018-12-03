# -*- coding: utf-8 -*-
import pytest

from utils.proj_eul_math import prime


class TestGetPrimeFactorization:

    @pytest.mark.parametrize(
        argnames=['num', 'expected'],
        argvalues=[
            (2, {2: 1}),
            (4, {2: 2}),
            (19, {19: 1}),
            (459, {3: 3, 17: 1}),
        ],
        ids=[
            'Smallest value',
            'Sieve of Atkins edge case',
            'Larger prime',
            'Larger number',
        ],
    )
    def test_non_error_cases(self, num, expected):
        # Given a <num> bigger than one
        # When we get its prime factorization
        result = prime.get_prime_factorization(num)
        # Then the result should be <expected>
        assert result == expected

    def test_error_case(self):
        # Given a number with no prime factorization
        # Then we should get a ValueError
        with pytest.raises(ValueError):
            # When we try to get its prime factorization
            prime.get_prime_factorization(1)


class TestIsPrime:

    @pytest.mark.parametrize(
        argnames=['num', 'expected'],
        argvalues=[
            (1, False),
            (2, True),
            (4, False),
            (19, True),
            (899809363, True),
            (899809367, False),
        ],
        ids=[
            'Prime edge case',
            'Smallest value',
            'Sieve of Atkins edge case',
            'Slightly larger prime',
            'Huge-ass prime',
            'Huge-ass composite',
        ],
    )
    def test_is_prime(self, num, expected):
        # Given a <num>
        # When we check if it's prime
        result = prime.is_prime(num)
        # Then the result should be <expected>
        assert result == expected
