# Задание 6
# Добавить в класс Pet атрибут counter = 0, значение которого увеличивается при создании любого объекта.


class Pet:
    counter = 0

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
        Pet.counter += 1


    @staticmethod
    def jump(m):
        print(f'Jump {m} meters')

    @staticmethod
    def run():
        print('Run!')

    @staticmethod
    def sleep():
        print('Time to sleep...')

    def birthday(self):
        self.age += 1


class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @staticmethod
    def bark():
        print('Woof!')

    @staticmethod
    def jump(m):
        if m <= 0.5:
            print(f'Jump {m} meters')
        else:
            print('Dogs cannot jump so high')


class Cat(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @staticmethod
    def meow():
        print('Meow!')

    @staticmethod
    def jump(m):
        if m <= 2:
            print(f'Jump {m} meters')
        else:
            print('Cats cannot jump so high')


class Parrot(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @staticmethod
    def fly():
        print('Fly!')

    @staticmethod
    def jump(m):
        if m <= 0.05:
            print(f'Jump {m} meters')
        else:
            print('Parrots cannot jump so high')


dog = Dog('Tosha', 15, 'Masha')
cat = Cat('Kot', 5, 'Masha')
parrot = Parrot('Kesha', 1, 'Masha')

print(Pet.counter)