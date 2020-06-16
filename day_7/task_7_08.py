# 8. lambda, Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i это порядковый номер строки
# в списке. Использовать генератор списков.
names = ['Masha', 'Sasha', 'Alex', 'Anton', 'Ivan']

def func_8(strings):
    new_list = []
    for index, item in enumerate(strings):
        new_list.append(f'{index} - {item}')
    return new_list


print(func_8(names))