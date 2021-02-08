class road:
    def __init__(self, length, width):
        self.weight, self.gauge = (10, 5)
        print(float(self.weight) * float(self.gauge) * float(length) * float(width))


r1 = road(250, 10)
