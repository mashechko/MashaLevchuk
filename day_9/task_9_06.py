# 6. Добавить в метод инициализации новый приватный атрибут - master. Создать метод get_master() который возвращает
# значение атрибута master.
class Dog:
    def __init__(self, height, weight, name, age, master):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self._master = master

    def get_master(self):
        return self._master


dog = Dog('100sm', '15kg', 'Bob', '5', 'Masha')
print(f"Name: {dog.name}, age: {dog.age}. Bob's height: {dog.height}, Bob's weight: {dog.weight}")
print(dog._master)
