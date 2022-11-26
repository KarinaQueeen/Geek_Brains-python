# Циклы while и for

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)               # инвертируем число

# в цикле while есть else, он выполняется после тела цикла

list = [1, 2, 3, 4]
for i in list:                # счетчик
    print(i)

r = range(10)                 # перечисление 0, 2, 3, 4, 5, 6, 7, 8, 9
r = range(1, 5)               # 1, 2, 3, 4 
r = range(1, 10, 2)           # 1, 3, 5, 7, 9

for i in 'text':                
    print(i)                  # побуквенная разбивка