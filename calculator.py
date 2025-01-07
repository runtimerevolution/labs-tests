class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot compute the square root of a negative number")
        return x ** 0.5
