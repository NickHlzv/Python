class Road:
    def __init__(self, length, width):
        self._weight, self._gauge, self._length, self._width = (10, 5, length, width)

    def mass(self):
        return float(self._weight) * float(self._gauge) * float(self._length) * float(self._width)


r1 = Road(250, 10)
print(r1.mass())
