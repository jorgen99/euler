import unittest
from ettan import EulerOne


class EulerOneTest(unittest.TestCase):

    def setUp(self):
        self.euler_one = EulerOne(1000)

    def test_euler_one(self):
        self.assertEqual(self.euler_one.sum_divisible_three_and_five(), 233168)

    def test_functional_sum_more_explicit(self):
        self.assertEqual(self.euler_one.functional_sum_more_explicit(), 233168)

    def test_functional_sum_less_explicit(self):
        self.assertEqual(self.euler_one.functional_sum_less_explicit(), 233168)

    def test_functiona2_sum1(self):
        self.assertEqual(self.euler_one.functional_sum_with_comprehension(), 233168)


if __name__ == '__main__':
    unittest.main()
