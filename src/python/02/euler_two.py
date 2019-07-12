class EulerTwo:

    def fib(self, i):
        if i < 2:
            return i

        return self.fib(i - 1) + self.fib(i - 2)

    def even_terms(self, maximum):
        i = 0
        result = []
        while True:
            f = self.fib(i)
            if f > maximum:
                break
            if f % 2 == 0:
                result.append(f)

            i += 1

        return result

    def sum_even_terms(self, maximum):
        return sum(self.even_terms(maximum))

    def even_terms_recursive(self, maximum):
        return self.__even_terms_recursive(maximum, 0, [])

    def __even_terms_recursive(self, maximum, i, result):
        f = self.fib(i)
        if f > maximum:
            return result
        if f % 2 == 0:
            result.append(f)

        return self.__even_terms_recursive(maximum, i + 1, result)

    def sum_even_terms_recursive(self, maximum):
        return sum(self.even_terms_recursive(maximum))
