# Задание 9
# Унаследовать от класса Pet два класса: Horse, Donkey. Переопределить в классах методы voice.
# Создать класс Mule. Метод voice должен быть унаследован от класса Donkey


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


class Horse(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @staticmethod
    def voice():
        print("Horse's neighing")


class Donkey(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @staticmethod
    def voice():
        print('Iaa')


class Mule(Donkey, Horse):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)


horse = Horse('Tosha', 15, 'Masha')
donkey = Donkey('Kot', 5, 'Masha')
mule = Mule('Kesha', 1, 'Masha')


def voices(pets):
    """
    Принимает список животных и вызывает функцию voice

    :param pets: список животных
    :type pets: list
    """
    for pet in pets:
        pet.voice()


voices([horse, donkey, mule])
