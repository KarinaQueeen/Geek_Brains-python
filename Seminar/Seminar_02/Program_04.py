# Программа определяет количество заданного слова в тексте.

text = input('Введите текст: ')
word = input('Введите слово: ')

print(text.count(word))

# или
# для поиска вхождений с наложением

count = 0         
                   
for i in range(len(text)):
    if word in text[i: i + len(word)]:
        count += 1

print(count)
