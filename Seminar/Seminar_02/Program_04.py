# Программа принимает две строки, и определяет количество вхождений одной строки в другую

text = input('Введите текст ► ')
word = input('Введите слово ► ')
print(text.count(word))

# или

inkrement = 0                            # для поиска вхождений с наложением
for i in range(len(tex)):
    if word in text[i: i + len(word)]:   # можно конец не указывать [i:]  
        inkrement += 1
print(inkrement)