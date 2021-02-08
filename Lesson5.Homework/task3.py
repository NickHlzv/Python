with open('file3.txt', 'r', encoding='utf-8') as f:
    data = {}
    for line in f:
        data.update({line.split()[0]: line.split()[1]})
sum = 0
for k, v in data.items():
    sum += float(v)
    if float(v) < 20000:
        print(k)
print(sum/len(data))
