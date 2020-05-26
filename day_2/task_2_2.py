# 2.	Создать строку равную предпоследнему символу введенной строки
str_in = input('Введите строку: ')
try:
    str_out = str_in[-2]
    print(str_out)
except IndexError:
    print('Недостаточный размер строки')