# Задание 10 Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена. Добавить валидацию в
# конструкторе на ввод корректных данных. Создать иерархию ошибок.


class Book:
    def __init__(self, pages, year, author, price):
        if isinstance(pages, int) and isinstance(year, int):
            self.pages = pages
        else:
            raise TypeError('Неверно указано число страниц')
        if isinstance(year, int):
            self.year = year
        else:
            raise TypeError('Неверно указан год')
        if isinstance(author, str) and author[0].isupper():
            self.author = author
        else:
            raise TypeError('Неверно указан автор')
        try:
            self.price = float(price)
        except ValueError:
            print('Неверный формат')


book = Book(50, 2001, 'Masha', '5')
