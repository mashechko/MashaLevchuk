# 9. Создать скрипт, который принимает имя папки и создает ее рядом со скриптом


def create_directory(directory_name):
    import os

    path = os.getcwd()
    print(f"Текущая директория для создания папки: {path}")
    new_path = f'{path}\\' + directory_name

    try:
        os.mkdir(new_path)
    except OSError:
        print("Не удалось создать папку")
    else:
        print("Папка создана")


create_directory('my_directory')
