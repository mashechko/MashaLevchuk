import random

# 1. Найти max число в списке с помощью lambda.

list = []
for _ in range(10):
    list.append(random.randint(1, 10))

print(list)

func_1 = lambda x: max(x)
print(func_1(list))