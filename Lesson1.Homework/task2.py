user_time = input('Введите время в секундах')
if user_time.isdigit():
    user_time = int(user_time)
    hours = user_time // 3600
    minutes = (user_time % 3600) // 60
    seconds = user_time % 60
    print('{}:{}:{}'.format(hours, minutes, seconds))
else:
    print('Ну епрст просил же время ввести')
