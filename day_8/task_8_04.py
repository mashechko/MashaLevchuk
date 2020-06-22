# 4. Имеется текстовый файл. Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.
with open('zero.txt', 'r') as f:  # Проверяем, какой файл был сначала
   print(f.readlines())

with open('zero.txt', 'r+') as f:
   data = f.readlines()

new_data = []
for i in range(len(data)):
   if '0' in data[i]:
      new_data.append(data[i].replace('0', '1'))
   elif '1' in data[i]:
      new_data.append(data[i].replace('1', '0'))

with open('new_zero.txt', 'w') as f:
   for i in range(len(new_data)):
      f.write(new_data[i])

with open('new_zero.txt', 'r') as f:  # Проверяем, произошла ли замена
   print(f.readlines())



