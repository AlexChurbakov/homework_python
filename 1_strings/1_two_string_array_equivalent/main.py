"""
На вход даны два массива строк array_string_1 и array_string_2,
верните True, если они представляют одинаковые строки, и False в противном случае.
Пример:
1) array_string_1 = ['ab', 'c'], array_string_2 = ['a', 'bc'] => 'abc' == 'abc' (True)
1) array_string_1 = ['ab'], array_string_2 = ['a', 'bc'] => 'ab' != 'abc' (False)

Решение необходимо написать в функции, предоставленной ниже. Функция должна возвращать bool значение.
Строки в верхнем и нижнем регистре с одинаковыми символами считаются совпадающими.
Для проверки установите все необходимые библиотеки из файла requirements.txt и выполните команду из корня проекта:
pytest ./1_two_string_array_equivalent/test.py
"""
def is_array_string_are_equal(array_string_1: list[str], array_string_2: list[str]) -> bool:
    str1 = ""
    str2 = ""
    for element in array_string_1:
        str1 = str1 + element
    for element in array_string_2:
        str2 = str2 + element
    up1 = str1.upper()
    up2 = str2.upper()

    print(up1, "   ", up2)
    if up1 == up2:
        return True
    else: return False

