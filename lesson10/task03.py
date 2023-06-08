# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division



@pytest.mark.parametrize('args, result', [
    ([5], 5),
    pytest.param([2, 4, 8], 0.0625, marks=pytest.mark.smoke),
    pytest.param([8, 2, 0], ZeroDivisionError, marks=pytest.mark.skip)])
def test_param(args, result):
    assert all_division(*args) == result
