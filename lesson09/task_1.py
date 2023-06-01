# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
from pathlib import Path

# Здесь пишем код
import string

with open('test_file/task1_data.txt', 'r', encoding='utf-8') as input_file:
    text = input_file.read()

    digits = string.digits
    for digit in digits:
        text = text.replace(digit, '')

with open('test_file/task1_answer.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')