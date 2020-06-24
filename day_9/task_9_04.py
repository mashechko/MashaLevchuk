# 4. Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run,
# bark. Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на
# экран все его атрибуты.
class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    @classmethod
    def jump(cls):
        print('Jump!')

    @classmethod
    def run(cls):
        print('Run!')

    @classmethod
    def bark(cls):
        print('Woof!')


dog = Dog('100sm', '15kg', 'Bob', '5')
print(f"Name: {dog.name}, age: {dog.age}. Bob's height: {dog.height}, Bob's weight: {dog.weight}")
dog.run()
dog.jump()
dog.bark()
