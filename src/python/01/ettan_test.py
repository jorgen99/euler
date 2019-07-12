import unittest
from ettan import EulerOne


class EulerOneTest(unittest.TestCase):

    def test_sum_up_to_ten(self):
        euler_one = EulerOne(10)
        self.assertEqual(euler_one.sum_divisible_one_and_fives(), 23)

    def test_euler_one(self):
        euler_one = EulerOne(1000)
        self.assertEqual(euler_one.sum_divisible_one_and_fives(), 233168)

    def test_functional_sum_more_explicit(self):
        euler_one = EulerOne(1000)
        self.assertEqual(euler_one.functional_sum_more_explicit(), 233168)

    def test_functional_sum_less_explicit(self):
        euler_one = EulerOne(1000)
        self.assertEqual(euler_one.functional_sum_less_explicit(), 233168)

    def test_functiona2_sum1(self):
        euler_one = EulerOne(1000)
        self.assertEqual(euler_one.functional_sum2(), 233168)


if __name__ == '__main__':
    unittest.main()
