def pair_division(a, b):
    return a / b if b != 0 else 'Мы на 0 не делим'


a = input('Введите число a')
b = input('Введите число b')
if a.isdigit() and b.isdigit():
    print(pair_division(int(a), int(b)))
else:
    print('Числа должны быть целыми, попробуйте еще')
