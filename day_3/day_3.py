from math import sqrt
# [spam, ham] = ['yum', 'YUM']
# print(spam, ham)
# a = int(input('Первое число: '))
# b = int(input('Второе число: '))
# print(f'{a} плюс {b} равно {a + b}')
#
# string = 'Hello,_my_name_is_Alex'
# string_list = string.split('_')
# result = ' '.join(string_list)
# print(result)
#
# string = 'ping pong'
# result = string.replace('p', 'k')
# print(result)
#
# string = input('Предложение из двух слов: ')
# string_list = string.split()
# new_string = ' '.join(string_list[::-1])
# print(f'! {new_string} !')
#
# string = input("Введите предложение: ")
# if len(string) % 3 == 0 and len(string) > 0:
#     print(f'{string}!')
# elif len(string) == 0:
#     print('Пустая строка')
# else:
#     print(string)
#
# string = input("Введите предложение: ").split()
# if 'code' in string:
#     print('Yes')
# else:
#     print('No')
#
# age = int(input("Введите возраст: "))
# if age <= 0:
#     print('Wrong input')
# elif age < 18:
#     print('CocaCola')
# else:
#     print('Beer')
#
# string = input('Введите строку: ')
# if len(string) > 5:
#     print(string)
# elif len(string) < 5:
#     print('Need more')
# elif len(string) == 5:
#     print("It's five")
#
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# c = int(input("Введите c: "))
# d = b ** 2 - (4 * a * c)
# if d > 0:
#     x_1 = (-b + sqrt(d)) / (2 * a)
#     x_2 = (-b - sqrt(d)) / (2 * a)
#     print(f'Корни уравнения: {x_1} {x_2}')
# elif d == 0:
#     x = (-b + sqrt(d)) / (2 * a)
#     print(f'Корень один: {x}')
# else:
#     print('Нет корней')
#
# mail = input('Введите почтовый адрес: ')
# try:
#     if mail.split('@')[1] == 'gmail.com':
#         print(mail)
#     else:
#         print('domain name is not supported')
# except IndexError:
#     print('Неверный формат данных')

mail = input('Введите почтовый адрес: ')
symbols = ['-', '_', '.']
try:
    mail_list = mail.split("@")
    for i in mail_list[0]:
       if i.isalpha() or i.isdigit() or i in symbols:
           pass
    if mail_list[1][0] not in symbols and mail_list[1][-1]:
        for i in range(0, len(mail_list[1]) - 1):
            if mail_list[1][i] in symbols and mail_list[1][i+1] not in symbols:
                pass
except IndexError:
    print('Неверный формат данных')