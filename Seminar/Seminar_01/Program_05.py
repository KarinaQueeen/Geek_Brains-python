# Программа принимает на вход дровь, выдает перове цифру дробной части

num = float(input('Введите дробное число: '))
a = num - int (num)
a = int (a * 10)
print(a)

# или

print(int (10 * num) % 10)

n = input('Введите дробное число: ').split('.')         # разделение строки
print(n[-1][0])                                         # 5.63 [5][63] ,берем число из последнего разделения и там элемент под индексом 0