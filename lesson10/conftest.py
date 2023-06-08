import pytest
import datetime
import time

@pytest.fixture(scope="class")
def print_start_end_time():
    start_time = datetime.datetime.now()
    print(f"\nВремя начала: {start_time}")
    yield
    end_time = datetime.datetime.now()
    print(f"Время окончания: {end_time}")

@pytest.fixture()
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\nВремя выполнения теста: {end_time - start_time} секунд")

def test_example(timer):
    time.sleep(2)
    assert True