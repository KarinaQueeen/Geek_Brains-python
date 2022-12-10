# Программа выдает список факториалов по основаниям от 1 до N (натуральное число). 

num = int(input('Введите число: '))
new_list = []
f = 1

for i in range(1, num + 1):
    f *= i
    new_list.append(f)

print(new_list)
