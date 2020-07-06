# Задание 3
# Добавить в класс Perrot  новый атрибут – species


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


class Parrot(Pet):
    def __init__(self, name, age, master, species):
        super().__init__(name, age, master)
        self.species = species

    @staticmethod
    def fly():
        print('Fly!')

    @staticmethod
    def jump(m):
        if m <= 0.05:
            print(f'Jump {m} meters')
        else:
            print('Parrots cannot jump so high')

