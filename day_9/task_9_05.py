# 5. Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта.
# Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name


dog = Dog('100sm', '15kg', 'Bob', '5')
print(f"Name: {dog.name}, age: {dog.age}. Bob's height: {dog.height}, Bob's weight: {dog.weight}")
dog.change_name('Boby')
print(dog.name)
