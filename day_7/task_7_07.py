# 7. Написать декоратор, который будет выводить время выполнения функции
import time
import random


def function_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения: {end - start}')
    return wrapper()


@function_time
def sleeping():
    time.sleep(3)


sleeping()