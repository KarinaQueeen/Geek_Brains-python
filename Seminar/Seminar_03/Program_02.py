# Программа находит количество пар (равных друг другу чисел) в списоке целых чисел заданной размерностью.

import random

size = int(input('Введите размер: '))
pairs = 0
new_list = [random.randint(1, 9) for i in range(size)]

for l in range(size):
    for k in range(l + 1, size):
        if new_list[l] == new_list[k]:
            pairs += 1

print(new_list)
print(pairs)

# или с помощью среза

for l in range(size):
    for k in new_list[l + 1:]:
        if new_list[l] == k:
            pairs += 1

# или с помощью картежа

for h, el in enumerate(new_list):  
    pairs += new_list[h + 1:].count(el)
