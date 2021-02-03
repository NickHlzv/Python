from functools import reduce
lst = [num for num in range(100, 1001) if num % 2 == 0]
print(reduce(lambda el, next_el: el*next_el, lst))
