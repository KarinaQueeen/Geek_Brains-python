# Программа выдает перове цифру дробной части числа.

num = float(input('Введите дробное число: '))

a = num - int(num)
a = int(a * 10)

print(a)

# или

print(int(10 * num) % 10)

# или

n = input('Введите дробное число: ').split('.')    

print(n[-1][0])                                     