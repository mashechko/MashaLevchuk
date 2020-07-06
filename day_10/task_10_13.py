from abc import ABC, abstractmethod


class Feline(ABC):
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @abstractmethod
    def meow(self):
        """Кот мяукает"""


class Canine(ABC):
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @abstractmethod
    def bark(self):
        """Собака гавкает"""


class Dog(Canine):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        print(f'Woof! My name is {self.name}')


class Cat(Feline):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        print(f'Meow! My name is {self.name}')


dog = Dog('Tosha', 15, 'Masha')
cat = Cat('Kot', 5, 'Masha')

dog.bark()
cat.meow()