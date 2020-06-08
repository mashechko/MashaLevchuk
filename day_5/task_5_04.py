import random

#Дана целочисленная матрица А[n,m]. Посчитать количество элементов матрицы, превосходящих среднее арифметическое
# значение элементов матрицы и сумма индексов которых четна

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

def average(matrix):
    sum = 0
    for i in range(len(matrix)):
        for item in matrix[i]:
            sum += item
    average = sum / (len(matrix) * len(matrix[0]))
    return average


counter = 0
for i, ii in enumerate(matr):
    for j, jj in enumerate(matr[i]):
        if jj > average(matr) and (i + j) % 2 == 0:
            counter += 1

print(f'Среднее значение в матрице: {average(matr)}')
print(f'Количество элементов больше среднего с четной суммой индексов: {counter}')