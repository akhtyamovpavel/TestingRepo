from unittest import mock

from simple_example import our_sum


@mock.patch('simple_example.our_sum', return_value=9)
def test_sum(sum_mock):
    assert 9 == sum_mock(2, 3)


def side_effect_sum(a, b):
    return a + b * b


@mock.patch('simple_example.our_sum', side_effect=side_effect_sum)
def test_sum_side(sum_mock):
    assert 11 == sum_mock(2, 3)  # 11 == 2 + 3 * 3
