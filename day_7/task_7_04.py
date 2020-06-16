import random

# 4. lambda, Дан список чисел. Вернуть список, где каждый число переведено в строку [5, 3] -> [‘5’, ‘3’]

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 10))

print(numbers)

numbers = list(map(lambda x: str(x), numbers))
print(numbers)