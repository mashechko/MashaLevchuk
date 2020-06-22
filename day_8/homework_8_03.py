# 3. Дан файл, содержащий различные даты. Каждая дата - это число, месяц и год. Найти самую раннюю дату.
import datetime
with open('dates.txt', 'r') as f:
    data = f.read().split()
min_date = datetime.datetime.strptime(data[0], '%d.%m.%Y')

for line in data:
    if datetime.datetime.strptime(line, '%d.%m.%Y') < min_date:
        min_date = datetime.datetime.strptime(line, '%d.%m.%Y')

print(min_date)
