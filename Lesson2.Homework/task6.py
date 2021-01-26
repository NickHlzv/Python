stock_count = input('Введите количество товаров целым числом: ')
while not stock_count.isdigit():
    stock_count = input('Введите целое число уже: ')
else:
    stock_count = int(stock_count)
print(stock_count)
stock_list = []
name_values = []
price_values = []
count_values = []
metric_values = []
for i in range(1, stock_count+1):
    name = input(f'Введите название {i}го товара: ')
    price = input(f'Введите цену {i}го товара: ')
    count = input(f'Введите количество {i}го товара: ')
    metric = input(f'Введите единицы измерения {i}го товара: ')
    stock = {'название': name,
             'цена': price,
             'количество': count,
             'ед': metric
             }
    enumerate_stock = (i, stock)
    stock_list.append(enumerate_stock)
    name_values.append(name)
    price_values.append(price)
    count_values.append(count)
    metric_values.append(metric)
    print(stock_list[i-1])
data_values = [name_values, price_values, count_values, metric_values]
result = {}
keys = list(stock.keys())
for i in range(0, len(stock)):
    result.update({keys[i]: data_values[i]})
    print(keys[i], result[keys[i]])
print(result)
