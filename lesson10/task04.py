# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
class TestClass:
    def test_method_1(self, print_start_end_time, timer):
        assert 1 + 1 == 2


    def test_method_2(self, print_start_end_time, timer):
        assert (1, 2, 3) == (1, 2, 3)