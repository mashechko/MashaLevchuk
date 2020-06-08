import random


# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями. Найти сумму всех элементов матрицы,
# которые кратны 3.
n = int(input('Введите размер матрицы: '))
matr = []
for i in range(n):
    list = []
    for j in range(n):
        list.append(random.randint(1, 100))
    matr.append(list)

print('Исходная матрица:')
for l in matr:
    print(l)

sum = 0
for i in range(len(matr)):
    for j in matr[i]:
        if j % 3 == 0:
            sum += j

print(f'Сумма элементов матрицы кратных 3: {sum}')