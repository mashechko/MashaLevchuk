# 6. Имеются два текстовых файла с одинаковым числом строк. Выяснить, совпадают ли их строки. Если нет, то получить
# номер первой строки, в которой эти файлы отличаются друг от друга.

with open('first_file.txt', 'r') as f:
   data_1 = f.readlines()

with open('second_file.txt', 'r') as f:
   data_2 = f.readlines()

if len(data_1) == len(data_2):
    for i in range(len(data_1)):
        if data_1[i] != data_2[i]:
            print(data_1[i], data_2[i])
            break
else:
    print('В файлах разное количество строк')
