# 2. Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

func_2 = lambda x: f'Hello, {x}'

name = input("Введите имя: ")
print(func_2(name))