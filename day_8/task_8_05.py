# 5. Имеется текстовый файл. Все четные строки этого файла записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.
with open('some_text.txt', 'r') as f:
    data = f.readlines()

for index, line in enumerate(data):
    if (index + 1) % 2 == 0:
        with open('even.txt', 'a') as f:
            f.write(line)
    else:
        with open('odds.txt', 'a') as f:
            f.write(line)

