int1 = 12
float1 = 1.4256
str1 = 'И снова здравствуй'
str2 = input('Введите Имя')
int2 = input('Введите целое число')
if int2.isdigit():
    print('{}, {}, {}, {}, {}'.format(int1, float1, str1, str2, int(int2)))
else:
    print('Ну елки зеленые просил же целое число')
