from operator import truediv
def decode_numbers(numbers: str) -> str | None:
    """Пишите ваш код здесь."""
    numbers = numbers.split(" ")
    result = ""
    for number in numbers:
        if is_correct(number):
            pos = len(number)
            match pos:
                case 1:
                    match number[0]:
                        case "0":
                            result += " "
                        case "1":
                            result += "."
                        case "2":
                            result += "а"
                        case "3":
                            result += "д"
                        case "4":
                            result += "и"
                        case "5":
                            result += "м"
                        case "6":
                            result += "р"
                        case "7":
                            result += "ф"
                        case "8":
                            result += "ш"
                        case "9":
                            result += "ь"
                case 2:
                    match number[0]:
                        case "1":
                            result += ","
                        case "2":
                            result += "б"
                        case "3":
                            result += "е"
                        case "4":
                            result += "й"
                        case "5":
                            result += "н"
                        case "6":
                            result += "с"
                        case "7":
                            result += "х"
                        case "8":
                            result += "щ"
                        case "9":
                            result += "э"
                case 3:
                    match number[0]:
                        case "1":
                            result += "?"
                        case "2":
                            result += "в"
                        case "3":
                            result += "ж"
                        case "4":
                            result += "к"
                        case "5":
                            result += "о"
                        case "6":
                            result += "т"
                        case "7":
                            result += "ц"
                        case "8":
                            result += "ъ"
                        case "9":
                            result += "ю"
                case 4:
                    match number[0]:
                        case "1":
                            result += "!"
                        case "2":
                            result += "г"
                        case "3":
                            result += "з"
                        case "4":
                            result += "л"
                        case "5":
                            result += "п"
                        case "6":
                            result += "у"
                        case "7":
                            result += "ч"
                        case "8":
                            result += "ы"
                        case "9":
                            result += "я"
                case 5:
                    result += ":"
                case 6:
                    result += ";"
        else:
            return None
    if result == "":
        return None
    return result

def is_correct(number: str) -> bool:
    if number[0] == "0":
        if len(number) == 1:
            return True
        else:
            return False
    elif number[0] == "1":
        if len(number) <= 6:
            for i in number:
                if i != number[0]:
                    return False
            return True
        else:
            return False
    elif len(number) <= 4:
        for i in number:
            if i != number[0]:
                return False
            else:
                return True