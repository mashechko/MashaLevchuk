# 6. lambda, Дан список чисел. Найти произведение всех чисел, которые кратны 3.
import random
from functools import reduce

numb = []
for _ in range(10):
    numb.append(random.randint(1, 10))

numb_3 = reduce(lambda x, y: x * y, list(filter(lambda x: x % 3 == 0, numb)))

print(numb_3)
print(numb)

