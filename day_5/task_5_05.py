# Создать список с фамилиями. Вывести все фамилии, которые начинаются на П и заканчиваются на а

list_of_lastnames = ['Павлова', 'Смирнов', 'Петриченко', 'Зайцев', 'Па']
for lastname in list_of_lastnames:
    if lastname[0] == 'П' and lastname[-1] == 'а':
        print(lastname)