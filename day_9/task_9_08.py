# 8. Сделать все атрибуты класса Dog приватными. Сделать для каждого атрибута getter и setter используя декораторы.
# Все change методы удалить
class Dog:
    def __init__(self, height, weight, name, age):
        self._height = height
        self._weight = weight
        self._name = name
        self._age = age

    height = property()
    weight = property()
    name = property()
    age = property()

    @height.getter
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @weight.getter
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @age.getter
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


dog = Dog('100sm', '15kg', 'Bob', '5')
print(f"Name: {dog._name}, age: {dog._age}. Bob's height: {dog._height}, Bob's weight: {dog._weight}")