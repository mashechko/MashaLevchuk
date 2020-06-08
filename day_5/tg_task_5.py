from math import tan


# 5. Найти Y, если Y = X1 + X2 + … + Xn,   X = Z^3 - B + A^2 / tgX^2?. Количество X вводятся пользователем программы.
# Для каждого X значения Z, B, А, ? разные (вводятся пользователем программы).
def find_y(number_of_x):
    print('X = Z^3 - B + A^2 / tgC^2')
    y = 0
    for _ in range(number_of_x):
        a = int(input('Введите значение A: '))
        b = int(input('Введите значение B: '))
        z = int(input('Введите значение Z: '))
        c = int(input('Введите значение C: '))
        x = (z ** 3 - b + a ** 2) / tan(c) ** 2
        y += x

    return y


print(find_y(2))
