# Переменные, присвоение, типы данных, ввод, вывод 
                                     # комментарий
a = 123                              # int
b = 1.23                             # float
print(a)                             # вывод в консоль
c = None                             # не присвоено значение, 
print(type(c))                       # узнать тип данных
d = 'text'                           # str
e = "te'xt"                          # если нужно ' использовать в тексте 
f = 'te\txt'                         # TAB
g = 'te\nxt'                         # перенос на другую строку
print(f)
print(g)
print(d, e)                          # вывод нескольких переменных
print(a,'слово',b)                   # вывод данных с текстом
print('{} слово {}'.format(a,b))     # вывод данных с текстом с помощью формата (можно поменять местами print('{1} слово {0}'.format(a,b))) 
print(f'{a} слово {b}')              # вывод данных с помощью интерполяции
h = True                             # boolean
i = []                               # строки
g = input()                          # считать данные (по умолчанию тип данных str)
k = int(input())                     


text = 'привет, мир!'
print(len(text))                    # 12 - количество строк
print('мир' in text)                # True
print(text.isdigit())               # False - являются ли все символы строки числами?
print(text.islower())               # True - являются ли все символы строки символами нижнего регистра?
print(text.replace('мир', 'МИР'))   # замена

help (text.istitle())               # стпавка по функции

print(text [0])                     # п
print(text [1])                     # р
print(text [len(text) - 1])         # !
print(text [-4])                    # м
print(text [:])                     # привет, мир!     автоматически print(text [0 : len(text) - 1])   (срезы)
print(text [: 2])                   # пр               или [0 : 2]
print(text [len(text) - 2:])        # р!
print(text [2 : 4])                 # ив
print(text [4 : -6])                # ет
print(text [0 : len(text) : 3])     # пв,и             или [::3]

# Списки

num = [1, 2, 3, 4]
print(num)                          # [1, 2, 3, 4]

n = range(1, 6)
num = list (n)
print(num)                          # [1, 2, 3, 4, 5]
num [0] = 10
print(num)                          # [10, 2, 3, 4, 5]

num.append(6)                       # [10, 2, 3, 4, 5, 6]
num.remove(2)                       # [10, 3, 4, 5, 6]            или     del num [1]

 