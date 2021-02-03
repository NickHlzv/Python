index = 0
lst = input('Введите числа через пробел. Если напишите не число то все пересчитатся только числа').split()
result = 0
while True:
    if len(lst) > 0:
        try:
            float(lst[index])
        except (ValueError, TypeError):
            break
        if index == len(lst) - 1:
            result += float(lst[index])
            lst = input('Введите еще числа через пробел, чтобы выйти напишите любой другой символ').split()
            index = 0
            continue
        else:
            result += float(lst[index])
        index += 1
    else:
        lst = input('Введите еще числа через пробел, чтобы выйти напишите любой другой символ').split()
print(result)
