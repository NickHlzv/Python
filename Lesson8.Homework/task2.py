class Div_Zer(ZeroDivisionError):

    @staticmethod
    def div_vaild(number1, number2):
        try:
            res = number1 / number2
        except ZeroDivisionError:
            raise Div_Zer
        else:
            return res


try:
    print(Div_Zer.div_vaild(15, 0))
except Div_Zer:
    print('Нельзя на 0 делить')
