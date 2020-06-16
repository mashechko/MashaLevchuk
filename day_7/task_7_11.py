# 11. Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный
def mirror(func):
    def wrapper(details, **kwargs):
        data = {}
        for key, value in kwargs.items():
            data[key] = value * details
        func(details, **data)
    return wrapper

def second(func):
    def wrapper(**kwargs):
        data = {}
        for key, value in kwargs.items():
            data[key] = 0 if value % 3 == 0 else value
        func(**data)
    return wrapper


@second
@mirror
def function(*args, **kwargs):
    print(kwargs)


function(details=5, a=1, b=2, c=3, d=4)

