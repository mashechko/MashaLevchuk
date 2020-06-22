# 1. Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст. Создать отчетный файл с информацией по
# количеству людей входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.
import csv
c_1, c_2, c_3, c_4, c_5 = 0, 0, 0, 0, 0

with open('homework_1.csv', "r") as csv_fd:
    reader = csv.DictReader(csv_fd, delimiter=';')
    for row in reader:
        if 1 <= int(row['age']) <= 12:
            c_1 += 1
        elif 13 <= int(row['age']) <= 18:
            c_2 += 1
        elif 19 <= int(row['age']) <= 25:
            c_3 += 1
        elif 26 <= int(row['age']) <= 40:
            c_4 += 1
        elif int(row['age']) > 40:
            c_5 += 1

information = f'Возрастная гурппа 1-12: {c_1} \nВозрастная гурппа 13-18: {c_2} \nВозрастная гурппа 19-25: {c_3} \n' \
              f'Возрастная гурппа 26-40: {c_4} \nВозрастная гурппа 40+: {c_5}'
print(information)

with open('people_info.txt', 'w') as f:
    f.write(information)