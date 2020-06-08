import random

# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.
n = int(input('Введите размер матрицы: '))
matr = []
for i in range(n):
    list = []
    for j in range(n):
        list.append(random.randint(1, 9))
    matr.append(list)

print('Исходная матрица:')
for l in matr:
    print(l)