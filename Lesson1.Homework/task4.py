user_number = input('Введите целое положительное число')
maximum = 0
if not user_number.isdigit():
    print('Вы издеваетесь? Число должно быть целым и положительным')
elif int(user_number) > 0:
    list_user_number = list(user_number)
    for number in list_user_number:
        if maximum < int(number):
            maximum = int(number)
    print(maximum)
else:
    print('Вы издеваетесь? Число должно быть целым и положительным')
