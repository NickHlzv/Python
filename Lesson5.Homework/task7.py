import json
with open('file7.txt', 'r', encoding='utf-8') as f:
    firms = {}
    average = 0
    count = 0
    for line in f:
        gain = float(line.split()[2])
        costs = float(line.split()[3])
        firms.update({line.split()[0]: gain - costs})
        if costs < gain:
            average += gain - costs
            count += 1
    average = average/count
    avg_dict = {'average_profit': average}
    result = [firms, avg_dict]
with open('data7.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
print(result)
