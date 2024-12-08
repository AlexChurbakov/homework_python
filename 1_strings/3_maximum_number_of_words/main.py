"""
Вам дан список предложений.
Предложение содержит только слова, которые разделены единичными пробелами.
Необходимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    i = 1
    max_i = 0
    for sentenc in sentences:
        for word in sentenc:
            if word == ' ':
                i += 1
            if max_i < i:
                max_i = i
        i = 1
    return max_i