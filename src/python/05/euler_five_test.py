import unittest
from hamcrest import *
from euler_five import EulerFive


class EulerFiveTest(unittest.TestCase):

    def setUp(self):
        self.euler_five = EulerFive()

    def test_division_with_one_to_ten(self):
        up_to_ten = self.euler_five.smallest_multiple(10)
        assert_that(up_to_ten, is_(2520))

    def test_division_with_one_to_twenty(self):
        up_to_twenty = self.euler_five.smallest_multiple(20)
        assert_that(up_to_twenty, is_(232792560))


if __name__ == '__main__':
    unittest.main()
