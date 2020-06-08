# 3. С помощью анонимной функции извлеките из списка числа, делимые на 15.
list = [45, 48, 78, 96]


def fltr(list):
    new_list = []
    for item in list:
        if item % 15 == 0:
            new_list.append(item)
    return new_list


print(fltr(list))

# new_list = filter(lambda x: x % 15 ==0, list)
