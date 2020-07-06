# 5. Извлечь все слова, начинающиеся на гласную
# AV is largest Analytics community of India
import re

result = re.findall(r'\b[eyuioa]\w+', r'AV is largest Analytics community of India',
                    flags=re.IGNORECASE)
print(result)