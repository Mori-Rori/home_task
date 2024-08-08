def get_mask_card_number(card_number: str) -> str:
    # Проверяем, что длина номера карты соответствует ожидаемой
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Формируем маску
    masked_number = f"XXXX XX{card_number[6:8]} **** XXXX"
    return masked_number


def get_mask_account_number(account_number: str) -> str:
    # Проверяем, что длина номера счета соответствует ожидаемой
    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")

    # Формируем маску (например, 10 символов открытых, остальные закрыты)
    masked_number = f"{account_number[:10]} **** ****"
    return masked_number


def get_masked_info(info: str) -> str:
    # Разделяем строку на слова
    parts = info.split()

    # Первый элемент - тип, остальные - номер
    card_type = parts[0]
    number = ''.join(parts[1:])  # Объединяем остальные части в номер

    # Проверяем тип карты и применяем соответствующую маскировку
    if card_type in ["Visa", "Maestro"]:
        return get_mask_card_number(number)
    elif card_type == "Счет":
        return get_mask_account_number(number)
    else:
        raise ValueError("Неизвестный тип карты или счета")




from datetime import datetime


def get_date(date_str: str) -> str:
    # Преобразуем строку в объект datetime
    date_obj = datetime.fromisoformat(date_str)

    # Форматируем дату в нужный формат
    formatted_date = date_obj.strftime("%d.%m.%Y")

    return formatted_date
