user_number = input('Введите число')
if user_number.isdigit():
    second_number = user_number + user_number
    third_number = user_number + user_number + user_number
    result = int(user_number) + int(second_number) + int(third_number)
    print(result)
else:
    print('Опять ты за свое. Я хочу целое число')
