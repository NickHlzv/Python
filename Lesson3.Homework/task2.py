def user_data(**params):
    values = ''
    for d_value in params.values():
        values += str(d_value) + ' '
    return values


print(user_data(name='Nick', last_name='Hlzv', age=23, city='Vrn', email='trabadur@mail.ru', phone='9812491258'))
