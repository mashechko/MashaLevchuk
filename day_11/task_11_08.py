# 8. Создать скрипт, который при запуске принимает неопределенное количество аргументов и считает сумму тех из них,
# что являются цифрами


def counter():
    sum = 0
    args = []
    print("Чтобы прекратить ввод введите 'quit'")
    while True:
        arg = input("Введите аргумент: ")
        if arg == 'quit':
            break
        args.append(arg)

    for item in args:
        if item.isdigit():
            sum += int(item)

    return sum


result = counter()
print(result)
