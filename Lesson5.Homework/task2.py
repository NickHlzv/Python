with open('file2.txt', 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1
        print(f'В строке {count} число слов = {len(line.split())} ')
    print(f'Число строк в файле: {count}')
