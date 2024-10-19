
from typing import List

def get_mask_card_number(card_number: str) -> str:
    # удаляем ненужные пробелы в номере
    card_number = card_number.replace(" ", '')
    # проверяем длину номера
    if len(card_number) != 16:
        raise ValueError('Номер кредитной карты должен содержать 16 цифр.')

    # создаем маску
    masked_number = f"{card_number[:4]} {card_number[4:6]}<strong> </strong><strong> {card_number[-4:]}"

    return masked_number


# Тесты для функции get_mask_card_number
def test_get_mask_card_number():
    # Тесты с корректными данными
    valid_tests = [
        ("4000123456789010", "4000 12 9010"),
        ("1234567812345678", "1234 56 5678"),
        ("   4000 1234 5678 9010   ", "4000 12 9010"),  # Пробелы вокруг
        ("4000 1234 5678 9010", "4000 12 9010"),  # Пробелы внутри
    ]

    for card_number, expected in valid_tests:
        assert get_mask_card_number(card_number) == expected

    # Проверка выброса исключений для неправильных данных
    invalid_tests = [
        ("1234", "Номер кредитной карты должен содержать 16 цифр."),
        ("123456789012345678", "Номер кредитной карты должен содержать 16 цифр."),
        ("1234 5678 9012 345", "Номер кредитной карты должен содержать 16 цифр."),
        ("abcd efgh ijkl mnop", "Номер кредитной карты должен содержать 16 цифр."),  # Неподходящие символы
    ]

    for card_number, expected_message in invalid_tests:
        try:
            get_mask_card_number(card_number)
        except ValueError as e:
            assert str(e) == expected_message
        else:
            assert False, f"Expected ValueError for input '{card_number}' not raised."


# Запуск тестов
if __name__ == "__main__":
    test_get_mask_card_number()
    print("Все тесты прошли успешно!")


def get_mask_account(account_number: str) -> str:
    # Удаляем лишние пробелы, если они есть
    account_number = account_number.replace(" ", "")

    # Проверяем длину номера счета
    if len(account_number) < 4:
        raise ValueError('Номер счета должен содержать не менее 4 цифр.')

    # Создаем маску
    masked_number = "<strong>" + account_number[-4:]

    return masked_number


# Тесты для функции get_mask_account
def test_get_mask_account():
    # Тесты с корректными данными
    valid_tests = [
        ("123456789", "6789"),
        ("9876543210", "3210"),
        ("   1234   ", "1234"),  # Пробелы вокруг
        ("4567 8901 2345 6789", "6789"),  # Пробелы внутри
    ]

    for account_number, expected in valid_tests:
        assert get_mask_account(account_number) == expected

    # Проверка выброса исключений для неправильных данных
    invalid_tests = [
        ("123", 'Номер счета должен содержать не менее 4 цифр.'),
        ("", 'Номер счета должен содержать не менее 4 цифр.'),
        ("   ", 'Номер счета должен содержать не менее 4 цифр.'),
    ]

    for account_number, expected_message in invalid_tests:
        try:
            get_mask_account(account_number)
        except ValueError as e:
            assert str(e) == expected_message
        else:
            assert False, f"Expected ValueError for input '{account_number}' not raised."


# Запуск тестов
if __name__ == "__main__":
    test_get_mask_account()
    print("Все тесты прошли успешно!")
