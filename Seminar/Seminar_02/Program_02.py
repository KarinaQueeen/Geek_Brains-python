# Программа создает словарь с целыми ключами n из диапазона от 1 до заданного N и значениями (3n + 1).

num = int(input('N = '))
our_dict = {}

for i in range(1, num + 1):
    our_dict[i] = 3 * i + 1
    
print(our_dict)

# или

print({i: 3 * i + 1 for i in range(1, int(input('N = ')) + 1)}) 