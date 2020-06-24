# 9. Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master. Каждый класс содержит
# конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep. Класс Parrot имеет дополнительный метод fly.
# Cat - meow, Dog - bark.
class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @classmethod
    def jump(cls):
        print('Jump!')

    @classmethod
    def run(cls):
        print('Run!')

    @classmethod
    def sleep(cls):
        print('Time to sleep...')

    def birthday(self):
        self.age += 1

    @classmethod
    def bark(cls):
        print('Woof!')


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @classmethod
    def jump(cls):
        print('Jump!')

    @classmethod
    def run(cls):
        print('Run!')

    @classmethod
    def sleep(cls):
        print('Time to sleep...')

    def birthday(self):
        self.age += 1

    @classmethod
    def meow(cls):
        print('Meow!')


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @classmethod
    def jump(cls):
        print('Jump!')

    @classmethod
    def run(cls):
        print('Run!')

    @classmethod
    def sleep(cls):
        print('Time to sleep...')

    def birthday(self):
        self.age += 1

    @classmethod
    def fly(cls):
        print('Fly!')
