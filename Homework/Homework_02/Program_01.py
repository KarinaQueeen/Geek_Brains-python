#Программа принимает на вход вещественное число и показывает сумму его цифр

num = input()
sum_num = 0
for lm in num:
    if lm.isdigit():                                       
        sum_num += int(lm)
print(f'Сумма цифр числа {num} равна {sum_num}')

sum_n = sum([int(lm) for lm in num if lm.isdigit()])       
print(sum_n)