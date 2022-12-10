# Программа возвращает список с произведениями парных элементов первоначального списка. 
# Парой считаются первый и последний элемент, второй и предпоследний и т.д. 
# Если элементов нечетное количество – центральный элемент умножается сам на себя.

import random
import math

new_list = [random.randint(1, 9)
            for r in range(int(input('Введите размер списка: ')))]
multi_list = []

for el in range(math.ceil(len(new_list)/2)):
    multi_list.append(new_list[el] * new_list[-el - 1])

print(new_list)
print(multi_list)
