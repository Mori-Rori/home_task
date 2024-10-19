
from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации.
    :param state: Значение ключа 'state', по умолчанию 'EXECUTED'.
    :return: Новый список словарей, соответствующих указанному значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


# Упрощенные тесты
def test_filter_by_state():
    # Пример входных данных
    data = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'PENDING'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 4, 'state': 'CANCELED'},
    ]

    # Тестирование с состоянием по умолчанию (EXECUTED)
    result = filter_by_state(data)
    assert result == [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]

    # Тестирование с другим состоянием (PENDING)
    result = filter_by_state(data, 'PENDING')
    assert result == [{'id': 2, 'state': 'PENDING'}]

    # Тестирование с состоянием, которого нет в данных (например, CANCELED)
    result = filter_by_state(data, 'CANCELED')
    assert result == [{'id': 4, 'state': 'CANCELED'}]

    # Тестирование с состоянием, которого нет в данных
    result = filter_by_state(data, 'COMPLETED')
    assert result == []  # Ожидаем пустой список


# Запуск тестов
if __name__ == '__main__':
    test_filter_by_state()
    print('Все тесты прошли успешно!')


from typing import List, Dict


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param data: Список словарей для сортировки.
    :param reverse: Параметр, задающий порядок сортировки. По умолчанию True (убывание).
    :return: Новый отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)


# Упрощенные тесты
def test_sort_by_date():
    # Пример входных данных с датами в строковом формате
    data = [
        {'id': 1, 'date': '2023-10-01'},
        {'id': 2, 'date': '2023-09-15'},
        {'id': 3, 'date': '2023-10-10'},
        {'id': 4, 'date': '2023-08-20'},
    ]

    # Тестирование сортировки по убыванию (по умолчанию)
    result = sort_by_date(data)
    expected = [
        {'id': 3, 'date': '2023-10-10'},
        {'id': 1, 'date': '2023-10-01'},
        {'id': 2, 'date': '2023-09-15'},
        {'id': 4, 'date': '2023-08-20'},
    ]
    assert result == expected

    # Тестирование сортировки по возрастанию
    result = sort_by_date(data, reverse=False)
    expected = [
        {'id': 4, 'date': '2023-08-20'},
        {'id': 2, 'date': '2023-09-15'},
        {'id': 1, 'date': '2023-10-01'},
        {'id': 3, 'date': '2023-10-10'},
    ]
    assert result == expected

    # Тестирование с пустым списком
    result = sort_by_date([])
    assert result == []  # Ожидаем пустой список


# Запуск тестов
if __name__ == '__main__':
    test_sort_by_date()
    print('Все тесты прошли успешно!')
