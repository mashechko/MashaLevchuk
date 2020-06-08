# Создать список учеников подобной структуры. Определить средний балл оценок по всем предметам, и вывести сведения о
# студентах, средний балл которых больше 4.

pupils = [
    {'firstname': 'Masha', 'Group': 42, 'physics': 7, 'informatics': 6, 'history': 8},
    {'firstname': 'Igor', 'Group': 42, 'physics': 9, 'informatics': 9, 'history': 10},
    {'firstname': 'Sveta', 'Group': 7, 'physics': 2, 'informatics': 2, 'history': 2},
    {'firstname': 'Misha', 'Group': 42, 'physics': 10, 'informatics': 8, 'history': 5},
    {'firstname': 'Olya', 'Group': 15, 'physics': 5, 'informatics': 10, 'history': 10}
]

print('Студенты со средним баллом больше 4: ')
for pupil in pupils:
    average = (pupil['physics'] + pupil['informatics'] + pupil['history']) / 3
    if average > 4:
        print(f"{pupil['firstname']}, группа {pupil['Group']}. Средний балл: {average}")