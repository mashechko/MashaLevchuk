# 8. Написать функцию, вычисляющую наибольший общий делитель
def function_8(a, b):
    """
    Функция, вычисляющая наибольший общий делитель
    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: наибольший общий делитель
    :rtype: int
    """
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gsd = a + b

    return gsd
