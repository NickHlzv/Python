def sum_2(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        in_data = [a, b, c]
        in_data.remove(min(in_data))
        return sum(in_data)
    else:
        return 'В функцию sum_2 можно передавать только данные типа int и float'


print(sum_2(19.6, 15, 52.4124))
