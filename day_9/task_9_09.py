# 9. ������� ��� ������: Dog, Cat, Parrot. �������� ������� ������: name, age, master. ������ ����� ��������
# ����������� � ������: run, jump, birthday(����������� age �� 1), sleep. ����� Parrot ����� �������������� ����� fly.
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
