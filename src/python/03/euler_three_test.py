import sys
import unittest
from hamcrest import *
from euler_three import EulerThree


class EulerThreeTest(unittest.TestCase):

    def setUp(self):
        self.euler_three = EulerThree()

    def test_it_should_return_True_for_actual_primes(self):
        self.primes_below_100 = [2, 3, 5, 7, 11, 13, 17,
                                 19, 23, 29, 31, 37, 41,
                                 43, 47, 53, 59, 61, 67,
                                 71, 73, 79, 83, 89, 97]

        for i in range(2, 100):
            prime = self.euler_three.is_prime(i)
            if i in self.primes_below_100:
                assert_that(prime, is_(True), "True for i %i" % i)
            else:
                assert_that(prime, is_(False), "False for i %i" % i)

    def test_prime_factors_of_13195(self):
        factors = self.euler_three.prime_factors(13195)
        assert_that(factors, contains(5, 7, 13, 29))

    def test_prime_factors_of_13195_by_recursion(self):
        # Python does not have tail recursion so this
        # is not a good idea, just to check if the
        # implementation actually works
        #
        # From:
        # https://stackoverflow.com/a/3323008/5264
        sys.setrecursionlimit(13200)

        factors = self.euler_three.prime_factors_recursive(13195)
        assert_that(factors, contains(5, 7, 13, 29))

    def test_prime_factors_of_600851475143(self):
        max_factor = self.euler_three.max_prime_factor(600851475143)
        assert_that(max_factor, is_(6857))


if __name__ == '__main__':
    unittest.main()
