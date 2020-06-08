import random


# Написать игру. Пользователь должен угадать число. Сперва вводиться диапазон угадывания. После колличество попыток.
# В случае правильного ответа - выводить You are the winner. В случае неправильного давать игроку подсказку(больше
# или меньше искомое число). Если за указанное количество попыток число не угадано - выводить: You are the loser
# и правильное число.

def guess_number():
    ot = int(input('От: '))
    do = int(input('До: '))
    try_number = int(input('Введите количество попыток: '))
    number = random.randint(ot, do)
    while try_number:
        guess = int(input('Угадайте число: '))
        if number == guess:
            print('You are winner')
            break
        elif number > guess:
            print('Загаданное число больше')
        elif number < guess:
            print('Загаданное число меньше')
        try_number -= 1
    else:
        print(f'You are loser {number}')


guess_number()