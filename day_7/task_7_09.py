# 9. Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов и выводит словарь
# с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
from functools import reduce

func_9 = reduce(lambda x, y: dict(f'{y}{y}', x), )

print(func_9())

