import math
class Calculator:
    def add(self, x, y):
        return x + y


    def square_root(self, x):
        if x < 0:
            raise ValueError('Cannot take square root of a negative number')
        return math.sqrt(x)
    def subtract(self, x, y):
        return x - y
