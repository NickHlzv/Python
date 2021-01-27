count = input('Введите размер списка: ')
while not count.isdigit():
    count = input('Размер списка может быть только целым числом. Прошу нормально вводить: ')
else:
    count = int(count)
lst = []
for el in range(1, count+1):
    lst_el = input(f'Введите {el}й элемент списка: ')
    lst.append(lst_el)
print(lst)
for i in range(0, count-1, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)
