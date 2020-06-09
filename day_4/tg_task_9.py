# 9. Переставить по алфавиту буквы слов в строке
def function_9(text):
    """
    СОртировка букв в словах в тексте по алфавиту
    :param text: исхожный текст
    :type text: str
    :return: текст с отсортированными словами
    :rtype: str
    """
    words = []
    for word in text.split():
        words.append(''.join(sorted(word)))
    return ' '.join(words)