# Задание 5 Создать класс MyTime. Атрибуты: hours, minutes, seconds. Переопределить магические методы сравнения(
# равно, не равно), сложения, вычитания, вывод на экран. Перегрузить конструктор на обработку входных параметров
# вида: одна строка, три числа, другой объект класса MyTime. В остальных случаях создавать объект по-умолчанию(0-0-0)
import time
from datetime import timedelta

class MyTime():

    def __init__(self, string=None, h=None, m=None, s=None, obj=None):
        if string:
            t = time.strptime(string, "%H-%M-%S")
        elif h and m and s:
            t = time.strptime(f'{h}-{m}-{s}', "%H-%M-%S")
        elif obj:
            t = time.strptime(f'{obj.hours}-{obj.minutes}-{obj.seconds}', "%H-%M-%S")
        else:
            t = time.strptime(f'{0}-{0}-{0}', "%H-%M-%S")

        self.t = t
        self.hours = t.tm_hour
        self.minutes = t.tm_min
        self.seconds = t.tm_sec

    def __str__(self):
        return f'{self.hours}-{self.minutes}-{self.seconds}'

    def __eq__(self, other):
        return self.t == other.t

    def __ne__(self, other):
        pass

    def __add__(self, other):
        return self.t + timedelta(other)

    def __sub__(self, other):
        return self.t - timedelta(other)


mytime_1 = MyTime(string="23-06-21")
mytime_2 = MyTime(h="23", m="06", s="20")
mytime_3 = MyTime(obj=mytime_2)

print(mytime_1)
print(mytime_2)
print(mytime_3)
print(mytime_1 == mytime_2)