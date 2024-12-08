def encode_text(text: str) -> str | None:
    """Пишите ваш код здесь."""
    result = ""
    text = list(text)
    for liter in text:
        if is_correct_2(liter):
            match liter:
                case " ":
                    result += "0"
                case ".":
                    result += "1"
                case ",":
                    result += "11"
                case "?":
                    result += "111"
                case "!":
                    result += "1111"
                case ":":
                    result += "11111"
                case ";":
                    result += "111111"
                case "а":
                    result += "2"
                case "б":
                    result += "22"
                case "в":
                    result += "222"
                case "г":
                    result += "2222"
                case "д":
                    result += "3"
                case "е":
                    result += "33"
                case "ж":
                    result += "333"
                case "з":
                    result += "3333"
                case "и":
                    result += "4"
                case "й":
                    result += "44"
                case "к":
                    result += "444"
                case "л":
                    result += "4444"
                case "м":
                    result += "5"
                case "н":
                    result += "55"
                case "о":
                    result += "555"
                case "п":
                    result += "5555"
                case "р":
                    result += "6"
                case "с":
                    result += "66"
                case "т":
                    result += "666"
                case "у":
                    result += "6666"
                case "ф":
                    result += "7"
                case "х":
                    result += "77"
                case "ц":
                    result += "777"
                case "ч":
                    result += "7777"
                case "ш":
                    result += "8"
                case "щ":
                    result += "88"
                case "ъ":
                    result += "888"
                case "ы":
                    result += "8888"
                case "ь":
                    result += "9"
                case "э":
                    result += "99"
                case "ю":
                    result += "999"
                case "я":
                    result += "9999"
        else:
            return None
        result += " "

    result_1 = ""
    for i in range(len(result) - 1):
        result_1 += result[i]
    if result_1 == "":
        return None
    return result_1

def is_correct_2(l: str) -> bool:
    if(l!= ":" and l!= "й" and l!= "б" and l!= "в" and l!= "г" and l!= "д" and l!= "е" and l!= "ж" and l!= "з" and
       l!= "и" and l!= "к" and l!= "л" and l!= "м" and l!= "н" and l!= "ы" and l!= "о" and l!= "п" and l!= "р" and
       l!= "с" and l!= "т" and l!= "у" and l!= "ф" and l!= "х" and l!= "ц" and l!= "ч" and l!= "ш" and l!= "щ" and
       l!= "ь" and l!= "ъ" and l!= "э" and l!= "ю" and l!= "я" and l!= " " and l!= "." and l!= "," and l!= "?" and
       l!= "!" and l!= ";" and ord(l)!= ord("а")):
        return False
    else:
        return True