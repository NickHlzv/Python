input_str = input('Введите строку разделяя ее пробелами: ')
words = input_str.split()
for i, word in enumerate(words):
    print(f'{i+1} {word[:10]}')
