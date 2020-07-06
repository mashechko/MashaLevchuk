# 10. Дописать скрипт. Программа принимает имя папки и имя файла. Создает папку и создает в ней файл.


def create_directory_and_file(directory_name, file_name):
    import os

    path = os.getcwd()
    print(f"Текущая директория для создания папки: {path}")
    dir_path = f'{path}\\' + directory_name

    try:
        os.mkdir(dir_path)
    except OSError:
        print("Не удалось создать папку")
    else:
        print("Папка создана")

    file_path = f'{dir_path}\\' + file_name

    try:
        with open(file_path, 'w'):
            pass
    except:
        print("Не удалось создать файл")
    else:
        print("Файл создан")


create_directory_and_file('my_directory', 'new_file.txt')
