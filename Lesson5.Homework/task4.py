with open('file4.txt', 'r', encoding='utf-8') as f:
    data = []
    for line in f:
        data.append(line)
f.close()
data[0] = data[0].replace('One', 'Один')
data[1] = data[1].replace('Two', 'Два')
data[2] = data[2].replace('Three', 'Три')
data[3] = data[3].replace('Four', 'Четыре')
print(data)
with open('file4.txt', 'w', encoding='utf-8') as f:
    for i in range(len(data)):
        f.writelines(data[i])



