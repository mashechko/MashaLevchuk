import random

# Дан двумерный массив n × m элементов. Определить, сколько раз встречается число 7 среди элементов массива

w = int(input('Введите ширину матрицы матрицы: '))
h = int(input('Введите высоту матрицы матрицы: '))

matr = []
for i in range(h):
    list = []
    for j in range(w):
        list.append(random.randint(1, 100))
    matr.append(list)

print('Исходная матрица:')
for l in matr:
    print(l)

counter = 0
for i in range(len(matr)):
    for j in matr[i]:
        if j == 7:
            counter += 1

print(f'Количество семерок в матрице: {counter}')