# Задание 11
from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @abstractmethod
    def jump(self, m):
        """Jump X meters"""


class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def jump(self, m):
        if m <= 0.5:
            print(f'Jump {m} meters')
        else:
            print('Dogs cannot jump so high')


class Cat(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def jump(self, m):
        if m <= 2:
            print(f'Jump {m} meters')
        else:
            print('Cats cannot jump so high')


class Parrot(Pet):
    def __init__(self, name, age, master, species):
        super().__init__(name, age, master)
        self.species = species

    def jump(self, m):
        if m <= 0.05:
            print(f'Jump {m} meters')
        else:
            print('Parrots cannot jump so high')


dog = Dog('Tosha', 15, 'Masha')
cat = Cat('Kot', 5, 'Masha')
parrot = Parrot('Kesha', 1, 'Masha', 'Ara')
dog.jump(5)
dog.jump(0.5)
cat.jump(1)
parrot.jump(1)
