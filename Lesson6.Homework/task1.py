import time


class TrafficLight:
    modes = ['Красный', 'Желтый', 'Зеленый']

    def __init__(self, color='Красный'):
        self.__color = color
        self.times = [7, 2, 5]

    def running(self):
        index = TrafficLight.modes.index(self.__color)
        while True:
            print(TrafficLight.modes[index])
            time.sleep(self.times[index])
            if index == len(TrafficLight.modes) - 1:
                switch = input('Продолжаем? Если да нажмите Enter, если нет то что нибудь напишите')
                if switch:
                    break
                else:
                    index = 0
                    continue
            index += 1


traffic = TrafficLight()
traffic.running()
