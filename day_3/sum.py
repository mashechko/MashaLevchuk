l_1 = ['1']  # 1 копейка (рубль)
l_2 = ['2', '3', '4']  # 2, 3, 4 копейки (рубля)
l_3 = ['5', '6', '7', '8', '9', '0']  # 5, 6, 7, 8, 9, 0 копеек (рублей)


def print_rub(number):
    if number > 0:
        if str(number)[-1] in l_1:
            word = 'рубль'
        elif str(number)[-1] in l_2:
            word = 'рубля'
        elif str(number)[-1] in l_3:
            word = 'рублей'
        else:
            number, word = '', ''
    return f'{number} {word}'


def print_cop(number):
    if number > 0:
        if str(number)[-1] in l_1:
            word = 'копейка'
        elif str(number)[-1] in l_2:
            word = 'копейки'
        elif str(number)[-1] in l_3:
            word = 'копеек'
    else:
        number, word = '', ''
    return f'{number} {word}'


sum = input("Введите сумму: ")


