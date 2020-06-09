import random


# 4. С помощью функции заполнить матрицы случайными числами. Написать функцию, вычисляющую сумму двух матриц.
# Вывести на экран две исходные матрицы и их сумму
def function_4(matrix_1, matrix_2):
    """
    Сумма матриц
    :param matrix_1: первая матрица
    :type matrix_1: list
    :param matrix_2: вторая матрица
    :type matrix_2: list
    :return: сумма матриц
    :rtype: list
    """
    sum_matrix = []
    for i in range(len(matrix_1)):
        sum = []
        for j in range(len(matrix_1[i])):
            sum.append(matrix_1[i][j] + matrix_2[i][j])
        sum_matrix.append(sum)
    return sum_matrix


matr_1, matr_2 = [], []
for i in range(3):
    list = []
    for j in range(3):
        list.append(random.randint(1, 10))
    matr_1.append(list)

for i in range(3):
    list = []
    for j in range(3):
        list.append(random.randint(1, 10))
    matr_2.append(list)

print('Исходные матрицы')
for l, m in zip(matr_1, matr_2):
    print(l, m)

print('Сумма матриц')
new_matr = function_4(matr_1, matr_2)
for l in new_matr:
    print(l)
