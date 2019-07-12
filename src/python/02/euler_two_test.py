import unittest
from hamcrest import *
from euler_two import EulerTwo


class EulerTwoTest(unittest.TestCase):

    def setUp(self):
        self.euler_two = EulerTwo()

    # fib sequence
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

    def test_fib_zero(self):
        fib_zero = self.euler_two.fib(0)
        assert_that(fib_zero, is_(0))

    def test_fib_one(self):
        fib_one = self.euler_two.fib(1)
        assert_that(fib_one, is_(1))

    def test_fib_two(self):
        fib_two = self.euler_two.fib(2)
        assert_that(fib_two, is_(1))

    def test_fib_ten(self):
        fib_ten = self.euler_two.fib(10)
        assert_that(fib_ten, is_(55))

    def test_euler_two(self):
        sum_even_terms = self.euler_two.sum_even_terms(4000000)
        assert_that(sum_even_terms, is_(4613732))


if __name__ == '__main__':
    unittest.main()

