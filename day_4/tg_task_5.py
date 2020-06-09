from .tg_task_8 import function_8


# 5. Найти наименьшее общее кратное (НОК) пар целых положительных чисел через наибольший общий делитель (НОД) по
# формуле lcm = ab / gcd(a; b), где lcm - НОК, gcd - НОД, a и b - числа.
def function_5(a, b):
    """
    Наименьшее общее кратное пар чисел
    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: наименьшее общее кратное
    :rtype: int
    """
    lcm = int(a * b / function_8(a, b))
    return lcm
