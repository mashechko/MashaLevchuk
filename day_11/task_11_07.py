# 7. Создать бесконечный генератор случайных чисел. Использовать в генераторе временную задержку from time import sleep
import random
from time import sleep


def simple_generator():
    while True:
        sleep(1)
        yield random.randint(1, 1000)


get_iter = simple_generator()
for _ in range(10):
    print(next(get_iter))
