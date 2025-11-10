from unittest import mock

import simple_example


# Вариант 1: Патчим в пространстве имен модуля, где используется функция
@mock.patch('simple_example.our_sum', return_value=9)
def test_sum(mock_sum):
    # Используем функцию через модуль, а не напрямую импортированную
    assert 9 == simple_example.our_sum(2, 3)
    # Проверяем, что мок был вызван
    mock_sum.assert_called_once_with(2, 3)


# Вариант 2: Использование side_effect для кастомной логики
def side_effect_sum(a, b):
    return a + b * b


@mock.patch('simple_example.our_sum', side_effect=side_effect_sum)
def test_sum_side(mock_sum):
    # side_effect позволяет задать кастомную функцию вместо return_value
    result = simple_example.our_sum(2, 3)  # 11 == 2 + 3 * 3
    assert 11 == result
    mock_sum.assert_called_once_with(2, 3)


# Вариант 3: Если нужно импортировать напрямую, патчим в пространстве имен теста
from simple_example import our_sum


@mock.patch('tests.our_sum', return_value=9)
def test_sum_direct_import(mock_sum):
    # Теперь мок работает, так как патчим в пространстве имен tests
    assert 9 == our_sum(2, 3)
    mock_sum.assert_called_once_with(2, 3)
