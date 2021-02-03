from itertools import count, cycle


def numbers(start: int, end: int):
    lst = []
    for i in count(start):
        lst.append(i)
        if i >= end:
            return lst


def repeater(lst, counter: int):
    iterator = 0
    for i in cycle(lst):
        lst.append(i)
        iterator += 1
        if iterator >= counter:
            return lst


c = len(numbers(3, 10))*2
print(repeater(numbers(3, 10), c))
