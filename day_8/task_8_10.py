# 10. В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней
# символов и слов. Результат записать в другой файл.

with open('some_text.txt', 'r') as f:
    data = f.readlines()

len_strok = f' Количество строк в файле: {len(data)}'
with open('task_10.txt', 'w') as f:
    f.write(len_strok + '\n')

i = 1
for line in data:
    count_symbols = f'Строка {i}. Количество символов: {len(line)}, '
    count_words = f'количество слов: {len(line.split())}'
    with open('task_10.txt', 'a') as f:
        f.write(count_symbols)
        f.write(count_words + '\n')
    i +=1

with open('task_10.txt', 'r') as f:
    info = f.readlines()

for line in info:
    print(ascii(line))
