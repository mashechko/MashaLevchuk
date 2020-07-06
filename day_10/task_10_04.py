# Задание 4
# Добавить в класс Pet пустой метод voice. Заменить имена методов bark, meow на voice. Добавить voice для класса Parrot.
# Создать функцию, принимающая список животных и вызывающая у каждого животного метод voice.


class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    @staticmethod
    def jump(m):
        print(f'Jump {m} meters')

    @staticmethod
    def run():
        print('Run!')

    @staticmethod
    def sleep():
        print('Time to sleep...')

    @staticmethod
    def voice():
        pass

    def birthday(self):
        self.age += 1


class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @staticmethod
    def voice():
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
    def voice():
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
    def voice():
        print('AAAAAAA')

    @staticmethod
    def jump(m):
        if m <= 0.05:
            print(f'Jump {m} meters')
        else:
            print('Parrots cannot jump so high')


dog = Dog('Tosha', 15, 'Masha')
cat = Cat('Kot', 5, 'Masha')
parrot = Parrot('Kesha', 1, 'Masha')


def voices(pets):
    """
    Принимает список животных и вызывает функцию voice

    :param pets: список животных
    :type pets: list
    """
    for pet in pets:
        pet.voice()


voices([dog, cat, parrot])