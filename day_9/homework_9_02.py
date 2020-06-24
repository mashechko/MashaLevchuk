# 2. —оздать класс Car. јтрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0). ћетоды: увеличить скорости
# (скорость + 5), уменьшение скорости(скорость  - 5), стоп(сброс скорости на 0), отображение скорости, разворот
# (изменение знака скорости). ¬се атрибуты приватные.
class Car:
    def __init__(self, brand, model, year, speed=None):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = 0

    def speed_raise(self):
        self._speed += 5

    def speed_down(self):
        self._speed -= 5

    def stop(self):
        self._speed = 0

    def change_direction(self):
        self._speed *= (-1)
