class Car:
    _is_police = False

    def __init__(self, speed, color, name):
        self.speed, self.color, self.name = speed, color, name

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction: str):
        print(f'Машина поворачивает {direction}')

    def show_speed(self):
        print(f'Скорость машины: {self.speed}км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость городской машины: {self.speed}км/ч') if self.speed <= 60 else print(
            f'Превышение скорости городской машины')


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость рабочей машины: {self.speed}км/ч') if self.speed <= 40 else print(
            f'Превышение скорости рабочей машины')


class SportCar(Car):
    def show_speed(self):
        print(f'Скорость пушки-гонки: {self.speed}км/ч') if self.speed < 200 else print(
            f'О да ты Шумахер ({self.speed}км/ч)')


class PoliceCar(Car):
    _is_police = True

    def arrest(self, car: Car):
        car.speed = 0
        car.stop()
        print(f'{car.name} задержан')


car = Car(50, 'Белый', 'Хендай')
town_car = TownCar(65, 'Желтый', 'Шевроле')
loader = WorkCar(45, 'Желтый', 'Погрузчик JBC')
police_car = PoliceCar(80, 'Черный', 'Полицейская БМВ')
street_racer = SportCar(300, 'Красный', 'Пушка-гонка')
car.go()
car.turn('Направо')
car.show_speed()
car.stop()
town_car.show_speed()
loader.show_speed()
police_car.show_speed()
print(loader._is_police)
print(police_car._is_police)
print(street_racer._is_police)
street_racer.show_speed()
police_car.arrest(street_racer)
street_racer.show_speed()
