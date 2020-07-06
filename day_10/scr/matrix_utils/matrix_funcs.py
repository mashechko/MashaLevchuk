def max_el(matrix):
    max_el = matrix.data[0][0]
    for line in matrix.data:
        for element in line:
            if element > max_el:
                max_el = element

    return max_el


def min_el(matrix):
    min_el = matrix.data[0][0]
    for line in matrix.data:
        for element in line:
            if element < min_el:
                min_el = element

    return min_el


def sum_el(matrix):
    sum_el = 0
    for line in matrix.data:
        for element in line:
            sum_el += element

    return sum_el