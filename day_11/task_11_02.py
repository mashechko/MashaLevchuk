# 2. Вернуть первые два символа каждого слова
# AV is largest Analytics community of India
import re

result = re.findall(r'\b\w\w', r'AV is largest Analytics community of India')
print(result)
