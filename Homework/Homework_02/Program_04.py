# Программа создает список из N элементов, заполненный целыми числами из промежутка [-N, N] 
# и находит произведение элементов с индексами, указанными в файле indexes.txt.

import random

num = int(input('Введите число: '))
new_list = [random.randint(-num, num) for r in range(num)]
index_list = []
prod = 1

with open('indexes.txt') as data:
    for index in data:
        index_list.append(int(index))

for i in range(-num, num):
    if i in index_list:
        prod *= new_list[i]
      # print(f'({i})')

print(new_list)
print(prod)
