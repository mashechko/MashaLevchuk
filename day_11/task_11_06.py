# 6. Проверить телефонный номер (номер должен быть длиной 10 знаков и начинаться с 8 или 9)
# ['9999999999', '999999-999', '99999x9999']
import re

number_list = ['9999999999', '999999-999', '99999x9999']

for number in number_list:
    result = re.fullmatch(r'[89]\d{9}', number)
    print(f'{number} - YES' if result else f'{number} - NO')
