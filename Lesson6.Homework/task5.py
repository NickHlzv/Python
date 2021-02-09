class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} рисует')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка: "{self.title}" рисует')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш: "{self.title}" рисует')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер: "{self.title}" рисует')


chalk = Stationery('Мел')
pen = Pen('Черная ручка')
pencil = Pencil('Чертежный карандаш')
handle = Handle('Строительный маркер')
chalk.draw()
pen.draw()
pencil.draw()
handle.draw()
