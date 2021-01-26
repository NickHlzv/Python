months = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
number = input('Введите номер месяца целым числом')
while not number.isdigit():
    number = input('Прошу же число. Введите: ')
else:
    number = int(number)
if 0 < number <= 12:
    print(months[number-1])
else:
    print('нет месяца с таким номером')
