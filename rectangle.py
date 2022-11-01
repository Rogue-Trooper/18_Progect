class Rectangle:

    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def calculate_square(self):
        return self.a * self.b

    def calculator_perimeter(self):
        return (self.a + self.b) * 2

    def get_info(self):
        return f"Rectangle: a = {self.a}, b = {self.b}"

    def __del__(self):
        pass
