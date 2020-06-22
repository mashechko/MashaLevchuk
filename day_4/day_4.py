import random

# list = []
# for _ in range(11):
#     list.append(random.randint(1, 10))
#
# print(list)
# sum = 0
# for item in list:
#     sum += item
#
# print(sum)
#
#
# def result(a, b):
#     """
#     Sum a and b
#     :param a: firs number
#     :type a: int
#     :param b: second number
#     :type b: int
#     :return:
#     :rtype: int
#     """
#     return a + b
#
#
# print(result(5, 61))
#
# def calculator(a, b, action, order=True):
#     """
#
#     :param a: first number
#     :type a: int
#     :param b: second second number
#     :type b: int
#     :param action: what to do
#     :type action: str
#     :return: int
#     """
#     if not order:
#         a, b = b, a
#     if action == "+":
#         result = a + b
#     elif action == "-":
#         result = a - b
#     elif action == "*":
#         result = a * b
#     elif action == "/":
#         try:
#             result = a / b
#         except ZeroDivisionError:
#             result = "Нельзя делить на 0"
#     else:
#         "Неверный формат даных"
#     return result
#
#
# print(calculator(5, 18, "/", False))
# print(calculator(5, 0, "/"))

matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# result = matrix[0][1]
# for i in range(len(matrix)):
#     if matrix[i][1] > result:
#         result = matrix[i][1]
#
# print(result)
#
#
# def max_matrix(matrix, index, search=True):
#     """
#     Return max element of matrix[index]
#     :param matrix: matrix
#     :type matrix: list
#     :param index:
#     :type index: int
#     :return: max element
#     :rtype: int
#     """
#     try:
#         result = max(matrix[index])
#     except IndexError:
#         print("Недостаточная ширина матрицы")
#
#     if not search:
#         result = 0
#         try:
#             for i in range(len(matrix)):
#                 if matrix[i][index] > result:
#                     result = matrix[i][index]
#         except IndexError:
#             print("Недостаточная ширина матрицы")
#     return result
#
#
# print(max_matrix(matr, 1))
#
# def max_and_min(matrix):
#     max_el = 0
#     for i in range(len(matrix)):
#         for item in matrix[i]:
#             if item > max_el:
#                 max_el = item
#     min_el = max_el
#     for i in range(len(matrix)):
#         for item in matrix[i]:
#             if item < min_el:
#                 min_el = item
#     return f'Максимальный элемент: {max_el}, минимальный элемент: {min_el}.'
#
#
# print(max_and_min(matr))
#
# def replace_item(matrix, item_base, item_repl):
#     """
#
#     :param item_repl:
#     :param matrix:
#     :type matrix: list
#     :param item_base:
#     :type item_base: int
#     :return:
#     """
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == item_base:
#                 matrix[i][j] = item_repl
#     return matrix
#
#
# new_matr = replace_item(matr, 8, 0)
# for i in range(len(new_matr)):
#     print(new_matr[i])
#
# def repl_diag(matrix):
#     first_index = 0
#     second_index = len(matrix[0]) - 1
#     for i in range(len(matrix)):
#         matrix[i][second_index] = 0
#         second_index -= 1
#         matrix[i][first_index] = 1
#         first_index += 1
#     return matrix
#
# new_matr = repl_diag(matr)
# for i in range(len(new_matr)):
#     print(new_matr[i])
# def change_zero(matrix, average):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] < average:
#                 matrix[i][j] = 0
#     return matrix
#
#
# def change_one(matrix, average, max_el):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] > average and matrix[i][j] != max_el:
#                 matrix[i][j] = 1
#     return matrix
#
#
# def max_and_average(matrix):
#     max_el = 0
#     sum = 0
#     second_index = len(matrix[0]) - 1
#     for i in range(len(matrix)):
#         for item in matrix[i]:
#             if item > max_el:
#                 max_el = item
#                 sum += item
#     average = sum / (len(matrix) * len(matrix[0]))
#     new_matrix = change_zero(matrix, average)
#     new_matrix = change_one(new_matrix, average, max_el)
#     for i in range(len(matrix)):
#         if matrix[i][second_index] != max_el:
#             matrix[i][second_index] = random.randint(0, 10)
#             second_index -= 1
#     return new_matrix
#
#
# new_matr = max_and_average(matr)
# for i in range(len(new_matr)):
#     print(new_matr[i])

a = [
    [1, 7, 7],
    [5, 9, 7],
    [5, 5, 2]
]
b = [
    [9, 2, 2],
    [1, 5, 2],
    [1, 1, 4]
]


def replacement(matrix_1, matrix_2):
    index = 0
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            if matrix_1[i][j] == matrix_1[i][index]:
                if index < len(matrix_1[i]) - 1:
                    index += 1
                    continue
            matrix_1[i][j], matrix_2[i][j] = matrix_2[i][j], matrix_1[i][j]

    return matrix_1, matrix_2


print(replacement(a, b))
