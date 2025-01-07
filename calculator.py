import math
class Calculator:
    def add(self, x, y):
        return x + y


    def square_root(self, x):
        if x < 0:
            raise ValueError('Cannot take square root of a negative number')
        return math.sqrt(x)
    def subtract(self, x, y):
    def factorial(self, n):
        if n < 0:
            raise ValueError('Factorial is not defined for negative numbers')
        if n == 0:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

        return x - y
