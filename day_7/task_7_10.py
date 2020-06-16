# 10. Создать декоратор для функции, которая принимает список чисел. Декоратор должен производить предварительную
# проверку данных - удалять все четные элементы из списка.
import random

numb = []
for _ in range(10):
    numb.append(random.randint(1, 10))


def odd_only(func):
    def wrapper(numbers):
        new_dict= {}
        for index, i in enumerate(numbers, start=1):
            new_dict[i] = index
        return func(new_dict)
    return wrapper


@odd_only
def numbers(numbers_list):
    return numbers_list


print(numbers(["a", "b", "c"]))