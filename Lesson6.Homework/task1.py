import time


class traffic_light:
    modes = ['Красный', 'Желтый', 'Зеленый']
    times = [7, 2, 5]

    def __init__(self, _color='Красный'):
        self._color = _color

    def running(self):
        index = traffic_light.modes.index(self._color)
        switch = ''
        while True:
            print(traffic_light.modes[index])
            time.sleep(traffic_light.times[index])
            if index == len(traffic_light.modes) - 1:
                switch = input('Продолжаем? Если да нажмите Enter, если нет то что нибудь напишите')
                if switch:
                    break
                else:
                    index = 0
                    continue
            index += 1


traffic = traffic_light('Зеленый')
traffic.running()
