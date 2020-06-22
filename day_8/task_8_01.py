# 1. Имеется текстовый файл. Напечатать:
with open('some_text.txt', 'r') as f:
    data = f.readlines()
# a) его первую строку;
print(ascii(data[0]))
# b) его пятую строку;
print(ascii(data[4]))
# c) его первые 5 строк;
for i in range(5):
    print(ascii(data[i]))
# d) его строки с s1-й по s2-ю;
for i in range(2):
    print(ascii(data[i]))
# e) весь файл.
for line in data:
    print(ascii(line))

