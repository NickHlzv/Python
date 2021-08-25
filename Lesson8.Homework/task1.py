class Date:
    def __init__(self, string):
        self.value = string

    @classmethod
    def to_number(cls, date_str):
        try:
            number = int(''.join(date_str.split('-')))
            return number
        except ValueError:
            print("Некорректно дату вводим")

    @staticmethod
    def valid(date_str):
        date_lst = date_str.split('-')
        try:
            if len(date_lst) != 3:
                print('Дата некорректная, нужно ввести в формате dd-mm-yyyy. Дата автоматически приведется к формату')
                return '01-01-2001'
            if int(date_lst[0]) < 1 or int(date_lst[0]) > 31:
                date_lst[0] = '01'
                print('День должен быть от 1 до 31 включительно')
            if int(date_lst[1]) < 1 or int(date_lst[1]) > 12:
                date_lst[1] = '01'
                print('Месяц должен быть от 1 до 12 включительно')
            if int(date_lst[2]) < 0:
                date_lst[2] = '999'
                print('Год не может быть меньше 0')
            return '-'.join(date_lst)
        except ValueError:
            print("Некорректно дату вводим")


print(Date.to_number('01-01-2000'))
print(Date.valid('04-05-2001'))
