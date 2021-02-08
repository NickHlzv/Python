class Worker:
    def __init__(self, name, surname, position='уборщик'):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'директор': {'Оклад': 70000, 'Премия': 20000},
                        'офисный клерк': {'Оклад': 40000, 'Премия': 5000},
                        'уборщик': {'Оклад': 20000, 'Премия': 1000}}
        self.positions = []
        for i in self._income.keys():
            self.positions.append(i)


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        if self.positions.count(self.position) >= 1:
            result = self._income[self.position]
            return result['Оклад'] + result['Премия']
        else:
            return 'Нет такой должности'


stuff = Position('Василий', 'Лентюгов', 'директор')
print(stuff.get_full_name())
print(stuff.get_total_income())
