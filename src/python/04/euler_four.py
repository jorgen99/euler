

# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two
# 3-digit numbers.
#
# Answer: 906609
class EulerFour:

    def is_palindrome(self, n):
        return str(n) == "".join(reversed(str(n)))

    def max_palindromic(self, n):
        maximum = 10 ** n
        # Brute force down to one order of magnitude
        # from the max number
        lowest = 10 ** (n - 1)
        largest = 0
        for i in range(maximum, lowest, -1):
            for j in range(maximum, lowest, -1):
                current_product = i * j
                if self.is_palindrome(current_product):
                    if current_product > largest:
                        largest = current_product

        return largest
