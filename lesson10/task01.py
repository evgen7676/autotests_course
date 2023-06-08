# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

def generate_random_name():
    while True:
        name = ' '.join([''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 15))) for _ in range(2)])
        yield name

gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Здесь пишем код