inner = '25 10 15'
with open('file5.txt', 'w', encoding='utf-8') as f:
    f.write(inner)
with open('file5.txt', 'r', encoding='utf-8') as f:
    out = f.read().split()
    sum = 0
for el in out:
    sum += int(el)
print(sum)
