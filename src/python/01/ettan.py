class EulerOne:

    def __init__(self, maximum):
        self.maximum = maximum
        self.one_to_max = range(1, maximum)

    @staticmethod
    def multiple_of_3_or_5(number):
        if number % 3 == 0 or number % 5 == 0:
            return number
        else:
            return None

    def sum_divisible_three_and_five(self):
        result = 0
        for i in self.one_to_max:
            if self.multiple_of_3_or_5(i):
                result += i
        return result

    def functional_sum_more_explicit(self):
        return sum(
            filter(
                lambda i: i is not None,
                list(
                    self.multiple_of_3_or_5(i) for i in self.one_to_max)))

    def functional_sum_less_explicit(self):
        return sum(
            filter(None,  # if function is None return items that is not None
                   (self.multiple_of_3_or_5(i) for i in self.one_to_max)))

    def functional_sum_with_comprehension(self):
        return sum(
            (i for i in self.one_to_max if self.multiple_of_3_or_5(i) is not None))
