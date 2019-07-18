

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?
#
# Answer: 232792560
class EulerFive:

    def smallest_multiple(self, n):
        current_number = n
        while True:
            all_are_multiples = self.check_all_multiples(n, current_number)
            if all_are_multiples:
                return current_number

            current_number += n

    def check_all_multiples(self, n, current_number):
        for i in range(n, 0, -1):
            if current_number % i != 0:
                return False

        return True
