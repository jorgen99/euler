import unittest
from hamcrest import *
from euler_four import EulerFour


class EulerFourTest(unittest.TestCase):

    def setUp(self):
        self.euler_three = EulerFour()

    def test_is_palindrome(self):
        is_palindrome = self.euler_three.is_palindrome(1001)
        assert_that(is_palindrome, is_(True))

        is_palindrome = self.euler_three.is_palindrome(9009)
        assert_that(is_palindrome, is_(True))

        is_palindrome = self.euler_three.is_palindrome(202)
        assert_that(is_palindrome, is_(True))

    def test_2_digit_numbers(self):
        palindrome = self.euler_three.max_palindromic(2)
        assert_that(palindrome, is_(9009))

    def test_3_digit_numbers(self):
        palindrome = self.euler_three.max_palindromic(3)
        assert_that(palindrome, is_(906609))


if __name__ == '__main__':
    unittest.main()
