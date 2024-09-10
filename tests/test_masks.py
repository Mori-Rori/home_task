from src.masks import get_mask_card_number


def test_get_mask_card_number():
    # Тестирование валидных номеров карт
    assert get_mask_card_number("4000 1234 5678 9010") == "4000 12** **** 9010"
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"
    assert get_mask_card_number("4000123456789010") == "4000 12** **** 9010"
    assert get_mask_card_number(" 4000 1234 5678 9010  ") == "4000 12** **** 9010"

    # Тестирование неправильной длины номера карты
    try:
        get_mask_card_number("1234 5678 9012")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for short card number not raised."

    try:
        get_mask_card_number("1234 5678 9012 34567")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for long card number not raised."

    # Тестирование недопустимых символов
    try:
        get_mask_card_number("4000 1234 ABCD 9010")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid characters not raised."


# Запуск тестов
if __name__ == "__main__":
    test_get_mask_card_number()
    print("All tests passed!")
