# 1. Вернуть первое слово из строки
# AV is largest Analytics community of India
import re

result = re.split(r'\W+', 'AV is largest Analytics community of India')[0]
print(result)



