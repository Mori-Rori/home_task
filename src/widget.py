from src.masks import get_mask_card_number, get_mask_account  # забираем обе


from datetime import datetime


def mask_account_card(info: str) -> str:
    """ возвращает входящую строку -  счет/карту с замаскированным ногмером """
    # Разделяем строку на слова
    parts = info.split()
    number = ''.join(parts[-1])
    if parts[0].lower() == 'счет':
        # Маскируем номер счета
        masked_number = get_mask_account(number)  # используем импортированную функцию
        return f"{parts[0]} {masked_number} "
    else:
        # Маскируем номер карты
        masked_number = get_mask_card_number(number)  # используем импортированную функцию
        return f"{' '.join(parts[:-1])} {masked_number} "


def get_date(date_str: str) -> str:
    """Преобразуем строку в объект datetime"""
    date_obj = datetime.fromisoformat(date_str)

    # Форматируем дату в нужный формат
    formatted_date = date_obj.strftime("%d.%m.%Y")

    return formatted_date


if __name__ == '__main__':
    print(mask_account_card("Счет 12345678901234567890"))  # должны увидеть в терминале: Счет **7890
    print(mask_account_card("Visa Classic 1234567890123456"))  # should see в терминале:VisaClassic 1234 56** **** 3456
