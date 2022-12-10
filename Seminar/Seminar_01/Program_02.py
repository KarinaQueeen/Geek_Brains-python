# Программа находит максимальное из 5 чисел.

print('Введите 5 чисел')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
e = int(input('e = '))

print('Максимальное число: ')
if a > b and a > c and a > d and a > e:
    print(a)
elif b > c and b > d and b > e:
    print(b)
elif c > d and c > e:
    print(c)
elif d > e:
    print(d)
else:
    print(e)

# или

list = [int(input('Введите число 1: ')), int(input('Введите число 2: ')),
        int(input('Введите число 3: ')), int(input('Введите число 4: ')), int(input('Введите число 5: '))]

print('Максимальное число:', max(list))

# или

max = list[0]
for i in list:
    if i > max:
        max = i
print(max)
