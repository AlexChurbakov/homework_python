import os
from decimal import Decimal
from unicodedata import decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    _ = get_employees_info()
    parsed_employees_info = []

    # Ваш код ниже
    for stroka in _:
        word_array = stroka.split(" ")
        person = {"id" : int, "name" : str, "last_name" : str, "age" : int, "position" : str, "salary" : decimal}
        print (word_array)
        key = 0
        for key, word in enumerate(word_array):
            match word:
                case "id":
                    person["id"] = int(word_array[key + 1])
                    print (person["id"])
                case "name":
                    person["name"] = word_array[key + 1]
                    print(person["name"])
                case "last_name":
                    person["last_name"] = word_array[key + 1]
                    print(person["last_name"])
                case "age":
                    person["age"] = int(word_array[key + 1])
                    print(person["age"])
                case "position":
                    person["position"] = word_array[key + 1]
                    print(person["position"])
                case "salary":
                    person["salary"] = Decimal(word_array[key + 1])
                    print(person["salary"])
            parsed_employees_info.append(person)
    return parsed_employees_info