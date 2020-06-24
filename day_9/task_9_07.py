# 7. Добавить новый приватный атрибут адрес(по-умолчанию равен ‘Minsk’). Добавить getter и
# setter для адреса.
class Dog:
    def __init__(self, height, weight, name, age, master):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self._master = master
        self._address = 'Minsk'

    address = property()

    @address.getter
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value


dog = Dog('100sm', '15kg', 'Bob', '5', 'Masha')
print(f"Name: {dog.name}, age: {dog.age}. Bob's height: {dog.height}, Bob's weight: {dog.weight}")

dog.address = 'Grodno'
print(dog.address)
