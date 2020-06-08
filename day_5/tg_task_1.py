from collections import Counter


# 1. Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
def search_words(text):
    """
    Принимает текст и выводит два слова: самое частое и длинное
    :param text: исходный текст
    :return: самое длинное и самое частое слово
    """
    words = {}
    for word in text.split():
        if word not in words:
            words[word] = 0
        words[word] += 1
    most_common = Counter(words).most_common()[0][0]

    longest = max(text.split(), key=len)
    return f'Самое частое слово: {most_common}. Самое длинное слово: {longest}'
