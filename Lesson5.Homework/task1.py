with open('file1.txt', 'w', encoding='utf-8') as f:
    content = input('Введите текст для записи. Об окончании записи свидетельствует пустая строка')
    while content:
        f.writelines(content+'\n')
        content = input('Введите текст для записи. Об окончании записи свидетельствует пустая строка')
