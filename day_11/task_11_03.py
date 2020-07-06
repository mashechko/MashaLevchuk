# 3. вернуть список доменов из списка адресов электронной почты
# abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz
import re

result = re.findall(r'@(\w+\.\w+)', r'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, '
                                  r'first.test@rest.biz')
print(result)
