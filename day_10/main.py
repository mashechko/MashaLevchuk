# Задание 14
# Создать пакет следующей структуры:
# src/
# -matrix_utils/
# --matrix_classes.py
# --matrix_funcs.py
# -main.py


from MashaLevchuk.day_10.scr.matrix_utils import matrix_classes, matrix_funcs
# Задание 15 Создать класс Matrix. Атрибуты - data(содержит саму матрицу - список списков), n, m. Определить
# конструктор(с параметрами(передача размерности: n, m и диапазона случайных чисел: a, b), по-умолчанию(матрица 5 на
# 5 где все элементы равны нулю), копирования) , переопределить магический метод __str__ для красивого вывода.
# Описать функции, которые принимают на вход объект класса Matrix. Функции позволяют искать максимальный элемент
# матрицы, минимальный, сумму всех элементов. Создать в файле main.py матрицу. Воспользоваться всеми описанными
# функциями и методами


matrix_zero = matrix_classes.Matrix()
matrix_int = matrix_classes.Matrix(3, 5, 1, 9)
print(matrix_int.data)
print(matrix_funcs.sum_el(matrix_int))
print(matrix_funcs.max_el(matrix_int))
print(matrix_funcs.min_el(matrix_int))
