# Задание 2.01
firstname = 'Маша'
lastname = 'Левчук'
age = '19'
print(f'Привет, меня зовут {firstname} {lastname}, мне {age} лет')

first_list = ['a', 'b', 42]
print(first_list)

first_list.append('last item')
first_list.insert(0, 'first item')
print(first_list)

second_list = ['a', 'b', 'c']
first_list.extend(second_list)
print(first_list)

print('True' if 'c' in first_list else 'False')

print(first_list.count('a'))

# Пузырьковая сортировка
random_list = [15, 26, 154, 159, 977, 45, 69]
for item in range(len(random_list) - 1):
    for i in range(len(random_list) - item - 1):
        if random_list[i] > random_list[i+1]:
            random_list[i], random_list[i+1] = random_list[i+1], random_list[i]

print(random_list)

dict = {"firstname": 'Маша', "lastname": 'Левчук', "age": '19'}
print(dict['firstname'])
print(dict.get('несуществующий элемент', 'not found'))

for key, value in dict.items():
    print(f'{key} - {value}')

# Задание 2.03
list = [1, 2]
tuple = (3, 4)


name = 'аша'
print('Это полиндром' if name == name[::-1] else 'Это не полиндром')

data = 'Sasha 4fdg3, Masha 23'
data = data.replace(',', ' ').split()
names, ages = [], []

s_age = ''
m_name = ''

age = ''
for item in data:
    for i in item:
        if i.isdigit():
            age += i
for i in range(0, len(data), 2):
    print(f'Name: {data[i]} {age[i:i+2]}')
print(age)