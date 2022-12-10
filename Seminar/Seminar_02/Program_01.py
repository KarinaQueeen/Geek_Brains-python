# Программа выдаёт последовательность из N членов: 1, -3, 9, -27, 81, … .

print('Введите количество членов поседовательности: ')
num = int(input())
x = 1
new_list = []

while num != 0:
    new_list.append(x)
    x = x * -3
    num -= 1

print(*new_list, sep=', ')

# или

for i in range(int(input('Введите количество членов поседовательности: '))):
    print((-3) ** i, end=' ')

# или

result = [1]

for l in range(int(input('Введите количество членов поседовательности: ')) - 1):
   result.append(result[-1] * -3)

print(*result, sep=', ')
    
# или

n = int(input('Введите количество членов поседовательности: '))
output = -1 / 3
print (*(output := int(output * -3) for k in range(n)), sep = ', ')
