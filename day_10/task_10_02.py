# Задание 2
# Добавить метод jump, принимающий высоту прыжка. Метод выводит сообщение “Jump X meters”
# Переопределить метод jump в дочерних классах. Если передать методу jump класса dog значение больше 0.5,
# выводить сообщение “Dogs cannot jump so high, аналогично для кошек(2), для попугаев(0.05)


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
dog.jump(5)
dog.jump(0.1)
cat.jump(1)
parrot.jump(1)
