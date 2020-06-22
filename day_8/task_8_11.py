# 11. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть
# служит пустая строка.

with open('input_text.txt', 'w') as f:
    while True:
        data = input()
        if data == '':
            break
        f.write(data + '\n')

with open('input_text.txt', 'r') as f:
   data = f.readlines()

for line in data:
    print(ascii(line))