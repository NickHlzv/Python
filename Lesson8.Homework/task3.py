class Number_valid(ValueError):
    @staticmethod
    def validation(value):
        if not value.isdigit():
            raise Number_valid
        else:
            return value


user_val = None
result = []
while user_val != 'stop':
    user_val = input('Введите значение')
    try:
        result.append(int(Number_valid.validation(user_val)))
    except Number_valid:
        print('В список вносятся только числовые данные')
print(result)
