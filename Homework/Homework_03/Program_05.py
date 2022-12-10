# Программа создает список чисел Фибоначчи размерностью 2N + 1 для отрицательной и положительной части (Негафибоначчи).

num = int(input('Введите размерность: '))
new_list = [1, 0, 1]

for i in range(num - 1):
    new_list.append(new_list[-1] + new_list[-2])
    new_list.insert(0, new_list[1] - new_list[0])

print(new_list)
