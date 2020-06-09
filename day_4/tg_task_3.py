# 3. Возведение выражений в степень с натуральным показателем оформить в виде функции, как нахождение
# произведения одинаковых множителей. Не использовать стандартной математической функции
# вычисления степени.
def function_3(expression, degree):
    """
    Функция возведения в степень
    :param expression: выражение
    :param degree: степень
    :return:
    """
    result = 1
    for _ in range(degree):
        result *= expression
    return result


def function_3_1(x):
    """
    Программа вычисления  выражения: y = (x6*(x-5)3) / (2*x+1)5
    :param x: аргумент функции
    :return:
    """
    result = (function_3(x, 6) * function_3((x - 5), 3)) / function_3((2 * x + 1), 5)
    return result
