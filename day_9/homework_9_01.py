# 1. Создать пять классов описывающие реальные объекты. Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.
class Human:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    name = property()
    age = property()
    gender = property()

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

    @gender.getter
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @staticmethod
    def say_hello():
        print('Hello, world!')

    def presentation(self):
        print(f'My name is {self._name}, I am {self._age} years old.')


class Planet:
    def __init__(self, name, radius):
        self._name = name
        self._radius = radius
        self._ispopulation = False
        self._population = 0

    name = property()
    radius = property()
    population = property()
    ispopulation = property()

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @radius.getter
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @population.getter
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @ispopulation.getter
    def ispopulation(self):
        return self._ispopulation

    @ispopulation.setter
    def ispopulation(self, value):
        self._ispopulation = value

    def raise_population(self, quantity=None):
        """Увеличивает популяцию на quantity, по умолчанию в два раза больше"""

        if quantity:
            self._population += quantity
        else:
            self._population *= 2

    def create_live(self):
        self._ispopulation = True


class Telephone:
    def __init__(self, brand, charge, number):
        self._brand = brand
        self._charge = charge
        self._number = number

    brand = property()
    charge = property()
    number = property()

    @brand.getter
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @charge.getter
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, value):
        self._charge = value

    @number.getter
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    def calling(self):
        print(f'Number {self._number} is calling...')

    def charge_down(self):
        self._charge -= 10
        if self._charge == 0:
            print('Пора зарядить телефон')


class Car:
    def __init__(self, brand, seats, fuel_rest):
        self._brand = brand
        self._seats = seats
        self._fuel_rest = fuel_rest

    brand = property()
    seats = property()
    fuel_rest = property()

    @brand.getter
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @seats.getter
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value

    @fuel_rest.getter
    def fuel_rest(self):
        return self._fuel_rest

    @fuel_rest.setter
    def fuel_rest(self, value):
        self._fuel_rest = value

    @classmethod
    def start_trip(cls):
        print('Поехали!')

    def fuel_flow(self):
        self._fuel_rest -= 10
        if self._fuel_rest == 20:
            print('Пора заправиться')


masha = Human('Masha', 19, 'female')
masha.say_hello()
masha.presentation()

earth = Planet('Earth', 6_371_302)
earth.create_live()
earth.raise_population(7_000_000_000)
print(earth._population)

tel = Telephone('Iphone', 100, '+375297873131')
tel.calling()
tel._charge = 10
tel.charge_down()

car = Car('Bugatti', 2, 30)
car.start_trip()
car.fuel_flow()