# 12. Дан файл, в котором через пробел записаны натуральные числа. Вывести на экран суммы цифр каждого числа.

with open('numbers.txt', 'r') as f:
    data = f.read()

numbers_list = data.split()
print(numbers_list)

sum_numbers = []
for number in numbers_list:
    sum = 0
    for element in number:
        sum += int(element)
    sum_numbers.append(f'{number} -> {sum}')

print(sum_numbers)