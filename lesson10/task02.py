# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

def test_all_division():
    assert all_division(10, 2, 5) == 1
    assert all_division(100, 5, 2) == 10
    assert all_division(12, 4, 3) == 1
    assert all_division(24, 3, 4) == 2


def test_all_division_mask():
    assert all_division(10, 2, 5) == 1
    assert all_division(100, 5, 2) == 10
    assert all_division(12, 4, 3) == 1

def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(8, 2, 0)

@pytest.mark.smoke
def test_correct_calculation():
    assert all_division(2, 4, 8) == 0.0625

def test_single_element():
    assert all_division(5) == 5

@pytest.mark.smoke
def test_all_division_smoke():
    assert all_division(10, 2, 5) == 1
    assert all_division(100, 5, 2) == 10


