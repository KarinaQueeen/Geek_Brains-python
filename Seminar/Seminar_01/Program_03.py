# Программа находит максимальное из 5 чисел    

list = [int(input('Введите число 1: ')), int(input('Введите число 2: ')), int(input('Введите число 3: ')), int(input('Введите число 4: ')), int(input('Введите число 5: '))]
print('Максимальное число:', max(list))

# или 

max = list [0]
for i in list:
    if i > max:
        max = i
print(max)
