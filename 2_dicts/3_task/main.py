def format_phone(phone_number: str) -> str:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    #formatted_phone_number = ""
    number = phone_number
    for cif in phone_number:
        if (
                cif != "1" and cif != "2" and cif != "3" and cif != "4" and cif != "5" and cif != "6" and cif != "7" and cif != "8" and cif != "9" and cif != "0"):
            number = number.replace(cif, "")
    if len(number) == 11:
        formatted_phone_number = "8 (9" + number[2] + number[3] + ") " + number[4] + number[5] + number[6] + "-" + \
                                 number[7] + number[8] + "-" + number[9] + number[10]
    elif len(number) == 10:
        formatted_phone_number = "8 (9" + number[1] + number[2] + ") " + number[3] + number[4] + number[5] + "-" + \
                                 number[6] + number[7] + "-" + number[8] + number[9]
    else:
        formatted_phone_number = number
    return formatted_phone_number