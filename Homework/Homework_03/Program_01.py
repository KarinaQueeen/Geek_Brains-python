# Программа считает сумму элементов списка, имеющих нечетные индексы.

import random

new_list = [random.randint(1, 99)
            for r in range(int(input('Введите размер списка: ')))]

print('Сумма чисел с нечетными индексами в списке ', new_list, 'равна',
      sum(new_list[i] for i in range(len(new_list)) if i % 2 != 0))
