class Rectangle:

    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def calculate_square(self):
        return self.a * self.b

    def calculator_perimeter(self):
        return (self.a + self.b) * 2

    def __repr__(self):
        return f"Technical information about instance."

    def __str__(self):
        return f"Rectangle: a = {self.a}, b = {self.b}"

    def __del__(self):
        pass