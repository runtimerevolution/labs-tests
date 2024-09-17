
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
    
# The class calculator already has multiplication and division. No further modification needed.