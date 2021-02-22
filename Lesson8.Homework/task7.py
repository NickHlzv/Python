class Complex:
    def __init__(self, value, value2=0):
        self.value = complex(value, value2)

    def __add__(self, other):
        return Complex(self.value + other.value)

    def __mul__(self, other):
        return Complex(self.value * other.value)

    def __str__(self):
        return str(self.value)


c1 = Complex(3, 7)
c2 = Complex(5, 9)
c3 = c2 + c1
c4 = c2 * c1
print(c1)
print(c2)
print(c3)
print(c4)
print(complex(3, 7) * complex(5, 9))
