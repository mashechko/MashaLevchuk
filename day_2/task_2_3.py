# 3. Создать строку равную первым пяти символам введенной строки
str_in = input('Введите строку: ')
try:
    str_out = str_in[:5]
    print(str_out)
except IndexError:
    print('Недостаточный размер строки')