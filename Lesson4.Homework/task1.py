from sys import argv


def salary(hours, h_pay, award):
    return (float(hours) * float(h_pay)) + float(award)


if len(argv) == 4:
    print(salary(argv[1], argv[2], argv[3]))
else:
    print('Нужно выполнить через командную строку вида "python <путь до файла> <кол-во часов> <ставка> <премия>"')
