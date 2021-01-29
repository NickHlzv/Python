def pow1(x, y):
    if isinstance(x, (int, float)) and isinstance(y, int):
        return x ** y
    else:
        return 'в функции pow1 x может быть int и float, y должно быть int'


def pow2(x, y):
    if isinstance(x, (int, float)) and isinstance(y, int):
        if y > 0:
            pw = x
            for count in range(1, y):
                x *= pw
            return x
        elif y < 0:
            y *= -1
            pw = x
            for count in range(1, y):
                x *= pw
            return 1 / x
        else:
            return 1


print(pow1(2, -3))
print(pow2(2, -3))
