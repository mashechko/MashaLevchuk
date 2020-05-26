# 4. Создать строку равную введенной строку без последних двух символов
str_in = input('Введите строку: ')
try:
    str_out = str_in[:(len(str_in)-2)]
    print(str_out)
except IndexError:
    print('Недостаточный размер строки')