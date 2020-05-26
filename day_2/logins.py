login = input('Введите логин: ')
if 1 <= len(login) <= 10:
    if login[:2] == 'io' and login[2:].isdigit():
        print('Correct')
    else:
        print('Incorrect')
else:
    print('Incorrect')