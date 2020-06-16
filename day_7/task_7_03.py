# 3. Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в
# другой список

names = ['Masha', 'Sasha', 'Alex', 'Anton', 'Ivan']

greetings = (list(map(lambda x: f'Hello, {x}', names)))

print(greetings)
for item in greetings:
    print(item)
