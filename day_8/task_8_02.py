# 2. Создать текстовый файл и записать в него 6 строк. Записываемые строки вводятся с клавиатуры.

with open('input_text.txt', 'w') as f:
    for _ in range(6):
        data = input() + '\n'
        f.write(data)

with open('input_text.txt', 'r') as f:
   data = f.readlines()

for line in data:
    print(ascii(line))