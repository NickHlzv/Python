class Cell:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return str(self.count)

    def __add__(self, other):
        s_count = self.count
        o_count = other.count
        return Cell(o_count + s_count)

    def __sub__(self, other):
        s_count = self.count
        o_count = other.count
        result = s_count - o_count
        return Cell(result) if result > 0 else 'Не может быть клеток меньше одной'

    def __mul__(self, other):
        s_count = self.count
        o_count = other.count
        return Cell(s_count * o_count)

    def __truediv__(self, other):
        s_count = self.count
        o_count = other.count
        if o_count != 0:
            return Cell(round(s_count / o_count))
        else:
            return 'Мы на ноль не делим'

    def make_order(self, count_in_row):
        result = ''
        for i in range(int(self.count)):
            result += '*'
            if (i + 1) % count_in_row == 0:
                result += '\n'
        return result


cell1 = Cell(12)
cell2 = Cell(4)
print(cell1 + cell2)
cell3 = cell1 - cell2
print(cell3)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(5))
print(cell2.make_order(3))
print(((Cell(24) - Cell(12)) / Cell(4)) * Cell(100))
print(Cell(300).make_order(50))
