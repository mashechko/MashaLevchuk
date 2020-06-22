# 3. В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.
with open('input_text.txt', 'a') as f:
    for _ in range(3):
        data = input() + '\n'
        f.write(data)

with open('input_text.txt', 'r') as f:
   data = f.readlines()

for line in data:
    print(ascii(line))