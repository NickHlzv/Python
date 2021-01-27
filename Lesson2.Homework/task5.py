my_list = [7, 5, 3, 3, 2]
new_elem = input('Введите новый элемент списка целым числом, для заврешения напишите любой другой символ')
while new_elem.isdigit():
    new_elem = int(new_elem)
    my_list.append(new_elem)
    my_list = sorted(my_list, reverse=True)
    print(my_list)
    new_elem = input('Введите новый элемент списка, для заврешения напишите любой другой символ')
