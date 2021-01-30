def my_func(word):
    result = ''.join([letter[0].upper() + letter[1:] for letter in word.split()])
    return result


in_str = input('Введите строку: ').split()
print(' '.join(my_func(word) for word in in_str))
