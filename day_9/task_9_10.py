# 10. Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet. Удалить в дочерних классах те методы, которые имеются у родительского
# класса. Создать объект каждого класса и вызвать все его методы.
class Pet:
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


class Dog(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @classmethod
    def bark(cls):
        print('Woof!')

class Cat(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @classmethod
    def meow(cls):
        print('Meow!')


class Parrot(Pet):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    @classmethod
    def fly(cls):
        print('Fly!')


dog = Dog('Tosha', 15, 'Masha')
print(f"{dog.name}'s age: {dog.age}")
dog.bark()
dog.jump()
dog.run()
dog.birthday()
print(f"{dog.name}'s age: {dog.age}")
cat = Cat('Kot', 5, 'Masha')
cat.meow()
parrot = Parrot('Kesha', 1, 'Masha')
parrot.fly()
