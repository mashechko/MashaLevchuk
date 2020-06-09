import random

# 2. Описать функцию вычисления f(x) по формуле:
# f(x)= x^2 при -2<=x<2;
# x^2+4x+5 при x>=2;
# 4 при x<-2.
# Используя эту функцию для n заданных чисел, вычислить f(x).
# Среди вычисленных значений найти наибольшее.
def function_2(number):
    """Функция вычисления f(x) в зависимости от значения x"""
    if -2 <= number < 2:
        return number ** 2
    elif number >= 2:
        return number ** 2 + 4 * number + 5
    elif number < -2:
        return 4


function_2_list = []
function_2_result = []
for _ in range(11):
    function_2_list.append(random.randint(1, 10))
print(f'{function_2_list} - набор значений')

for number in function_2_list:
    function_2_result.append(function_2(number))
print(f'{function_2_result} - результат выполнения функции')

print(f'{max(function_2_result)} - наибольшее значение')