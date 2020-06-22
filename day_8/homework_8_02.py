# 2. Создать csv файл с данными о ежедневной погоде. Структура:  Дата, Место, Градусы, Скорость ветра. Найти среднюю
# погоду(скорость ветра и градусы) для Минск за последние 7 дней.
import csv
import datetime

today = datetime.datetime.now()
after = today + datetime.timedelta(days=7)
data = []
with open('weather.csv', 'r') as f:
    degree, speed = 0, 0
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        if row['Место'] == 'Минск' and today <= datetime.datetime.strptime(row['Дата'], '%d.%m.%Y') <= after:
            degree += int(row['Градусы'])
            speed += float(row['Скорость ветра'].replace(',', '.'))
    average_degree = degree / 7
    average_speed = speed / 7

print(f'Средняя температура: {average_degree}. Средняя скорость ветра: {average_speed}')
