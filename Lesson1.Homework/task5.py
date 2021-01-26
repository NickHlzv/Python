gain = input('Введите выручку')
costs = input('Введите издержку')
if not gain.isdigit() and not costs.isdigit():
    print('Опять ты не пойми что вводишь, а надо целое число')
elif int(gain) <= int(costs):
    print('Ваша контора не приносит прибыли или работает в убыток')
else:
    profitability = int(gain) / int(costs)
    print('Вы прибыльное предприятие. Ваша рентабленость равна {}'.format(profitability))
    employees = input('А теперь введите число сотрудников')
    while not employees.isdigit():
        employees = input('Может все таки введешь целое число: ')
    print(int(gain) - int(costs))
    gain_employee = (int(gain) - int(costs)) / int(employees)
    print('Прибыль на сотрудника равна: {}'.format(gain_employee))
