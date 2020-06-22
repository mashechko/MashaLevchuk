# 7. Создать матрицу случайных чисел и сохранить ее в json файл. После прочесть ее, обнулить все четные элементы и
# сохранить в другой файл
import random
import json


def create_matrix():
    n = int(input('Введите размер матрицы: '))
    matr = []
    for i in range(n):
        list = []
        for j in range(n):
            list.append(random.randint(1, 9))
        matr.append(list)
    return matr


matr_1 = create_matrix()
matr_2 = create_matrix()
matr_3 = create_matrix()

with open('matrix.json', 'w') as f:
    matr = {"matrix": {
        "matr_1": matr_1,
        "matr_2": matr_2,
        "matr_3": matr_3
    }
    }
    json.dump(matr, f)

with open('matrix.json', 'r') as f:
    data = json.load(f)["matrix"]

# for i in range(len(data)):
#     for j in range(len(data[i])):
#         if data[i][j] % 2 == 0:
#             data[i][j] = 0
#
# print(type(matr))
# with open('matrix_0.data', 'w') as f:
#     matix = {"matrix": data}
#     json.dump(matix, f)
#
# with open('matrix_0.data', 'r') as f:
#     data = json.load(f)["matrix"]

for line in data:
    print(line)
