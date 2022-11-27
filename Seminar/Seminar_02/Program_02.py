# Программа которая принимает на вход число N и выдаёт последовательность из N членов: 1, -3, 9, -27, 81, …

print('Введите количество членов поседовательности: ')
num = int(input())
x = 1
new_list = []
while num != 0:
    new_list.append(x)
    x = x * -3
    num -= 1
print(*new_list, sep = ', ')     

# или

for i in range(num):
    print((-3) ** i, end = ' ')

# или

result = [1]
for _ in range(num):
    print(*result, sep = ', ')
    result.append(result[len(result) - 1] * -3)            # result.append(result[-1] * -3)

# Моржовый оператор
# output = -1 / 3
# print (*(output := int(output * -3) for i in range(N)), sep = ', ')