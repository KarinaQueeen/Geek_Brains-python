# Программа принимает значение N, выдает отрезок от -N до N.

num = int(input('Введите число: '))
new_list = list(range(-num, num + 1))

print(new_list)

# или

print(*new_list, sep=',')

# или

[print(i, end=',') for i in new_list]
