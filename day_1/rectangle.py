from math import sqrt
a = int(input("Введите стороны треугольника: "))
b = int(input())
c = int(input())

p = (a + b + c) / 2

space = sqrt(p * (p - a) * (p - b) * (p - c))
print(f'Площадь треугольника равна {space}')