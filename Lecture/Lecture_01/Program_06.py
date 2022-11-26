# Функции

def metod (x):                # def Название функции (переменные):
    if x == 1:                # тело метода
        return 'Целое'        # оператор возвращения           
    elif x == 2.3:
        return 23
    else:
        return                # ничего не возвращает

arg = 1
print(metod(arg))