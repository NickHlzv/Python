def my_func(word):
    result = ''.join(word[0].upper() + word[1:])
    return result


in_str = input('Введите строку: ').split()
print(' '.join(my_func(word) for word in in_str))
