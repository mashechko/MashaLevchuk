import random
n = int(input("Введите размер матрицы: "))
matrix = []
for _ in range(n):
    list = []
    for _ in range(n):
        list.append(random.randint(1, 9))
    matrix.append(list)

print("Исходная матрица")
for st in matrix:
    print(st)

if len(matrix) == len(matrix[0]):
    k = 0
    for _ in range(len(matrix) // 2 + 1):
        for i in range(k, len(matrix) - k):
            matrix[k][i] = 0
            matrix[len(matrix) - 1 - k][i] = 0
            matrix[i][len(matrix) - 1 - k] = 0
            matrix[i][k] = 0
        k += 2
else:
    print("Это не квадратная матрица")

print("Измененная матрица")
for st in matrix:
    print(st)