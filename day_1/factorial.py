number = int(input('Факториал какого числа считать? '))


i, result = 1, 1
while i < number:
    i += 1
    result *= i

print(result)