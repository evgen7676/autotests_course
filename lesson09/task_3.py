# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases
from pathlib import Path

# Здесь пишем код
with open('test_file/task_3.txt', 'r') as f:
    current_sequence_total = 0
    grand_total = 0
    sequence_totals = []
    for line in f:
        line = line.strip()
        if line == "":
            sequence_totals.append(current_sequence_total)
            current_sequence_total = 0
        else:
            price = float(line)
            current_sequence_total += price
    sequence_totals.append(current_sequence_total)
    sequence_totals.sort(reverse=True)
    three_most_expensive_purchases = sum(sequence_totals[:3])
    print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346