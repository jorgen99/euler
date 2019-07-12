class EulerOne:

    def __init__(self, maximum):
        self.maximum = maximum

    @staticmethod
    def multiple_of_3_or_5(number):
        if number % 3 == 0 or number % 5 == 0:
            return number
        else:
            return None

    def sum_divisible_one_and_fives(self):
        result = 0
        for i in range(1, self.maximum):
            if self.multiple_of_3_or_5(i):
                result += i
        return result

    def functional_sum_more_explicit(self):
        return sum(
            filter(
                lambda i: i is not None,
                list(
                    self.multiple_of_3_or_5(i) for i in (range(1, self.maximum)))))

    def functional_sum_less_explicit(self):
        return sum(
            filter(None,
                   (self.multiple_of_3_or_5(i) for i in (range(1, self.maximum)))))

    def functional_sum2(self):
        return sum(
            (i for i in range(1, self.maximum) if self.multiple_of_3_or_5(i) is not None))
