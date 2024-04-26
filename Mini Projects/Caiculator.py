class AdvancedCalculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero!"

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a >= 0:
            return a ** 0.5
        else:
            return "Error: Square root of a negative number!"

    def factorial(self, n):
        if n < 0:
            return "Error: Factorial of a negative number!"
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result


# Example usage:
calculator = AdvancedCalculator()
print("5 + 3 =", calculator.add(5, 3))
print("5 - 3 =", calculator.subtract(5, 3))
print("5 * 3 =", calculator.multiply(5, 3))
print("5 / 3 =", calculator.divide(5, 3))
print("2 ^ 3 =", calculator.power(2, 3))
print("Square root of 25 =", calculator.square_root(25))
print("Factorial of 5 =", calculator.factorial(5))

