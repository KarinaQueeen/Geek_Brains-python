# Программа переводит целое число из десятичной системы счисления в двоичную.

num = int(input('Введите число: '))
new_list = []

while num:
    new_list.append(num % 2)
    num //= 2

print(*new_list[::-1])
