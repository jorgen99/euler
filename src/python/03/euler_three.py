from math import sqrt


# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# Answer: 6857
class EulerThree:

    @staticmethod
    def is_prime(n):
        # https://en.wikipedia.org/wiki/Primality_test
        if n <= 3:
            return n > 1
        elif n % 2 == 0 or n % 3 == 0:
            return False

        for i in range(5, int(sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True

    def prime_factors(self, n):
        result = []
        possible_primes = [2] + list(range(3, int(sqrt(n)), 2))
        for i in possible_primes:
            if self.is_prime(i) and n % i == 0:
                result.append(i)
                n /= i

        if n != 1:
            result.append(n)

        return result

    def max_prime_factor(self, n):
        return max(self.prime_factors(n))

    def prime_factors_recursive(self, n):
        possible_primes = [2] + list(range(3, n, 2))
        return self.__prime_factors(n, possible_primes, [])

    def __prime_factors(self, reminder, possible_primes, result):
        if not possible_primes:
            return result

        prime = possible_primes.pop(0)
        if self.is_prime(prime) and reminder % prime == 0:
            result.append(prime)
            reminder /= prime

        return self.__prime_factors(reminder, possible_primes, result)
