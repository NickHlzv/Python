def fact(n):
    result = 1
    for i in range(1, n):
        result *= i
        yield result


for el in fact(6):
    print(el)
