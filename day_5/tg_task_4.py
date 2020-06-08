import random


# 4. Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
def unique_items(list_1, list_2):
    list_1 = set(list_1) - set(list_2)
    return list_1


first_list, second_list = [], []
for _ in range(random.randint(1, 20)):
    first_list.append(random.randint(1, 100))
for _ in range(random.randint(1, 20)):
    second_list.append(random.randint(1, 100))

print(first_list, second_list, sep='\n')
print(unique_items(first_list, second_list))
