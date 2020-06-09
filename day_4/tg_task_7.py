# 7. Написать функцию, которая переводит число из десятичной системы счисления в двоичную или восьмеричную
def function_7(number_10, base):
    """
    Перевод десятичного числа в двоичную или восьмеричную систему счисления
    :param number_10: число в десятичной системе счисления
    :param base: основание системы счисления
    :return:
    """
    number_2_8 = []
    if base == 2:
        while number_10:
            number_2_8.append(str(number_10 % 2))
            number_10 //= 2
    elif base == 8:
        while number_10:
            number_2_8.append(str(number_10 % 8))
            number_10 //= 8
    else:
        print('Неверное основание системы счисления')
    return ''.join(number_2_8[::-1])