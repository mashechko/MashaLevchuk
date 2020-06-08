# 2. Нужно проверить, все ли числа в последовательности уникальны.

def unique(sequense):
    """
    Возвращает True, если все элементы последовательности уникальны
    """
    if len(sequense) == len(set(sequense)):
        return True
    else:
        return False


print(unique([45, 48, 78, 96]))
print(unique([45, 48, 48, 96]))
