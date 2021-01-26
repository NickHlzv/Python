kilos = input('Введите расстояние первой пробежки в километрах')
end_kilos = input('Введите конечную дистанцию в километрах')
while not kilos.isdigit() or not end_kilos.isdigit():
    kilos = input('Введите расстояние первой пробежки в километрах целым числом')
    end_kilos = input('Введите конечную дистанцию целым числом')
kilos = int(kilos)
end_kilos = int(end_kilos)
day_count = 1
while kilos < end_kilos:
    print('{}-й день: {}'.format(day_count, kilos))
    kilos *= 1.1
    day_count += 1
print('{}-й день: {}'.format(day_count, kilos))
